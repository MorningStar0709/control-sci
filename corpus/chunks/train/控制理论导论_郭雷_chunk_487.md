# 最优控制必要条件——极大值原理

下面分别对控制无约束和控制受约束两种类型进行论述.

控制无约束的极大值原理 (古典变分方法). 控制无约束指 $\mathbb{U}_r = \mathbb{R}^r$ .

首先讨论终端时刻 $t_f$ 固定，并且系统终端状态不受约束（即自由端点）的情况。这时 $S = \mathbb{R}^n$ 。从古典变分法角度，自由端点情况下的最优控制问题是将系统状态方程 (7.1.1) 看成约束条件，并在此约束条件下求使 $J[u]$ 达到极小的容许控制函数。于是可通过引入 Lagrange 乘子向量值函数将求 $J[u]$ 的条件极小问题化为求泛函

$$J _ {1} [ u ] = k (x \left(t _ {f}\right)) + \int_ {t _ {0}} ^ {t _ {f}} \left(l (x (t), u (t)) + \psi^ {\mathrm{T}} (t) (\dot {x} (t) - f (x (t), u (t)))\right) \mathrm{d} t \tag {7.1.5}$$

的无条件极小问题，其中 $\psi^{\mathrm{T}}(t)=[\psi_{1}(t),\cdots,\psi_{n}(t)]$ 为待求的 Lagrange 乘子函数.
利用分部积分公式

$$\int_ {t _ {0}} ^ {t _ {f}} \psi^ {\mathrm{T}} (t) \dot {x} (t) \mathrm{d} t = \psi^ {\mathrm{T}} (t _ {f}) x (t _ {f}) - \psi^ {\mathrm{T}} (t _ {0}) x _ {0} - \int_ {t _ {0}} ^ {t _ {f}} \dot {\psi} ^ {\mathrm{T}} (t) x (t) \mathrm{d} t$$

能将 $J_{1}[u]$ 写为

$$J _ {1} [ u ] = k (x (t _ {f})) + \psi^ {\mathrm{T}} (t _ {f}) x (t _ {f}) - \psi^ {\mathrm{T}} (t _ {0}) x _ {0}- \int_ {t _ {0}} ^ {t _ {f}} \dot {\psi} ^ {\mathrm{T}} (t) x (t) \mathrm{d} t - \int_ {t _ {0}} ^ {t _ {f}} H (x (t), u (t), \psi (t)) \mathrm{d} t. \tag {7.1.6}$$

式 (7.1.6) 中 $H(x, u, \psi) \stackrel{\mathrm{def}}{=} -l(x, u) + \psi^{\mathrm{T}} f(x, u)$ 称为系统 (7.1.1) 和性能指标 (7.1.3) 的 Hamilton 函数.

设 $u^{*}(t)$ 是系统 (7.1.1) 和性能指标 (7.1.3) 的最优控制， $x^{*}(t)$ 是相应的最优轨线， $x^{*}(t_{0}) = x_{0}.u^{*}(t), x^{*}(t)$ 使 $J_{1}[u]$ 达到极小，即 $J_{1}[u^{*}] \leqslant J_{1}[u], \forall u(\cdot) \in \mathcal{U}_{[t_{0}, t_{f}]}.$ 令 $\varepsilon$ 为充分小的实数，而 $\delta u(t)$ 为定义在 $[t_{0}, t_{f}]$ 上的任一分段连续函数（规定除 $t_{f}$ 外，其他不连续时刻为右连续）。易知

$$u (\cdot) \stackrel {\mathrm{def}} {=} u ^ {*} (\cdot) + \varepsilon \delta u (\cdot) \in \mathcal {U} _ {[ t _ {0}, t _ {f} ]}, \tag {7.1.7}$$

且式 (7.1.1) 的对应于式 (7.1.7) 中 $u(t)$ 的轨线 $x(t)$ 能表示为

$$x (t) = x ^ {*} (t) + \varepsilon \delta x (t) + \frac {\varepsilon^ {2}}{2} \delta^ {2} x (t) + o (\varepsilon^ {2}), \tag {7.1.8}$$

其中 $\delta x(t)$ 为轨线 $x(t)$ 关于 $x^{*}(t)$ 的一次变分，由下式求解：

$$
\left\{ \begin{array}{l l} { \frac {\mathrm{d}}{\mathrm{d} t} \delta x (t) = \frac {\partial f}{\partial x} \Big | _ {*} \delta x (t) + \frac {\partial f}{\partial u} \Big | _ {*} \delta u (t),} \\ { \delta x (t _ {0}) = 0 (n \text {维零向量}),} \end{array} \right. \tag {7.1.9}
$$

$\delta^2 x(t)$ 为轨线 $x(t)$ 关于 $x^{*}(t)$ 的二次变分，由下式确定

$$\delta^ {2} x (t) = \lim _ {\varepsilon \rightarrow 0} \frac {2}{\varepsilon^ {2}} [ x (t) - x ^ {*} (t) - \varepsilon \delta x (t) ]. \tag {7.1.10}$$
