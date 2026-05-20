$$
\left[ \begin{array}{c c} s I - A _ {o} & B _ {o} \\ - C _ {o} & 0 \end{array} \right] \sim \left[ \begin{array}{c c} I _ {s} & 0 \\ 0 & N _ {L} (s) \end{array} \right]
$$

9.10 给定 $N(s)D^{-1}(s)$ ，其中

$$
N (s) = [ s + 2 \quad s + 1 ], D (s) = \left[ \begin{array}{c c} s + 1 & 0 \\ s ^ {2} + s - 2 & s - 1 \end{array} \right]
$$

试判断其控制器形实现是否为最小实现，并定出控制器形实现的维数。

9.11 设有 $q \times p$ 的 $G(s) = N(s)D^{-1}(s) = D_{L}^{-1}(s)N_{L}(s)$ 均为不可简约的 MFD,

试论证：

(i) $N(s)D^{-1}(s)$ 的控制器形实现和 $D_{L}^{-1}(s)N_{L}(s)$ 的观测器形实现在维数上是否相同；

(ii) 这两个实现之间是否是代数等价的；.

(iii) 如果 $N(s)D^{-1}(s)$ 和 $D_{L}^{-1}(s)N_{L}(s)$ 中有一个是可简约的，则对上述问题作出的回答是否仍然是正确的，如不正确则应作何更改。

9.12 设 $(A, B, C)$ 和 $(\overline{A}, \overline{B}, \overline{C})$ 是给定传递函数矩阵 $G(s)$ 是任意两个最小实现，试推导两个实现的能控性格拉姆矩阵 $W_{c}[0, t_{a}]$ 和 $\overline{W}_{c}[0, t_{a}]$ 及两个实现的能观测性格拉姆矩阵 $W_{o}[0, t_{a}]$ 和 $\overline{W}_{o}[0, t_{a}]$ 间的关系式。

9.13 设 $N(s)D^{-1}(s)$ 为 $q \times p$ 的严格真右 MFD，且有

$$N (s) = N _ {0} + N _ {1} s + \dots + N _ {\mu - 1} s ^ {\mu - 1}D (s) = D _ {0} + D _ {1} s + \dots + D _ {\mu} s ^ {\mu}$$

其中 $D_{\mu}$ 设为非奇异。现表：

$$\overline {{{D}}} _ {0} = D _ {\mu} ^ {- 1} D _ {0}, \overline {{{D}}} _ {1} = D _ {\mu} ^ {- 1} D _ {1}, \dots , \overline {{{D}}} _ {\mu - 1} = D _ {\mu} ^ {- 1} D _ {\mu - 1}$$

试证明：如下的状态空间描述

$$
\begin{array}{r l} \dot {x} & = \left[ \begin{array}{c c c c c} 0 & I & & & \\ \vdots & & \ddots & & \\ \vdots & & & \ddots & I \\ 0 & & & & - \overline {{D}} _ {0} - \overline {{D}} _ {1} \dots - \overline {{D}} _ {\mu - 1} \end{array} \right] x + \left[ \begin{array}{c} 0 \\ \vdots \\ \vdots \\ 0 \\ D _ {\mu} ^ {- 1} \end{array} \right] u \\ y & = [ N _ {0}, N _ {1}, \dots , N _ {\mu - 1} ] x \end{array}
$$

是 $N(s)D^{-1}(s)$ 的一个能控形实现。

9.14 设一个离散时间系统的脉冲传递函数矩阵为:

$$
G (z) = \left[ \begin{array}{c c} \frac {z + 2}{z + 1} & \frac {1}{z + 3} \\ \frac {z}{z + 1} & \frac {z + 1}{z + 2} \end{array} \right]
$$

(i) 求出它的一个实现；

(ii) 求出它的一个最小实现。
