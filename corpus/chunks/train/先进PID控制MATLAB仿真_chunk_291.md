```matlab
alfa1=6;alfa2=11;alfa3=6;
M=2;
if M==1
    epc=0.01;
elseif M==2
    if t<=1;
    R=100*t^3;
    elseif t>1;
    R=100;
    end
    epc=1/R;
elseif M==3
    nmn=0.1;
    R=100*(1-exp(-nmn*t))/(1+exp(-nmn*t));
    epc=1/R;
end

e=y-x(1);
sys(1)=x(2)+alfa1/epc*e;
sys(2)=b*ut+x(3)+alfa2/epc^2*e;
sys(3)=alfa3/epc^3*e;
function sys=mdlOutputs(t,x,u)
sys(1)=x(1);
sys(2)=x(2);
sys(3)=x(3); 
```

b. 对象 S 函数：chap5\_8plant.m  
```matlab
function [sys,x0,str,ts]=s_function(t,x,u,flag)
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
sizes.NumOutputs = 3;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 0; 
```

```matlab
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0.5;0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
J=10;
ut=u(1);

d=3.0*sin(t);
sys(1)=x(2);
sys(2)=1/J*(ut-d);
function sys=mdlOutputs(t,x,u)
J=10;
d=3.0*sin(t);
f=-d/J;
sys(1)=x(1);
sys(2)=x(2);
sys(3)=f; 
```

c. 作图程序：chap5\_8plot.m  
```matlab
close all;

figure(1);
plot(t,x(:,1),'k',t,x(:,4),'r:','linewidth',2);
xlabel('time(s)');ylabel('x1 and x1 estimation');
legend('angle practical value','angle estimation');

figure(2);
plot(t,x(:,2),'k',t,x(:,5),'r:','linewidth',2);
xlabel('time(s)');ylabel('x2 and x2 estimation');
legend('angle speed practical value','angle speed estimation');

figure(3);
plot(t,x(:,3),'k',t,x(:,6),'r:','linewidth',2);
xlabel('time(s)');ylabel('x3 and x3 estimation');
legend('fx practical value','fx estimation'); 
```  
② 离散系统仿真。

a. 主程序: chap5\_9.m  
```matlab
%Discrete ESO
clear all;
close all;
ts=0.001; %Sampling time
xk=[0.15 0];
x1p_1=0;x2p_1=0;x3p_1=0;
u_1=0;x1_1=0;
for k=1:1:3000 
```

```matlab
time(k) = k*ts;
u(k) = sin(2*pi*k*ts);

tSpan=[0 ts];
para=[u(k) time(k)]; %D/A
[t,xx]=ode45('chap5_9plant',tSpan,xk,[],para); %Plant
xk=xx(length(xx),:); %A/D
x1(k)=xk(1);
x2(k)=xk(2);
th(k)=x1(k);

J=10;
dt(k)=3.0*sin(time(k));
fx(k)=-1/J*dt(k);
b=1/J;

h1=6;h2=11;h3=6;
