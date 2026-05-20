(1) 当 $\omega_{i}=0$ 时， $|G(j0)|=\sqrt{\frac{1}{\left(\frac{0}{a}\right)^{2}+1}}=1$ 。  
(2) 随着 $\omega_{i}$ 的增加， $|G(j\omega_{i})|$ 会不断地降低。  
(3) 当 $\omega_{i}=a$ 时， $|G(ja)|=\sqrt{\frac{1}{\left(\frac{a}{a}\right)^{2}+1}}=\sqrt{\frac{1}{1+1}}=0.707$ 。  
(4) 当 $\omega_{\mathrm{i}} \to \infty$ 时, $\frac{\omega_{\mathrm{i}}}{a} \to \infty$ , 此时 $\lim_{\omega_{\mathrm{i}} \to \infty} |G(\mathrm{j}\omega_{\mathrm{i}})| = \lim_{\omega_{\mathrm{i}} \to \infty} \sqrt{\frac{1}{\left(\frac{\omega_{\mathrm{i}}}{a}\right)^2 + 1}} = 0$ 。

同理,分析式(9.3.2b),可得:

(1) 当 $\omega_{i}=0$ 时， $\angle G(j0)=-\arctan\frac{0}{a}=0$ 。  
(2) 随着 $\omega_{i}$ 的增加， $\angle G(j\omega_{i})$ 会不断地降低。  
(3) 当 $\omega_{i}=a$ 时， $\angle G(j\omega_{i})=-\arctan\frac{\omega_{i}}{a}=-\frac{\pi}{4}$ 。  
(4) 当 $\omega_{i}\rightarrow\infty,\frac{\omega_{i}}{a}\rightarrow\infty$ 时， $\angle G(j\omega_{i})=\lim_{\omega_{i}\rightarrow\infty}\left(-\arctan\frac{\omega_{i}}{a}\right)=-\frac{\pi}{2}$

根据上述分析, 当 $G(s)=\frac{a}{s+a}$ 时, $\left|G(j\omega_{i})\right|$ 和 $\angle G(j\omega_{i})$ 随 $\omega_{i}$ 的变化示意图如图 9.3.2 所示。

![](image/382a3a2ad3f4e395788bb05d4ec9577eef6acf0b2af61ee8bd88f4bcff3298e3.jpg)  
(a) $\left|G(j\omega_{i})\right|$ 随 $\omega_{i}$ 的变化

![](image/ff7184d3ea4f9c04439dcf7d057e82201d3571af2619931df5c7a135a534f468.jpg)

<details>
<summary>line</summary>

| ω_i | ∠G(jω_i) |
| --- | -------- |
| 0   | 0        |
| a     | -π/4     |
| a     | -π/2     |
</details>

(b) $\angle G(\mathrm{j}\omega_{\mathrm{i}})$ 随 $\omega_{\mathrm{i}}$ 的变化  
图 9.3.2 $G(s)=\frac{a}{s+a}$ 的频率响应

从信号处理的角度来分析, 观察图 9.3.2(a) 可以发现, $G(s) = \frac{a}{s + a}$ 是一个低通滤波器。其中, $a$ 被称为截止频率 (Cut-off Frequency)。当输入信号频率 $\omega_{i} < a$ 时, 振幅大部分会被保留下来; 而当 $\omega_{i} > a$ 时, 振幅就会被缩小, 而且 $\omega_{i}$ 越大, 输出的振幅就越小。正是因为这个性质, 在实际应用中, 一阶系统常常被用来降噪。一般情况下, 噪声信号与信息信号相比多为高频率、小振幅的信号。如图 9.3.3 所示, 有效信号是频率 $\omega_{i} = 1$ 的正弦信号 $\sin t$ 。在使用传感器采集数据的时候, 同时还采集到了高频噪声, 因此得到的输入信号就有很多“毛刺”。将其输入到一个低通滤波器 $G(s) = \frac{a}{s + a} = \frac{1}{s + 1}$ 之后, 原始的正弦信号被保留下来, 大部分的高频噪声则被过滤掉了, 因此得到了一条光滑的曲线。另外, 因为 $G(s)$ 截止频率 $a = 1$ , 所以当输入频率为 $\omega_{i} = 1$ 时, 输出的振幅是原来的 0.707 倍, $|G(j\omega_{i})| = 0.707$ 。

在信号处理学科中, $G(s)=\frac{1}{s+1}$ 被称为一阶巴特沃思滤波器(Butterworth Filter)。有兴趣的读者可以参考相关资料。

![](image/df618eba82808192504243e7685b21e5e07f1d938dfdf3ca81538a8e48f74224.jpg)
