（4）被控对象程序：chap17\_7plant.m  
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
sizes.NumOutputs = 3;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0.5;0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
J=1.0;
ut=u(1);

F=0.5*x(2)+1.5*sign(x(2));
sys(1)=x(2);
sys(2)=1/J*(ut-F);
function sys=mdlOutputs(t,x,u) 
```

```matlab
J=1.0;
sys(1)=x(1);
sys(2)=x(2);
sys(3)=J; 
```

(5) 作图程序: chap17\_7plot.m  
```matlab
close all;
figure(1);
subplot(211);
plot(t,y(:,1),'r',t,y(:,2),'k:','linewidth',2)
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','position tracking');
subplot(212);
plot(t,cos(t),'r',t,y(:,3),'k:','linewidth',2)
xlabel('time(s)');ylabel('Speed tracking');
legend('ideal speed signal','Speed tracking');
figure(2);
plot(t,ut(:,1),'r','linewidth',2)
xlabel('time(s)');ylabel('Control input');
figure(3);
plot(t,y(:,4),'r',t,p(:,1),':,'linewidth',2)
xlabel('time(s)');ylabel('J and its estimation'); 
```
