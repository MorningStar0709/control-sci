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
```

```matlab
error(['Unhandled flag = ',num2str(flag)]);
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes=simsizes;
sizes.NumContStates =2;
sizes.NumDiscStates =0;
sizes.NumOutputs =2;
sizes.NumInputs =2;
sizes.DirFeedthrough =0;
sizes.NumSampleTimes =1;
sys=simsizes(sizes);
x0 =[0;1];
str =[];
ts =[0 0];
function sys=mdlDerivatives(t,x,u)
A=[-2 3;1 1];
C=[1 0;0 1];
B=[1 1;0 1];
Gama=0.95;
norm(eye(2)-C*B*Gama); % Must be smaller than 1.0
U=[u(1);u(2)];
dx=A*x+B*U;
sys(1)=dx(1);
sys(2)=dx(2);
function sys=mdlOutputs(t,x,u)
sys(1)=x(1);
sys(2)=x(2); 
```

(4) 控制器子程序: chap11\_2ctrl.m  
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
sizes.NumInputs = 4;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = []; 
```

```matlab
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
e1=u(1);e2=u(2);
de1=u(3);de2=u(4); 
```

```javascript
e=[e1 e2]';
de=[de1 de2]'; 
```

```javascript
Kp=2.0;
Gama=0.95;
Kd=Gama*eye(2); 
```

```txt
Tol=Kp*e+Kd*de; % PD Type 
```

```javascript
sys(1)=Tol(1);
sys(2)=Tol(2); 
```

(5) 指令程序: chap11\_2input.m  
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
sizes.NumOutputs = 4;
sizes.NumInputs = 0;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
x1d=sin(3*t);
dx1d=3*cos(3*t);
x2d=cos(3*t);
dx2d=-3*sin(3*t);

sys(1)=x1d;
sys(2)=x2d;
sys(3)=dx1d;
sys(4)=dx2d; 
```
