# 2.5.2 仿真实例

被控对象为

$$G (s) = \frac {1 3 3}{s ^ {2} + 2 5 s}$$

对比式（2.14），可得 $K_{g}=133/25$ ， $T_{g}=1/25$ ， $\omega_{g}=\frac{1}{T_{g}}=25$ 。

取最大相位裕度为 $\phi_{\mathrm{m}} = 60$ ，根据式（2.23）得 $\alpha = \left(\frac{1 + \sin\phi_{\mathrm{m}}}{\cos\phi_{\mathrm{m}}}\right)^2 = 13.9282$ 。根据式（2.17）～式（2.21）得 $\omega_{\mathrm{c}} = \omega_{\mathrm{g}} / \sqrt{\alpha} = 6.6987$ ， $\omega_{\mathrm{i}} = \omega_{\mathrm{g}} / \alpha = 1.7949$ ， $K_{\mathrm{p}} = \omega_{\mathrm{c}} / K_{\mathrm{g}} = 1.2592$ 。 $K(s)G(s)$ 的Bode图如图2-18所示，可见，所设计的方法符合对称整定法，闭环系统阶跃响应如图2-19所示。

![](image/8ce9f8b9baa3d9c9304f7da25904cbae2b13956a8bd49781c418bdcbf6d0e6b9.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Magnitude (dB) | Phase (deg) |
| --- | --- | --- |
| 10^-1 | 50 | -180 |
| 10^0 | 0 | -120 |
| 10^1 | -50 | -150 |
| 10^2 | -100 | -170 |
| 10^3 | -150 | -180 |
</details>

图 2-18 $K(s)G(s)$ 的 Bode 图（对称整定法）

![](image/46784bd7fd566d2142b1bb162855e813b4e292881befb9dbe871109cba3839b0.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.2 |
| 1.0 | 1.0 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
</details>

图 2-19 闭环系统阶跃响应

〖仿真程序〗 chap2\_7.m

```txt
clear all;
close all;
G=tf(133,[1 25 0]);
Kg=133/25;
Tg=1/25;
wg=1/Tg; 
```

```matlab
ph_max=60*pi/180; %Designed maximum phase margin
alfa=((1+sin(ph_max))/cos(ph_max))^2;

wc=wg/sqrt(alfa);
wi=wg/alfa;
Kp=wc/Kg;

K=Kp*tf([1 wi],[1 0]);

figure(1);
bode(G*K);

Gc=K*G/(1+K*G);
figure(2);
step(Gc); 
```

![](image/a4438ef3bff700ba14352ab2331eef79a9c27eec18856235db5f6c7a046bbb4b.jpg)
