Fe=Mm*(ddxc-ddxp)+Bm*(dxc-dxp)+Km*(xc-xp);
if x1<=1.0
    Fe=[0 0]';
end

xd=[x(1);x(3)];
dxd=[x(2);x(4)];
ddxd=inv(Mm)*((-Fe+Mm*ddxc+Bm*dxc+Km*xc)-Bm*dxd-Km*xd);

sys(1)=x(2);
sys(2)=ddxd(1);
sys(3)=x(4);
sys(4)=ddxd(2);

function sys=mdlOutputs(t,x,u)
xc=[1.0-0.2*cos(pi*t) 1.0+0.2*sin(pi*t)]';
dxc=[0.2*pi*sin(pi*t) 0.2*pi*cos(pi*t)]';
ddxc=[0.2*pi^2*cos(pi*t) -0.2*pi^2*sin(pi*t)]';
Mm=[1 0;0 1];
Bm=[10 0;0 10];
Km=[40 0;0 40];

x1=u(7);dx1=u(8);ddx1=u(9);
x2=u(10);dx2=u(11);ddx2=u(12);

xp=[x1 x2]';
dxp=[dx1 dx2]';
ddxp=[ddx1 ddx2]'; 
```

```matlab
if x1>=1.0
xp=[1.0 xp(2)]';dxp=[0 dxp(2)]';ddxp=[0 ddxp(2)]';
end

Fe=Mm*(ddxc-ddxp)+Bm*(dxc-dxp)+Km*(xc-xp);
if x1<=1.0
    Fe=[0 0]';
end

xd=[x(1);x(3)];
dxd=[x(2);x(4)];
S=inv(Mm)*((-Fe+Mm*ddxc+Bm*dxc+Km*xc)-Bm*dxd-Km*xd); %ddxd

sys(1)=x(1);
sys(2)=x(2);
sys(3)=S(1);
sys(4)=x(3);
sys(5)=x(4);
sys(6)=S(2);
sys(7)=Fe(1);
sys(8)=Fe(2); 
```

（4）控制器及被控对象 S 函数：chap14\_3system.m  
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
global J FxKpKd
sizes = simsizes;
sizes.NumContStates = 4;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 10;
sizes.NumInputs = 8;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0.8 0 1.0 0]; %x(0)=xc(0) 
```

```matlab
str=[];
ts=[];
J=0;Dx=0;Cx=0;Gx=0;Fx=[0 0];
Kp=500*eye(2);
Kd=10*eye(2);
function sys=mdlDerivatives(t,x,u)
global J FxKpKd
xd1=u(1);dxd1=u(2);ddxd1=u(3);
xd2=u(4);dxd2=u(5);ddxd2=u(6);

Fe1=u(7);Fe2=u(8);
Fe=[Fe1 Fe2]';
l1=1;l2=1;
P=[1.66 0.42 0.63 3.75 1.25];
g=9.8;
L=[l1^2 l2^2 l1*l2 l1 l2];

pl=0.5;

M=P+pl*L;
Q=(x(1)^2+x(3)^2-l1^2-l2^2)/(2*l1*l2);
q2=acos(Q);
dq2=-1/sqrt(1-Q^2);

A=x(3)/x(1);
p1=atan(A);
d_p1=1/(1+A^2);

B=sqrt(x(1)^2+x(3)^2+l1^2-l2^2)/(2*l1*sqrt(x(1)^2+x(3)^2));
p2=acos(B);
d_p2=-1/sqrt(1-B^2);

if q2>0
    q1=p1-p2;
    dq1=d_p1-d_p2;
else
    q1=p1+p2;
    dq1=d_p1+d_p2;
end
