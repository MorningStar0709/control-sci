其中 z 是输入, y 是输出, $p(\cdot)$ 和 $q(\cdot)$ 是定义域上的足够光滑的函数, 且 $q(\cdot) \neq 0$ 。非线性输入-输出模型简化为例 13.4 的线性系统的传递函数模型。通过在输入端增加 m 个积分器扩展系统的动态特性, 并将 $u = z^{(m)}$ 作为扩展系统的控制输入①。扩展系统为 $n + m$ 阶。取状态变量为

$$
\zeta = \left[ \begin{array}{c} {z} \\ {z ^ {(1)}} \\ {\vdots} \\ {z ^ {(m - 1)}} \end{array} \right], \quad \xi = \left[ \begin{array}{c} {y} \\ {y ^ {(1)}} \\ {\vdots} \\ {\vdots} \\ {y ^ {(n - 1)}} \end{array} \right], \qquad x = \left[ \begin{array}{c} {\zeta} \\ {\xi} \end{array} \right]
$$

可得到扩展系统的状态模型

$$
\begin{array}{l} \dot {\zeta} = A _ {u} \zeta + B _ {u} u \\ \dot {\xi} = A _ {c} \xi + B _ {c} [ p (x) + q (x) u ] \\ y = C _ {c} \xi \\ \end{array}
$$

其中 $(A_{c}, B_{c}, C_{c})$ 是 $n$ 积分器链的标准形表示， $(A_{u}, B_{u})$ 是表示 $m$ 积分器链的可控标准形对。设 $D \subset R^{n+m}$ 为定义域，在其上 $p$ 和 $q$ 足够光滑且 $q \neq 0$ 。利用 $(A_{c}, B_{c}, C_{c})$ 的特殊结构，容易看出 $y^{(i)} = C_{c} A_{c}^{i} \xi, \quad 1 \leqslant i \leqslant n - 1, \quad y^{(n)} = p(x) + q(x) u$

因此，系统的相对阶为 $n$ 。为了求出零动态方程，注意到 $L_{f}^{i - 1}h(x) = \xi_{i}$ ，从而 $Z^{*} = \{x\in R^{n + m}|\xi = 0\}$ 并可计算出 $u^{*}(x) = -p(x) / q(x)$ 在 $\xi = 0$ 时的值。因此零动态系统为

$$\dot {\zeta} = A _ {u} \zeta + B _ {u} u ^ {*} (x)$$

回顾 $\zeta$ 的定义很容易看出， $\zeta_{1} = z$ 满足 $m$ 阶微分方程

$$0 = p \left(z, z ^ {(1)}, \dots , z ^ {(m - 1)}, 0, 0, \dots , 0\right) + q \left(z, z ^ {(1)}, \dots , z ^ {(m - 1)}, 0, 0, \dots , 0\right) z ^ {(m)} \tag {13.25}$$

该方程与由方程(13.24)中令 $y(t)\equiv0$ 时得出的方程相同。对于线性系统,方程(13.25)简化为一个线性微分方程,与传递函数的分子多项式一致。通过研究方程(13.25),可确定系统的最小相位特性。为了把系统转换为标准形,注意到 $\xi$ 是y及其直到n-1阶导数的向量,所以只需求一个函数 $\phi=\phi(\zeta,\xi):R^{n+m}\rightarrow R^{m}$ ,使得

$$\frac {\partial \phi}{\partial \zeta} B _ {u} + \frac {\partial \phi}{\partial \xi} B _ {c} q (x) = 0$$

相当于 $\frac{\partial\phi_i}{\partial\zeta_m} +\frac{\partial\phi_i}{\partial\xi_n} q(x) = 0,1\leqslant i\leqslant m$ (13.26)

在某些特殊情况下,这些偏微分方程有解。例如,如果 q 是常数, $\phi$ 可取为

$$\phi_ {i} = \zeta_ {i} - \frac {1}{q} \xi_ {n - m + i}, 1 \leqslant i \leqslant m$$

另外一种情况见习题 13.5。

△
