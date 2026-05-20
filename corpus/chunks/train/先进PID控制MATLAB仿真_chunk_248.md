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
```

```matlab
str = [];
ts = [0 0];
function sys=mdlDerivatives(t,x,u)
vt=u(1);
e=x(1)-vt;
nmn=6;
alfa=18;
sys(1)=x(2)-nmn*(abs(e))^0.5*sign(e);
sys(2)=-alfa*sign(e);
function sys=mdlOutputs(t,x,u)
sys = x; 
```

c. 作图程序：chap4\_6plot.m  
```matlab
close all;

figure(1);
subplot(211);
plot(t,sin(t),'r',t,r(:,1),'k:','linewidth',2);
xlabel('time(s)');ylabel('signal');
legend('ideal signal','signal with noise');
subplot(212);
plot(t,sin(t),'r',t,y(:,1),'k:','linewidth',2);
legend('ideal signal','x1 by Levant TD');

figure(2);
subplot(211);
plot(t,cos(t),'r',t,r(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('derivative signal');
legend('ideal derivative signal','derivative signal by Matlab');
subplot(212);
plot(t,cos(t),'r',t,y(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('derivative signal');
legend('ideal derivative signal','x2 by Levant TD'); 
```

② 离散系统仿真：chap4\_7.m   
```matlab
%Discrete Levant TD
close all;
clear all;
T=0.001;
y_1=0;dy_1=0;
for k=1:1:10000
    t=k*T;
    time(k)=t;
    u(k)=sin(k*T);
    du(k)=cos(k*T); 
```

```matlab
d(k)=0.5; %Noise
d(k)=-0.5; %Noise
d(k)=0.5*sign(rands(1)); %Noise
if mod(k,100)==1
    up(k)=u(k)+1*d(k); %Practical signal
else
    up(k)=u(k);
end
up(k)=up(k)+0.15*rands(1);

alfa=8;nmna=6;    %M=1    Low Frequency

y(k)=y_1+T*(dy_1-nmna*sqrt(abs(y_1-up(k)))*sign(y_1-up(k)));
dy(k)=dy_1-T*alfa*sign(y_1-up(k));

y_1=y(k); dy_1=dy(k);
end
figure(1);
subplot(211);
plot(time,u,'r',time,up,'k:','linewidth',2);
xlabel('time(s)'),ylabel('input signal');
legend('sin(t)',signal with noises');
subplot(212);
plot(time,u,'r',time,y,'k:','linewidth',2);
xlabel('time(s)'),ylabel('input signal');
legend('sin(t)',signal with TD');
