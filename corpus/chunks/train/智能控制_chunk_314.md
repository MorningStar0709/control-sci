# (3) 被控对象 S 函数: chap5\_6plant. m

```matlab
function [sys,x0,str,ts] = MIMO_Tong_plant(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts] = mdlInitializeSizes;
case 1,
    sys = mdlDerivatives(t,x,u);
case 3,
    sys = mdlOutputs(t,x,u);
case {2,4,9}
    sys = [];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end 
```

```matlab
function [sys,x0,str,ts] = mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 4;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 6;
sizes.NumInputs = 4;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 0;
sys = simsizes(sizes);
x0 = [0 0 0 0];
str = [];
ts = [];
function sys = mdlDerivatives(t,x,u)
r1 = 1;r2 = 0.8;
m1 = 1;m2 = 1.5;

D11 = (m1+m2)* r1^2+m2* r2^2+2*m2*r1*r2*cos(x(3));
D22 = m2*r2^2;
D21 = m2*r2^2+m2*r1*r2*cos(x(3));
D12 = D21;
D = [D11 D12;D21 D22];

C12 = m2*r1*sin(x(3));
C = [-C12*x(4) - C12*(x(2) + x(4));C12*x(1) 0];

g1 = (m1+m2)* r1*cos(x(3)) + m2*r2*cos(x(1) + x(3));
g2 = m2*r2*cos(x(1) + x(3));
G = [g1;g2];

Fr = [10*x(2) + 3* sign(x(2));10*x(4) + 3* sign(x(4))];
told = [0.05*sin(20*t);0.1*sin(20*trows);
tol = [u(1) u(2)]';
S = inv(D)*(tol-C*[x(2);x(4)]-G-Fr);

sys(1) = x(2);
sys(2) = S(1);
sys(3) = x(4);
sys(4) = S(2);
function sys = mdlOutputs(t,x,u)
Fr = [10*x(2) + 3* sign(x(2));10*x(4) + 3* sign(x(4))];

sys(1) = x(1);
sys(2) = x(2);
sys(3) = x(3);
sys(4) = x(4);
sys(5) = Fr(1);
sys(6) = Fr(2); 
```

(4) 作图程序: chap5\_6plot.m

close all;

```matlab
figure(1);
subplot(211);
plot(t,yd1(:,1),'r',t,y(:,1),'b');
xlabel('time(s)');ylabel('Position tracking 1');
subplot(212);
plot(t,yd2(:,1),'r',t,y(:,3),'b');
xlabel('time(s)');ylabel('Position tracking 2');

figure(2);
subplot(211);
plot(t,y(:,5),'r',t,u(:,3),'b');
xlabel('time(s)');ylabel('F and Fc');
subplot(212);
plot(t,y(:,6),'r',t,u(:,4),'b');
xlabel('time(s)');ylabel('F and Fc');

figure(3);
subplot(211);
plot(t,u(:,1),'r');
xlabel('time(s)');ylabel('Control input of Link1');
subplot(212);
plot(t,u(:,2),'r');
xlabel('time(s)');ylabel('Control input of Link2'); 
```

(5) 隶属函数设计程序: chap5\_6mf.m  
```matlab
clear all;
close all;

L1 = -pi/6;
L2 = pi/6;
L = L2 - L1;

T = L* 1/1000;

x = L1:T:L2;
figure(1);
for i = 1:1:5
    gs = -[(x + pi/6 - (i - 1)* pi/12)/(pi/24)].^2;
    u = exp(gs);
    hold on;
    plot(x,u);
end

xlabel('x');ylabel('Membership function degree'); 
```
