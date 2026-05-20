for j = 26:1:50
    sys(j) = S2(j-25);
end

function sys = mdlOutputs(t,x,u)
r = 0.1* sin(t);
dr = 0.1* cos(t);
ddr = -0.1* sin(t);

e = u(1);
de = u(2);
x1 = r - e;
x2 = de - dr;

k1 = 2;
k2 = 1;
k = [k2;k1];
E = [e,de]';
for i = 1:1:25
    thtaf(i,1) = x(i);
end

for i = 1:1:25
    thtag(i,1) = x(i+25);
end

FS1 = 0;
for l1 = 1:1:5
    gs1 = -[(x1 + pi/6 - (l1 - 1)* pi/12)/(pi/24)]^2;
    u1(l1) = exp(gs1);
end

for l2 = 1:1:5
    gs2 = -[(x2 + pi/6 - (l2 - 1)* pi/12)/(pi/24)]^2;
    u2(l2) = exp(gs2);
end

for l1 = 1:1:5
    for l2 = 1:1:5
    FS2(5*(l1 - 1)+l2) = u1(l1)* u2(l2);
    FS1 = FS1 + u1(l1)* u2(l2);
    end
end

FS = FS2/(FS1 + 0.001); 
```

```matlab
fx1 = thtaf'* FS';
gx1 = thtag'* FS' + 0.001;
ut = 1/gx1* (-fx1 + ddr + k'* E);
sys(1) = ut;
sys(2) = fx1;
sys(3) = gx1; 
```

(4) 被控对象 S 函数: chap5\_4plant. m  
```matlab
% S-function for continuous state equation
function[sys,x0,str,ts] = s-function(t,x,u,flag)

switch flag,
% Initialization
    case 0,
    [sys,x0,str,ts] = mdlInitializeSizes;
case 1,
    sys = mdlDerivatives(t,x,u);
% Outputs
    case 3,
    sys = mdlOutputs(t,x,u);
% Unhandled flags
    case {2,4,9}
    sys = [];
% Unexpected flags
    otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end

function[sys,x0,str,ts] = mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 2;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 3;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 0;

sys = simsizes(sizes);
x0 = [pi/60 0];
str = [];
ts =rows;
function sys = mdlDerivatives(t,x,u)
g = 9.8;
mc = 1.0;
m = 0.1;
l = 0.5;
S = l*(4/3 - m*(cos(x(1)))^2/(mc + m)); 
```

```matlab
fx = g* sin(x(1)) - m* l* x(2)^2* cos(x(1))* sin(x(1))/(mc+m);
fx = fx/S;
gx = cos(x(1))/(mc+m);
gx = gx/S;

sys(1) = x(2);
sys(2) = fx + gx*u;
function sys = mdlOutputs(t, x, u)
g = 9.8;
mc = 1.0;
m = 0.1;
l = 0.5;

S = l* (4/3 - m* (cos(x(1)))^2/(mc+m));
fx = g* sin(x(1)) - m* l* x(2)^2* cos(x(1))* sin(x(1))/(mc+m);
fx = fx/S;
gx = cos(x(1))/(mc+m);
gx = gx/S;

sys(1) = x(1);
sys(2) = fx;
sys(3) = gx; 
```

(5) 作图程序: chap5\_4 plot. m  
```matlab
close all;

figure(1);
plot(t,y(:,1),'r',t,y(:,2),'b');
xlabel('time(s)');ylabel('Position tracking');

figure(2);
plot(t,u(:,1),'r');
xlabel('time(s)');ylabel('Control input');

figure(3);
plot(t,fx(:,1),'r',t,fx(:,2),'b');
xlabel('time(s)');ylabel('fx and estimated fx');
figure(4);
plot(t,gx(:,1),'r',t,gx(:,2),'b');
xlabel('time(s)');ylabel('gx and estimated gx'); 
```
