# 习题

4.1 给定单变量线性定常系统

$$
\begin{array}{l} \dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 2 5 0 & 0 & - 5 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 1 0 \end{array} \right] u \\ y = [ - 2 5 \quad 5 \quad 0 ] x \\ \end{array}
$$

(i) 判断系统是否为渐近稳定；

(ii) 判断系统是否为 BIBO 稳定。

4.2 设有二阶非线性系统为:

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - \sin x _ {1} - x _ {2} \\ \end{array}
$$

(i) 定出所有的平衡状态；

(ii) 求出各平衡点处的线性化状态方程, 并判断是否为渐近稳定。

4.3 判断下列系统的原点平衡状态 $x_{0} = 0$ 是否为大范围渐近稳定：

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - x _ {1} - x _ {1} ^ {2} x _ {2} \end{array} \right.
$$

4.4 判断下列系统的原点平衡状态 $x_{e} = 0$ 是否为大范围渐近稳定：

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - x _ {1} ^ {3} - x _ {2} \end{array} \right.
$$

4.5 给定线性时变系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - \frac {1}{t + 1} & - 1 0 \end{array} \right] \boldsymbol {x}, \quad t \geqslant 0
$$

判断其原点平衡状态是否为大范围渐近稳定(提示: 取 $V(x,t)=\frac{1}{2}\left[x_{1}^{2}+(t+1)x_{1}^{2}\right]$ )。

4.6 设有非线性自治系统 $\dot{x} = f(x), f(0) = 0$ ，再表系统的雅可比（Jacobi）矩阵

$$
F (\boldsymbol {x}) \triangleq \frac {\partial f (\boldsymbol {x})}{\partial \boldsymbol {x} ^ {T}} = \left[ \begin{array}{c} \frac {\partial f _ {1} (\boldsymbol {x})}{\partial x _ {1}} \dots \dots \frac {\partial f _ {1} (\boldsymbol {x})}{\partial x _ {n}} \\ \vdots \\ \frac {\partial f _ {n} (\boldsymbol {x})}{\partial x _ {1}} \dots \dots \frac {\partial f _ {n} (\boldsymbol {x})}{\partial x _ {n}} \end{array} \right]
$$

证明：当 $F(\pmb{x}) + F^T (\pmb{x})$ 为负定时，系统的原点平衡状态 $\pmb{x}_{\epsilon} = \mathbf{0}$ 为大范围渐近稳定（提示：采用李亚普诺夫主稳定性定理，取 $V(\pmb {x}) = f^{T}(\pmb {x})f(\pmb {x}))$ 。

4.7 利用上题给出的结论判断下列系统是否为大范围渐近稳定：

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = - 3 x _ {1} + x _ {2} \\ \dot {x} _ {2} = x _ {1} - x _ {2} - x _ {2} ^ {3} \end{array} \right.
$$

4.8 考察二阶线性定常系统：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right] \boldsymbol {x} \triangleq A \boldsymbol {x}
$$

利用李亚普诺夫方程法证明：此系统的原点平衡状态 $x_{i} = 0$ 为大范围渐近稳定的条件是：

$$\det A > 0, \quad a _ {1 1} + a _ {2 2} < 0$$

(提示: 李亚普诺夫方程中取 Q = I)。

4.9 利用李亚普诺夫方法判断下列系统是否为大范围渐近稳定：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} - 1 & 1 \\ 2 & - 3 \end{array} \right] \boldsymbol {x}, \quad Q = I
$$

4.10 设有渐近稳定的单变量线性定常系统：

$$\dot {x} = A x + b u, \quad y = c x, x (0) = x _ {0}$$

其中 $u(t) \equiv 0$ 。再表 $P$ 是下列李亚普诺夫方程

$$P A + A ^ {T} P = - \mathbf {c} ^ {T} \mathbf {c}$$

的正定对称解阵。试证明：

$$\int_ {0} ^ {\infty} y ^ {2} (t) d t = x _ {0} ^ {T} P x _ {0}$$

4.11 给定完全能控的线性定常系统

$$\dot {x} = A x + B u$$

其中取 $u = -B^T W^{-1}(T)x$ ，而

$$W (T) = \int_ {0} ^ {T} e ^ {- A t} B B ^ {T} e ^ {- A ^ {T} t} d t, \quad T > 0$$

试证明所构成的闭环系统是渐近稳定的。

4.12 给定离散时间系统为

$$
\boldsymbol {x} (k + 1) = \left[ \begin{array}{r r r} 1 & 4 & 0 \\ - 3 & - 2 & - 3 \\ 2 & 0 & 0 \end{array} \right] \boldsymbol {x} (k)
$$

用两种方法判断系统是否为渐近稳定。
