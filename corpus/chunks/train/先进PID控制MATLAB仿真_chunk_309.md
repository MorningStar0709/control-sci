# (1) 微分器测试

① 非线性跟踪微分器主程序：chap6\_1.m

```matlab
clear all;
close all;

h=0.001; %Sampling time
delta=150;
r1_1=0;r2_1=0;
vn_1=0;
for k=1:1:10000
time(k)=k*h;

v(k)=sin(2*pi*k*h);
n(k)=0.05*rands(1);
vn(k)=v(k)+n(k);
dv(k)=2*pi*cos(2*pi*k*h);

r1(k)=r1_1+h*r2_1;
r2(k)=r2_1+h*chap6_1fst(r1_1-v(k),r2_1,delta,h);

dvn(k)=(vn(k)-vn_1)/h; %By difference

vn_1=vn(k);

r1_1=r1(k);
r2_1=r2(k);
end

figure(1);
subplot(211); 
```

```matlab
plot(time,v,'k:',time,vn,'r:','linewidth',2);
xlabel('time(s)'),ylabel('signal');
legend('ideal signal','signal with noise');
subplot(212);
plot(time,v,'k:',time,r1,'r:','linewidth',2);
xlabel('time(s)'),ylabel('signal');
legend('ideal signal','signal by TD');
figure(2);
subplot(211);
plot(time,dv,'k:',time,dvn,'r:','linewidth',2);
xlabel('time(s)'),ylabel('derivative signal');
legend('ideal derivative signal','derivative signal by difference');
subplot(212);
plot(time,dv,'k:',time,r2,'r:','linewidth',2);
xlabel('time(s)'),ylabel('derivative signal');
legend('ideal derivative signal','derivative signal by TD'); 
```

② fst(·) 函数程序: fst.m

```matlab
function f=fst(x1,x2,delta,h)
d=delta*h;
d0=h*d;
y=x1+h*x2;
a0=sqrt(d^2+8*delta*abs(y));
if abs(y)>d0
    a=x2+(a0-d)/2*sign(y);
else
    a=x2+y/h;
end

if abs(a)>d
    f=-delta*sign(a);
else
    f=-delta*a/d;
end 
```

(2) 基于微分器的 PD 控制

主程序：chap6\_2.m

```matlab
close all;
clear all;
h=0.001;
y_1=0;yp_1=0;
dy_1=0;
%Plant
a=25;b=133;
```

```matlab
sys=tf(b,[1,a,0]);
dsys=c2d(sys,h,'z');
[num,den]=tfdata(dsys,'v');
u_1=0;u_2=0;
p_1=0;p_2=0;
for k=1:1:5000
t=k*h;
time(k)=t;

p(k)=-den(2)*p_1-den(3)*p_2+num(2)*u_1+num(3)*u_2;
dp(k)=(p(k)-p_1)/h;

yd(k)=sin(t);
dyd(k)=cos(t);
d(k)=0.5*sign(rands(1));%Noise
if mod(k,100)==1|mod(k,100)==2
    yp(k)=p(k)+d(k);    %Practical signal
else
    yp(k)=p(k);
end

M=1;
if M==1    %By Difference
    y(k)=yp(k);
    dy(k)=(yp(k)-yp_1)/h;
elseif M==2    %By TD
    delta=1000;
    y(k)=y_1+h*dy_1;
    dy(k)=dy_1+h*fst(y_1-yp(k),dy_1,delta,h);
end
kp=10;kd=0.5;
u(k)=kp*(yd(k)-y(k))+kd*(dyd(k)-dy(k));

y_1=y(k);
yp_1=yp(k);
dy_1=dy(k);

u_2=u_1;u_1=u(k);
p_2=p_1;p_1=p(k);
end
figure(1);
plot(time,p,'k',time,yp,'r:',time,y,'b:','linewidth',2);
xlabel('time(s)');ylabel('position tracking');
legend('ideal position signal','position signal with noise','position signal by TD');
figure(2);
plot(time,yd,'k',time,p,'r:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','tracking signal'); 
```

![](image/60dc28ff9243f9d1e55dacc5bad3ee5b62fa0b1151d4b015d4a45dc6eb798dec.jpg)
