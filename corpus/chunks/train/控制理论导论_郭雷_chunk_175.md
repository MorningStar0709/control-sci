$$
\begin{array}{l} 0 = \left(\boldsymbol {x} ^ {*}\right) ^ {\mathrm{T}} f \left(\boldsymbol {x} ^ {*}\right) = \left(\boldsymbol {x} ^ {*}\right) ^ {\mathrm{T}} \int_ {0} ^ {1} D f \left(\sigma \boldsymbol {x} ^ {*}\right) \mathrm{d} \sigma \boldsymbol {x} ^ {*} \\ = \frac {1}{2} \left(\boldsymbol {x} ^ {*}\right) ^ {\mathrm{T}} \int_ {0} ^ {1} M _ {f} \left(\sigma \boldsymbol {x} ^ {*}\right) \mathrm{d} \sigma \boldsymbol {x} ^ {*} \neq 0. \\ \end{array}
$$

此矛盾说明命题2.4.4成立.

定理 2.4.21(Krasovskii) 对于非线性微分方程 (2.4.19)，设 $f(x)$ 在 $R^{n}$ 中连续可微。如果 (1) $\forall x \in R^{n}, M_{f}(x)$ 为负定矩阵；(2) $\lim_{|x| \to \infty} |f(x)| = +\infty$ ，则微分方程 (2.4.19) 的平衡解 x = 0 全局渐近稳定。

证明 定义标量函数

$$W (x) \stackrel {\text { def }} {=} f ^ {\mathrm{T}} (x) f (x). \tag {2.4.42}$$

由命题2.4.4知， $W(x)$ 是 $\mathbb{R}^n$ 上的正定函数． $W(x)$ 沿微分方程(2.4.19)对时间 $t$ 的全导数为

$$
\begin{array}{l} \dot {W} (x) \mid_ {(2. 4. 1 9)} = \frac {\mathrm{d} f ^ {\mathrm{T}} (x)}{\mathrm{d} t} \left| _ {(2. 4. 1 9)} f (x) + f ^ {\mathrm{T}} (x) \frac {\mathrm{d} f (x)}{\mathrm{d} t} \right| _ {(2. 4. 1 9)} \\ = f ^ {T} (x) \left(\frac {\partial f (x)}{\partial x}\right) ^ {T} f (x) + f ^ {T} (x) \left(\frac {\partial f (x)}{\partial x}\right) f (x) \\ = f ^ {\mathbf {T}} (x) \left(\left(\frac {\partial f (x)}{\partial x}\right) ^ {\mathbf {T}} + \frac {\partial f (x)}{\partial x}\right) f (x) \\ = f ^ {T} (x) M _ {f} (x) f (x). \\ \end{array}
$$

依假设 $M_{f}(x)$ 为负定矩阵，且 $f(x) \neq 0, \forall x \neq 0, x \in \mathbb{R}^{n}$ . 因此 $\dot{W}(x)|_{(2.4.19)}$ 是 $\mathbb{R}^n$ 中的负定函数。由定理2.4.20知微分方程(2.4.19)的平衡解 $x = 0$ 是全局渐近稳定的。

Krasovskii 定理提供了一类非线性向量微分方程全局渐近稳定的一个充分条件.

例2.4.6 考察非线性二阶向量微分方程

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c} - x _ {1} \\ x _ {1} - x _ {2} - x _ {2} ^ {3} \end{array} \right], \tag {2.4.43}
$$

其右端向量值函数 $f(x)$ 为

$$
f (x) = \left[ \begin{array}{c} - x _ {1} \\ x _ {1} - x _ {2} - x _ {2} ^ {3} \end{array} \right], \qquad x \in \mathbb {R} ^ {2},
$$

而

$$
\frac {\partial f}{\partial x} = \left[ \begin{array}{c c} - 1 & 0 \\ 1 & - 1 - 3 x _ {2} ^ {2} \end{array} \right].
$$

所以

$$
M _ {f} (x) = \frac {\partial f}{\partial x} + \left(\frac {\partial f}{\partial x}\right) ^ {\mathrm{T}} = \left[ \begin{array}{c c} - 2 & 1 \\ 1 & - 2 - 6 x _ {2} ^ {2} \end{array} \right].
$$

由于对任意 $x_0 = [x_{10}, x_{20}]^{\mathrm{T}} \neq 0$ ，有
