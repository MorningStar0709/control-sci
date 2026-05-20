(6) 姿态子系统控制器程序: chap15\_2Actrl.m  
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
```

```matlab
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 0;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 3;
sizes.NumInputs = 14;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
chap15_2int;

dphid=0;ddphid=0;
thetad=u(1);
psid=u(2);
dthetad=u(4);
ddthetad=u(5);
dpsid=u(7);
ddpsid=u(8);

theta=u(9);dtheta=u(10);
psi=u(11);dpsi=u(12);
phi=u(13);dphi=u(14);

thetaa=theta-thetad;dthetaa=dtheta-dthetad;
psie=psi-psid;dpsie=dpsi-dpsid;
phie=phi-phid;dphie=dphi-dphid;

kp4=15;kd4=15;
kp5=15;kd5=15;
kp6=15;kd6=15;

u2=-kp4*thetaa-kd4*dthetaa+ddthetad+l*K4/I1*dthetad;
u3=-kp5*psie-kd5*dpsie+ddpsid+l*K5/I2*dpsid;
u4=-kp6*phie-kd6*dphie+ddphid+l*K6/I3*dphid;

sys(1)=u2;
sys(2)=u3;
sys(3)=u4; 
```

(7) 微分器程序: chap15\_2td1.m  
```matlab
function [sys,x0,str,ts] = spacemodel(t,x,u,flag)
switch flag,
case 0,
[sys,x0,str,ts]=mdlInitializeSizes;
case 1, 
```

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
sizes.NumContStates    = 3;
sizes.NumDiscStates    = 0;
sizes.NumOutputs    = 3;
sizes.NumInputs    = 1;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0    = [0 0 0];
str = [];
ts    = [0 0];
function sys=mdlDerivatives(t,x,u)
ebs=0.10;
vt=u(1);
temp1=(abs(ebs*x(2))^(9/7))*sign(ebs*x(2));
temp2=x(1)-vt+temp1;
temp2=abs(temp2)^(1/3)*sign(temp2);
temp3=abs(ebs^2*x(3))^(3/5)*sign(ebs^2*x(3));
sys(1)=x(2);
sys(2)=x(3);
sys(3)=(-2^(3/5)*4*temp2-4*temp3)*1/ebs^3;
function sys=mdlOutputs(t,x,u)
v=u(1);
sys(1)=v;
sys(2)=x(2);
sys(3)=x(3); 
```
