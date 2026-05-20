figure(1);
plot(t,y(:,1),'k',t,y(:,2),'r:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','position tracking');

figure(2);
subplot(211);
plot(t,s(:,1),'k',t,s(:,2),'r:','linewidth',2);
xlabel('time(s)');ylabel('signal');
legend('position signal with noise','position signal with TD');
subplot(212);
plot(t,y(:,3),'r',t,s(:,3),'k:','linewidth',2);
xlabel('time(s)');ylabel('signal');
legend('practical derivative signal','deritive signal with TD');

figure(3);
plot(t,n(:,1),'k','linewidth',2);
xlabel('time(s)');ylabel('signal'); 
```

f. 毛刺信号生成程序：chap4\_8maoci.m  
```matlab
function [sys,x0,str,ts] = Differentiator(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 3,
sys=mdlOutputs(t,x,u);
case {1,2,4,9}
sys = [];
otherwise
error(['Unhandled flag = ',num2str(flag)]);
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 0;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 1;
sizes.NumInputs = 0;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1; 
```

```matlab
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
persistent k
if t==0
    k=0;
end
k=k+1;

d=0.50*sign(rands(1)); %Noise
if mod(k,100)==0
    n=d; %Practical signal
else
    n=0;
end
%n=n+0.03*rands(1);
sys=n; 
```

② 离散系统仿真：chap4\_9.m。

```matlab
%PID based on Discrete Levant TD
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

yd(k)=sin(t);
dyd(k)=cos(t);
p(k)=-den(2)*p_1-den(3)*p_2+num(2)*u_1+num(3)*u_2;

d(k)=0.5*sign(rands(1));
if mod(k,100)==1|mod(k,100)==2
    yp(k)=p(k)+d(k);    %Practical signal
else
    yp(k)=p(k); 
```

```matlab
end

M=2;
if M==1 %By Difference
    y(k)=yp(k);
    dy(k)=(yp(k)-yp_1)/T;
elseif M==2 %By TD
    alfa=8;nmna=6;
    y(k)=y_1+T*(dy_1-nmna*sqrt(abs(y_1-yp(k)))*sign(y_1-yp(k)));
    dy(k)=dy_1-T*alfa*sign(y_1-yp(k));
end

kp=10;kd=0.1;
u(k)=kp*(yd(k)-y(k))+kd*(dyd(k)-dy(k));

y_1=y(k);
yp_1=yp(k);
dy_1=dy(k);

u_2=u_1;u_1=u(k);
p_2=p_1;p_1=p(k);
end
