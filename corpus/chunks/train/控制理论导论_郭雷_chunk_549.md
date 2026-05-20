$$
\left\{ \begin{array}{l} \dot {x} (t) = A x (t) + B u (t), \\ x (0) = x _ {0}, \end{array} \right. \tag {7.3.37}
J _ {\beta} [ u ] = \frac {1}{2} \int_ {0} ^ {+ \infty} \left(x ^ {\mathrm{T}} (t) Q x (t) + u ^ {\mathrm{T}} (t) R u (t)\right) \mathrm{e} ^ {2 i \beta t} \mathrm{d} t. \tag {7.3.38}
$$

假定 $(A, B)$ 完全能控， $(A, C^{\mathrm{T}})$ 完全能观测， $Q = CC^{\mathrm{T}}$ 。对关系式 (7.3.37)，(7.3.38) 作变量替换

$$
\left\{ \begin{array}{l} \xi (t) = \mathrm{e} ^ {\beta t} x (t), \\ v (t) = \mathrm{e} ^ {\beta t} u (t). \end{array} \right. \tag {7.3.39}
$$

我们得到

$$
\left\{ \begin{array}{l} \dot {\xi} (t) = (\beta I _ {n} + A) \xi (t) + B v (t), \\ \xi (0) = x _ {0}, \end{array} \right. \tag {7.3.40}
J [ v ] = \frac {1}{2} \int_ {0} ^ {+ \infty} \left(\xi^ {\mathrm{T}} (t) Q \xi (t) + v ^ {\mathrm{T}} (t) R v (t)\right) \mathrm{d} t, \tag {7.3.41}
$$

其中 $I_{n}$ 为 $n \times n$ 单位矩阵.

命题7.3.1 矩阵对 $((A + \beta I_n), B)$ 完全能控的充要条件是矩阵对 $(A, B)$ 完全能控，矩阵对 $((A + \beta I_n), C^{\mathrm{T}})$ 完全能观测的充要条件是矩阵对 $(A, C^{\mathrm{T}})$ 完全能观测.

证明 事实上，由

$$
\operatorname{rank} [ B, (A + \beta I _ {n}) B, \dots , (A + \beta I _ {n}) ^ {n - 1} B ] = \operatorname{rank} [ B, A B, \dots , A ^ {n - 1} B ],
\operatorname{rank} \left[ \begin{array}{c} C ^ {\mathrm{T}} \\ C ^ {\mathrm{T}} (A + \beta I _ {n}) \\ \vdots \\ C ^ {\mathrm{T}} (A + \beta I _ {n}) ^ {n - 1} \end{array} \right] = \operatorname{rank} \left[ \begin{array}{c} C ^ {\mathrm{T}} \\ C ^ {\mathrm{T}} A \\ \vdots \\ C ^ {\mathrm{T}} A ^ {n - 1} \end{array} \right],
$$

即知命题结论成立.

这样，在 $(A, B)$ 完全能控， $(A, C^{\mathrm{T}})$ 完全能观测的假设下，线性二次最优调节问题 (7.3.40)，(7.3.41) 满足定理 7.3.6 的假设，从而可直接得如下结论：

(1) 问题 (7.3.40), (7.3.41) 的最优控制综合函数 $v^{*}(\xi)$ 为

$$v ^ {*} (\xi) = - R ^ {- 1} B ^ {T} P _ {\beta} ^ {*} \xi ,$$

这里 $P_{\beta}^{*}$ 是如下 Riccati 矩阵代数方程：

$$P (A + \beta I _ {n}) + (A + \beta I _ {n}) ^ {\mathrm{T}} P + Q - P B R ^ {- 1} B ^ {\mathrm{T}} P = 0 \tag {7.3.42}$$

的唯一正定对称解矩阵；

(2) 相应于问题 (7.3.40) 的最优闭环系统

$$\dot {\xi} = (A + \beta I _ {n}) \xi - B R ^ {- 1} B ^ {\mathrm{T}} P _ {\beta} ^ {*} \xi$$

是全局渐近稳定的。利用变量代换 (7.3.39) 可得

$$\lim _ {t \rightarrow \infty} \mathrm{e} ^ {\beta t} x (t) = \lim _ {t \rightarrow \infty} \xi (t) = 0.$$

综上所述得到：

定理7.3.7 给定 $\beta > 0$ . 对于线性二次最优调节问题 (7.3.37) 和 (7.3.38), 当 $(A, B)$ 完全能控, $(A, C^{\mathrm{T}})$ 完全能观测 $(Q = CC^{\mathrm{T}})$ 时, 有

(1) 闭环系统

$$\dot {x} = (A + \beta I _ {n}) x - B R ^ {- 1} B ^ {\mathrm{T}} P _ {\beta} ^ {*} x \tag {7.3.43}$$

是全局渐近稳定的，其中 $P_{\beta}^{*}$ 是式(7.3.42)的唯一正定对称解矩阵；

(2) $\forall x_0 \in \mathbb{R}^n$ , 关系式 (7.3.37) 和 (7.3.38) 的最优闭环系统

$$\dot {x} (t) = A x (t) + B u _ {\beta} ^ {*} (x (t))$$

初值为 $x(0) = x_0$ 的轨线 $x_{\beta}^{*}(t)$ 与系统(7.3.43)带相同初态的轨线 $\tilde{x}_{\beta}^{*}(t)$ 之间满足关系式

$$x _ {\beta} ^ {*} (t) = \mathrm{e} ^ {- \beta t} \tilde {x} _ {\beta} ^ {*} (t).$$

定理 7.3.7 表明，对任意给定 $\beta > 0$ ，关系式 (7.3.37) 和 (7.3.38) 的最优闭环系统具有衰减度 $\beta$ .
