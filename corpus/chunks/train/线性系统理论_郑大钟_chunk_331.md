$$
\begin{array}{l} \boldsymbol {c} _ {i} (s I - A _ {i}) ^ {- 1} \boldsymbol {b} _ {i} = [ f _ {i \mu_ {i}}, \dots , f _ {i 1} ] \left[ \begin{array}{l l l l} (s - \lambda_ {i}) & 1 & & \\ & \ddots & \ddots & \\ & & \ddots & 1 \\ & & & (s - \lambda_ {i}) \end{array} \right] ^ {- 1} \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \\ = \frac {1}{(s - \lambda_ {i}) ^ {\mu_ {i}}} \left[ f _ {i \mu_ {i}}, \dots , f _ {i 1} \right] \left[ \begin{array}{c c c} * & \dots & * \\ \vdots & & (s - \lambda_ {i}) \\ \vdots & & \vdots \\ * & \dots & * (s - \lambda_ {i}) ^ {\mu_ {i} - 1} \end{array} \right] \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \\ = \frac {f _ {i i} (s - \lambda_ {i}) ^ {\mu_ {i} - 1} + ^ {\prime} \cdots + f _ {i \mu i}}{(s - \lambda_ {i}) ^ {\mu_ {i}}} = \sum_ {k = 1} ^ {\mu_ {i}} \frac {f _ {i k}}{(s - \lambda_ {i}) ^ {k}} \tag {9.67} \\ \end{array}
$$

这样，把(9.67)代入(9.66)，即得

$$\tilde {\boldsymbol {c}} (s I - \widetilde {A}) ^ {- 1} \tilde {\boldsymbol {b}} = \sum_ {i = 1} ^ {p} \sum_ {k = 1} ^ {\mu_ {i}} \frac {f _ {i k}}{(s - \lambda_ {i}) ^ {k}} = g (s) \tag {9.68}$$

从而就完成了证明。

在并联形实现中， $\tilde{A}$ 具有约当规范形的形式，所以通常也将这类实现称为约当形实现。对给定传递函数 $g(s)$ ，构造其并联形实现 $(\tilde{A}, \tilde{b}, \tilde{c})$ 中的一个主要难点，是需要事先确定出 $g(s)$ 的极点 $\lambda_i (i = 1, \cdots, p)$ 和各个系数 $f_{ik} (k = 1, \cdots, \mu_i)$ 。当 $g(s)$ 的次数 $n$ 比较高时，这在计算上将不是一件容易的事。此外，如果极点 $\lambda_i$ 中包含共轭复数对，那么实现的系数矩阵 $\tilde{A}$ 和 $\tilde{c}$ 中都会出现复数元，这对于系统分析和系统仿真来说将是不方便的。为克服这一困难，需要引入适当的等价变换，现以如下例子来加以说明。考虑 $p = 3$ 的一个并联形实现

$$
\tilde {A} = \left[ \begin{array}{c c} A _ {1} & \\ & \bar {A} _ {1} \\ & & A _ {3} \end{array} \right], \quad \hat {\boldsymbol {b}} = \left[ \begin{array}{l} \boldsymbol {b} _ {1} \\ \boldsymbol {b} _ {1} \\ \boldsymbol {b} _ {3} \end{array} \right], \quad \tilde {\boldsymbol {c}} = [ \boldsymbol {c} _ {1}, \bar {\boldsymbol {c}} _ {1}, \boldsymbol {c} _ {3} ] \tag {9.69}
$$

其中，矩阵块 $\tilde{\pmb{c}}_1$ 和 $\overline{A}_1$ 分别共轭于 $\mathbf{c}_1$ 和 $A_{1}$ ，其余为实数矩阵块。现引入如下的等价变换

$$A = P \tilde {A} P ^ {- 1}, \boldsymbol {b} = P \tilde {\boldsymbol {b}}, \mathbf {c} = \tilde {\mathbf {c}} P ^ {- 1} \tag {9.70}$$

且变换阵 $P$ 和其逆矩阵 $P^{-1}$ 分别为

$$
P = \left[ \begin{array}{c c c} I & & 0 \\ j I & - j I & 0 \\ \hdashline 0 & & 0 \end{array} \right], P ^ {- 1} = \left[ \begin{array}{c c c} \frac {1}{2} I & - \frac {1}{2} j I & 0 \\ \frac {1}{2} I & \frac {1}{2} j I & 0 \\ \hdashline 0 & & 0 \end{array} \right] \tag {9.71}
$$

而 $j^2 = -1$ 。于是，将(9.69)和(9.71)代入(9.70)，即可得到
