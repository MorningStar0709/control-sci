%进入主要循环，直到满足精度要求  
```matlab
G=50; %最大迭代次数
for kg=1:1:G
time(kg)=kg;
%变异
fori=1:Size
kx=kxi(i,:);
    r1 = 1;r2=1;r3=1;r4=1;
while(r1 == r2 || r1 == r3 || r2 == r3 || r1 == i || r2 == i || r3 == i || r4 == i || r1 == r4 || r2 == r4 || r3 == r4)
    r1 = ceil(Size * rand(1));
    r2 = ceil(Size * rand(1));
    r3 = ceil(Size * rand(1));
    r4 = ceil(Size * rand(1));
end
h(i,:)=BestS+F*(kxi(r1,:)-kxi(r2,:));
    %h(i,:)=X(r1,:)+F*(X(r2,:)-X(r3,:));
    for j=1:CodeL    %检查值是否越界
if h(i,j)<MinX(j)
h(i,j)=MinX(j);
elseif h(i,j)>MaxX(j)
h(i,j)=MaxX(j);
end
end
%交叉
for j = 1:1:CodeL
tempr = rand(1);
if (tempr<cr)
v(i,j) = h(i,j);
else
v(i,j) = kxi(i,j);
end 
```

```matlab
end
%选择
    if(chap10_4plant(v(i,:),BsJ)<chap10_4plant(kxi(i,:),BsJ))
kxi(i,:)=v(i,:);
end
%判断和更新
    if chap10_4plant(kxi(i,:),BsJ)<BsJ %判断当此时的指标是否为最优的情况
BsJ=chap10_4plant(kxi(i,:),BsJ);
BestS=kxi(i,:);
end
end
BestS
BsJ
BsJ_kg(kg)=chap10_4plant(BestS,BsJ);
end
display('ideal value: kx=[0.3,1.5]');
BestS
figure(1);
plot(timef,yd,'r',timef,y,'k:','linewidth',2);
xlabel('Time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
figure(2);
plot(time,BsJ_kg,'r','linewidth',2);
xlabel('Times');ylabel('Best J'); 
```

(2) 子程序: chap10\_4plant.m  
```matlab
functionBsJ=pid_fm_def(kx,BsJ)
globalyd y timef
a=50;b=400;
ts=0.001;
sys=tf(b,[1,a,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');
u_1=0;u_2=0;
y_1=0;y_2=0;
e_1=0;
B=0;
G=500;
for k=1:1:G
timef(k)=k*ts;
yd(k)=0.5*sin(2*pi*k*ts);
y(k)=-den(2)*y_1-den(3)*y_2+num(2)*u_1+num(3)*u_2;
e(k)=yd(k)-y(k);
de(k)=(e(k)-e_1)/ts; 
```

```matlab
speed(k)=(y(k)-y_1)/ts;
% Disturbance Signal: Coulomb & Viscous Friction
Ff(k)=sign(speed(k))*(0.30*abs(speed(k))+1.50);
kp=50;kd=0.50;
u(k)=kp*e(k)+kd*de(k); %PD control
u(k)=u(k)-Ff(k); % with friction
%kx=[0.3,1.5]; %Idea Identification
Ffc(k)=sign(speed(k))*(kx(1)*abs(speed(k))+kx(2));
u(k)=u(k)+Ffc(k)*1.0; %With friction compensation
u_2=u_1;u_1=u(k);
y_2=y_1;y_1=y(k);
e_1=e(k);
end
fori=1:1:G
Ji(i)=0.999*abs(e(i))+0.01*u(i)^2*0.1;
B=B+Ji(i);
end
BsJ=B; 
```

![](image/3c24ce2861d58951cadc2dacfa9bef6fba1fbb856ce59e40a67138836a1754d2.jpg)
