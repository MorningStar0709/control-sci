qd1=u(1);
d_qd1=0.2*0.5*pi*cos(0.5*pi*t);
qd2=u(2);
d_qd2=0.2*0.5*pi*sin(0.5*pi*t);

q1=u(3);dq1=u(4);q2=u(5);dq2=u(6);
e1=q1-qd1;
e2=q2-qd2;
de1=dq1-d_qd1;
de2=dq2-d_qd2;

th=[x(1)x(2)x(3)x(4)x(5);x(6)x(7)x(8)x(9)x(10)]';
xi=[e1;e2;de1;de2];
h=zeros(5,1);
for j=1:1:5
    h(j)=exp(-norm(xi-c(:,j))^2/(2*b(j)*b(j)));
end

gama=20;

% Adaptive Law
S=gama*h*xi'*P*B;
S=S';
for i=1:1:5
sys(i)=S(1,i);
sys(i+5)=S(2,i);
end

function sys=mdlOutputs(t,x,u)
```

```matlab
global c b kvkp

qd1=u(1);
d_qd1=0.2*0.5*pi*cos(0.5*pi*t);
dd_qd1=-0.2*(0.5*pi)^2*sin(0.5*pi*t);

qd2=u(2);
d_qd2=0.2*0.5*pi*sin(0.5*pi*t);
dd_qd2=0.2*(0.5*pi)^2*cos(0.5*pi*t);
dd_qd=[dd_qd1;dd_qd2];

q1=u(3);dq1=u(4);
q2=u(5);dq2=u(6);
ddq1=u(7);ddq2=u(8);
ddq=[ddq1;ddq2];

e1=q1-qd1;
e2=q2-qd2;
de1=dq1-d_qd1;
de2=dq2-d_qd2;
e=[e1;e2];
de=[de1;de2];

v=13.33;
q01=8.98;
q02=8.75;
g=9.8;

D0=[v+q01+2*q02*cos(q2) q01+q02*cos(q2);
q01+q02*cos(q2) q01];
C0=[-q02*dq2*sin(q2)-q02*(dq1+dq2)*sin(q2)
q02*dq1*sin(q2) 0];
G0=[15*g*cos(q1)+8.75*g*cos(q1+q2);
8.75*g*cos(q1+q2rows);
dq=[dq1;dq2];

tol1=D0*(dd_qd-kv*de-kp*e)+C0*dq+G0;

d_D=0.2*D0;
d_C=0.2*C0;
d_G=0.2*G0;
d1=2;d2=3;d3=6;
d=[d1+d2*norm([e1,e2])+d3*norm([de1,de2])];
% d=[20*sin(2*t);20*sin(2*t)];
f=inv(D0)*(d_D*ddq+d_C*dq+d_G+d);

xi=[e1;e2;de1;de2];
h=zeros(5,1);
```

```matlab
for j=1:1:5
    h(j)=exp(-norm(xi-c(:,j))^2/(2*b(j)*b(j)));
end

M=2;
if M==1
fn=[0 0];
tol=tol1;
elseif M==2
fn=[0 0];
    tol2=-D0*f;
tol=tol1+tol2;
elseif M==3
th=[x(1)x(2)x(3)x(4)x(5);x(6)x(7)x(8)x(9)x(10)]';
fn=th'*h;
    tol2=-D0*fn;
tol=tol1+1*tol2;
end

sys(1)=tol(1);
sys(2)=tol(2);
sys(3)=f(1);
sys(4)=fn(1);
sys(5)=f(2);
sys(6)=fn(2); 
```

(4) 被控对象子程序: chap9\_6plant.m  
```matlab
% S-function for continuous state equation
function [sys,x0,str,ts]=s_function(t,x,u,flag)

switch flag,
% Initialization
    case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 1,
    sys=mdlDerivatives(t,x,u);
% Outputs
    case 3,
    sys=mdlOutputs(t,x,u);
% Unhandled flags
    case {2,4,9}
    sys = [];
% Unexpected flags
    otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end 
```
