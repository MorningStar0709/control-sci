# 【仿真实例】

被控对象为

$$G (s) = \frac {5 2 3 5 0 0}{s ^ {3} + 8 7 . 3 5 s ^ {2} + 1 0 4 7 0 s}$$

采样时间为 1ms，输入指令信号为 R=20。采用本控制算法进行阶跃响应。其中 M=1 时为积分分离式 PID 控制，响应结果，如图 1-51 所示；M=2 时为步进式积分分离 PID 控制，响应结果及输入信号的变化如图 1-52 和图 1-53。

![](image/58c71eab019c6e3d80aa0856aaaca545a5d42d28c7324cfb718ac0528a38c592.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0 | 0 |
| 0.1 | 20 | 20 |
| 0.2 | 20 | 20 |
| 0.3 | 20 | 20 |
| 0.4 | 20 | 20 |
| 0.5 | 20 | 20 |
| 0.6 | 20 | 20 |
| 0.7 | 20 | 20 |
| 0.8 | 20 | 20 |
| 0.9 | 20 | 20 |
| 1.0 | 20 | 20 |
</details>

![](image/83aa6472b00c9dd9b4cefa514789e17ef0bfe910aa5e419d217c6e69c042ca6b.jpg)

<details>
<summary>line</summary>

| time(s) | Control Input |
| --- | --- |
| 0.0 | 10.0 |
| 0.1 | 0.0 |
| 0.2 | 0.0 |
| 0.3 | 0.0 |
| 0.4 | 0.0 |
| 0.5 | 0.0 |
| 0.6 | 0.0 |
| 0.7 | 0.0 |
| 0.8 | 0.0 |
| 0.9 | 0.0 |
| 1.0 | 0.0 |
</details>

图 1-51 积分分离阶跃响应（M=1）  
![](image/7e03d40254ec796f6516349cd50d0a5bb413f71f607012db5ce0f46e8fcf6c76.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.1 | ~2.0 | ~1.8 |
| 0.2 | ~6.0 | ~5.5 |
| 0.3 | ~12.0 | ~11.0 |
| 0.4 | ~20.0 | ~19.5 |
| 0.5 | ~20.0 | ~19.5 |
| 0.6 | ~20.0 | ~19.5 |
| 0.7 | ~20.0 | ~19.5 |
| 0.8 | ~20.0 | ~19.5 |
| 0.9 | ~20.0 | ~19.5 |
| 1.0 | ~20.0 | ~19.5 |
</details>

![](image/d5c3bb5329affa716a171baf7b852dfbffd18ba798591a3d5b44011bccf6ac21.jpg)

<details>
<summary>line</summary>

| time(s) | Control Input |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 0.5 |
| 0.2 | 1.0 |
| 0.3 | 1.5 |
| 0.4 | 2.0 |
| 0.5 | 0.0 |
| 0.6 | 0.0 |
| 0.7 | 0.0 |
| 0.8 | 0.0 |
| 0.9 | 0.0 |
| 1.0 | 0.0 |
</details>

图 1-52 步进式积分分离阶跃响应和控制输入（M=2）  
![](image/0c66a3f7d769ae2badfdcacae57e4138db4bfbb5c4ec3cb715ef64e6e781c233.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position value |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 2.0 |
| 0.2 | 6.0 |
| 0.3 | 12.0 |
| 0.4 | 20.0 |
| 0.5 | 20.0 |
| 0.6 | 20.0 |
| 0.7 | 20.0 |
| 0.8 | 20.0 |
| 0.9 | 20.0 |
| 1.0 | 20.0 |
</details>

图 1-53 步进式阶跃信号 $y_{\mathrm{d}}(k)$ 的变化

〖仿真程序〗 chap1\_24.m  
```matlab
%PID Control with Gradual approaching input value
clear all;
close all;

ts=0.001;
sys=tf(5.235e005,[1,87.35,1.047e004,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;u_3=0;u_4=0;u_5=0;
y_1=0;y_2=0;y_3=0;
error_1=0;error_2=0;ei=0;

kp=0.50;ki=0.05;
rate=0.25;
ydi=0.0;

for k=1:1:1000
time(k)=k*ts;
R=20; %Step Signal
