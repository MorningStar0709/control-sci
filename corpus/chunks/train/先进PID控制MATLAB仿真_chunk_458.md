# 〖仿真程序〗

(1) 主程序: chap10\_3.m  
```matlab
%PD tuning control based on DE
clear all;
close all;
globalydy timef

F=1.20;    %变异因子: [1,2]
cr=0.6;    %交叉因子

Size=30;
CodeL=2;
MinX=[0 0];
MaxX=[20 1];

fori=1:1:CodeL
kxi(:,i)=MinX(i)+(MaxX(i)-MinX(i))*rand(Size,1);
end

BestS=kxi(1,:);    %全局最优个体
BsJ=0;
fori=2:Size
if chap10_3plant(kxi(i,:),BsJ)<chap10_3plant(BestS,BsJ)
BestS=kxi(i,:);
end
end
BsJ=chap10_3plant(BestS,BsJ);

%进入主要循环，直到满足精度要求
G=50; %最大迭代次数
for kg=1:1:G
time(kg)=kg;
%变异
fori=1:Size
kx=kxi(i,:);
    r1 = 1;r2=1;r3=1;r4=1;
while(r1 == r2 || r1 == r3 || r2 == r3 || r1 == i || r2 == i || r3 == i ||r4==i ||r1==r4||r2==r4||r3==r4)
    r1 = ceil(Size * rand(1));
    r2 = ceil(Size * rand(1));
    r3 = ceil(Size * rand(1));
    r4 = ceil(Size * rand(1));
end 
```

```matlab
h(i,:)=BestS+F*(kxi(r1,:)-kxi(r2,:)); %h(i,:)=X(r1,:)+F*(X(r2,:)-X(r3,:)); for j=1:CodeL %检查值是否越界 if h(i,j)<MinX(j) h(i,j)=MinX(j); elseif h(i,j)>MaxX(j) h(i,j)=MaxX(j); end end %交叉 for j=1:1:CodeL tempr=rand(1); if (tempr<cr) v(i,j)=h(i,j); else v(i,j)=kxi(i,j); end end %选择 if(chap10_3plant(v(i,:),BsJ)<chap10_3plant(kxi(i,:),BsJ)) kxi(i,:)=v(i,:); end %判断和更新 if chap10_3plant(kxi(i,:),BsJ)<BsJ %判断当此时的指标是否为最优的情况 BsJ=chap10_3plant(kxi(i,:),BsJ); BestS=kxi(i,:); end end BestS BsJ BsJ BsJ_kg(kg)=chap10_3plant(BestS, BsJ); end display('kp,kd'); BestS figure(1); plot(timef,yd,'r',timef,y,'k:',linewidth',2); xlabel('Time(s)');ylabel('yd,y'); legend('Ideal position signal','Position tracking'); figure(2); plot(time,BsJ_kg,'r','linewidth',2); xlabel('Times');ylabel('Best J'); figure(3); plot(time,kp,'r',time,kd,'k','linewidth',2); xlabel('Time(s)');ylabel('kp,kd'); legend('kp','kd');
```

(2) 被控对象子程序: chap10\_3plant.m  
```matlab
functionBsJ=pid_fm_def(kx,BsJ)
globalyd y timef
ts=0.001;
sys=tf(400,[1,50,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;
y_1=0;y_2=0;
e_1=0;
B=0;

G=500;
for k=1:1:G
timef(k)=k*ts;
yd(k)=1.0;

y(k)=-den(2)*y_1-den(3)*y_2+num(2)*u_1+num(3)*u_2;
e(k)=yd(k)-y(k);
de(k)=(e(k)-e_1)/ts;
speed(k)=(y(k)-y_1)/ts;

kp=kx(1);kd=kx(2);
u(k)=kp*e(k)+kd*de(k); %PID control

u_2=u_1;u_1=u(k);
y_2=y_1;y_1=y(k);
e_1=e(k);
end

fori=1:1:G
Ji(i)=0.999*abs(e(i))+0.01*u(i)^2*0.1;
B=B+Ji(i);
if e(i)<0 %Punishment
    B=B+10*abs(e(i));
end

end

BsJ=B; 
```

![](image/b239d46c6f03d2a8fbac215bcdd939ed14c51430f1be9f9625a258418d56dcef.jpg)
