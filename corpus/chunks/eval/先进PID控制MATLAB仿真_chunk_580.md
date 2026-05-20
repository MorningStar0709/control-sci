（4）位置控制器程序：chap14\_4P\_ctrl.m  
```matlab
function [sys,x0,str,ts] = spacemodel(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 1,
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
sizes.NumContStates = 0;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 2;
sizes.NumInputs = 5;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
xd=u(1);
yd=u(2);
xd=t;dxd=1;
yd=sin(0.5*xd)+0.5*xd+1;
dyd=0.5*cos(0.5*xd)+0.5;

x1=u(3);
y1=u(4);

kp1=10;
xe=x1-xd;
u1=-kp1*xe+dxd; 
```

```matlab
kp2=10;
ye=y1-yd;
u2=-kp2*ye+dyd;
thd=atan(u2/u1);
v=u1/cos(thd);
sys(1)=v;
sys(2)=thd; 
```

(5) 被控对象程序: chap14\_4plant.m  
```matlab
function [sys,x0,str,ts] = spacemodel(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 1,
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
sizes.NumContStates = 3;
sizes.NumOutputs = 3;
sizes.NumInputs = 2;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [0;0;0];
str = [];
ts = [0 0];
function sys=mdlDerivatives(t,x,u)
v=u(1);
w=u(2);
th=x(3);

sys(1)=v*cos(th);
sys(2)=v*sin(th);
sys(3)=w;
function sys=mdlOutputs(t,x,u)
sys(1)=x(1);
sys(2)=x(2);
sys(3)=x(3); 
```

(6) 微分器程序: chap14\_4td.m  
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
sizes.NumOutputs = 1;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [1 0];
str = [];
ts = [0 0];
function sys=mdlDerivatives(t,x,u)
n=u(1);
e=x(1)-n;
R=100;

sys(1)=x(2);
sys(2)=-2*R^2*e-R*x(2);
function sys=mdlOutputs(t,x,u)
sys = x(2); 
```
