(2) 给定 $\gamma_0 > 0, \forall w(\cdot) \in L_2[[0, +\infty); \mathbb{R}^{r_1}]$ , 系统

$$
\left\{ \begin{array}{l} \dot {x} = (A - B _ {2} R _ {2} ^ {- 1} B _ {2} ^ {\mathrm{T}} P ^ {*}) x + B _ {1} w (t), \\ z = C _ {1} x - D _ {1 2} R _ {2} ^ {- 1} B _ {2} ^ {\mathrm{T}} P ^ {*} x, \end{array} \right. \tag {7.5.21}
$$

的零初态响应 $z_{c}(t) \stackrel{\mathrm{def}}{=} Cx(t) - D_{12}R_{2}^{-1}B_{2}^{\mathrm{T}}P^{*}x(t)$ 满足不等式

$$\int_ {0} ^ {+ \infty} z _ {c} ^ {\mathrm{T}} (t) z _ {c} (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t.$$

综上所述得到：

定理 7.5.1 对于线性定常系统 (7.5.16)，当 $(A, C_{1})$ 完全能观测时，其全息情况下的 $H_{\infty}$ 控制次优问题可解，即给定 $\gamma_{0} > 0$ ，状态反馈形式的控制规律 $u^{*}(x) = -R_{2}^{-1} B_{2}^{\mathrm{T}} P^{*} x$ 满足

(1) 相应于 (7.5.16) 的闭环受干扰系统 (7.5.20) 内部稳定；

(2) 对于给定的 $\gamma_0 > 0$ , 有

$$\int_ {0} ^ {+ \infty} z _ {c} ^ {\mathrm{T}} (t) z _ {c} (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t, \quad \forall w \in L _ {2} ([ 0, \infty); \mathbb {R} ^ {r _ {1}}),$$

其中 $z_{c}(t)$ 是系统 (7.5.21) 的零初态响应， $P^{*}$ 是 Riccati 矩阵代数方程 (7.5.19) 的正定对称解矩阵.

推论 7.5.1 对于线性定常系统 (7.5.16). 当 $(A, C_{1})$ 完全能观测时，其全息情况下的 $H_{\infty}$ 控制次优问题可解，即状态反馈形式的控制规律 $u^{*}(x) = -R_{2}^{-1} B_{2}^{\mathrm{T}} P_{1} x$ 是系统 (7.5.16) 的 $H_{\infty}$ 控制次优问题的解，这里 $P_{1}$ 是 Riccati 型矩阵代数不等式

$$P A + A ^ {\mathrm{T}} P + C _ {1} ^ {\mathrm{T}} C _ {1} + \frac {1}{\gamma_ {0}} P B _ {1} B _ {1} ^ {\mathrm{T}} P - P B _ {2} R _ {2} ^ {- 1} B _ {2} ^ {\mathrm{T}} P \leqslant 0 \tag {7.5.22}$$

的正定对称解矩阵.

本节仅限于介绍 $H_{\infty}$ 控制初步，旨在让读者了解 $H_{\infty}$ 控制问题的提法，最基本结果以及与最优控制问题和定量微分对策问题的联系。对线性定常 $H_{\infty}$ 控制问题中诸多成熟的内容如 Riccati 矩阵代数方程 (不等式) 正定 (半正定) 对称解矩阵的存在性，求解方法以及动态输出反馈形式的控制规律等皆未涉及，有兴趣的读者可参阅本书第 6 章和文献 [6].

非线性 $H_{\infty}$ 控制

仿射非线性系统的 $L_{2}$ - 增益. 考察仿射非线性系统

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + G (x) w, \\ z = h (x), \end{array} \right. \tag {7.5.23}
$$

其中 $x \in \mathbb{R}^n$ 为系统状态变量， $w \in \mathbb{R}^r$ 为作用于系统的外部干扰， $z \in \mathbb{R}^m$ 为系统被调输出， $G(x) = [g_1(x), g_2(x), \cdots, g_r(x)], f(x), g_i(x), i = 1, 2, \cdots, r$ 皆为定义在 $\mathbb{R}^n$ 上的光滑 $n$ 维向量场， $h(x)$ 为定义在 $\mathbb{R}^n$ 上的光滑 $m$ 维向量值函数，且 $f(0) = 0$ 。为简单起见称 (7.5.23) 为系统。下面假设
