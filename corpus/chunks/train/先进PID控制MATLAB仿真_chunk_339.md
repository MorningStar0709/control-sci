⑥ 被控对象 S 函数：chap6\_11plant.m  
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
x0=[0.15;0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
ut=u(1);

f=-25*x(2)+33*sin(pi*t); %Unknown part
b=133;
sys(1)=x(2);
sys(2)=f+b*ut;
function sys=mdlOutputs(t,x,u)
f=-25*x(2)+33*sin(pi*t); %Unknown part
sys(1)=x(1);
sys(2)=x(2);
sys(3)=f; 
```  
⑦ 作图程序：chap6\_11plot.m

```matlab
close all;
figure(1);
plot(t,x(:,1),'r',t,x(:,2),'k:',t,x(:,4),'b-,'linewidth',2);
xlabel('time(s)'),ylabel('position signal');
legend('ideal signal', 'transient position signal', 'position tracking');
figure(2);
subplot(311);
plot(t,z(:,1),'r',t,x(:,4),'k:','linewidth',2);
xlabel('time(s)'),ylabel('z1,y');
legend('practical position signal', 'position signal estimation');
subplot(312);
plot(t,z(:,2),'r',t,x(:,5),'k:','linewidth',2);
xlabel('time(s)'),ylabel('z2,dy');
legend('practical speed signal', 'speed signal estimation');
subplot(313);
plot(t,z(:,3),'r',t,x(:,6),'k:','linewidth',2);
xlabel('time(s)'),ylabel('z3,x3');
legend('practical uncertain part', 'uncertain part estimation'); 
```
