其中， $A$ 是赫尔维茨矩阵，且对于所有 $t\geqslant 0$ 和 $x\in R^n$ ，有 $\| g(t,x)\| _2\leqslant \gamma \| x\| _2$ 。设 $Q = Q^{\mathrm{T}} > 0$ ，并对于 $P$ 解李雅普诺夫方程

$$P A + A ^ {\mathrm{T}} P = - Q$$

由定理4.6可知方程存在唯一解 $P = P^{\mathrm{T}} > 0$ 。二次李雅普诺夫函数 $V(x) = x^{\mathrm{T}}Px$ 满足式(9.3)至式(9.5)，特别是有

$$
\begin{array}{l} \lambda_ {\min} (P) \| x \| _ {2} ^ {2} \leqslant V (x) \leqslant \lambda_ {\max} (P) \| x \| _ {2} ^ {2} \\ \frac {\partial V}{\partial x} A x = - x ^ {T} Q x \leqslant - \lambda_ {\min} (Q) \| x \| _ {2} ^ {2} \\ \left\| \frac {\partial V}{\partial x} \right\| _ {2} = \| 2 x ^ {\mathrm{T}} P \| _ {2} \leqslant 2 \| P \| _ {2} \| x \| _ {2} = 2 \lambda_ {\max} (P) \| x \| _ {2} \\ \end{array}
$$

$V(x)$ 沿扰动系统轨线的导数满足

$$\dot {V} (t, x) \leqslant - \lambda_ {\min} (Q) \| x \| _ {2} ^ {2} + 2 \lambda_ {\max} (P) \gamma \| x \| _ {2} ^ {2}$$

因此,如果 $\gamma<\lambda_{\min}(Q)/2\lambda_{\max}(P)$ ，则原点是全局指数稳定的。由于该边界取决于 Q 的选择，因此现在要做的是如何选择 Q，使比值 $\lambda_{\min}(Q)/\lambda_{\max}(P)$ 最大。可以证明当 Q=I 时，该比值最大（见习题 9.1）。

例9.2 考虑二阶系统

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - 4 x _ {1} - 2 x _ {2} + \beta x _ {2} ^ {3} \\ \end{array}
$$

其中常数 $\beta \geqslant 0$ 未知。把该系统看成具有方程(9.1)形式的扰动系统，有

$$
f (x) = A x = \left[ \begin{array}{c c} 0 & 1 \\ - 4 & - 2 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right], \quad g (x) = \left[ \begin{array}{c} 0 \\ \beta x _ {2} ^ {3} \end{array} \right]
$$

A 的特征值为 $-1 \pm j \sqrt{3}$ ，因此 A 是赫尔维茨矩阵。李雅普诺夫方程

$$P A + A ^ {T} P = - I$$

的解为

$$
P = \left[ \begin{array}{c c} \frac {3}{2} & \frac {1}{8} \\ \frac {1}{8} & \frac {5}{1 6} \end{array} \right]
$$

如例9.1所示，当 $c_{3} = 1$ 且

$$c _ {4} = 2 \lambda_ {\max} (P) = 2 \times 1. 5 1 3 = 3. 0 2 6$$

时, 李雅普诺夫函数 $V(x) = x^{\mathrm{T}}Px$ 满足不等式(9.3)至不等式(9.5)。对于所有 $|x_{2}| \leqslant k_{2}$ ，扰动项 $g(x)$ 满足

$$\| g (x) \| _ {2} = \beta | x _ {2} | ^ {3} \leqslant \beta k _ {2} ^ {2} | x _ {2} | \leqslant \beta k _ {2} ^ {2} \| x \| _ {2}$$

分析至此,虽然我们知道只要轨线 $x(t)$ 限定在一个紧集内, $x_{2}(t)$ 就是有界的,但还不知道 $x_{2}(t)$ 的边界。我们以 $k_{2}$ 为待定系数继续分析。用 $V(x)$ 作为该扰动系统的备选李雅普

诺夫函数,可得 $\dot{V}(x)\leqslant-\|x\|_{2}^{2}+3.026\beta k_{2}^{2}\|x\|_{2}^{2}$

因此,如果 $\beta < \frac{1}{3.026k_{2}^{2}}$

则 $\dot{V}(x)$ 是负定的。为了估计边界 $k_{2}$ ，设 $\Omega_{c} = \{x \in R^{2} \mid V(x) \leqslant c\}$ 对于任何正常数 $c$ ，集合 $\Omega_{c}$ 是有界闭集， $\Omega_{c}$ 的边界就是李雅普诺夫曲面

$$V (x) = \frac {3}{2} x _ {1} ^ {2} + \frac {1}{4} x _ {1} x _ {2} + \frac {5}{1 6} x _ {2} ^ {2} = c$$

在曲面 $V(x) = c$ 上， $|x_2|$ 的最大值由曲面方程对 $x_1$ 的偏微分确定，其结果为
