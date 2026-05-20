# 〖仿真程序〗

(1) 控制主程序: chap1\_6.m  
```matlab
%Discrete PID control for continuous plant
clear all;
close all;

ts=0.001; %Sampling time
xk=zeros(2,1);
e_1=0;
u_1=0;

for k=1:1:2000
time(k) = k*ts;

yd(k)=0.50*sin(1*2*pi*k*ts);

para=u_1;
tSpan=[0 ts];
[tt,xx]=ode45('chap1_6plant',tSpan,xk,[],para);
xk = xx(length(xx),:);
y(k)=xk(1);

e(k)=yd(k)-y(k);
de(k)=(e(k)-e_1)/ts;

u(k)=20.0*e(k)+0.50*de(k);
%Control limit
if u(k)>10.0
    u(k)=10.0;
end
if u(k)<-10.0
    u(k)=-10.0;
end

u_1=u(k);
e_1=e(k);
end
figure(1);
plot(time,yd,'r',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
figure(2);
plot(time,yd-y,'r','linewidth',2);
xlabel('time(s)'),ylabel('error'); 
```

(2) 连续对象子程序: chap1\_6plant.m   
```matlab
function dy = PlantModel(t,y,flag,para) 
```

```matlab
u=para;
J=0.0067;B=0.1;
dy=zeros(2,1);
dy(1)=y(2);
dy(2)=-(B/J)*y(2)+(1/J)*u; 
```
