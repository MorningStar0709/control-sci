# 1.3.4 增量式 PID 控制算法及仿真

当执行机构需要的是控制量的增量（例如驱动步进电机）时，应采用增量式 PID 控制。根据递推原理可得

$$u (k - 1) = k _ {\mathrm{p}} (\text { error } (k - 1) + k _ {\mathrm{i}} \sum_ {j = 0} ^ {k - 1} \text { error } (j) + k _ {\mathrm{d}} (\text { error } (k - 1) - \text { error } (k - 2))) \tag {1.6}$$

增量式 PID 控制算法

$$\Delta u (k) = u (k) - u (k - 1)\Delta u (k) = k _ {\mathrm{p}} (\text { error } (k) - \text { error } (k - 1)) + k _ {\mathrm{i}} \text { error } (k) + k _ {\mathrm{d}} (\text { error } (k) - 2 \text { error } (k - 1) + \text { error } (k - 2)) \tag {1.7}$$

根据增量式 PID 控制算法，设计了仿真程序，被控对象如下：

$$G (s) = \frac {4 0 0}{s ^ {2} + 5 0 s}$$

PID 控制参数： $k_{p}=8,\quad k_{i}=0.10,\quad k_{d}=10$ 。增量式 PID 阶跃跟踪结果如图 1-21 所示。

![](image/7795b553e0f7c1349949c937b5026ce707992873158d78380b6501f23cfd490c.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.1 | 0.8 | 0.8 |
| 0.2 | 0.9 | 0.9 |
| 0.3 | 0.95 | 0.95 |
| 0.4 | 0.98 | 0.98 |
| 0.5 | 0.99 | 0.99 |
| 0.6 | 0.995 | 0.995 |
| 0.7 | 0.998 | 0.998 |
| 0.8 | 0.999 | 0.999 |
| 0.9 | 0.9995 | 0.9995 |
| 1.0 | 1.0 | 1.0 |
</details>

图 1-21 增量式 PID 阶跃跟踪

〖仿真程序〗 chap1\_12.m

```matlab
%Increment PID Controller
clear all;
close all;

ts=0.001;
sys=tf(400,[1,50,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0.0;u_2=0.0;u_3=0.0;
y_1=0;y_2=0;y_3=0; 
```

```matlab
x=[0,0,0]';
error_1=0;
error_2=0;
for k=1:1:1000
    time(k)=k*ts;

    yd(k)=1.0;
    kp=8;
    ki=0.10;
    kd=10;

    du(k)=kp*x(1)+kd*x(2)+ki*x(3);
    u(k)=u_1+du(k);

    if u(k)>=10
    u(k)=10;
    end
    if u(k)<=-10
    u(k)=-10;
    end
    y(k)=-den(2)*y_1-den(3)*y_2+num(2)*u_1+num(3)*u_2;

    error=yd(k)-y(k);
    u_3=u_2;u_2=u_1;u_1=u(k);
    y_3=y_2;y_2=y_1;y_1=y(k);

    x(1)=error-error_1; %Calculating P
    x(2)=error-2*error_1+error_2; %Calculating D
    x(3)=error; %Calculating I

    error_2=error_1;
    error_1=error;
end

figure(1);
plot(time,yd,'r',time,y,'k','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('ideal position value','tracking position value'); 
```

由于控制算法中不需要累加，控制增量 $\Delta u(k)$ 仅与最近 k 次的采样有关，所以误动作时影响小，而且较容易通过加权处理获得比较好的控制效果。

在计算机控制系统中，PID 控制是通过计算机程序实现的，因此它的灵活性很大。一些原来在模拟 PID 控制器中无法实现的问题，在引入计算机以后，就可以得到解决，于是产生了一系列的改进算法，形成非标准的控制算法，以改善系统品质，满足不同控制系统的需要。

![](image/b50d272195ce9cce6785f99f1a8954032554e31506399bbe6ae26cbf81073415.jpg)
