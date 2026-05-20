(4) 积分程序: chap7\_2i.m  
```matlab
function [sys,x0,str,ts] = spacemodel(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 3,
    sys=mdlOutputs(t,x,u);
case {2,4,9}
    sys=[];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 0;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 1;
sizes.NumInputs = 3;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 0;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = []; 
```

```matlab
function sys=mdlOutputs(t,x,u)
xd=u(1);
dxd=cos(t);

x1=u(2);
x2=u(3);
e=xd-x1;
de=dxd-x2;

c=5;
s=de+c*e;

sys(1)=s; 
```

(5) 作图程序: chap7\_2plot.m

```matlab
close all;

figure(1);
subplot(211);
plot(t,x(:,1),'r',t,x(:,2),'b:','linewidth',2);
xlabel('time(s)');ylabel('position tracking');
legend('Ideal position signal','Position signal tracking');
subplot(212);
plot(t,cos(t),'r',t,x(:,3),'b:','linewidth',2);
xlabel('time(s)');ylabel('speed tracking');
legend('Ideal speed signal','Speed signal tracking');

figure(2);
plot(t,ut(:,1),'r','linewidth',2);
xlabel('time(s)');ylabel('control input'); 
```

![](image/84d07b754282019b5bd2dd75538d9910b3d4bd22bea4587087bef908a88679f7.jpg)
