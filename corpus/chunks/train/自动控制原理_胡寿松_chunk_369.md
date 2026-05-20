根据主导极点思想,可将校正后的系统等价为二阶系统。由 $\sigma \%$ 及 $t_s$ 要求,可以近似求出系统的阻尼比 $\zeta$ 、无阻尼自然频率 $\omega_{n}$ 及要求的相角裕度 $\gamma$ 。由性能指标要求:

$$\sigma \% = 100 \mathrm{e} ^ {- \pi \zeta / \sqrt {1 - \zeta^ {2}}} \% = 10 \%t _ {s} = \frac {4 . 4}{\zeta \omega_ {n}} = 3 \mathrm{s} (\Delta = 2 \%)$$

解得 $\zeta=0.59$ 和 $\omega_{n}=2.49$ 。再由式(6-5)

$$\gamma = \arctan \frac {2 \zeta}{\sqrt {\sqrt {1 + 4 \zeta^ {4}} - 2 \zeta^ {2}}}$$

求出 $\gamma=59.2^{\circ}\approx60^{\circ}$

明确了以上频域设计要求后,可采用如下步骤及 MATLAB 文本在频域内设计超前校正网络:

1) 由 $e_{s}(\infty)$ 要求，取 $K_{1} = 500$ ，绘出未校正系统的伯德图，并计算已有相角裕度。  
2）确定所需的附加超前相角 $\varphi_{m}$ 。  
3）根据最大超前角公式(6-21)

$$\sin \varphi_ {m} = \frac {a - 1}{a + 1}$$

计算超前网络的分度系数

$$a = \frac {1 + \sin \varphi_ {m}}{1 - \sin \varphi_ {m}}$$

4）计算 $10 \lg a$ ，在未校正系统的伯德图上确定与幅值增益 $-10 \lg a$ 对应的最大超前角频率 $\omega_{m}$ 。以上过程的程序文本如图 6-38 所示。

![](image/e678ede2554aca3cb079602b2a9f8ffc1f800580ed7547ed6df5376b73e3ae37.jpg)  
(a) 伯德图  
图 6-38 程序文本与仿真(MATLAB)

```matlab
K1=500; numg=[1]; deng=[1,15,50,0];
[num,den]=series(K1,1,numg,deng);
w=logspace(-1,2,200);
[mag,phase,w]=bode(num,den,w);
[Gm,Pm,Wcg,Wcp]=margin(mag,phase,w); %计算已有相角裕度
Phi=(60-Pm)*pi/180; %计算所需的附加超前相角
a=(1+sin(Phi))/(1-sin(Phi)); %计算a
M=-10*log10(a)*ones(length(w),1); %为确定ωm，绘制-10lga线
[mag,phase,w]=bode(num,den,w);
semilogx(w,20*log10(mag),w,M); grid
(b) MATLAB文本
```  
图 6-38 程序文本与仿真(MATLAB)(续)

5) 在频率 $\omega_{m}$ 附近绘校正后系统的对数幅频渐近线，该渐近线在 $\omega_{m}$ 处与 0dB 线相交，其斜率等于未校正时的斜率加上 20dB/dec；由该渐近线与未校正系统对数幅频曲线的交点，可确定超前校正网络的零点 z；由 p=az 得到超前校正网络的极点 p。  
6）绘制校正后系统的伯德图，检验所得系统的相角裕度是否满足设计要求，若不满足，则重复以上设计步骤。  
7) 加大系统增益 $K_{1}$ ，例如取 $K_{1}=1800$ ，以补偿由超前校正网络带来的幅值衰减 $(1/a)$ 。  
以上过程如图 6-39 所示的程序文本。

![](image/af53534d0b3709d7c6fd639b410b9555b835e81487463b9a986d021c69a8b66f.jpg)

(a) 校正后的伯德图  
```matlab
K1=1800;
G0=tf([1],[1,15,50,0]);
Gc=tf(K1*[1,3.5],[1,25]); %超前校正网络传递函数
G=series(G0,Gc);
margin(G);grid
(b) MATLAB 文本
```  
图 6-39 超前校正网络文本与仿真(MATLAB)

8) 仿真计算系统的阶跃响应, 验证最后的设计结果。若设计结果不能满足要求, 则重复前面的设计步骤。本步骤的程序文本如图 6-40 所示。

![](image/e38d1b9e87bc7ea5a578605163a71f87d862e5fe7a4bd5034dabe9778534865f.jpg)

<details>
<summary>line</summary>

| Time /sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.1 |
| 1.0 | 1.0 |
| 1.5 | 1.0 |
</details>
