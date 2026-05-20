$$\left\| \Phi (t; t _ {0}) \right\| \leqslant M \mathrm{e} ^ {- \alpha (t - t _ {0})}, \quad \forall t \geqslant t _ {0},$$

其中 $\alpha = (\ln 2) / t_1$ .

从定义2.4.10和定理2.4.6能够得到下列两个命题.

命题2.4.1 线性时变微分方程(2.4.11)的平衡解 $x = 0$ 的一致渐近稳定性等价于其零解的指数稳定性.

命题2.4.2 如果式(2.4.11)的系数矩阵 $A(t)$ 使得 $A(t) + A^{\mathrm{T}}(t)$ 的最大特征值 $\lambda^{+}(t)$ 满足

$$\lambda^ {+} (t) \leqslant - h < 0, \quad \forall t \in [ 0, + \infty),$$

这里 $h$ 是某大于零的实数，则微分方程 (2.4.11) 的零解是指数稳定的，并且 $h$ 是微分方程 (2.4.11) 的衰减度.

Lyapunov 第二方法是研究微分方程稳定性的一种方法。这种方法不是通过求出微分方程的解的表达式以了解其解的稳定性，而是通过研究与微分方程有直接关系的所谓 Lyapunov 函数的性质，来了解其解的稳定性。所以这种方法又叫做 Lyapunov 直接方法。此方法不仅适用于线性微分方程，而且特别适用于非线性微分方程。首先讨论定常微分方程

$$\frac {\mathrm{d} x}{\mathrm{d} t} = f (x) \tag {2.4.19}$$

的稳定性问题．我们总假定 $f(0) = 0$ ，并且以 $x(t_0) = x_0 \in \mathbb{R}^n$ 为初值的解 $x(t; x_0)$ 在 $[0, +\infty)$ 上存在唯一.

下面首先给出正、负定函数和 $K$ 函数的定义及其有关性质

设 $\Omega_{n} \subset \mathbb{R}^{n}$ 为包含原点 $x = 0$ 的开区域，令 $J \stackrel{\mathrm{def}}{=} [0, +\infty)$ ， $W(x)$ 和 $V(t, x)$ 分别表示定义在 $\Omega_{n}$ 和 $J \times \Omega_{n}$ 上的连续实值函数，于是 $W(\cdot) \in C(\Omega_{n}, \mathbb{R})$ ， $V(\cdot, \cdot) \in C(J \times \Omega_{n}, \mathbb{R})$ 。

定义 2.4.11 $^{[10]}$ (1) 称函数 $W(x)$ 在 $\Omega_{n}$ 上正（负）定，是指 $W(x) \geqslant 0 (\leqslant 0), \forall x \in \Omega_{n}$ ，并且仅当 x = 0 时 $W(x) = 0;$

(2) 称函数 $W(x)$ 在 $\Omega_{n}$ 上半正 (负) 定，是指 $W(x) \geqslant 0 (\leqslant 0), \forall x \in \Omega_{n}$ ;

(3) 当 $\Omega_{n} = \mathbb{R}^{n}$ 时，称 $W(x)$ 为无穷大正定函数，是指 $W(x)$ 正定，并且 $\lim_{|x|\to +\infty}W(x) = +\infty$ 。无穷大正定函数也称径向无界函数；

(4) 称 $V(\cdot, \cdot) \in C(J \times \Omega_n, \mathbb{R})$ 正定，是指存在正定函数 $W(\cdot) \in C(\Omega_n, \mathbb{R})$ 使得 $V(t, x) \geqslant W(x), \forall x \in \Omega_n$ ，并且 $V(t, 0) \equiv 0$ ; 称 $V(t, x)$ 负定，是指 $-V(t, x)$ 正定；

(5) 称 $V(\cdot, \cdot) \in C(J \times \Omega_n, \mathbb{R})$ 半正定，是指存在半正定函数 $W(\cdot) \in C(\Omega_n, \mathbb{R})$ 使得 $V(t, x) \geqslant W(x)$ ; 称 $V(t, x)$ 半负定，是指 $-V(t, x)$ 半正定；

(6) 称 $V(\cdot, \cdot) \in C(J \times \Omega_n, \mathbb{R})$ 具有无穷小上界，是指存在正定函数 $W_1(\cdot) \in C(\Omega_n, \mathbb{R})$ ，使 $|V(t, x)| \leqslant W_1(x), \forall x \in \Omega_n$ ;

(7) 称 $V(\cdot, \cdot) \in C(J \times \Omega_n, \mathbb{R})$ 具有无穷大下界, 是指存在无穷大正定函数 $W_2(\cdot) \in C(\Omega_n, \mathbb{R})$ , 使 $V(t, x) \geqslant W_2(x), \forall x \in \Omega_n$ ;

(8) 如果 $V(\cdot, \cdot) \in C(J \times \Omega_n, \mathbb{R})$ , $W(\cdot) \in C(\Omega_n, \mathbb{R})$ 可正可负, 则称其为变号函数.
