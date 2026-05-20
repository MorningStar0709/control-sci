a, b, c, $\theta$ 和 k 是正常数。已知以 $y = x_{3}$ 作为输出时，系统的相对阶为 2，因此是部分可反馈线性化的。下面研究状态方程能否完全线性化。我们有

$$
a d _ {f} g = [ f, g ] = \left[ \begin{array}{c} a \\ c x _ {3} \\ - \theta x _ {2} \end{array} \right]; a d _ {f} ^ {2} g = [ f, a d _ {f} g ] = \left[ \begin{array}{c} a ^ {2} \\ (a + b) c x _ {3} \\ (b - a) \theta x _ {2} - \theta k \end{array} \right]
$$

矩阵 $\mathcal{G} = [g, ad_{f}g, ad_{f}^{2}g] = \left[ \begin{array}{ccc}1 & a & a^{2}\\ 0 & cx_{3} & (a + b)cx_{3}\\ 0 & -\theta x_{2} & (b - a)\theta x_{2} - \theta k \end{array} \right]$

的行列式为 $\operatorname{det} \mathcal{G} = c\theta(-k + 2bx_2)x_3$

因此，当 $x_{2} \neq k / 2b, x_{3} \neq 0$ 时， $\mathcal{G}$ 的秩为3。如果 $[g, ad_{f}g] \in D$ ，则分布 $D = \operatorname{span}\{g, ad_{f}g\}$ 是对合的。有

$$
[ g, a d _ {f} g ] = \frac {\partial (a d _ {f} g)}{\partial x} g = \left[ \begin{array}{l l l} 0 & 0 & 0 \\ 0 & 0 & c \\ 0 & - \theta & 0 \end{array} \right] \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right] = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \end{array} \right]
$$

因此， $D$ 是对合的，定理13.2的条件在定义域

$$D _ {0} = \{x \in R ^ {3} \mid x _ {2} > \frac {k}{2 b}, x _ {3} > 0 \}$$

内成立。继续求满足方程(13.34)和方程(13.35)的函数 $h$ 。无激励系统在 $x_{1} = 0$ 和 $x_{2} = k / b$ 有一个平衡点集合。取理想工作点为 $x^{*} = [0,k / b,\omega_{0}]^{\mathrm{T}}$ ，这里 $\omega_0$ 是角速度 $x_{3}$ 的理想设定点。我们希望找到满足

$$\frac {\partial h}{\partial x} g = 0; \quad \frac {\partial (L _ {f} h)}{\partial x} g = 0; \quad \frac {\partial (L _ {f} ^ {2} h)}{\partial x} g \neq 0$$

的 $h(x)$ ，且 $h(x^{*}) = 0$ 。根据条件

$$\frac {\partial h}{\partial x} g = \frac {\partial h}{\partial x _ {1}} = 0$$

可知 $h$ 一定与 $x_{1}$ 无关，因此

$$L _ {f} h (x) = \frac {\partial h}{\partial x _ {2}} [ - b x _ {2} + k - c x _ {1} x _ {3} ] + \frac {\partial h}{\partial x _ {3}} \theta x _ {1} x _ {2}$$

又根据 $[\partial (L_f h) / \partial x]g = 0$ 推出，如果

$$h = c _ {1} \left[ \theta x _ {2} ^ {2} + c x _ {3} ^ {2} \right] + c _ {2}$$

$c_{1}$ 和 $c_{2}$ 为常数，则 $cx_{3}\frac{\partial h}{\partial x_{2}} = \theta x_{2}\frac{\partial h}{\partial x_{3}}$

成立。选择 $c_{1} = 1$ ，并为满足条件 $h(x^{*}) = 0$ ，取

$$c _ {2} = - \theta (x _ {2} ^ {*}) ^ {2} - c (x _ {3} ^ {*}) ^ {2} = - \theta (k / b) ^ {2} - c \omega_ {0} ^ {2}$$

如此选择 $h$ ，则 $L_{f}h$ 和 $L_{f}^{2}h$ 为

$$L _ {f} h (x) = 2 \theta x _ {2} (k - b x _ {2}), \quad L _ {f} ^ {2} h (x) = 2 \theta (k - 2 b x _ {2}) (- b x _ {2} + k - c x _ {1} x _ {3})$$

因此 $\frac{\partial(L_f^2 h)}{\partial x} g = \frac{\partial(L_f^2 h)}{\partial x_1} = -2c\theta (k - 2bx_2)x_3$

而且只要 $x_{2} \neq k / 2b, x_{3} \neq 0$ ，条件 $[\partial (L_f^2 h) / \partial x]g \neq 0$ 就成立。假设 $x_{3}^{*} > 0$ ，容易验证（见习题13.15）映射 $z = T(x)$ 是 $D_{0}$ 上的微分同胚映射，且状态方程在 $z$ 坐标系中有明确定义，定义域为

$$D _ {z} = T (D _ {0}) = \left\{z \in R ^ {3} \mid z _ {1} > \theta \phi^ {2} (z _ {2}) - \theta (k / b) ^ {2} - c \omega_ {0} ^ {2}, z _ {2} < \frac {\theta k ^ {2}}{2 b} \right\}$$

这里 $\phi(\cdot)$ 是映射 $2\theta x_{2}(k-bx_{2})$ 的逆映射，当 $x_{2}>k/2b$ 时有定义。定义域 $D_{z}$ 包含原点 z=0。
