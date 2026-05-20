```matlab
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes=simsizes;
sizes.NumContStates =0;
sizes.NumDiscStates =0;
sizes.NumOutputs =4;
sizes.NumInputs =0;
sizes.DirFeedthrough =1;
sizes.NumSampleTimes =1;
sys=simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
q1d=sin(3*t);
dq1d=3*cos(3*t);
q2d=cos(3*t);
dq2d=-3*sin(3*t);

sys(1)=q1d;
sys(2)=dq1d;
sys(3)=q2d;
sys(4)=dq2d; 
```

(4) 被控对象子程序: chap11\_1plant.m  
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
sizes.NumContStates = 4;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 4;
sizes.NumInputs = 2;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [0;3;1;0]; % Must be equal to x(0) of ideal input
str = [];
ts = [0 0];
function sys=mdlDerivatives(t,x,u) 
```

```matlab
Tol=[u(1) u(2)]';
g=9.81;
d1=10;d2=5;
l1=1;l2=0.5;
lc1=0.5;lc2=0.25;
l1=0.83;l2=0.3;

D11=d1*lc1^2+d2*(l1^2+lc2^2+2*ll1*lc2*cos(x(3)))+l1+l2;
D12=d2*(lc2^2+l1*lc2*cos(x(3)))+l2;
D21=D12;
D22=d2*lc2^2+l2;
D=[D11 D12;D21 D22];
h=-d2*l1*lc2*sin(x(3));
C11=h*x(4);
C12=h*x(4)+h*x(2);
C21=-h*x(2);
C22=0;
C=[C11 C12;C21 C22];
g1=(d1*lc1+d2*l1)*g*cos(x(1))+d2*lc2*g*cos(x(1)+x(3));
g2=d2*lc2*g*cos(x(1)+x(3));
G=[g1;g2];

a=1.0;
d1=a*0.3*sin(t);
d2=a*0.1*(1-exp(-t));
Td=[d1;d2];

S=-inv(D)*C*[x(2);x(4)]-inv(D)*G+inv(D)*(Tol-Td);

sys(1)=x(2);
sys(2)=S(1);
sys(3)=x(4);
sys(4)=S(2);
function sys=mdlOutputs(t,x,u)
sys(1)=x(1); % Angle1:q1
sys(2)=x(2); % Angle1 speed:dq1
sys(3)=x(3); % Angle2:q2
sys(4)=x(4); % Angle2 speed:dq2 
```

(5) 控制器子程序: chap11\_1ctrl.m  
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
) 
```
