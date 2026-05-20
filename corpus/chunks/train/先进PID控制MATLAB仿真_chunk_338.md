④ 控制器 S 函数：chap6\_11ctrl.m  
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
sizes.NumContStates = 0;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 1;
sizes.NumInputs = 2;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys=simsizes(sizes);
x0=[];
str=[];
ts=[0 0];
function sys=mdlOutputs(t,x,u)
e1=u(1);
e2=u(2);
%NPID Parameters
delta0=0.02;
alfa01=3/4;alfa02=3/2; %0<alfa1<1<alfa2
beta01=6.0;beta02=1.5;
kp=beta01;kd=beta02;

if abs(e1)>delta0
    fal1=abs(e1)^alfa01*sign(e1);
else
    fal1=e1/(delta0^(1-alfa01));
end
if abs(e2)>delta0
    fal2=abs(e2)^alfa02*sign(e2);
else
    fal2=e2/(delta0^(1-alfa02));
end

ut=kp*fal1+kd*fal2; %NPD 
```

```javascript
sys(1)=ut; 
```

⑤ 扩张观测器 S 函数：chap6\_11eso.m  
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
sizes.NumInputs = 2;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0;0;0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
%ESO Parameters
beta1=100;beta2=300;beta3=1000;
delta1=0.0025;
alfa1=0.5;alfa2=0.25;
x1=u(1);
ut=u(2);
e=x(1)-x1;

if abs(e)>delta1
    fal1=abs(e)^alfa1*sign(e);
else
    fal1=e/(delta1^(1-alfa1));
end
if abs(e)>delta1
    fal2=abs(e)^alfa2*sign(e);
else
    fal2=e/(delta1^(1-alfa2));
end 
```

```matlab
b=133;
sys(1)=x(2)-beta1*e;
sys(2)=x(3)-beta2*fal1+b*ut;
sys(3)=-beta3*fal2;
function sys=mdlOutputs(t,x,u)
sys(1)=x(1);
sys(2)=x(2);
sys(3)=x(3); 
```
