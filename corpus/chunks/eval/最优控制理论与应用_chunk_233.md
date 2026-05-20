# 11.4.1 线性定常系统 $H_{\infty}$ 最优控制问题的提出

考虑带外干扰的线性定常系统

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} _ {1} \boldsymbol {w} + \boldsymbol {B} _ {2} \boldsymbol {u}z = C _ {1} x + D _ {1 1} w + D _ {1 2} u \tag {11-20}\mathbf {y} = \boldsymbol {C} _ {2} \mathbf {x} + \boldsymbol {D} _ {2 1} \mathbf {w}$$

其中 $x \in \mathbb{R}^n$ 是状态, $u \in \mathbb{R}^{r_1}$ 是控制输入信号, $w \in \mathbb{R}^{r_2}$ 是外干扰输入信号（辅助信号), $y \in \mathbb{R}^{m_1}$ 是测量输出信号, $z \in \mathbb{R}^{m_2}$ 是系统输出信号（评价信号）, $A, B_1, B_2, C_1, C_2, D_{11}, D_{12}, D_{21}$ 皆为适当维数的常数阵。

系统(11-20)的 $H_{\infty}$ 最优控制问题是求控制量 $\pmb{u}$ , 使得:

(1) 闭环系统内稳定, 即当 w = 0 时闭环系统

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} _ {2} \boldsymbol {u} \tag {11-21}$$

是渐近稳定的；

(2) 对于 $\forall w(t) \in L_{2}[0, +\infty)$ ，控制量 u 使得系统

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} _ {1} \boldsymbol {w} + \boldsymbol {B} _ {2} \boldsymbol {u} \quad \boldsymbol {x} (0) = \mathbf {0} \tag {11-22}\boldsymbol {z} = \boldsymbol {C} _ {1} \boldsymbol {x} + \boldsymbol {D} _ {1 1} \boldsymbol {w} + \boldsymbol {D} _ {1 2} \boldsymbol {u}$$

的输出满足不等式

$$\int_ {0} ^ {+ \infty} z ^ {\mathrm{T}} (t) z (t) \mathrm{d} t \leqslant l _ {2} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t \tag {11-23}$$

其中：

$$l _ {2} = \sup _ {\boldsymbol {w} (t) \in L _ {2} [ 0, + \infty)} \frac {\int_ {0} ^ {+ \infty} \boldsymbol {z} ^ {\mathrm{T}} (t) \boldsymbol {z} (t) \mathrm{d} t}{\int_ {0} ^ {+ \infty} \boldsymbol {w} ^ {\mathrm{T}} (t) \boldsymbol {w} (t) \mathrm{d} t}$$

不等式(11-23)是在所求控制量 $\pmb{u}$ 作用下，闭环系统对外干扰抑制能力的一种度量， $l_{2}$ 称为系统式(11-20)的 $L_{2}-$ 增益，它反映了带外干扰的闭环系统的输出能量对外干扰信号能量的衰减程度。这里的控制量 $\pmb{u}$ 可以是状态反馈(当全部状态可观测时)和观测输出的静态输出反馈,也可以是状态量和观测输出量的动态反馈。至于选择什么结构形式的控制器,要视系统的要求和实现的难易来选定。

在 $H_{\infty}$ 控制器设计中，将寻求满足上述条件(1)和(2)的控制量 $\pmb{u}$ 的问题称为“最优问题”，其中涉及到求 $L_{2} -$ 增益 $l_{2}$ 的问题。虽然从理论上讲，在一定条件下，可证明系统式(11-20)的 $L_{2} -$ 增益存在，但实际上却很难求得它。

因此，从工程实现考虑，在用 $H_{\infty}$ 控制方法求控制器时，常根据工程设计要求而采取给定增益 $\gamma_{0}$ 的所谓“次优控制问题”。

$H_{\infty}$ 控制设计的次优问题是指对于事先给定的 $0 < \gamma_0 < +\infty$ ，寻求控制量 $\pmb{u}$ ，使得满足：

（1）闭环系统内稳定，即当 w=0 时，闭环系统式(11-21)是渐近稳定的。

(2) 对 $\forall w(t) \in L_2[0, +\infty)$ , 控制量 $\pmb{u}$ 使得系统 (11-22) 的系统输出具有如下性质:

$$\int_ {0} ^ {+ \infty} z ^ {\mathrm{T}} (t) z (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t$$
