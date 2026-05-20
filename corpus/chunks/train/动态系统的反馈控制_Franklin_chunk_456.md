# 例 7.26 单摆的对称根轨迹估计器设计

令 $\omega_{0}=1$ ，画出单摆线性化方程的估计器对称根轨迹。取输出为位置的噪声测量，该测量的噪声强度比为 q。

解答。已知系统方程

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - \omega_ {0} ^ {2} & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] w

y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + v
$$

由式 $(7.164)$ 可得

$$G _ {\mathrm{e}} (s) = \frac {1}{s ^ {2} + \omega_ {0} ^ {2}}$$

$180^{\circ}$ 的对称根轨迹如图7.34所示。生成对于 $\omega_{0}=1$ ，对称根轨迹的MATLAB语句如下：

$$
\begin{array}{l} \text {s = tf('s');} \\ \text {G = 1 / (s^2 + 1);} \\ \text {sysGG = G*G;} \\ \text {rlocus(sysGG);} \end{array}
$$

![](image/155817dcaecea2cba5f83f04bb472aeae94cc3de02201b663b4165bac46dc5ec.jpg)

<details>
<summary>line</summary>

| 实轴 | 虚轴 (q=365) | 虚轴 (q=0) |
| --- | --- | --- |
| 5 | 5 | 5 |
| 4 | 4 | 4 |
| 3 | 3 | 3 |
| 2 | 2 | 2 |
| 1 | 1 | 1 |
| 0 | 0 | 0 |
| 1 | -1 | -1 |
| 2 | -2 | -2 |
| 3 | -3 | -3 |
| 4 | -4 | -4 |
| 5 | -5 | -5 |
</details>

图 7.34 倒立摆估计器设计的对称根轨迹

对于给定值 q，选择两个稳定的根，比如对于 q=365， $s=-3+j3.18$ ，然后用于估计器极点配置。
