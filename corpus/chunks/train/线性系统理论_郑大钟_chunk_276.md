# 7.1 矩阵分式描述

右 MFD 和左 MFD 给定 $q \times p$ 的具有有理分式矩阵形式的传递函数矩阵 $G(s)$ ，则一定存在 $q \times p$ 和 $p \times p$ 的多项式矩阵 $N(s)$ 和 $D(s)$ ，以及 $q \times q$ 和 $q \times p$ 的多项式矩阵 $A(s)$ 和 $B(s)$ ，使成立

$$G (s) = N (s) D ^ {- 1} (s) \tag {7.1}$$

和

$$G (s) = A ^ {- 1} (s) B (s) \tag {7.2}$$

并且，称 $N(s)D^{-1}(s)$ 为 $G(s)$ 的一个右矩阵分式描述，简写为右MFD；而称 $A^{-1}(s)\times B(s)$ 为 $G(s)$ 的一个左矩阵分式描述，简写为左MFD。这里，MFD是Matrix-Fraction Description的缩写。

例 给定传递函数矩阵 $G(s)$ 如下:

$$
G (s) = \left[ \begin{array}{c c} \frac {(s + 1)}{(s + 2) ^ {2} (s + 3) ^ {2}} & \frac {s}{(s + 3) ^ {2}} \\ \frac {- (s + 1)}{(s + 3) ^ {2}} & \frac {- s}{(s + 3) ^ {2}} \end{array} \right]
$$

则通过找出它的列最小公分母

$$d _ {c 1} (s) = (s + 2) ^ {2} (s + 3) ^ {2}, d _ {c 2} (s) = (s + 3) ^ {2}$$

就可定出它的一个右 MFD 为

$$
G (s) = \left[ \begin{array}{c c} (s + 1) & s \\ - (s + 1) (s + 2) ^ {2} & - s \end{array} \right] \left[ \begin{array}{c c} (s + 2) ^ {2} (s + 3) ^ {2} & 0 \\ 0 & (s + 3) ^ {2} \end{array} \right] ^ {- 1}
$$

而通过找出它的行最小公分母

$$d _ {r 1} (s) = (s + 2) ^ {2} (s + 3) ^ {2}, d _ {r 2} (s) = (s + 3) ^ {2}$$

则可定出它的一个左MFD为

$$
G (s) = \left[ \begin{array}{c c} (s + 2) ^ {2} (s + 3) ^ {2} & 0 \\ 0 & (s + 3) ^ {2} \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} (s + 1) & s (s + 2) ^ {2} \\ - (s + 1) & - s \end{array} \right]
$$

几点推论 下面,从 MFD 的定义出发,对其性质作如下的几点讨论:

(1) 给定 $G(s)$ 的任一右 MFD

$$G (s) = N (s) D ^ {- 1} (s) \tag {7.3}$$

则规定

$$\text { MFD 的次数 } \triangleq \deg \det D (s) \tag {7.4}$$

类似地, 对 $G(s)$ 的任一左 MFD

$$G (s) = A ^ {- 1} (s) B (s) \tag {7.5}$$

我们规定

$$\text { MFD 的次数 } \triangleq \deg \det A (s) \tag {7.6}$$

（2）对给定传递函数阵 $G(s)$ ，其右MFD和左MFD都不是唯一的。并且，不同的MFD，常可能有不同的次数。

例 给定传递函数矩阵 $G(s)$ 如下:

$$
G (s) = \left[ \begin{array}{c c} \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}} & \frac {s}{(s + 2) ^ {2}} \\ \frac {- s}{(s + 2) ^ {2}} & \frac {- s}{(s + 2) ^ {2}} \end{array} \right]
$$

采用不同的方法,可求出它的两个右矩阵分式描述为:

$$
G (s) = N _ {1} (s) D _ {1} ^ {- 1} (s) = \left[ \begin{array}{c c} s & s \\ - s (s + 1) ^ {2} & - s \end{array} \right] \left[ \begin{array}{c c} (s + 1) ^ {2} (s + 2) ^ {2} & 0 \\ 0 & (s + 2) ^ {2} \end{array} \right] ^ {- 1}
$$

和

$$
G (s) = N _ {2} (s) D _ {2} ^ {- 1} (s) = \left[ \begin{array}{c c} s & 0 \\ - s & s ^ {2} \end{array} \right] \left[ \begin{array}{c c} 0 & - (s + 1) ^ {2} (s + 2) \\ (s + 2) ^ {2} & (s + 2) \end{array} \right] ^ {- 1}
$$

而且不难看出,两个 MFD 的阶次是不相同的,分别为

$$\deg \det D _ {1} (s) = 6, \quad \deg \det D _ {2} (s) = 5$$

(3) 令 $\overline{N}(s)\overline{D}^{-1}(s)$ 为 $G(s)$ 的一个右 MFD, $W(s)$ 为任一相应维数的非奇异多项式矩阵，并定义

$$\bar {N} (s) = N (s) W ^ {- 1} (s), \quad \bar {D} (s) = D (s) W ^ {- 1} (s) \tag {7.7}$$

则 $N(s)D^{-1}(s)$ 也必是 $G(s)$ 的一个右MFD，且成立
