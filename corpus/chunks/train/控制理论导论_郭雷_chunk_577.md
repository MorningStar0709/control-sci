定理 7.5.2 一个渐近稳定受外干扰影响的仿射非线性系统 (7.5.23), 如果方程 (7.5.27) 存在非负解, 则 $\forall w(\cdot) \in L_2([0, +\infty); \mathbb{R}^r)$ , (7.5.23) 相应于 $w(\cdot)$ 的零初态响应 $z(t)$ 满足不等式 (7.5.28).

推论 7.5.2 一个渐近稳定受外干扰影响的仿射非线性系统 (7.5.23), 当偏微分不等式

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial x} f (x) + \frac {1}{2 \gamma_ {0}} \left(\frac {\partial J}{\partial x}\right) G (x) G ^ {\mathrm{T}} (x) \left(\frac {\partial J}{\partial x}\right) ^ {\mathrm{T}} + h ^ {\mathrm{T}} (x) h (x) \leqslant 0, \\ J (0) = 0 \end{array} \right.
$$

存在非负解时， $\forall w(\cdot) \in L_2[[0, +\infty); \mathbb{R}^r]$ ，(7.5.23) 相应于 $w(t)$ 的零初态响应 $z(t)$ 满足不等式 (7.5.23).

仿射非线性系统的 $H_{\infty}$ 控制. 考察受外干扰的仿射非线性控制系统

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + G _ {1} (x) w + G _ {2} (x) u, \\ z = h _ {1} (x) + K _ {1 1} (x) w + K _ {1 2} (x) u, \\ y = h _ {2} (x) + K _ {2 2} (x) w, \end{array} \right. \tag {7.5.29}
$$

其中 $x \in R^{n}, u \in R^{r_{2}}, w \in R^{r_{1}}, z \in R^{m_{1}}$ 和 $y \in R^{m_{2}}$ 分别是系统状态变量，控制输入变量，外干扰变量，被调输出变量和量测输出变量， $G_{1}(x) = [g_{1}^{1}(x), g_{2}^{1}(x), \cdots, g_{r_{1}}^{1}(x)]$ ， $G_{2}(x) = [g_{1}^{2}(x), g_{2}^{2}(x), \cdots, g_{r_{2}}^{2}(x)]$ ， $f(x), g_{i}^{1}(x), g_{j}^{2}(x), i = 1, 2, \cdots, r_{1}, j = 1, 2, \cdots, r_{2}$ 皆是定义在 $R^{n}$ 上的光滑 n 维向量场， $h_{1}(x), h_{2}(x)$ 和 $K_{11}(x), K_{12}(x), K_{22}(x)$ 分别是定义在 $R^{n}$ 上的相应维数的向量值和阵值函数.

非线性系统 (7.5.29) 的 $H_{\infty}$ 控制问题指的是：寻找（设计）控制规律（控制器） $u = u(\cdot)$ ，使得系统 (7.5.29) 在 $u = u(\cdot)$ 的作用下有

(1) 当 $w = 0$ 时，相应于 (7.5.29) 的闭环系统

$$\dot {x} = f (x) + G (x) u (\cdot) \tag {7.5.30}$$

是渐近稳定的，即系统内部稳定；

(2) $\forall w(\cdot) \in L_2([0, +\infty); \mathbb{R}^{r_1})$ , 受 $w(t)$ 影响的闭环系统

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + G _ {1} (x) w (t) + G _ {2} (x) u (\cdot), \\ x (0) = 0 \end{array} \right. \tag {7.5.31}
$$

的解 $x(t)$ 对应的 $z_{c}(t) \stackrel{\mathrm{def}}{=} h_{1}(x(t)) + K_{11}(x(t))w(t) + K_{12}(x(t))u(\cdot)$ (即带干扰 $w(t)$ 的闭环系统的零初响应) 满足 $L_{2}$ -增益不等式

$$\int_ {0} ^ {+ \infty} z _ {c} ^ {\mathrm{T}} (t) z _ {c} (t) \mathrm{d} t \leqslant \mathcal {G} _ {2 c} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t, \tag {7.5.32}$$

并且 $\mathcal{G}_{2c}$ 是满足上述不等式的最小常数，这里

$$\mathcal {G} _ {2 c} = \sup _ {w (t) \in L _ {2} (| 0, + \infty); \mathbb {R} ^ {\tau_ {1}})} \frac {\int_ {0} ^ {+ \infty} z _ {c} ^ {\mathrm{T}} (t) z _ {c} (t) \mathrm{d} t}{\int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t}, \text {称为受干扰闭环系统的} L _ {2 ^ {-}} \text {增益}.$$
