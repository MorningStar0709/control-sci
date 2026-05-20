# 9.3 有理分式矩阵传递函数的一些典型实现

我们现在来推广讨论多输入-多输出系统的传递函数矩阵的实现问题。通常，一个传递函数矩阵可采用多种形式的描述来加以表示，所以相应地需要采用不同的方法来构造其实现。本节中，假定所研究的传递函数矩阵 $G(s)$ 是严格真的，且以有理分式矩阵形式的描述来表示：

$$G (s) = \left(g _ {i j} (s)\right), i = 1, \dots , q; j = 1, \dots , p \tag {9.79}$$

再令 $d(s)$ 为 $g_{ij}(s)(i=1,\cdots,q;i=1,\cdots,p)$ 的最小公分母，并具有如下形式：

$$d (s) = s ^ {k} + \alpha_ {k - 1} s ^ {k - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {9.80}$$

则可将 $G(s)$ 进而表为

$$G (s) = \frac {1}{d (s)} P (s) = \frac {1}{d (s)} \left[ P _ {k - 1} s ^ {k - 1} + \dots + P _ {1} s + P _ {0} \right] \tag {9.81}$$

其中 $P_{m}(m=0,1,\cdots,k-1)$ 为 $q \times p$ 常阵。下面，我们来介绍(9.81)所示传递函数矩阵 $G(s)$ 的一些典型的实现。

能控形实现 给定传递函数矩阵 $G(s)$ 如(9.81)所示, 则其能控形实现 $(A, B, C)$ 为

$$
\begin{array}{l} A = \left[ \begin{array}{c c c c c} 0 & I _ {p} & & & \\ \vdots & & \ddots & & \\ \vdots & & & \ddots & \\ 0 & & & I _ {p} \\ - \alpha_ {0} I _ {p} & - \alpha_ {1} I _ {p} \dots \dots & - \alpha_ {k - 1} I _ {p} \end{array} \right], \quad B = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ I _ {p} \end{array} \right] \\ C = \left[ P _ {0}, P _ {1}, \dots , P _ {k - 1} \right] \tag {9.82} \\ \end{array}
$$

证 先来证明 $(A, B, C)$ 是 $G(s)$ 的实现。令

$$
V (s) \triangleq (s I - A) ^ {- 1} B = \left[ \begin{array}{c} V _ {1} (s) \\ \vdots \\ V _ {k} (s) \end{array} \right] \tag {9.83}
$$

其中， $V_{i}(s)$ ( $i=1,\cdots,k$ ) 为 $p \times p$ 矩阵。则由此可导出

$$(s I - A) V (s) = B \quad \text {或} \quad s V (s) = A V (s) + B \tag {9.84}$$

再考虑到(9.82)中矩阵 $A$ 和 $B$ 的形式，故由上式可进而得到

$$
\left\{ \begin{array}{l} V _ {2} (s) = s V _ {1} (s) \\ V _ {3} (s) = s V _ {2} (s) = s ^ {2} V _ {1} (s) \\ \dots \dots . \\ V _ {k} (s) = s V _ {k - 1} (s) = s ^ {k - 1} V _ {1} (s) \end{array} \right. \tag {9.85}
$$

和

$$s V _ {k} (s) = - \alpha_ {0} V _ {1} (s) - \alpha_ {1} V _ {2} (s) - \dots - \alpha_ {k - 1} V _ {k} (s) + I _ {p} \tag {9.86}$$

将(9.85)代入(9.86)又可导出

$$\left(s ^ {k} + \alpha_ {k - 1} s ^ {k - 1} + \dots + \alpha_ {1} s + \alpha_ {0}\right) V _ {1} (s) = d (s) V _ {1} (s) = I _ {p} \tag {9.87}$$

或

$$V _ {1} (s) = \frac {1}{d (s)} I _ {p} \tag {9.88}$$

再将(9.88)代入(9.85)，有

$$V _ {i} (s) = \frac {1}{d (s)} s ^ {i - 1} I _ {p}, i = 1, 2, \dots , k \tag {9.89}$$

于是，即可得到

$$
\begin{array}{l} C (s I - A) ^ {- 1} B = C V (s) = P _ {0} V _ {1} (s) + P _ {1} V _ {2} (s) + \dots + P _ {k - 1} V _ {k} (s) \\ = \frac {1}{d (s)} \left(P _ {0} + P _ {1} s + \dots + P _ {k - 1} s ^ {k - 1}\right) = G (s) \tag {9.90} \\ \end{array}
$$

这就证明了 $(A, B, C)$ 为 $G(s)$ 的一个实现。再由于
