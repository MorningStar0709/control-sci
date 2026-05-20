```matlab
global J Fx
tol=J*Fx;
sys(1)=x(1);
sys(2)=x(2);
sys(3)=x(3);
sys(4)=x(4);
sys(5:6)=Fx(1:2);
sys(7:8)=tol(1:2); 
```

(3) 输入指令 S 函数: chap14\_2input.m  
```matlab
function [sys,x0,str,ts] = spacemodel(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 1,
sys=mdlDerivatives(t,x,u);
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
sizes.NumOutputs = 6;
sizes.NumInputs = 0;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
xd1=cos(t);
d_xd1=-sin(t);
dd_xd1=-cos(t);
xd2=sin(t);
d_xd2=cos(t);
dd_xd2=-sin(t);
sys(1)=xd1;
sys(2)=d_xd1;
sys(3)=dd_xd1;
sys(4)=xd2;
sys(5)=d_xd2; 
```

```txt
sys(6)=dd_xd2; 
```

(4) 作图程序: chap14\_2plot.m  
```matlab
closeall;

figure(1);
subplot(211);
plot(t,xd(:,1),'r',t,x(:,1),'b--','linewidth',2);
xlabel('time(s)');ylabel('position tracking of x axis');
legend('ideal x','practical x');
subplot(212);
plot(t,xd(:,4),'r',t,x(:,3),'b--','linewidth',2);
xlabel('time(s)');ylabel('position tracking of y axis');
legend('ideal y','practical y');

figure(2);
subplot(211);
plot(t,xd(:,2),'r',t,x(:,2),'b--','linewidth',2);
xlabel('time(s)');ylabel('velocity tracking of x axis');
legend('ideal dx','practical dx');
subplot(212);
plot(t,xd(:,5),'r',t,x(:,4),'b--','linewidth',2);
xlabel('time(s)');ylabel('velocity tracking of y axis');
legend('ideal dy','practical dy');

figure(3);
subplot(211);
plot(t,x(:,5),'r',t,x(:,6),'b--','linewidth',2);
xlabel('time(s)');ylabel('Conrol input Fx1 and Fx2');
legend('Fx of first link','Fx of second link');
subplot(212);
plot(t,x(:,7),'r',t,x(:,8),'b--','linewidth',2);
xlabel('time(s)');ylabel('Conrol input tol1 and tol2');
legend('tol of first link','tol of second link');

figure(4);
plot(xd(:,1),xd(:,4),'r','linewidth',2);
holdon;
plot(x(:,1),x(:,3),'b--','linewidth',1);
xlabel('x');ylabel('y');
legend('ideal trajectory','practical trajectory'); 
```

![](image/49e8e186ed98272c782de4b0e721b7930e114d83d76a9c1b2bc6e7036a929cc6.jpg)
