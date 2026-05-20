u2(1) = 1/(1 + exp(5*(xi(2)+2)));
u2(6) = 1/(1 + exp(-5*(xi(2)-2)));
for i = 2:1:5
    u2(i) = exp(-(xi(2)+1.5-(i-2))^2);
end

for i = 1:1:6
    for j = 1:1:6
    FS2(6*(i-1)+j) = u1(i)* u2(j);
    FS1 = FS1 + u1(i)* u2(j);
    end
end

FS = FS2/FS1;

ut = thtau'* FS';
sys(1) = ut; 
```

(4) 被控对象 S 函数: chap5\_5plant.m  
```matlab
% S- function for continuous state equation
function[sys,x0,str,ts] = s-function(t,x,u,flag)
switch flag,
% Initialization
    case 0,
    [sys,x0,str,ts] = mdlInitializeSizes;
case 1, 
```

```matlab
sys = mdlDerivatives(t, x, u);
% Outputs
    case 3,
    sys = mdlOutputs(t, x, u);
% Unhandled flags
    case {2, 4, 9}
    sys = [];
% Unexpected flags
    otherwise
    error(['Unhandled flag = ', num2str(flag)]);
end 
```

```matlab
function[sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 2;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 2;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 0; 
```

```javascript
sys = simsizes(sizes);
x0 = [1 0];
str = [];
ts = []; 
```

```matlab
function sys = mdlDerivatives(t,x,u)
sys(1) = x(2);
sys(2) = -25* x(2) + 133* u;
function sys = mdlOutputs(t,x,u)
sys(1) = x(1);
sys(2) = x(2); 
```

(5) 作图程序: chap5\_5 plot. m  
```matlab
close all;
figure(1);
plot(t,y(:,1),'r',t,y(:,2),'b');
xlabel('time(s)');ylabel('Position tracking');
figure(2);
plot(t,y(:,1)-y(:,2),'r');
xlabel('time(s)');ylabel('Position tracking error');
figure(3);
plot(t,u(:,1),'r');
xlabel('time(s)');ylabel('Control input'); 
```
