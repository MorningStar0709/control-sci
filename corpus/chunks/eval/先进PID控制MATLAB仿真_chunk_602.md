（4）姿态子系统被控对象程序：chap15\_2Aplant.m  
```matlab
function [sys,x0,str,ts]=chap14_5plant(t,x,u,flag)
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
sizes.NumContStates = 6;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 6;
sizes.NumInputs = 3;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 1;
sys=simsizes(sizes);
x0=[0 0 0 0 0 0];
str=[];
ts=[-1 0];
function sys=mdlDerivatives(t,x,u)
u2=u(1);u3=u(2);u4=u(3);

chap15_2int;

theta=x(1);dtheta=x(2);
psi=x(3);dpsi=x(4);
phi=x(5);dphi=x(6);

ddtheta=u2-l*K4*dtheta/I1;
ddpsi=u3-l*K5*dpsi/I2; 
```

```matlab
ddphi=u4-K6*dphi/I3;
sys(1)=x(2);
sys(2)=ddtheta;
sys(3)=x(4);
sys(4)=ddpsi;
sys(5)=x(6);
sys(6)=ddphi;
function sys=mdlOutputs(t,x,u)
theta=x(1);dtheta=x(2);
psi=x(3);dpsi=x(4);
phi=x(5);dphi=x(6);
sys(1)=theta;
sys(2)=dtheta;
sys(3)=psi;
sys(4)=dpsi;
sys(5)=phi;
sys(6)=dphi; 
```

(5) 位置子系统控制器程序: chap15\_2Pctrl.m  
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
sizes.NumOutputs = 3;
sizes.NumInputs = 12;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
chap15_2int; 
```

```matlab
x1=u(1);dx1=u(2);
y=u(3);dy=u(4);
z=u(5);dz=u(6);
phi=u(11);

dzd=0;ddzd=0;
ze=z-zd;
dze=dz-dzd;

kdx=5;kpx=5;
kdy=5;kpy=5;
kdz=5;kpz=5;
ulx=-kpx*x1-kdx*dx1;
uly=-kpy*y-kdy*dy;
ulz=-kpz*ze-kdz*dze+g+ddzd+K3/m*dzd;

X=(cos(phi)*cos(phi)*ulx+cos(phi)*sin(phi)*uly)/ulz;
%To Guarantee X is [-1,1]
if X>1
sin_thetad=1;
thetad=pi/2;
elseif X<-1
sin_thetad=-1;
thetad=-pi/2;
else
sin_thetad=X;
thetad=asin(X);
end
psid=atan((sin(phi)*cos(phi)*ulx-cos(phi)*cos(phi)*uly)/ulz);

u1=u1z/(cos(phi)*cos(psid));
sys(1)=u1;
sys(2)=thetad;
sys(3)=psid; 
```
