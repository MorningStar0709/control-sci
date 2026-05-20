```matlab
sys(1)=30*eF*r; %k0
sys(2)=30*eF*th; %k1
sys(3)=30*eF*dth; %k2
function sys=mdlOutputs(t,x,u)
sys(1)=x(1);
sys(2)=x(2);
sys(3)=x(3); 
```  
⑤ 被控对象 S 函数子程序：chap7\_6plant.m

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
sizes.NumInputs = 1;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys=simsizes(sizes);
x0=[0.5 0];
str=[];
ts=[-1 0];
function sys=mdlDerivatives(t,x,u)
a1=20;a2=25;a=133;
ut=u(1);
sys(1)=x(2);
sys(2)=-a1*x(2)-a2*x(1)+a*ut;
function sys=mdlOutputs(t,x,u)
sys(1)=x(1);
sys(2)=x(2); 
```

⑥ 作图程序：chap7\_6plot.m  
```matlab
close all;
figure(1);
subplot(211); 
```

```matlab
plot(t,y(:,2),'r',t,y(:,4),'b:','linewidth',2);
xlabel('time(s)');ylabel('position tracking');
legend('Ideal position signal','Position signal tracking');
subplot(212);
plot(t,y(:,3),'r',t,y(:,5),'b:','linewidth',2);
xlabel('time(s)');ylabel('speed tracking');
legend('Ideal speed signal','Speed signal tracking');
figure(2);
subplot(311);
plot(t,k(:,1),'r','linewidth',2);
xlabel('time(s)');ylabel('k0');
subplot(312);
plot(t,k(:,2),'r','linewidth',2);
xlabel('time(s)');ylabel('k1');
subplot(313);
plot(t,k(:,3),'r','linewidth',2);
xlabel('time(s)');ylabel('k2'); 
```
