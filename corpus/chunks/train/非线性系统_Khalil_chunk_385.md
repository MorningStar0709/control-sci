# 13.3 全状态线性化

一单输入系统 $\dot{x}=f(x)+g(x)u$ (13.27)

其中 $f$ 和 $g$ 在定义域 $D \subset R^n$ 上足够光滑, 如果存在一个足够光滑的函数 $h: D \to R$ , 使系统

$$\dot {x} = f (x) + g (x) u \tag {13.28}y = h (x) \tag {13.29}$$

在区域 $D_0 \subset D$ 上相对阶为 $n$ , 则系统(13.27)是可反馈线性化的。这一结论的解释如下: 相对阶为 $n$ 的系统, 其标准形可简化为

$$\dot {z} = A _ {c} z + B _ {c} \gamma (x) [ u - \alpha (x) ] \tag {13.30}y = C _ {c} z \tag {13.31}$$

另一方面,按照定义13.1,如果系统(13.27)是可反馈线性化的,则通过变量代换 $\zeta=S(x)$ ,将系统转换为 $\dot{\zeta}=A\zeta+B\bar{\gamma}(x)[u-\bar{\alpha}(x)]$

其中 $(A,B)$ 是可控的，且在某一定义域内 $\bar{\gamma} (x)\neq 0$ 。对于任何可控矩阵对 $(A,B)$ ，总可以找到一个非奇异矩阵 $M$ ，将 $(A,B)$ 转换为可控标准形①，即 $MAM^{-1} = A_{c} + B_{c}\lambda^{\mathrm{T}},MB = B_{c}$ ，这里 $(A_{c},B_{c})$ 表

示 $n$ 个积分器链。变量代换 $z = M\zeta = MS(x)\stackrel {\mathrm{def}}{=}T(x)$

将系统(13.27)转换为 $\dot{z} = A_{c}z + B_{c}\gamma (x)[u - \alpha (x)]$

其中 $\gamma(x)=\bar{\gamma}(x)$ , $\alpha(x)=\bar{\alpha}(x)-\lambda^{T}MS(x)/\gamma(x)$ 。因为

$$\dot {z} = \frac {\partial T}{\partial x} \dot {x}$$

所以等式 $A_{c}T(x) + B_{c}\gamma (x)[u - \alpha (x)] = \frac{\partial T}{\partial x}[f(x) + g(x)u]$

在所讨论的定义域内对于所有 x 和 u 都成立。取 u=0，则上式可分解为两个方程

$$\frac {\partial T}{\partial x} f (x) = A _ {c} T (x) - B _ {c} \alpha (x) \gamma (x) \tag {13.32}\frac {\partial T}{\partial x} g (x) = B _ {c} \gamma (x) \tag {13.33}$$

方程(13.32)等价于

$$
\frac {\partial T _ {1}}{\partial x} f (x) = T _ {2} (x)\frac {\partial T _ {2}}{\partial x} f (x) = T _ {3} (x)
\begin{array}{r c l} & \vdots \\ \frac {\partial T _ {n - 1}}{\partial x} f (x) & = & T _ {n} (x) \\ \frac {\partial T _ {n}}{\partial x} f (x) & = & - \alpha (x) \gamma (x) \end{array}
$$

方程(13.33)等价于

$$
\begin{array}{l} \frac {\partial T _ {1}}{\partial x} g (x) = 0 \\ \frac {\partial T _ {2}}{\partial x} g (x) = 0 \\ \frac {\partial T _ {n - 1}}{\partial x} g (x) = 0 \\ \frac {\partial T _ {n}}{\partial x} g (x) = \gamma (x) \neq 0 \\ \end{array}

\begin{array}{l} \frac {\partial T _ {n - 1}}{\partial x} g (x) = 0 \\ \frac {\partial T _ {n}}{\partial x} g (x) = \gamma (x) \neq 0 \\ \end{array}
$$

•
•
•

令 $h(x) = T_{1}(x)$ ，可看出

$$T _ {i + 1} (x) = L _ {f} T _ {i} (x) = L _ {f} ^ {i} h (x), \quad i = 1, 2, \dots , n - 1$$

$h(x)$ 满足偏微分方程

$$L _ {g} L _ {f} ^ {i - 1} h (x) = 0, i = 1, 2, \dots , n - 1 \tag {13.34}$$

其约束条件为

$$L _ {g} L _ {f} ^ {n - 1} h (x) \neq 0 \tag {13.35}$$

$\alpha$ 和 $\gamma$ 由下式给出：

$$\gamma (x) = L _ {g} L _ {f} ^ {n - 1} h (x), \quad \alpha (x) = - \frac {L _ {f} ^ {n} h (x)}{L _ {g} L _ {f} ^ {n - 1} h (x)} \tag {13.36}$$
