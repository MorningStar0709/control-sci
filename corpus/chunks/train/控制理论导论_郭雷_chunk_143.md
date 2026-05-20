定理2.2.4 设 $f(t, x)$ 为定义在矩形区域 $\pi(a, b) = \{(t, x) \mid |t - t_0| \leqslant a, |x - x_0| \leqslant b\}$ 上关于 $x$ 不减的连续函数， $\varphi(t)$ 为定义在 $[t_0 - a, t_0 + a]$ 上的连续函数，且当 $t \in [t_0 - a, t_0 + b]$ 时， $(t, \varphi(t)) \in \pi(a, b)$ .

(1) 如果

$$\varphi (t) \leqslant x _ {0} + \int_ {t _ {0}} ^ {t} f (\tau , \varphi (\tau)) \mathrm{d} \tau , \qquad \forall t \in [ t _ {0}, t _ {0} + a ], \tag {2.2.14}$$

或

$$\varphi (t) \geqslant x _ {0} + \int_ {t _ {0}} ^ {t} f (\tau , \varphi (\tau)) \mathrm{d} \tau , \quad \forall t \in [ t _ {0}, t _ {0} + a ], \tag {2.2.15}$$

则

$$\varphi (t) \leqslant \bar {x} (t) \quad \text {或} \quad \varphi (t) \geqslant \underline {{x}} (t), \qquad \forall t \in [ t _ {0}, t _ {0} + h ]; \tag {2.2.16}$$

(2) 如果

$$\varphi (t) \geqslant x _ {0} + \int_ {t _ {0}} ^ {t} f (\tau , \varphi (\tau)) \mathrm{d} \tau , \quad \forall t \in [ t _ {0} - h, t _ {0} ], \tag {2.2.17}$$

或

$$\varphi (t) \leqslant x _ {0} + \int_ {t _ {0}} ^ {t} f (\tau , \varphi (\tau)) \mathrm{d} \tau , \quad \forall t \in [ t _ {0} - h, t _ {0} ], \tag {2.2.18}$$

则

$$\varphi (t) \leqslant \bar {x} (t) \quad \text {或} \quad \varphi (t) \geqslant \underline {{{{x}}}} (t), \qquad \forall t \in [ t _ {0} - h, t _ {0} ],$$

其中 $h = \min (a, b / M)$ , $M = \max_{(t, x) \in \pi(a, b)} |f(t, x)|$ , 而 $\bar{x}(t)$ 和 $\underline{x}(t)$ 分别是方程 (2.2.1) 过点 $(t_0, x_0)$ 的最大解和最小解.

证明 按如下方式构造方程 (2.2.1) 过点 $(t_0, x_0)$ 的逐次逼近序列

$$
\begin{array}{l} x _ {0} (t) = \varphi (t), \\ x _ {1} (t) = x _ {0} + \int_ {t _ {0}} ^ {t} f (\tau , x _ {0} (\tau)) \mathrm{d} \tau , \\ \begin{array}{l} \vdots \\ x _ {n} (t) = x _ {0} + \int_ {t _ {0}} ^ {t} f (\tau , x _ {n - 1} (\tau)) \mathrm{d} \tau , \quad n = 1, 2, \dots . \end{array} \\ \end{array}
$$

能够证明， $\{x_{n}(t)\}$ 在区间 $[t_0 - h, t_0 + h]$ 上等度连续和一致有界，而在 $[t_0, t_0 + h]$ 上单调不减。根据 Ascoli-Arzelo 引理， $\{x_{n}(t)\}$ 在 $[t_0, t_0 + h]$ 上一致收敛于某连续函数 $x(t)$ 。显然， $x(t)$ 是方程 (2.2.1) 过 $(t_0, x_0)$ 点的解，且有 $\varphi(t) \leqslant x(t), t \in [t_0, t_0 + h]$ 。于是得到

$$\varphi (t) \leqslant \bar {x} (t) \quad t \in [ t _ {0}, t _ {0}. + h ].$$

同理可证，当式(2.2.15)成立时，有 $\varphi(t) \geqslant x(t)$ . 类似地可证(2)中结论.

定理 2.2.5(Gronwall 不等式) 设 $\lambda(t\cdot):[t_{0},t_{1}]\to\mathbb{R}_{+}$ 为可积函数， $\varphi(\cdot),\xi(\cdot):[t_{0},t_{1}]\to\mathbb{R}$ 为绝对连续函数．假定

$$\varphi (t) \leqslant \int_ {t _ {0}} ^ {t} \lambda (\tau) \varphi (\tau) \mathrm{d} \tau + \xi (t), \quad \forall t \in [ t _ {0}, t _ {1} ],$$

那么
