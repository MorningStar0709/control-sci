$$
\begin{array}{l} \dot {x} _ {1} = - x _ {1} + \frac {2 + x _ {3} ^ {2}}{1 + x _ {3} ^ {2}} u \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {3} = x _ {1} x _ {3} + u \\ y = x _ {2} \\ \end{array}
$$

在原点有一个开环平衡点。输出的导数为

$$
\begin{array}{l} \dot {y} = \dot {x} _ {2} = x _ {3} \\ \ddot {y} = \dot {x} _ {3} = x _ {1} x _ {3} + u \\ \end{array}
$$

因此系统在 $R^3$ 上的相对阶为2。在式(13.20)中应用 $L_{g}L_{f}h(x) = 1$ 和 $L_{f}^{2}h(x) = x_{1}x_{3}$ ，得

$$\gamma = 1, \quad \alpha (x) = - x _ {1} x _ {3}$$

为了描述零动态,把x限制为

$$Z ^ {*} = \{x \in R ^ {3} \mid x _ {2} = x _ {3} = 0 \}$$

并取 $u = u^{*}(x) = 0$ ，由此可得

$$\dot {x} _ {1} = - x _ {1}$$

表明该系统是最小相位的。为了把它变成标准形，选择一个函数 $\phi(x)$ ，使得

且

$$
T (x) = \left[ \begin{array}{l l l} \phi (x) & x _ {2} & x _ {3} \end{array} \right] ^ {\mathrm{T}}
\phi (0) = 0, \frac {\partial \phi}{\partial x} g (x) = 0
$$

在包含原点的某定义域上是微分同胚映射。偏微分方程

$$\frac {\partial \phi}{\partial x _ {1}} \cdot \frac {2 + x _ {3} ^ {2}}{1 + x _ {3} ^ {2}} + \frac {\partial \phi}{\partial x _ {3}} = 0$$

通过分离变量解出

$$\phi (x) = - x _ {1} + x _ {3} + \arctan x _ {3}$$

上式满足条件 $\phi(0) = 0$ 。映射 $T(x)$ 是全局微分同胚映射，这是因为对于任意 $z \in R^3$ ，方程 $T(x) = z$ 有唯一解。这样标准形

$$
\begin{array}{l} \dot {\eta} = (- \eta + \xi_ {2} + \arctan \xi_ {2}) \left(1 + \frac {2 + \xi_ {2} ^ {2}}{1 + \xi_ {2} ^ {2}} \xi_ {2}\right) \\ \dot {\xi} _ {1} = \xi_ {2} \\ \dot {\xi} _ {2} = (- \eta + \xi_ {2} + \arctan \xi_ {2}) \xi_ {2} + u \\ y = \xi_ {1} \\ \end{array}
$$

就是全局定义的。

△

例13.7 例13.3的场控直流电机在 $D_0 = \{x\in R^3 |x_2\neq 0\}$ 上的相对阶为2。运用式(13.20)，得

$$\gamma = \theta x _ {2}, \quad \alpha (x) = - \frac {\theta x _ {2} (- a x _ {1}) + \theta x _ {1} (- b x _ {2} + k - c x _ {1} x _ {3})}{\theta x _ {2}}$$

为了描述零动态,把x限制为

$$Z ^ {*} = \{x \in D _ {0} \mid x _ {3} = 0, x _ {1} x _ {2} = 0 \} = \{x \in D _ {0} \mid x _ {3} = 0, x _ {1} = 0 \}$$

取 $u = u^{*}(x) = 0$ ，得

$$\dot {x} _ {2} = - b x _ {2} + k$$

该零动态系统在 $x_{2} = k / b$ 处有一个渐近稳定平衡点，因而是最小相位系统。为了将其转换成标准形，需要找到一个函数 $\phi (x)$ ，使 $[\partial \phi /\partial x]g = \partial \phi /\partial x_1 = 0$ ，且 $T = [\phi (x),x_3,\theta x_1x_2]^{\mathrm{T}}$ 是某定义域 $D_{x}\subset D_{0}$ 上的微分同胚映射。选择 $\phi (x) = x_{2} - k / b$ ，则满足 $\partial \phi /\partial x_1 = 0$ 使 $T(x)$ 是 $D_{x} = \{x\in R^{3}|x_{2} > 0\}$ 上的微分同胚映射，同时将零动态系统的平衡点变换到原点。

例 13.8 考虑一个单输入-单输出非线性系统, 表示为 n 阶微分方程

$$
\begin{array}{l} y ^ {(n)} = p \left(z, z ^ {(1)}, \dots , z ^ {(m - 1)}, y, y ^ {(1)}, \dots , y ^ {(n - 1)}\right) \\ + q \left(z, z ^ {(1)}, \dots , z ^ {(m - 1)}, y, y ^ {(1)}, \dots , y ^ {(n - 1)}\right) z ^ {(m)}, m <   n \tag {13.24} \\ \end{array}
$$
