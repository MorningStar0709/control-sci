# 7.5 确定不可简约矩阵分式描述的算法

这一节中,我们来介绍几种常用的算法,以便由给定的传递函数矩阵的可简约MFD,来确定出传递函数矩阵的不可简约MFD。如前所述,不可简约的MFD具有最小阶次,因此相应地具有最简的结构。

算法1 这个算法依据如下的结论：令给定传递函数矩阵 $G(s)$ 的一个可简约MFD为 $\overline{N}(s)\overline{D}^{-1}(s)$ ，表 $R(s)$ 为 $\overline{D}(s)$ 和 $\overline{N}(s)$ 的一个最大右公因子，并重新定义 $D(s) = \overline{D}(s)R^{-1}(s)$ 和 $N(s) = \overline{N}(s)R^{-1}(s)$ ，那么 $N(s)D^{-1}(s)$ 必是 $G(s)$ 的一个不可简约的MFD。此结论的正确性，已在上节中关于不可简约MFD的性质3的证明过程里，进行了证明。

在上述结论的基础上,可给出算法的步骤如下:

① 利用行初等运算,求出 $\overline{D}(s)$ 和 $\overline{N}(s)$ 的一个最大右公因子 $R(s)$ 。

② 计算 $R(s)$ 的逆矩阵 $R^{-1}(s)$ 。

③ 计算 $\overline{D}(s)R^{-1}(s)$ 和 $\overline{N}(s)R^{-1}(s)$ ，取 $D(s) = \overline{D}(s)R^{-1}(s)$ 和 $N(s) = \overline{N}(s) \times R^{-1}(s)$ ，则 $N(s)D^{-1}(s)$ 为不可简约 MFD。

这种算法的优点是步骤简单,缺点是计算过程中包含求逆运算,而这在维数较高时往往是比较复杂的。

例 给定一个可简约 MFD 为 $\overline{N}(s)\overline{D}^{-1}(s)$ ，其中 $\overline{N}(s)$ 和 $\overline{D}(s)$ 分别为：

$$
\bar {N} (s) = \left[ \begin{array}{c c} s & s (s + 1) ^ {2} \\ - s (s + 1) ^ {2} & - s (s + 1) ^ {2} \end{array} \right],

\overline {{D}} (s) = \left[ \begin{array}{c c} (s + 1) ^ {2} (s + 2) ^ {2} & 0 \\ 0 & (s + 1) ^ {2} (s + 2) ^ {2} \end{array} \right]
$$

先求出 $\overline{D}(s)$ 和 $\overline{N}(s)$ 的一个 $\gcd$ 为

$$
R (s) = \left[ \begin{array}{c c} 1 & (s + 1) ^ {2} \\ - (s + 2) & 0 \end{array} \right]
$$

再对 $R(s)$ 求逆，得到

$$
R ^ {- 1} (s) = \left[ \begin{array}{c c} 0 & - \frac {1}{(s + 2)} \\ \frac {1}{(s + 1) ^ {2}} & \frac {1}{(s + 1) ^ {2} (s + 2)} \end{array} \right]
$$

于是，不可简约的 $N(s)D^{-1}(s)$ 即可定出，其中

$$
N (s) = \bar {N} (s) R ^ {- 1} (s) = \left[ \begin{array}{c c} s & s (s + 1) ^ {2} \\ - s (s + 1) ^ {2} & - s (s + 1) ^ {2} \end{array} \right] \left[ \begin{array}{c c} 0 & - \frac {1}{(s + 2)} \\ \frac {1}{(s + 1) ^ {2}} & \frac {1}{(s + 1) ^ {2} (s + 2)} \end{array} \right]

= \left[ \begin{array}{c c} s & 0 \\ - s & s ^ {2} \end{array} \right]

D (s) = \bar {D} (s) R ^ {- 1} (s) = \left[ \begin{array}{c c} (s + 1) ^ {2} (s + 2) ^ {2} & 0 \\ 0 & (s + 1) ^ {2} (s + 2) ^ {2} \end{array} \right]

\times \left[ \begin{array}{c c} 0 & - \frac {1}{(s + 2)} \\ \frac {1}{(s + 1) ^ {2}} & \frac {1}{(s + 1) ^ {2} (s + 2)} \end{array} \right] = \left[ \begin{array}{c c} 0 & - (s + 1) ^ {2} (s + 2) \\ (s + 2) ^ {2} & (s + 2) \end{array} \right]
$$

算法2 这个算法依据如下的结论:

结论 令 $\overline{N}(s)\overline{D}^{-1}(s)$ 为可简约 MFD, $U(s)$ 是使

$$
U (s) \left[ \begin{array}{l} \bar {D} (s) \\ \bar {N} (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] \tag {7.83}
$$
