kp=10;kd=10;
M=1;
if M==1 %With Compensation
    b=100;
    ut=kp*e+kd*de-1/b*fp;
elseif M==2 %Without Compensation
    ut=kp*e+kd*de;
end
sys(1)=ut; 
```

c. 扩张观测器 S 函数: chap5\_10eso.m  
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
```

```matlab
sizes.NumContStates = 3;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 3;
sizes.NumInputs = 4;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0'0'0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
ut=u(1);
th=u(2);

h1=6;h2=11;h3=6;
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

sys(1)=x(2)-h1/epc*(x(1)-th);
sys(2)=x(3)-h2/epc^2*(x(1)-th)+100*ut;
sys(3)=-h3/epc^3*(x(1)-th);
function sys=mdlOutputs(t,x,u)
fp=x(3);

sys(1)=x(1);
sys(2)=x(2);
sys(3)=fp; 
```

d. 对象 S 函数：chap5\_10plant.m  
```matlab
function [sys,x0,str,ts]=s_function(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 1,
    sys=mdlDerivatives(t,x,u); 
```

```matlab
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
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0.15;0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
ut=u(1);
b=100;

dt=100*sign(x(2));
fx=-25*x(2)-dt;

sys(1)=x(2);
sys(2)=fx+b*ut;
function sys=mdlOutputs(t,x,u)
dt=100*sign(x(2));
fx=-25*x(2)-dt;

sys(1)=x(1);
sys(2)=x(2);
sys(3)=fx; 
```

e. 作图程序：chap5\_10plot.m  
```matlab
close all;

figure(1);
plot(t,y(:,1),'k',t,y(:,2),'r:','linewidth',2);
xlabel('time(s)');ylabel('th and x1p');
legend('Ideal position','Position tracking');

figure(2);
subplot(211);
plot(t,x(:,1),'k',t,x(:,4),'r:','linewidth',2);
xlabel('time(s)');ylabel('th and x1p');
legend('practical position','position estimation'); 
```
