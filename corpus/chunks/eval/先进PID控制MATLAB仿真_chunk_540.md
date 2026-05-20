| Time (s) | control input, F |
| --- | --- |
| 0 | 0.0 |
| 1 | -1.5 |
| 2 | -0.5 |
| 3 | -0.2 |
| 4 | -0.1 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
| 11 | 0.0 |
| 12 | 0.0 |
| 13 | 0.0 |
| 14 | 0.0 |
| 15 | 0.0 |
| 16 | 0.0 |
| 17 | 0.0 |
| 18 | 0.0 |
| 19 | 0.0 |
| 20 | 0.0 |
</details>

图 13-12 关节点处边界控制输入 $\tau$ 和末端点处边界控制输入 F

〖仿真程序〗 chap13\_3.m  
```matlab
closeall;
clearall;
nx=10;
nt=40000;

tmax=20;L=0.6;
%Compute mesh spacing and time step
dx=L/(nx-1);
T=tmax/(nt-1);

%Create arrays to save data for export
t=linspace(0,nt*T,nt);
x=linspace(0,L,nx);

%Parameters
EI=2;m=6.78;rho=0.2211;Ih=0.0139;

thd=0.5;dthd=0;ddthd=0;

kp=30;kd=50;k=10;
F_1=0;
%Defineviriables and Initial condition:
y=zeros(nx,nt); %elastic deflection
th_2=0;th_1=0;
dth_1=0;
for j=1:nt
th(j)=0; %joint angle
end

for j=3:nt %Begin
e(j)=th_1-thd;
de(j)=dth_1-dthd;

%th(j)
yxx0=(y(3,j-1)-2*y(2,j-1)+y(1,j-1))/dx^2;

tol(j)=-kp*e(j)-kd*de(j); %PD control for the joint
th(j)=2*th_1-th_2+T^2/Ih*(tol(j)+EI*yxx0); %(A1)
dth(j)=(th(j)-th_1)/T;
ddth(j)=(th(j)-2*th_1+th_2)/T^2;

%get y(i,j),i=1,2, Boundary condition (A2)
y(1,:)=0; %y(0,t)=0, i=1
y(2,:)=0; %y(1,t)=0, i=2 
```

```matlab
%get y(i,j),i=3:nx-2
fori=3:nx-2
    yxxxx=(y(i+2,j-1)-4*y(i+1,j-1)+6*y(i,j-1)-4*y(i-1,j-1)+y(i-2,j-1))/dx^4;
    y(i,j)=T^2*(-i*dx*ddth(j)-EI*yxxxx/rho)+2*y(i,j-1)-y(i,j-2); %i*dx=x, (A3)
dy(i,j-1)=(y(i,j-1)-y(i,j-2))/T;
end

%get y(nx-1,j),i=nx-1
yxxxx(nx-1,j-1)=(-2*y(nx,j-1)+5*y(nx-1,j-1)-4*y(nx-2,j-1)+y(nx-3,j-1))/dx^4;
y(nx-1,j)=T^2*(-nx-1)*dx*ddth(j)-EI*yxxxx(nx-1,j-1)/rho)+2*y(nx-1,j-1)-y(nx-1,j-2); %(A6)
dy(nx-1,j)=(y(nx-1,j)-y(nx-1,j-1))/T;

%get y(nx,j),y=nx
yxxx_L=(-y(nx,j-1)+2*y(nx-1,j-1)-y(nx-2,j-1))/dx^3;
y(nx,j)=T^2*(-L*ddth(j)+(EI*yxxx_L+F_1)/m)+2*y(nx,j-1)-y(nx,j-2); %(A7)
dy(nx,j)=(y(nx,j)-y(nx,j-1))/T;
%%%%%%%%%%%%%%%%%%%%%
dzL=L*dth(j)+(y(nx,j)-y(nx,j-1))/T;

F(j)=-k*dzL; %P Control for the end
