# 【仿真实例】

被控对象为

$$G (s) = \frac {5 2 3 5 0 0}{s ^ {3} + 8 7 . 3 5 s ^ {2} + 1 0 4 7 0 s}$$

采样时间为1ms，对象输出上有一个幅值为0.5的正态分布的随机干扰信号。采用积分分离式PID控制算法进行阶跃响应，取 $\varepsilon = 0.20$ ，死区参数 $e_0 = 0.10$ ，采用低通滤波器对对象输出信号进行滤波，滤波器为

![](image/0b7ac9abf040752988b708530c218785c3354d9f89cae63f3ac92d4f56c720e2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["开始"] --> B["y_d(k), y(k)"]
    B --> C["e(k)=y_d(k)-c(k)"]
    C --> D{|e(k)|≤|e_o|?}
    D -->|是| E["u(k)=0"]
    D -->|否| F["u(k)=u_p(k)+u_l(k)+u_D(k)"]
    E --> G["u(k)"]
    F --> G
    G --> H["返回"]
```
</details>

图 1-45 带死区的 PID 控制算法程序框图

取 M=1，采用一般积分分离式 PID 控制方法，其控制结果如图 1-46 所示。取 M=2，采用带死区的积分分离式 PID 控制方法，其控制结果如图 1-47 所示。由仿真结果可以看出，引入带死区 PID 控制后，控制器输出更加平稳。

![](image/d7721588bcff9168e6713f3cef9a2e288b754ff30da1689e2652ad7f42be3e4a.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 1.0 | 1.0 |
| 0.2 | ~1.0 | ~1.0 |
| 0.4 | ~1.0 | ~1.0 |
| 0.6 | ~1.0 | ~1.0 |
| 0.8 | ~1.0 | ~1.0 |
| 1.0 | ~1.0 | ~1.0 |
| 1.2 | ~1.0 | ~1.0 |
| 1.4 | ~1.0 | ~1.0 |
| 1.6 | ~1.0 | ~1.0 |
| 1.8 | ~1.0 | ~1.0 |
| 2.0 | ~1.0 | ~1.0 |
</details>

图 1-46 不带死区 PID 控制 (M=1)

![](image/12ff7ad882fbd64c6ea503fe64b88200a64956230c7ab1960e4e26a6326325c6.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 1.0 | 1.0 |
| 0.2 | 1.0 | 1.0 |
| 0.4 | 1.0 | 1.0 |
| 0.6 | 1.0 | 1.0 |
| 0.8 | 1.0 | 1.0 |
| 1.0 | 1.0 | 1.0 |
| 1.2 | 1.0 | 1.0 |
| 1.4 | 1.0 | 1.0 |
| 1.6 | 1.0 | 1.0 |
| 1.8 | 1.0 | 1.0 |
| 2.0 | 1.0 | 1.0 |
</details>

![](image/5f7c1aa8aaa9402db46a38f1ea003fbf9a307d9b949234714062dda56e1d1f48.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 0.0 |
| 0.4 | 0.0 |
| 0.6 | 0.0 |
| 0.8 | 0.0 |
| 1.0 | 0.0 |
| 1.2 | 0.0 |
| 1.4 | 0.0 |
| 1.6 | 0.0 |
| 1.8 | 0.0 |
| 2.0 | 0.0 |
</details>

图 1-47 带死区 PID 控制 (M=2)

〖仿真程序〗 chap1\_22.m  
```matlab
%PID Controller with dead zone
clear all;
close all;

ts=0.001;
sys=tf(5.235e005,[1,87.35,1.047e004,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;u_3=0;u_4=0;u_5=0;
y_1=0;y_2=0;y_3=0;
yn_1=0;
error_1=0;error_2=0;ei=0;

sys1=tf([1],[0.04,1]); %Low Freq Signal Filter
dsys1=c2d(sys1,ts,'tucsin');
[num1,den1]=tfdata(dsys1,'v');
f_1=0;

for k=1:1:2000
time(k)=k*ts;

yd(k)=1; %Step Signal
