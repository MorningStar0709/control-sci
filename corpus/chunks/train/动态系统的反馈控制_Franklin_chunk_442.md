# 例 7.22 倒立摆的对称根轨迹设计

画出简单倒立摆的线性化方程的对称根轨迹图，令 $\omega_{0}=1$ 。取输出 z 为位置的两倍加上速度的和（使得位置和速度都加重或减弱）。

解答。系统的运动方程为

$$
\dot {\pmb {x}} = \left[ \begin{array}{l l} 0 & 1 \\ \omega_ {0} ^ {2} & 0 \end{array} \right] \pmb {x} + \left[ \begin{array}{l} 0 \\ - 1 \end{array} \right] \pmb {u} \tag {7.118}
$$

对于给定的输出，即 $2 \times$ 位置 + 速度，通过下式计算输出：

$$
z = \left[ \begin{array}{l l} 2 & 1 \end{array} \right] x \tag {7.119}
$$

由式 $(7.118)$ 和式 $(7.119)$ 计算，得

$$G _ {0} (s) = - \frac {s + 2}{s ^ {2} - \omega_ {0} ^ {2}} \tag {7.120}$$

对称 $0^{\circ}$ 根轨迹如图 7.24 所示。生成对称根轨迹的 Matlab 语句（对于 $\omega_{0}=1$ ）如下。

$$
\begin{array}{l} s = t f \left(^ {\prime} s ^ {\prime}\right); \\ G = - (s + 2) / (s ^ {2} - 1); \\ G 1 = - (- s + 2) / (s ^ {2} - 1); \\ \text { sysGG } = \text { G } ^ {*} \text { G1 }; \\ r l o c u s (s y s G G); \\ \end{array}
$$

对于 $\rho=1$ ，闭环极点为 $-1.36\pm j0.606$ 时，相应的 K=[-2.23 -2.73]，如果将本例中的系统矩阵代入到求解输入增益的式(7.97)中，则得到解为

$$
\mathbf {N} _ {x} = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right]
N _ {u} = 1\overline {{{N}}} = - 1. 2 3
$$

利用这些值，用 $N_{x}$ 和 $N_{u}$ 表示的控制律表达式(7.89b)可简化为

$$u = - K x + \overline {{N}} r$$

相应的位置阶跃响应如图 7.25 所示。

![](image/3235395feddb66e40e5eb584ccfcc5d6cdbb26a74b94b0fba7e55f00d2161013.jpg)

<details>
<summary>other</summary>

| Re(s) | Im(s) |
| --- | --- |
| -1 | 0 |
| 1 | 0 |
</details>

图 7.24 倒立摆的对称根轨迹设计

![](image/69fba1402bd91fb775ae2f155f9167b2e647700269e0cacffe0939f7864ea7c6.jpg)

<details>
<summary>line</summary>

| 时间/s | 位置, x₁ |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.2 |
| 1.0 | 0.4 |
| 1.5 | 0.6 |
| 2.0 | 0.8 |
| 2.5 | 0.9 |
| 3.0 | 0.95 |
| 3.5 | 0.98 |
| 4.0 | 0.99 |
| 4.5 | 1.0 |
</details>

图 7.25 倒立摆的阶跃响应

作为本节的最后一个例子，考虑磁带伺服电动机并介绍 LQR 设计，使用计算机直接求解出最优控制律。

从式(7.106)和式(7.108)可知，求解最优控制律需要的信息由系统矩阵 A, B 和输出矩阵 $C_{1}$ 给出。包括 Matlab 在内的大多数计算机辅助软件包都使用式(7.106)的更一般形式

$$\mathcal {J} = \int_ {0} ^ {\infty} (\boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {x} + \boldsymbol {u} ^ {\mathrm{T}} \boldsymbol {R} \boldsymbol {u}) \mathrm{d} t \tag {7.121}$$

如果取 $Q=\rho C_{1}^{T}C_{1}$ 和 R=1，则式(7.121)可化简为更简单的形式如式(7.106)。直接求解最优控制增益的 Matlab 语句为

$$\mathrm{K} = \mathrm{lqr} (\mathrm{A}, \mathrm{B}, \mathrm{Q}, \mathrm{R}) \tag {7.122}$$

开始 LQR 设计迭代的一个合理方法由布鲁森(Bryson)规则给出(Bryson 和 Ho, 1969)。在实际应用中，选取合理的 x 和 u 值的一个合适的方法是对角矩阵 Q 和 R 的初始选择满足

$$Q _ {i i} = 1 / [ x _ {i} ^ {2} ] \text { 的最大合理值 }R _ {i i} = 1 / [ u _ {i} ^ {2} ] \text { 的最大合理值 }$$

然后在逐步迭代过程中修正加权矩阵，使得在性能和控制量之间取得合理的折中。
