# 【仿真实例 1】基于低通滤波器的信号处理

设低通滤波器为

$$Q (s) = \frac {1}{0 . 0 4 s + 1}$$

采样时间为 1ms，输入信号为带有高频正弦噪声（100Hz）的低频（0.2Hz）正弦信号。采用低通滤波器滤掉高频正弦信号。滤波器的离散化采用 Tustin 变换，其 Bode 图如图 1-32 和图 1-33 所示。仿真结果表明，该滤波器对高频信号具有很好的滤波作用。

![](image/36d0bd74fd18b5dd829e28ff4a864f9dd970999662b2f6597b64377c9792f6cc.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Magnitude(dB) | Phase (deg) |
| --- | --- | --- |
| 1 | 0 | 0 |
| 10 | -5 | -45 |
| 100 | -20 | -85 |
| 1000 | -35 | -90 |
</details>

图 1-32 低通滤波器 Bode 图

![](image/5811001b25f0126074b47666db8215f5cc9caf3832bb979bed687e5e748b748e.jpg)

<details>
<summary>line</summary>

| time(s) | ideal signal,yd |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.2 |
| 1.0 | 0.4 |
| 1.5 | 0.5 |
| 2.0 | 0.4 |
| 2.5 | 0.2 |
| 3.0 | 0.0 |
| 3.5 | -0.2 |
| 4.0 | -0.4 |
| 4.5 | -0.2 |
| 5.0 | 0.0 |
</details>

![](image/ac14a91601bc19deb7a4b63f192c2450d2cf4b9b3a3911002c42cd202d614cf1.jpg)

<details>
<summary>line</summary>

| time(s) | filtered signal, y |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.3 |
| 1.0 | 0.5 |
| 1.5 | 0.4 |
| 2.0 | 0.2 |
| 2.5 | -0.1 |
| 3.0 | -0.4 |
| 3.5 | -0.6 |
| 4.0 | -0.5 |
| 4.5 | -0.3 |
| 5.0 | 0.0 |
</details>

图 1-33 原始信号及滤波后信号

〖仿真程序〗 chap1\_17.m  
```matlab
%Low Pass Filter
clear all;
close all;

ts=0.001;
Q=tf([1],[0.04,1]); %Low Freq Signal Filter
Qz=c2d(Q,ts,'tucsin');
[num,den]=tfdata(Qz,'v');

y_1=0;y_2=0;
yd_1=0;yd_2=0;
for k=1:1:5000
time(k)=k*ts;

%Input Signal with noise
n(k)=0.10*sin(100*2*pi*k*ts); %Noise signal
yd(k)=n(k)+0.50*sin(0.2*2*pi*k*ts); %Input Signal

y(k)=-den(2)*y_1+num(1)*yd(k)+num(2)*yd_1;

y_2=y_1;y_1=y(k);
yd_2=yd_1;yd_1=yd(k);
end

figure(1);bode(Q);
figure(2);
subplot(211);
plot(time,yd,'k','linewidth',2);
xlabel('time(s)');ylabel('ideal signal,yd');
subplot(212); 
```

```matlab
plot(time,y,'k','linewidth',2);
xlabel('time(s)');ylabel('filtered signal,y'); 
```
