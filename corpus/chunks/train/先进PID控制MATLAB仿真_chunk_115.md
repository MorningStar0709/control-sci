# 【仿真之一】采用 M 语言进行仿真

分三种情况进行：M=1 时，为未加噪声信号；M=2 时，为加噪声信号未加滤波；M=3 时，为加噪声信号加滤波。阶跃响应结果如图 1-34～图 1-36 所示。

![](image/7432ca38954f039fd015c6d96a8ebeeb961ec8f0d0839d4377abf53383d2356e.jpg)

图 1-34 普通 PID 控制阶跃响应 (M=1)  
![](image/c12dc7c2b193b77bf0579623bd3777916c824e67eaa412e5f8ac8f547ec1d4ee.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0 | 0 |
| 0.1 | ~15 | ~15 |
| 0.2 | ~20 | ~20 |
| 0.3 | ~22 | ~22 |
| 0.4 | ~23 | ~23 |
| 0.5 | ~24 | ~24 |
| 0.6 | ~25 | ~25 |
| 0.7 | ~26 | ~26 |
| 0.8 | ~27 | ~27 |
| 0.9 | ~28 | ~28 |
| 1.0 | ~29 | ~29 |
</details>

![](image/0b13144e74c0989d3e4b07bb43a7fd4d89165a66574029595de8cb845a65bdc4.jpg)

<details>
<summary>line</summary>

| time(s) | u |
| --- | --- |
| 0.0 | 4.5 |
| 0.1 | 2.0 |
| 0.2 | 1.0 |
| 0.3 | 0.5 |
| 0.4 | 0.3 |
| 0.5 | 0.2 |
| 0.6 | 0.1 |
| 0.7 | 0.1 |
| 0.8 | 0.1 |
| 0.9 | 0.1 |
| 1.0 | 0.1 |
</details>

图 1-35 无滤波器时 PID 控制阶跃响应 (M=2)

![](image/18dafe61b9c01d85178e5a439ba8e1bb67c451b16550cd2aff87f031833f392f.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0 | 0 |
| 0.1 | 15 | 15 |
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

![](image/35b382bc94cbe8721e7cd710e6352845c60e6f5b8e4df69487b2a07c3e542f09.jpg)

<details>
<summary>line</summary>

| time(s) | y |
| --- | --- |
| 0.0 | 4.0 |
| 0.1 | 2.0 |
| 0.2 | 0.5 |
| 0.3 | 0.0 |
| 0.4 | 0.0 |
| 0.5 | 0.0 |
| 0.6 | 0.0 |
| 0.7 | 0.0 |
| 0.8 | 0.0 |
| 0.9 | 0.0 |
| 1.0 | 0.0 |
</details>

图 1-36 加入滤波器后 PID 控制阶跃响应（M=3）

〖仿真程序〗 chap1\_18.m  
```matlab
%PID Controller with Partial differential
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

kp=0.20;ki=0.05;

sys1=tf([1],[0.04,1]); %Low Freq Signal Filter
dsys1=c2d(sys1,ts,'tucsin');
[num1,den1]=tfdata(dsys1,'v');
f_1=0;

M=3;
for k=1:1:1000
time(k)=k*ts;

yd(k)=20; %Step Signal
%Linear model
y(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(2)*u_1+num(3)*u_2+num(4)*u_3;
if M==1 %No noisy signal 
```

```matlab
error(k)=yd(k)-y(k);
filty(k)=y(k);
end

n(k)=5.0*rands(1); %Noisy signal
yn(k)=y(k)+n(k);

if M==2 %No filter
    filthy(k)=yn(k);
    error(k)=yd(k)-filty(k);
end
