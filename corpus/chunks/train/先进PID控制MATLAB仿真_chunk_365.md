(5) 被控对象子程序: chap7\_3plant.m  
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
sizes.NumContStates = 4;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 4;
sizes.NumInputs = 2;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0.09 0 -0.09 0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
p=[2.9 0.76 0.87 3.04 0.87];
g=9.8;

D0=[p(1)+p(2)+2*p(3)*cos(x(3)) p(2)+p(3)*cos(x(3));
    p(2)+p(3)*cos(x(3)) p(2)];
C0=[-p(3)*x(4)*sin(x(3)) -p(3)*(x(2)+x(4))*sin(x(3));
    p(3)*x(2)*sin(x(3)) 0]; 
```

$G0=[p(4)*g*cos(x(1))+p(5)*g*cos(x(1)+x(3));\quad p(5)*g*cos(x(1)+x(3))];$

```javascript
tol=u(1:2); 
```

```javascript
dq=[x(2);x(4)]; 
```

```javascript
d=20*sign(dq); 
```

```txt
S=inv(D0)*(tol-C0*dq-G0-d); 
```

```javascript
sys(1)=x(2); 
```

```javascript
sys(2)=S(1); 
```

```javascript
sys(3)=x(4); 
```

```javascript
sys(4)=S(2); 
```

```matlab
function sys=mdlOutputs(t,x,u)
```

```javascript
sys(1)=x(1);
```

```javascript
sys(2)=x(2); 
```

```javascript
sys(3)=x(3); 
```

```javascript
sys(4)=x(4); 
```

(6) 绘图子程序: chap7\_3plot.m  
```txt
close all; 
```

```javascript
figure(1); 
```

```txt
subplot(211); 
```

```javascript
plot(t,x(:,1),'r',t,x(:,5),'b:',linewidth',2); 
```

```javascript
xlabel('time(s)');ylabel('position tracking for link 1'); 
```

```javascript
legend('Ideal position signal', 'Position signal tracking'); 
```

```txt
subplot(212); 
```

```javascript
plot(t,x(:,2),'r',t,x(:,6),'b:',linewidth',2); 
```

```javascript
xlabel('time(s)');ylabel('speed tracking for link 1'); 
```

```javascript
legend('Ideal speed signal', 'Speed signal tracking'); 
```

```javascript
figure(2); 
```

```txt
subplot(211); 
```

```javascript
plot(t,x(:,3),'r',t,x(:,7),'b:',linewidth',2); 
```

```javascript
xlabel('time(s)');ylabel('position tracking for link 1'); 
```

```javascript
legend('Ideal position signal', 'Position signal tracking'); 
```

```txt
subplot(212); 
```

```javascript
plot(t,x(:,4),'r',t,x(:,8),'b:',linewidth',2); 
```
