$$
\begin{array}{l} V (x) = \frac {1}{2} x ^ {\mathrm{T}} \left[ \begin{array}{l l} \frac {1}{2} & \frac {1}{2} \\ \frac {1}{2} & 1 \end{array} \right] x + \int_ {0} ^ {x _ {1}} \left(y - \frac {1}{3} y ^ {3}\right) d y \\ = \frac {3}{4} x _ {1} ^ {2} - \frac {1}{1 2} x _ {1} ^ {4} + \frac {1}{2} x _ {1} x _ {2} + \frac {1}{2} x _ {2} ^ {2} \\ \end{array}
$$

且 $\dot{V} (x) = -\frac{1}{2} x_1^2 (1 - \frac{1}{3} x_1^2) - \frac{1}{2} x_2^2$

定义域 $D$ 定义为 $D = \{x\in R^2\mid -\sqrt{3} < x_1 <   \sqrt{3}\}$

很容易看出,在 $D-\{0\}$ 内,有 $V(x)>0$ 和 $\dot{V}(x)<0$ 。观察图8.3的相图可知,D不是 $R_{A}$ 的子集。

通过此例可知,为什么定理4.1或推论4.1中的D不是 $R_{A}$ 的估计值。即使始于D的轨线会从一个李雅普诺夫曲面 $V(x)=c_{1}$ 移动到另一个李雅普诺夫曲面 $V(x)=c_{2}$ 的内部,其中 $c_{2}<c_{1}$ ,但这并不能保证轨线会永远保持在D内。一旦轨线移动到D外,就不能保证 $\dot{V}(x)$ 为负。因而所有关于 $V(x)$ 减小到0的论证都不再成立。若 $R_{A}$ 是由D的一个正不变紧子集(a compact positively invariant subset)估算的时,就不会出现这一问题,即紧集 $\Omega\subset D$ 使得每条始于 $\Omega$ 的轨线在所有未来时刻都会保持在 $\Omega$ 内。定理4.4证明了 $\Omega$ 是 $R_{A}$ 的一个子集。最简单的估计值是集合①

$$\Omega_ {c} = \{x \in R ^ {n} \mid V (x) \leqslant c \}$$

其中 $\Omega_{c}$ 有界且包含于 $D$ 内。对于二次李雅普诺夫函数 $V(x) = x^{\mathrm{T}}Px, D = \{\|x\|_{2} < r\}$ ，可通过选择

$$c < \min _ {\| x \| _ {2} = r} x ^ {\mathrm{T}} P x = \lambda_ {\min} (P) r ^ {2}$$

保证 $\Omega_{c} \subset D$ 。当 $D = \{ |b^{\mathrm{T}}x| < r\}$ 时，其中 $b \in R^{n②}$ ，有

$$\min _ {| b ^ {T} x | = r} x ^ {\mathrm{T}} P x = \frac {r ^ {2}}{b ^ {\mathrm{T}} P ^ {- 1} b}$$

因此如果选取 $c < \min_{1 \leqslant i \leqslant p} \frac{r_i^2}{b_i^T P^{-1} b_i}$

则 $\{x^{T}Px\leqslant c\}$ 是 $D=\left\{\left|b_{i}^{T}x\right|<r_{i},i=1,\cdots,p\right\}$ 的一个子集。

考虑4.3节的线性化结果,将极大简化利用 $\Omega_{c}=\{x^{T}Px\leqslant c\}$ 估算吸引区的方法。在4.3节看到,如果雅可比矩阵

$$A = \left. \frac {\partial f}{\partial x} \right| _ {x = 0}$$

是赫尔维茨的,则通过对任意正定矩阵 Q 求解李雅普诺夫方程 $PA + A^{T}P = -Q$ , 总可以找到一个二次李雅普诺夫函数 $V(x) = x^{T}Px$ 。综上所述, 只要 A 是赫尔维茨的, 就可以估算原点的吸引区。下面的例题可以说明这一点。

例8.9 二阶系统

$$
\begin{array}{l} \dot {x} _ {1} = - x _ {2} \\ \dot {x} _ {2} = x _ {1} + \left(x _ {1} ^ {2} - 1\right) x _ {2} \\ \end{array}
$$

已在例 8.5 中讨论过。在例 8.5 中看到, 因为

$$
A = \left. \frac {\partial f}{\partial x} \right| _ {x = 0} = \left[ \begin{array}{l l} 0 & - 1 \\ 1 & - 1 \end{array} \right]
$$

是赫尔维茨的,所以原点是渐近稳定的。该系统的李雅普诺夫函数通过取 Q=I 并解关于 P 的李雅普诺夫方程 $PA + A^{T}P = -I$

确定。方程的唯一解是正定矩阵

$$
P = \left[ \begin{array}{c c} 1. 5 & - 0. 5 \\ - 0. 5 & 1 \end{array} \right]
$$
