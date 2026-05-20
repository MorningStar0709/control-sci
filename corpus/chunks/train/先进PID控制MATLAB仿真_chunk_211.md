# 【仿真方法一】

在离散方式下进行仿真，采用 M 语言进行编程。按预期闭环方法设计副调节器。由于副对象的传递函数为一阶，故由式（3.3）得到副回路闭环系统传递函数 $\varphi_{2}(z)=z^{-1}$ 。

主调节器采用 PI 控制，取 $k_{p}=1.2$ ， $k_{i}=0.02$ ，副调节器按控制律式（3.2）设计。副回路输入、输出及阶跃响应结果如图 3-3～图 3-5 所示。

![](image/dc84fdffe8edf1dcd6953a5a564183ac4322ce264b5d2f52bbeb45875d4916f7.jpg)

<details>
<summary>line</summary>

| time(s) | u1 | y2 |
| --- | --- | --- |
| 0 | 0.6 | 0.6 |
| 500 | 0.95 | 0.95 |
| 1000 | 1.0 | 1.0 |
| 1500 | 1.0 | 1.0 |
| 2000 | 1.0 | 1.0 |
| 2500 | 1.0 | 1.0 |
| 3000 | 1.0 | 1.0 |
| 3500 | 1.0 | 1.0 |
| 4000 | 1.0 | 1.0 |
</details>

图 3-3 副回路输入、输出

![](image/b4f1c7781bc96a9214d523aa44e77b9f7dc676108e7faf2f90e6c9dd1b6d2594.jpg)

<details>
<summary>line</summary>

| time(s) | R1 | y1 |
| --- | --- | --- |
| 0 | 0.6 | 0.6 |
| 500 | 0.95 | 0.95 |
| 1000 | 1.0 | 1.0 |
| 1500 | 1.0 | 1.0 |
| 2000 | 1.0 | 1.0 |
| 2500 | 1.0 | 1.0 |
| 3000 | 1.0 | 1.0 |
| 3500 | 1.0 | 1.0 |
| 4000 | 1.0 | 1.0 |
</details>

图 3-4 主回路阶跃响应

![](image/e5715e87d39f9473ede0b9797b4ccbc81074d0c4a6d6368b321bd3a759d19f3c.jpg)

<details>
<summary>line</summary>

| time(s) | disturbance |
| --- | --- |
| 0 | 0.008 |
| 500 | 0.006 |
| 1000 | 0.004 |
| 1500 | 0.002 |
| 2000 | 0.000 |
| 2500 | -0.002 |
| 3000 | -0.004 |
| 3500 | -0.006 |
| 4000 | -0.008 |
</details>

图 3-5 外加干扰信号

〖仿真程序〗 chap3\_1.m  
```matlab
%Series System Control
clear all;
close all;

ts=2;
sys1=tf(1,[10,1]);
dsys1=c2d(sys1,ts,'z');
[num1,den1]=tfdata(dsys1,'v');

sys2=tf(1,[10,1]);
dsys2=c2d(sys2,ts,'z');
[num2,den2]=tfdata(dsys2,'v');

dph=1/zpk('z',ts); 
```

```matlab
Gc2=dph/(dsys2*(1-dph));
[nump,denp]=tfdata(Gc2,'v');

u1_1=0.0;u2_1=0.0;
y1_1=0;y2_1=0;
e2_1=0;ei=0;

for k=1:1:2000
time(k)=k*ts;

R1(k)=1;
%Linear model
y1(k)=-den1(2)*y1_1+num1(2)*y2_1; %Main plant
y2(k)=-den2(2)*y2_1+num2(2)*u2_1; %Assistant plant
error(k)=R1(k)-y1(k);
ei=ei+error(k);
u1(k)=1.2*error(k)+0.02*ei; %Main Controller

e2(k)=u1(k)-y2(k); %Assistant Controller
u2(k)=-denp(2)*u2_1+nump(1)*e2(k)+nump(2)*e2_1;

d2(k)=0.01*rands(1);
u2(k)=u2(k)+d2(k);

%----Return of PID parameters----
u1_1=u1(k);
u2_1=u2(k);

e2_1=e2(k);

y1_1=y1(k);
y2_1=y2(k);
end

figure(1); %Assistant Control
plot(time,u1,'k',time,y2,'r:','linewidth',2);
xlabel('time(s)');ylabel('u1,y2');
legend('u1','y2');

figure(2); %Main Control
plot(time,R1,'k',time,y1,'r:','linewidth',2);
xlabel('time(s)');ylabel('R1,y1');
legend('R1','y1');

figure(3);
plot(time,d2,'r');
xlabel('time(s)');ylabel('disturbance'); 
```
