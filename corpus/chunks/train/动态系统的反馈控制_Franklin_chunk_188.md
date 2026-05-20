(a) $F(s)=\frac{1}{s(s+1)^{2}}$ ;

(b) $F(s)=\frac{s^{2}+s+1}{s^{5}-1}$ ;

(c) $F(s)=\frac{2(s^{2}+s+1)}{s(s+1)^{2}}$ ;

(d) $F(s)=\frac{s^{3}+s+2}{s^{4}-4};$

(e) $F(s)=\frac{4}{s^{4}+4}$ ;

(f) $F(s)=\frac{2(s+2)(s+5)^{2}}{(s^{2}+1)^{2}}$ ;

(g) $F(s)=\arctan\left(\frac{1}{s}\right)$ 。

3.9 使用拉普拉斯变换求下列常微分方程。

(a) $\ddot{y}(t)+\dot{y}(t)+3y(t)=0;\quad y(0)=1,$ $\dot{y}(0)=2;$

(b) $\ddot{y}(t)-2\dot{y}(t)+4y(t)=0;\quad y(0)=1,$ $\dot{y}(0)=2;$

(c) $\ddot{y}(t)+\dot{y}(t)=\sin t;\quad y(0)=1,\quad \dot{y}(0)=2;$

(d) $\ddot{y}(t)+3y(t)=\sin t;\quad y(0)=1,\quad \dot{y}(0)=2;$

(e) $\ddot{y}(t)+2\dot{y}(t)=\mathrm{e}^{t}$ ; $y(0)=1$ , $\dot{y}(0)=2$ ;

(f) $\ddot{y}(t)+y(t)=t;\quad y(0)=1,\quad\dot{y}(0)=-1.$

3.10 利用卷积积分求系统的阶跃响应，已知该系统的脉冲响应如下式，曲线如图 3.44 所示。

$$
h (t) = \left\{ \begin{array}{l l} t \mathrm{e} ^ {- t}, & t \geqslant 0 \\ 0, & t <   0 \end{array} \right.
$$

![](image/c22d7fc79f1d5c5f129d2ef4e5e539f5b6408d4f4994953f1193b7facfc5ba9c.jpg)

<details>
<summary>line</summary>

| 时间/s | h(t) |
| --- | --- |
| 0 | 0.0000 |
| 1 | 0.3700 |
| 2 | 0.2800 |
| 3 | 0.1800 |
| 4 | 0.0800 |
| 5 | 0.0300 |
| 6 | 0.0100 |
| 7 | 0.0050 |
| 8 | 0.0020 |
| 9 | 0.0010 |
| 10 | 0.0005 |
</details>

图 3.44 习题 3.10 的脉冲响应

3.11 利用卷积积分求系统的阶跃响应，已知该系统的脉冲响应如下式，曲线如图 3.45 所示。

$$
h (t) = \left\{ \begin{array}{l l} 1, & 0 \leqslant t \leqslant 2, \\ 0, & t <   0 \text {或} t > 2 \end{array} \right.
$$

![](image/1eb62108c11ea83d792c306f916e0fedf13399d9d0af4c157ff7ac32da9a2205.jpg)

<details>
<summary>line</summary>

| 时间/s | h(t) |
| --- | --- |
| -1 | 0 |
| -0.5 | 0 |
| 0 | 1 |
| 0.5 | 1 |
| 1 | 1 |
| 1.5 | 1 |
| 2 | 1 |
| 2.5 | 0 |
| 3 | 0 |
</details>

图 3.45 习题 3.11 的脉冲响应

3.12 考虑标准二阶系统

$$G (s) = \frac {\omega_ {\mathrm{n}} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2}}$$

![](image/f83057dac5b97650ba3a74a1793adc07331584e83c2a76fc0ad73d449a72622a.jpg)

<details>
<summary>line</summary>

| 时间/s | u(t) |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 3 | 0 |
</details>

图 3.46 习题 3.12 的输入图

(a) 写出图 3.46 所示信号的拉普拉斯变换。  
(b) 如果将该信号用于 $G(s)$ 中，其输出的拉普拉斯变换是什么？  
(c) 输入如图 3.46 所示，求系统的输出。

3.13 将一转动载荷与一场控直流电动机相连，该电动机电感可忽略不计。当输入为恒值100V时，输出载荷在1/2s内达到速度为1rad/s的测试被应用到电动机终端。同样可测得其输出稳态速度为2rad/s。确定电机的传递函数 $\frac{\Theta(s)}{V_{\mathrm{f}}(s)}$ 。

3.14 图 3.47 所示为计算机磁带驱动器简图。
