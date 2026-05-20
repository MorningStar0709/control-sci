$$
\left\{ \begin{array}{l} \dot {z} = A z + B u, \\ y = h (z). \end{array} \right.
$$

现在在 $z$ 坐标下向量场

$$\left\{X _ {1}, \dots , X _ {n} \right\} = \left\{g _ {1}, \dots , \mathrm{ad} _ {f} ^ {n _ {1} - 1} g _ {1}, \dots , g _ {m}, \dots , \mathrm{ad} _ {f} ^ {n _ {m} - 1} g _ {m} \right\}.$$

于是 $X_{i}=\delta_{i}=\frac{\partial}{\partial z_{i}}, i=1,\cdots,n.$ 由条件 (iii) 容易看出

$$L _ {X _ {i}} L _ {X _ {j}} h _ {s} (z) = 0, \quad s = 1, \dots , p,$$

这表明

$$\frac {\partial^ {2} h _ {s} (z)}{\partial z _ {i} \partial z _ {j}} = 0, \qquad 1 \leqslant i, j \leqslant n, s = 1, \dots , m,$$

即 $h_{s}(z)$ 是 $z$ 的线性函数．由假定 $h(z(x_0)) = 0$ ，可得

$$y = C z.$$

例8.3.1 考虑如下系统：

$$
\left\{ \begin{array}{l} {\dot {x} _ {1} = x _ {1} + u,} \\ {\dot {x} _ {2} = \frac {x _ {1}}{\cos (x _ {2})},} \\ {y = h (x) = \sin (x _ {2}).} \end{array} \right. \tag {8.3.13}
$$

我们考虑其在原点附近的线性等价问题。容易看出

$$
f = \left[ \begin{array}{c} {x _ {1}} \\ {x _ {1}} \\ {\overline {{{{\cos (x _ {2})}}}}} \end{array} \right], \qquad g = \left[ \begin{array}{c} {1} \\ {0} \end{array} \right], \qquad \text {及} \mathrm{ad} _ {f} g = - \left[ \begin{array}{c} {1} \\ {1} \\ {\overline {{{{\cos (x _ {2})}}}}} \end{array} \right],
$$

故条件 (i) 满足. 因为

$$
\begin{array}{l} \mathrm{d} h = (0, \cos (x _ {2})) \\ \mathrm{d} L _ {f} ^ {k} h = (1, 0), \quad k \geqslant 1, \\ \end{array}
$$

条件 (ii) 也满足. 再者,

$$L _ {g} h = 0, \quad L _ {g} L _ {f} ^ {k} h = 1, \quad k \geqslant 1.$$

因此

$$L _ {g} L _ {f} ^ {s} L _ {g} L _ {f} ^ {t} h = 0, \quad s \geqslant 0, t \geqslant 0.$$

于是条件 (iii) 得证. 所以系统 (8.3.13) 在原点等价于一个线性系统.

其次，我们寻找它的线性形式。设

$$
X _ {1} = g = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right], \quad X _ {2} = - \mathrm{ad} _ {f} ^ {g} = \left[ \begin{array}{c} 1 \\ 1 \\ \overline {{\cos (x _ {2})}} \end{array} \right].
$$

构造映射

$$F (z _ {1}, z _ {2}) = \phi_ {z _ {1}} ^ {X _ {1}} \circ \phi_ {z _ {2}} ^ {X _ {2}} (0).$$

首先，我们求 $\phi_{z_2}^{X_2}(0)$ ，即解微分方程

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} x _ {1}}{\mathrm{d} z _ {2}} = 1, \\ \frac {\mathrm{d} x _ {2}}{\mathrm{d} z _ {2}} = \frac {1}{\cos (x _ {1})}, \\ x _ {1} (0) = x _ {2} (0) = 0. \end{array} \right.
$$

其解为

$$x _ {1} = z _ {2}, \quad x _ {2} = \arcsin (z _ {2}).$$

其次，为得到 $F(z_{1},z_{2})$ ，我们解方程

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} x _ {1}}{\mathrm{d} z _ {1}} = 1, \\ \frac {\mathrm{d} x _ {2}}{\mathrm{d} z _ {1}} = 0, \\ x _ {1} (0) = z _ {2}, \\ x _ {2} (0) = \arcsin (z _ {2}). \end{array} \right.
$$

因此可得到映射 F 如下：

$$
\left\{ \begin{array}{l} x _ {1} = z _ {1} + z _ {2}, \\ x _ {2} = \arcsin (z _ {2}), \end{array} \right.
$$

而 $F^{-1}$ 为
