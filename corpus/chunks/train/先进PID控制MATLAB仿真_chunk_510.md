```matlab
sys=mdlDerivatives(t,x,u);
case 3,
    sys=mdlOutputs(t,x,u);
case {2,4,9}
    sys=[];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 2;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 2;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [0;1];
str = [];
ts = [0 0];
function sys=mdlDerivatives(t,x,u)
Tol=u(1);
J=10;

sys(1)=x(2);
sys(2)=1/J*Tol;
function sys=mdlOutputs(t,x,u)
sys(1)=x(1); %Angle
sys(2)=x(2); %Angle speed 
```

（4）控制器子程序：chap12\_1ctrl.m  
```matlab
function [sys,x0,str,ts] = spacemodel(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 3,
    sys=mdlOutputs(t,x,u);
case {2,4,9}
    sys=[];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 0;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 1;
sizes.NumInputs = 4;
sizes.DirFeedthrough = 1; 
```

```matlab
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
qd=u(1);dqd=u(2);
q=u(3);dq=u(4);

e=qd-q;
de=dqd-dq;
Kp=30;Kd=50;

M=3;
if M==1
    Tol=Kd*de; %D Type
elseif M==2
    Tol=Kp*e+Kd*de; %PD Type
elseif M==3
    Tol=Kd*exp(0.8*t)*de; %Exponential Gain D Type
end
sys(1)=Tol; 
```

(5) 指令程序: chap12\_1input.m  
```matlab
function [sys,x0,str,ts] = spacemodel(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 3,
    sys=mdlOutputs(t,x,u);
case {2,4,9}
    sys=[];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 0;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 2;
sizes.NumInputs = 0;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
qd=sin(t); 
```

```matlab
dqd=cos(t);
sys(1)=qd;
sys(2)=dqd; 
```
