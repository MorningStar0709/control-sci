M=1;
if M==1 %Without compensation
    ut=10*(yd-y)+10*(dyd-dy);
elseif M==2 %With compensation
    ut=10*(yd-y)+10*(dyd-dy)-1/133*fp;
end

sys(1)=ut; 
```

④ 被控对象 S 函数：chap6\_8plant.m  
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
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0.15;0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
ut=u(1);

fx=-25*x(2)-100*sign(x(2));
sys(1)=x(2); 
```

```matlab
sys(2)=fx+133*ut;
function sys=mdlOutputs(t,x,u)
fx=-25*x(2)-100*sign(x(2));
sys(1)=x(1);
sys(2)=x(2);
sys(3)=fx; 
```

⑤ 作图程序：chap6\_8plot.m  
```matlab
close all;

figure(1);
plot(t,y(:,1),'r',t,y(:,2),'k-','linewidth',2);
xlabel('time(s)');ylabel('yd and y');
legend('ideal position signal', 'tracking signal');

figure(2);
subplot(211);
plot(t,x(:,1),'r',t,x(:,4),'k','linewidth',2);
xlabel('time(s)');ylabel('th and x1p');
subplot(212);
plot(t,x(:,2),'r',t,x(:,5),'k','linewidth',2);
xlabel('time(s)');ylabel('dth and x2p');
figure(3);
plot(t,x(:,3),'r',t,x(:,6),'k','linewidth',2);
xlabel('time(s)');ylabel('f and fp'); 
```  
(2) 离散系统仿真

① 主程序：chap6\_9.m  
```matlab
clear all;
close all;
h=0.01; %Sampling time
%ESO Parameters
beta1=100;beta2=300;beta3=1000;
delta1=0.0025;
alfa1=0.5;alfa2=0.25;
kp=10;kd=0.3;
xk=zeros(2,1);
u_1=0;
z1_1=0;z2_1=0;z3_1=0;
for k=1:1:2000
time(k) = k*h;
p1=u_1;
p2=k*h; 
```

```matlab
tSpan=[0 h];
[tt,xx]=ode45('chap6_9plant',tSpan,xk,[],p1,p2);
xk = xx(length(xx).);
y(k)=xk(1);
dy(k)=xk(2);

yd(k)=sin(k*h);
dyd(k)=cos(k*h);

f(k)=-25*dy(k)+33*sin(pi*p2); %Unknown part
b=133;
x3(k)=f(k);
%ESO
e=z1_1-y(k);
z1(k)=z1_1+h*(z2_1-beta1*e);
z2(k)=z2_1+h*(z3_1-beta2*fal(e,alfa1,delta1)+b*u_1);
z3(k)=z3_1-h*beta3*fal(e,alfa2,delta1);

z1_1=z1(k);
z2_1=z2(k);
z3_1=z3(k);
%disturbance compensation
e1(k)=yd(k)-z1(k);
e2(k)=dyd(k)-z2(k);
