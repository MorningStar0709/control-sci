(1) $\forall w(\cdot) \in L_2([0, +\infty); \mathbb{R}^r)$ , 系统 (7.5.23) 的零初值问题的解 $x(t) \stackrel{\mathrm{def}}{=} x(t; 0, 0)$ 在 $[0, +\infty)$ 存在唯一;  
(2) $\forall w(\cdot) \in L_2([0, +\infty); \mathbb{R}^r)$ , 系统 (7.5.23) 的零初态响应 $z(\cdot) \stackrel{\mathrm{def}}{=} h(x(\cdot)) \in L_2([0, +\infty); \mathbb{R}^m)$ ;

(3) 当 $w = 0$ 时， $\dot{x} = f(x)$ 的零解渐近稳定.

定义 7.5.1 $G_{2}=\sup_{w\in L_{2}([0.+\infty);\mathbb{R}^{r})}\frac{\int_{0}^{+\infty}z^{\mathrm{T}}(t)z(t)\mathrm{d}t}{\int_{0}^{+\infty}w^{\mathrm{T}}(t)w(t)\mathrm{d}t}$ 称为系统 (7.5.23) 的 $L_{2}-$

增益.

显然，我们有

$$\int_ {0} ^ {+ \infty} z ^ {\mathrm{T}} (t) z (t) \mathrm{d} t \leqslant \mathcal {G} _ {2} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t, \quad \forall w \in L _ {2} ([ 0, + \infty); \mathbb {R} ^ {r}). \tag {7.5.24}$$

不等式 (7.5.24) 称为系统 (7.5.23) 的 $L_{2}$ -增益不等式.

这里关心的问题是：第一， $G_{2}$ 是否存在及如何求得，第二，在什么条件下不等式(7.5.24)成立。一般说来，第一个问题难于回答。对于第二个问题可得到部分解答：即根据工程设计要求及可能性，事先给定一个 $\gamma_{0}$ ，作为 $L_{2}$ -增益的初“估计”。然后再根据对系统的综合要求进行修正。

给定 $\gamma_0$ ，对于渐近稳定系统 $\dot{x} = f(x)$ ，探讨系统 (7.5.23) 的 $L_{2}$ -增益不等式何时成立。为此，取性能指标

$$J [ w ] = \frac {1}{2} \int_ {0} ^ {+ \infty} \left[ z ^ {\mathrm{T}} (t) z (t) - \gamma_ {0} w (t) ^ {\mathrm{T}} w (t) \right] \mathrm{d} t.$$

考察下列“最坏”干扰问题：

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + G (x) w, \\ z = h (x), \\ \max _ {w \in L _ {2} ([ 0, + \infty); \mathbb {R} ^ {r})} J [ w ]. \end{array} \right. \tag {7.5.25}
$$

利用7.1中关于HJB方程的结果，使问题(7.5.25)中 $J[w]$ 达到极大的 $\pmb{w}^{*}(x)$ 为

$$w ^ {*} (x) = \frac {1}{2 \gamma_ {0}} G ^ {\mathrm{T}} (x) \frac {\partial J ^ {*} (x)}{\partial x}, \tag {7.5.26}$$

其中 $J^{*}(x)$ 是下列带终端条件的偏微分方程：

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial x} f (x) + \frac {1}{2 \gamma_ {0}} \left(\frac {\partial J}{\partial x}\right) G (x) G ^ {\mathrm{T}} (x) \left(\frac {\partial J}{\partial x}\right) ^ {\mathrm{T}} + h ^ {\mathrm{T}} (x) h (x) = 0, \\ J (0) = 0 \end{array} \right. \tag {7.5.27}
$$

的非负解.

不难证明，对于渐近稳定系统 $\dot{x} = f(x)$ ，当方程(7.5.27)存在非负解 $J^{*}(x)$ 时， $\forall w(t) \in L_2[[0, +\infty); \mathbb{R}^r]$ ，成立不等式

$$\int_ {0} ^ {+ \infty} z ^ {\mathrm{T}} (t) z (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t, \tag {7.5.28}$$

其中 $z(t) \stackrel{\mathrm{def}}{=} h(x(t))$ 为系统 (7.5.23) 的零初态响应。综上所述可得：
