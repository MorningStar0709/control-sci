$$
B = \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ I _ {p} \end{array} \right], A B = \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ I _ {p} \\ * \end{array} \right], \dots \dots , A ^ {k - 1} B = \left[ \begin{array}{l} I _ {p} \\ * \\ \vdots \\ * \end{array} \right] \tag {9.91}
$$

其中，用“\*”表示的 $p \times p$ 矩阵是无需确知的常数矩阵。故由此可知能控性判别阵为

$$
Q _ {c} = [ B, A B, \dots , A ^ {k - 1} B ] = \left[ \begin{array}{l l l} & & I _ {p} \\ & \ddots & \\ I _ {p} & & * \end{array} \right] \tag {9.92}
$$

也即 $(A, B, C)$ 为能控。从而，就完成了证明过程。

不难看出，(9.82)的能控形实现是标量传递函数的能控规范形实现(9.53)的一般化形式。但是，一般来说，能控形实现 $(A, B, C)$ 不一定是完全能观测的。

能观测形实现 给定 $q \times p$ 的传递函数矩阵 $G(s)$ 如 (9.81) 所示, 则其能观测形实现 $(\overline{A}, \overline{B}, \overline{C})$ 为

$$
\bar {A} = \left[ \begin{array}{c c c} 0 & \dots & 0 \\ I _ {q} & & - \alpha_ {0} I _ {q} \\ & \ddots & \vdots \\ & I _ {q} & - \alpha_ {k - 1} I _ {q} \end{array} \right], \quad \bar {B} = \left[ \begin{array}{c} P _ {0} \\ P _ {1} \\ \vdots \\ P _ {k - 1} \end{array} \right]
\overline {{{C}}} = [ 0, \dots , 0, I _ {q} ] \tag {9.93}
$$

证 其证明过程和能控形实现的推证过程相类同,故略去。

需要指出，(9.93)的能观测形实现是标量传递函数的能观测规范形实现(9.61)的一般化形式。而且，能观测形实现 $(\overline{A},\overline{B},\overline{C})$ 和能控形实现 $(A,B,C)$ 之间在形式上有着对偶的关系。但由于一般地说 $q\neq p$ ，所以两者的维数是不相等的。此外，能观测形实现 $(\overline{A},\overline{B},\overline{C})$ 不能保证必为完全能控。
