# 5.3.1 问题描述

考虑如下 $n$ 阶非线性系统

$$
\left\{ \begin{array}{l} x ^ {(n)} = f (x, \dot {x}, \dots , x ^ {(n - 1)}) + g (x, \dot {x}, \dots , x ^ {(n - 1)}) u \\ y = x \end{array} \right. \tag {5.18}
$$

式中，f 和 g 为未知非线性函数， $u \in R$ 和 $y \in R$ 分别为系统的输入和输出。

设位置指令为 $y_{m}$ ，令

$$e = y _ {m} - y = y _ {m} - x, e = (e, \dot {e}, \dots , e ^ {(n - 1)}) ^ {\mathrm{T}} \tag {5.19}$$

选择 $\boldsymbol{K}=(k_{n},\cdots,k_{1})^{\mathrm{T}}$ ，使多项式 $s^{n}+k_{1}s^{(n-1)}+\cdots+k_{n}$ 的所有根都在复平面左半平面上。取控制律为

$$u ^ {*} = \frac {1}{g (\pmb {x})} [ - f (\pmb {x}) + y _ {m} ^ {(n)} + \pmb {K} ^ {\mathrm{T}} \pmb {e} ] \tag {5.20}$$

将式 $(5.20)$ 代入式 $(5.18)$ ，得到闭环控制系统的方程为

$$e ^ {(n)} + k _ {1} e ^ {(n - 1)} + \dots + k _ {n} e = 0 \tag {5.21}$$

由 K 的选取, 可得 $t \to \infty$ 时 $e(t) \to 0$ , 即系统的输出 y 渐近地收敛于理想输出 $y_{m}$ 。

可见,如果非线性函数 $f(x)$ 和 $g(x)$ 是已知的,则可以选择控制律 u 来消除其非线性的性质,然后再根据线性控制理论设计控制器。
