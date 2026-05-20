方程(5.364)的解存在,即对任意 $\widetilde{K}$ 可以定出一组解 $[t_{1m}, t_{1,m-1}, \cdots, t_{11}]$ 。但已知 $\{A, C\}$ 为能观测,且其能观测性指数为 $\nu$ ,则由此可知 $\{\overline{A}_{22}, \overline{A}_{12}\}$ 也为能观测,而其能观测性指数为 $\nu - 1$ 。这表明,在保证方程(5.364)的解存在的前提下,可把函数观测器的维数m取为 $\nu-1$ ; 因为, 此时仍有 rank V=n-q, 因而解 $[t_{1m}, t_{1,m-1}, \cdots, t_{1}]$ 存在, 也即等价地 $T_{1}$ 存在。据此, 利用 (5.363), 可定出 $T_{2}$ . 再根据 (5.355) 和 (5.357), 又可定出 G 和 N, 而 $H = T\bar{B}$ . 于是, 可构成 $\nu-1$ 维的渐近重构 Kx 的函数观测器。证明完成。

而且，从上述推证过程中还可归纳出设计重构 $Kx$ 的函数观测器的算法如下：

第 1 步：对给定能观测被估计系统，计算出其能观测性指数 v.

第 2 步：指定 $\nu - 1$ 个期望的函数观测器的特征值 $\lambda_1^*, \lambda_2^*, \dots, \lambda_{\nu-1}^*$ ，它们均应是具有负实部的共轭复数或负实数，计算出其相应的特征多项式：

$$\prod_ {i = 1} ^ {\nu - 1} \left(s - \lambda_ {i} ^ {*}\right) = s ^ {\nu - 1} + \alpha_ {\nu - 2} s ^ {\nu - 2} + \dots + \alpha_ {1} s + \alpha_ {0}$$

第3步：取

$$
F = \left[ \begin{array}{c c} {0} & \\ {\vdots} & {I _ {\nu - 2}} \\ {0} & \\ {- \alpha_ {0}} & {- \alpha_ {1} \dots - \alpha_ {\nu - 2}} \end{array} \right] - (\nu - 1) \times (\nu - 1) \text {阵}
M = [ 1 \quad 0 \dots 0 ] - 1 \times (\nu - 1) \text { 阵 }
$$

第4步：引入非奇异变换阵 $P^T = [C^T, R^T]$ ，其中 $\operatorname{rank} C = q, R$ 为任取仅需保证 $P$ 为非奇异。定出

$$\overline {{A}} = P A P ^ {- 1} = \left[ \underbrace {\frac {\overline {{A}} _ {1 1}}{\overline {{A}} _ {2 1}}} _ {q} \middle | \underbrace {\frac {\overline {{A}} _ {1 2}}{\overline {{A}} _ {2 2}}} _ {(n - q)} \right] \} (n - q)\bar {B} = P B = \left[ \frac {\bar {B} _ {1}}{\bar {B} _ {2}} \right] \} (n - q)\bar {K} = K P ^ {- 1} = \left[ \underbrace {\bar {K} _ {1}} _ {q}: \underbrace {\bar {K} _ {2}} _ {(n - q)} \right]$$

第5步：计算

$$
\begin{array}{l} \widetilde {K} \triangleq \overline {{K}} _ {2} \overline {{A}} _ {2 2} ^ {v - 1} + \alpha_ {v - 2} \overline {{K}} _ {2} \overline {{A}} _ {2 2} ^ {v - 2} + \dots + \alpha_ {1} \overline {{K}} _ {2} \overline {{A}} _ {2 2} + \alpha_ {0} \overline {{K}} _ {2} \\ L \triangleq \left[ \begin{array}{c c c c c} {I _ {q}} & {\cdot} & & & \\ & {\cdot} & {\cdot} & & \\ & & {\cdot} & & \\ {\alpha_ {v - 2} I _ {q}} & {\cdot} & {\cdot} & {\cdot} & \\ {\vdots} & & {\cdot} & {\cdot} & {\cdot} \\ {\alpha_ {1} I _ {q}} & {\cdot} & {\cdot} & {\alpha_ {v - 2} I _ {q}} & {I _ {q}} \end{array} \right] - (\nu - 1) q \times (\nu - 1) q \text {阵} \\ V \triangleq \left[ \begin{array}{c} {\overline {{{A}}} _ {1 2}} \\ {\overline {{{A}}} _ {1 2} \overline {{{A}}} _ {2 2}} \\ {\vdots} \\ {\overline {{{A}}} _ {1 2} \overline {{{A}}} _ {\lambda \lambda} ^ {v - 2}} \end{array} \right] - (v - 1) q \times (n - q) \text {阵} \\ \end{array}
$$
