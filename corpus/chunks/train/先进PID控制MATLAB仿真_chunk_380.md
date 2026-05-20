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
```

```matlab
sizes.NumDiscStates = 0;
sizes.NumOutputs = 3;
sizes.NumInputs = 0;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys=simsizes(sizes);
x0=[0 0];
str=[];
ts=[-1 0];
function sys=mdlDerivatives(t,x,u)
r=1.0*sign(sin(0.05*t*2*pi));
a0=30;a1=20;b=50;

sys(1)=x(2);
sys(2)=b*r-a1*x(2)-a0*x(1);
function sys=mdlOutputs(t,x,u)
r=1.0*sign(sin(0.05*t*2*pi));
sys(1)=r;
sys(2)=x(1);
sys(3)=x(2); 
```

③ 控制器子程序：chap7\_6ctrl.m  
```matlab
function [sys,x0,str,ts]=s_function(t,x,u,flag)
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
sizes.NumDiscStates = 0;
sizes.NumOutputs = 1;
sizes.NumInputs = 8;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys=simsizes(sizes);
x0=[];
str=[];
ts=[-1 0];
function sys=mdlOutputs(t,x,u)
r=u(1);
k0=u(4);k1=u(5);k2=u(6);
th=u(7);dth=u(8); 
```

```javascript
ut=k0*r+k1*th+k2*dth;
sys(1)=ut; 
```

④ 自适应律 S 函数子程序：chap7\_6adapt.m  
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
sizes.NumContStates = 3;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 3;
sizes.NumInputs = 5;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys=simsizes(sizes);
x0=[0 0 0];
str=[];
ts=[-1 0];
function sys=mdlDerivatives(t,x,u)
th=u(1);
dth=u(2);
r=u(3);
thm=u(4);
dthm=u(5);
b1=20;b2=30;b=50;
Am=[0,1;-b2,-b1];
eig(Am);
%Q=[10 0;0,10];
Q=[20,10;10,20];
P=lyap(Am',Q);
p12=P(1,2);
p22=P(2,2);

e=thm-th;
de=dthm-dth;
eF=p12*e+p22*de; 
```
