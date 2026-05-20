# 1.3.15 PID 控制的方波响应

设被控对象为一延迟对象

$$G (s) = \frac {\mathrm{e} ^ {- 8 0 s}}{6 0 s + 1}$$

采样时间为 20s，延迟时间为 4 个采样时间，即 80s，被控对象离散化为

$$y (k) = - \mathrm{den} (2) y (k - 1) + \mathrm{num} (2) u (k - 5)$$

由于方波信号的速度、加速度不连续，当位置跟踪指令为方波信号时，如采用滤波器对指令信号进行滤波，将滤波输出作为给定信号，可使方波响应及执行器的动作更加平稳，在工程上具有一定意义。

为了保证滤波后幅值不变，取三阶离散滤波器为

$$
\begin{array}{l} F (z - 1) = a _ {1} + a _ {2} z ^ {- 1} + a _ {1} z ^ {- 2} \\ 2 a _ {1} + a _ {2} = 1 \\ \end{array}
$$

取方波信号为 $y_{\mathrm{d}}(t)=\mathrm{sgn}\left(\sin\left(0.0001\pi t\right)\right)$ ，滤波器参数取 $a_{1}=0.10,\quad a_{2}=0.80$ 。

分两种情况进行仿真：M=1 时，为普通方波指令信号，方波响应结果如图 1-54 所示；M=2 时，为加滤波的方波指令信号，方波响应结果如图 1-55 所示。

可见，将方波指令信号加滤波后，方波响应更加平稳，控制输入信号的抖动消除。

![](image/a1b36e96cc8a30e1365266b972a68f2a5db9521d99809e3489a7da3fe51e97d6.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 10000 | -1.0 | -1.0 |
| 20000 | -1.0 | -1.0 |
| 30000 | 1.0 | 1.0 |
</details>

![](image/7fe11b10fbe25ac8c43671d6eba4ff7bfe3e731a6c648c98a7e10ab4ae7f1144.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0 | 0.5 |
| 10000 | -1.5 |
| 20000 | 1.5 |
| 30000 | 1.5 |
</details>

图 1-54 普通方波指令信号的 PID 响应和控制输入（M=1）

![](image/812a4ad2a9bec05b38e0530f032ff1538d9c055dc10b76f38b056e4cb7825706.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 10000 | -1.0 | -1.0 |
| 20000 | 1.0 | 1.0 |
| 30000 | 1.0 | 1.0 |
</details>

![](image/3d48a92ba0af4fde4ce62053b425926d2a84a4e8baf38e6c1a18198880e157b5.jpg)

<details>
<summary>line</summary>

| time(s) | Control Input |
| --- | --- |
| 0 | 0.5 |
| 10000 | -1.0 |
| 20000 | 0.5 |
| 30000 | 1.0 |
</details>

图 1-55 带滤波器的方波指令信号 PID 响应和控制输入（M=2）

〖仿真程序〗 chap1\_25.m  
```matlab
%PID Controller for Square Tracking with Filtered Signal
clear all;
close all;

ts=20;
sys=tf([1],[60,1],'inputdelay',80);
dsys=c2d(sys,ts,'zoh');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;u_3=0;u_4=0;u_5=0;
y_1=0;
error_1=0;
ei=0; 
```

```matlab
yd_1=0;yd_2=0;
for k=1:1:1500
time(k)=k*ts;

yd(k)=1.0*sign(sin(0.00005*2*pi*k*ts));

M=1;
switch M;
case 1
    yd(k)=yd(k);
case 2
    yd(k)=0.10*yd(k)+0.80*yd_1+0.10*yd_2;
end

%Linear model
y(k)=-den(2)*y_1+num(2)*u_5;

kp=0.80;
kd=10;
ki=0.002;

error(k)=yd(k)-y(k);
ei=ei+error(k)*ts;

u(k)=kp*error(k)+kd*(error(k)-error_1)/ts+ki*ei;

%Update parameters
u_5=u_4;u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
y_1=y(k);

error_2=error_1;
error_1=error(k);
yd_2=yd_1;
yd_1=yd(k);
end

figure(1);
subplot(211);
plot(time,yd,'',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
subplot(212);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input'); 
```

![](image/4a4fd95e9d22589e1989ac637fa8af6eff9423eab7cf67fa3ee61132f52ad300.jpg)
