c. 微分器 S 函数: chap4\_3td.m  
```matlab
function [sys,x0,str,ts] = Differentiator(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 1,
    sys=mdlDerivatives(t,x,u);
case 3,
    sys=mdlOutputs(t,x,u);
case {2,4,9}
    sys = [];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 2;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 2;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [0 0];
str = [];
ts = [0 0];
function sys=mdlDerivatives(t,x,u)
vt=u(1);
e=x(1)-vt;
R=1/0.01;a0=2;b0=1;
sys(1)=x(2);
sys(2)=R^2*(-a0*e-b0*x(2)/R);
function sys=mdlOutputs(t,x,u)
sys(1)=x(1);
sys(2)=x(2); 
```

d. 作图程序：chap4\_3plot.m  
```matlab
close all;
figure(1);
plot(t,y(:,1),'k',t,y(:,2),'r:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','tracking signal'); 
```

```matlab
figure(2);
subplot(211);
plot(t,s(:,1),'k',t,s(:,2),'r:','linewidth',2);
xlabel('time(s)');ylabel('signal');
legend('practical position signal','position signal with TD');
subplot(212);
plot(t,y(:,3),'k',t,s(:,3),'r:','linewidth',2);
xlabel('time(s)');ylabel('signal');
legend('ideal derivative signal','deritive signal with TD');
figure(3);
plot(t,n(:,1),'k','linewidth',2);
xlabel('time(s)');ylabel('signal'); 
```

② 数字仿真。

离散微分器控制程序：chap4\_4.m

```matlab
close all;
clear all;

T=0.001;
y_1=0;yp_1=0;
dy_1=0;

%Plant
a=25;b=133;
sys=tf(b,[1,a,0]);
dsys=c2d(sys,T,'z');
[num,den]=tfdata(dsys,'v');
u_1=0;u_2=0;
p_1=0;p_2=0;
for k=1:1:5000
t=k*T;
time(k)=t;

p(k)=-den(2)*p_1-den(3)*p_2+num(2)*u_1+num(3)*u_2;
dp(k)=(p(k)-p_1)/T;

yd(k)=sin(t);
dyd(k)=cos(t);
d(k)=1.5*sign(rands(1)); %Noise

if mod(k,100)==1|mod(k,100)==2
    yp(k)=p(k)+d(k);    %Practical signal
else
    yp(k)=p(k);
end
yp(k)=yp(k)+0.1*rands(1); 
```

```matlab
M=2;
if M==1 %By Difference
    y(k)=yp(k);
    dy(k)=(yp(k)-yp_1)/T;
elseif M==2 %By TD
    R=100;a0=2;b0=1;
    y(k)=y_1+T*dy_1;
    dy(k)=dy_1+T*R^2*(-a0*(y(k)-yp(k))-b0*dy_1/R);
end

kp=10;kd=0.2;
u(k)=kp*(yd(k)-y(k))+kd*(dyd(k)-dy(k));

if M==3 %Using ideal plant
    u(k)=kp*(yd(k)-p(k))+kd*(dyd(k)-dp(k));
end

y_1=y(k);
yp_1=yp(k);
dy_1=dy(k);

u_2=u_1;u_1=u(k);
p_2=p_1;p_1=p(k);
end

figure(1);
plot(time,p,'k',time,yp,'r-',time,y,'b:','linewidth',2);
xlabel('time(s)');ylabel('position tracking');
legend('ideal position signal','position signal with noise','position signal by TD');
figure(2);
plot(time,yd,'r',time,p,'k:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','position tracking'); 
```

![](image/faeefe59834b2fad6f80971778fe34e2a089b92c67ff80118e99183ded528929.jpg)
