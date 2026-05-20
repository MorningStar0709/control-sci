# 5.5.2 稳态状态调节器问题

设系统的状态方程为

$$\boldsymbol {X} (k + 1) = \boldsymbol {A} \boldsymbol {X} (k) + \boldsymbol {B} \boldsymbol {U} (k) \tag {5-74}$$

X 为 n 维状态向量, U 为 m 维输入向量。性能指标为

$$J = \sum_ {k = 0} ^ {\infty} \left[ \boldsymbol {X} ^ {\mathrm{T}} (k) \boldsymbol {Q} \boldsymbol {X} (k) + \boldsymbol {U} ^ {\mathrm{T}} (k) \boldsymbol {R} \boldsymbol {U} (k) \right] \tag {5-75}$$

假设 $(A, B)$ 可控或可稳， $R$ 为对称正定的常数阵， $Q$ 为对称正定的常数阵，或 $Q$ 为对称半正定常数阵，但 $(A, Q_1)$ 可观测或可检测， $Q = Q_1^T Q_1$ 。要求寻找最优控制使 $J$ 最小。

可以证明,对于上面的问题,最优控制是存在和唯一的,它可以表示为

$$\boldsymbol {U} (k) = - \boldsymbol {L X} (k) \tag {5-76}$$

L 为 $m \times n$ 维的常数反馈增益阵, 参考 (5-65), 将时变阵换成常数阵, L 可表示为

$$\boldsymbol {L} = \left(\boldsymbol {R} + \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K B}\right) ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K A} \tag {5-77}$$

其中 K 为 $n \times n$ 常数阵，是下面的矩阵黎卡提代数方程的唯一的对称正定解。在式(5-61)的矩阵黎卡提差分方程中，将时变阵换为常数阵，即可得出矩阵黎卡提代数方程为

$$- \boldsymbol {K} + \boldsymbol {Q} + \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {K} \boldsymbol {A} - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {K} \boldsymbol {B} (\boldsymbol {R} + \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} \boldsymbol {B}) ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} \boldsymbol {A} = \boldsymbol {0} (5 - 7 8)$$

最优反馈控制系统为

$$\boldsymbol {X} (k + 1) = [ \boldsymbol {A} - \boldsymbol {B L} ] \boldsymbol {X} (k) \tag {5-79}$$

它是渐近稳定的,即 $[A-BL]$ 的特征值的模小于1。

下面用例子来说明上述结果的应用。

例5-5 系统的状态方程为

$$x _ {1} (k + 1) = x _ {2} (k)x _ {2} (k + 1) = x _ {2} (k) + u (k) \tag {5-80}$$

性能指标为

$$J = \sum_ {k = 0} ^ {\infty} \left[ q x _ {1} ^ {2} (k) + u ^ {2} (k) \right] \tag {5-81}$$

寻找最优控制使 J 最小。

解 由状态方程式(5-80)和性能指标式(5-81)，可求得下面的矩阵

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 1 \end{array} \right], \quad \boldsymbol {B} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right], \quad \boldsymbol {Q} = \left[ \begin{array}{l l} q & 0 \\ 0 & 0 \end{array} \right], \quad \boldsymbol {R} = 1 \tag {5-82}
$$

因 $[B,AB] = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$ 非奇异，故系统可控。

当 $q > 0, Q$ 为半正定，故有下面的分解：

$$
\boldsymbol {Q} = \left[ \begin{array}{l l} q & 0 \\ 0 & 0 \end{array} \right] = \left[ \begin{array}{l} \sqrt {q} \\ 0 \end{array} \right] [ \sqrt {q} 0 ]
$$

即

$$
\boldsymbol {Q} _ {1} ^ {\mathrm{T}} = \left[ \begin{array}{c} \sqrt {q} \\ 0 \end{array} \right]
