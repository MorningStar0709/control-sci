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
sizes.NumContStates = 2;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 2;
sizes.NumInputs = 4;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 1;
sys=simsizes(sizes);
x0=[0 0];
str=[]; 
```

```matlab
ts=[-1 0];
function sys=mdlDerivatives(t,x,u)
tol=3;
th_tol=u(1);
yp=th_tol;

ut=u(2);

z_tol=[u(3);u(4)];
thp=x(1);wp=x(2);
%%%%
A=[0 1;-1 -10];
C=[1 0];

H=[0;1];

k1=0.1;k2=0.1; %Verify by design_K.m
z=[thp wp]';
%%%%
K=[k1 k2]';
dz=A*z+H*ut+K*(yp-C*z_tol);

for i=1:2
    sys(i)=dz(i);

end

function sys=mdlOutputs(t,x,u)
thp=x(1);wp=x(2);

sys(1)=thp;
sys(2)=wp; 
```

⑤ 作图程序：chap5\_13plot.m  
```matlab
close all;
figure(1);
plot(t,y(:,1),'k',t,y(:,3),'r:','linewidth',2);
xlabel('time(s)');ylabel('thd and y');
legend('ideal position signal','delayed position signal');
figure(2);
subplot(211);
plot(t,y1(:,1),'k',t,y1(:,3),'r:','linewidth',2);
xlabel('time(s)');ylabel('x1 and its estimate');
legend('ideal signal x1','estimation signal x1');
subplot(212);
plot(t,y1(:,2),'k',t,y1(:,4),'r:','linewidth',2);
xlabel('time(s)');ylabel('x2 and its estimate'); 
```

```matlab
legend('ideal signal x2','estimation signal x2');
figure(3);
subplot(211);
plot(t,y(:,1),'k',t,y(:,2),'r:','linewidth',2);
xlabel('time(s)');ylabel('thd and y');
legend('ideal position signal','position tracking signal');
subplot(212);
plot(t,cos(t),'k',t,y(:,3),'r:','linewidth',2);
xlabel('time(s)');ylabel('dthd and dy');
legend('ideal speed signal','speed tracking signal');
figure(4);
plot(t,ut(:,1),'k','linewidth',2);
xlabel('time(s)');ylabel('Control input'); 
```
