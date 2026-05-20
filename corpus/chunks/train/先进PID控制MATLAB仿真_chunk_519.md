（4）被控对象子程序：chap13\_1plant.m  
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
```

```matlab
sizes.NumOutputs = 2;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0 0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
ut=u(1);
m=4.4;b=18;k=2317;F=27.8;
x1=x(1);x2=x(2);

sys(1)=x(2);
sys(2)=1/m*(-b*x2-k*x1+F*ut);
function sys=mdlOutputs(t,x,u)
sys(1)=x(1);
sys(2)=x(2); 
```

(5) 作图程序: chap13\_1plot.m

```matlab
closeall;

figure(1);
plot(t,ur,'r',t,y(:,1),'k','linewidth',2);
legend('shaped signal','ideal signal');
xlabel('time(s)');ylabel('r');
figure(2);
plot(t,y(:,1),'r',t,y(:,2),'k','linewidth',2);
legend('ideal signal,r','out,y');
xlabel('time(s)');ylabel('r,y');

figure(3);
plot(t,ut(:,1),'r','linewidth',2);
legend('control input');
xlabel('time(s)');ylabel('ut'); 
```

![](image/3269bd1d1adb77d92fc7f18e385b7d002642791e10296b39cc0b8c6263f9b552.jpg)
