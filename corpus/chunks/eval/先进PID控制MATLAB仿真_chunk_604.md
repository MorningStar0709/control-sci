(8) 微分器程序: chap15\_2td2.m  
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
) 
```

```matlab
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 3;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 3;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [0 0 0];
str = [];
ts = [0 0];
function sys=mdlDerivatives(t,x,u)
ebs=0.04;
vt=u(1);
temp1=(abs(ebs*x(2))^(9/7))*sign(ebs*x(2));
temp2=x(1)-vt+temp1;
temp2=abs(temp2)^(1/3)*sign(temp2);
temp3=abs(ebs^2*x(3))^(3/5)*sign(ebs^2*x(3));
sys(1)=x(2);
sys(2)=x(3);
sys(3)=(-2^(3/5)*4*temp2-4*temp3)*1/ebs^3;
function sys=mdlOutputs(t,x,u)
v=u(1);
sys(1)=v;
sys(2)=x(2);
sys(3)=x(3); 
```

(9) 作图程序: chap15\_2plot.m  
```matlab
closeall;
figure(1);
subplot(311);
plot(t,x(:,1),'b','linewidth',2);
xlabel('Time(s)');ylabel('x');
legend('x');
subplot(312);
plot(t,x(:,3),'b','linewidth',2);
xlabel('Time(s)');ylabel('y');
legend('y');
subplot(313);
%zd=3*t./t;
zd=10*t./t;
plot(t,zd,'r--',t,x(:,5),'b','linewidth',2);
xlabel('Time(s)');ylabel('z');
legend('zd','z');
figure(2);
subplot(311); 
```

```matlab
plot(t,Angle(:,1)/pi*180,'r',t,x(:,7)/pi*180,'k','linewidth',2);
legend('\theta_d (degree)',\theta (degree)');
subplot(312);
plot(t,Angle(:,2)/pi*180,'r',t,x(:,9)/pi*180,'k','linewidth',2);
legend('\psi_d (degree)',\psi (degree)');
subplot(313);
plot(t,60*t./t,'r--',t,x(:,11)/pi*180,'b','linewidth',2);
legend('\phid(degree)',\phi (degree)');
figure(3);
subplot(411);
plot(t,ut(:,1),'k','linewidth',2);
legend('u1');
subplot(412);
plot(t,ut(:,2),'k','linewidth',2);
legend('u2');
subplot(413);
plot(t,ut(:,3),'k','linewidth',2);
legend('u3');
subplot(414);
plot(t,ut(:,4),'k','linewidth',2);
legend('u4'); 
```
