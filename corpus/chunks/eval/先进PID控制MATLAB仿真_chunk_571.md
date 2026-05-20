J=[-sin(q1)-sin(q1+q2)-sin(q1+q2);
cos(q1)+cos(q1+q2)cos(q1+q2)];
d_J=[-dq1*cos(q1)-(dq1+dq2)*cos(q1+q2)-(dq1+dq2)*cos(q1+q2);
    -dq1*sin(q1)-(dq1+dq2)*sin(q1+q2)-(dq1+dq2)*sin(q1+q2)];
D=[M(1)+M(2)+2*M(3)*cos(q2) M(2)+M(3)*cos(q2);
M(2)+M(3)*cos(q2) M(2)];
C=[-M(3)*dq2*sin(q2)-M(3)*(dq1+dq2)*sin(q2);
M(3)*dq1*sin(q2) 0];
```

```matlab
G=[M(4)*g*cos(q1)+M(5)*g*cos(q1+q2);
M(5)*g*cos(q1+q2)];
Dx=(inv(J))*D*inv(J);
Cx=(inv(J))*C-D*inv(J)*d_J)*inv(J);
Gx=(inv(J))*G;
e1=xd1-x(1);
e2=xd2-x(3);
de1=ddxd1-x(2);
de2=ddxd2-x(4);
e=[e1;e2];
de=[de1;de2];
dxd=[dxd1;dxd2];
ddxd=[ddxd1;ddxd2];
Fx=Dx*ddxd+Cx*dxd+Gx+Fe+Kp*e+Kd*de;
dx=[x(2);x(4)];
S=inv(Dx)*(Fx-Cx*dx-Gx);
sys(1)=x(2);
sys(2)=S(1);
sys(3)=x(4);
sys(4)=S(2);
function sys=mdlOutputs(t,x,u)
global J FxKpKd
xd1=u(1);dxd1=u(2);ddxd1=u(3);
xd2=u(4);dxd2=u(5);ddxd2=u(6);
Fe1=u(7);Fe2=u(8);
Fe=[Fe1 Fe2]';
l1=l1;l2=l;
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
```

```matlab
B=sqrt(x(1)^2+x(3)^2+l1^2-l2^2)/(2*11*sqrt(x(1)^2+x(3)^2));
p2=acos(B);
d_p2=-1/sqrt(1-B^2);

if q2>0
    q1=p1-p2;
    dq1=d_p1-d_p2;
else
    q1=p1+p2;
    dq1=d_p1+d_p2;
end

J=[-sin(q1)-sin(q1+q2)-sin(q1+q2);
cos(q1)+cos(q1+q2)cos(q1+q2)];
d_J=[-dq1*cos(q1)-(dq1+dq2)*cos(q1+q2)-(dq1+dq2)*cos(q1+q2);
    -dq1*sin(q1)-(dq1+dq2)*sin(q1+q2)-(dq1+dq2)*sin(q1+q2)];
D=[M(1)+M(2)+2*M(3)*cos(q2)M(2)+M(3)*cos(q2);
M(2)+M(3)*cos(q2)M(2)];
C=[-M(3)*dq2*sin(q2)-M(3)*(dq1+dq2)*sin(q2);
M(3)*dq1*sin(q2) 0];
G=[M(4)*g*cos(q1)+M(5)*g*cos(q1+q2);
M(5)*g*cos(q1+q2)];
Dx=(inv(J))'*D*inv(J);
Cx=(inv(J))'*(C-D*inv(J)*d_J)*inv(J);
Gx=(inv(J))'*G;

e1=xd1-x(1);
e2=xd2-x(3);
de1=dxd1-x(2);
de2=dxd2-x(4);
e=[e1;e2];
de=[de1;de2];

dxd=[dxd1;dxd2];
ddxd=[ddxd1;ddxd2];

Fx=Dx*ddxd+Cx*dxd+Gx+Fe+Kp*e+Kd*de;

dx=[x(2);x(4)];
S=inv(Dx)*(Fx-Cx*dx-Gx);

tol=J'*Fx;

sys(1)=x(1);
sys(2)=x(2);
sys(3)=S(1);
sys(4)=x(3);
```

```matlab
sys(5)=x(4);
sys(6)=S(2);
sys(7:8)=Fe(1:2);
sys(9:10)=tol(1:2); 
```

(5) 作图程序: chap14\_3plot.m  
```matlab
closeall;
