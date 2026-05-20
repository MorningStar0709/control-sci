不等式 (7.5.32) 称为系统的 $L_{2^{-}}$ 增益不等式.

注7.5.4 这里要找的控制规律 $u(\cdot)$ 可以是状态反馈形式 $u(x)$ , 可以是静态输出反馈形式 $u(y)$ , 也可以是动态输出反馈形式 $u(\xi)$ , 这里 $\xi$ 是待设计的动态系统的状态 (或输出), 即

$$\dot {\xi} = f _ {c} (\xi , y).$$

对设计的控制器 $u = u(\xi)$ (称为动态补偿器), 当 $w = 0$ 时相应的闭环系统指

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + G _ {2} (x) u (\xi), \\ \dot {\xi} = f _ {c} (\xi , y), \\ y = h _ {2} (x). \end{array} \right. \tag {7.5.33}
$$

于是系统 (7.5.29) 的 $H_{\infty}$ 控制问题提法 (1) 中谈到的闭环系统 (7.5.30) 的内部稳定性，在这里指的是系统 (7.5.33) 的渐近稳定性。

鉴于难于事先求得系统的 $L_{2}$ -增益 $\mathcal{G}_{2c}$ ，一般只能求得某种估计值。与线性系统相似，也有非线性 $H_{\infty}$ 控制的“次优问题”。

仿射非线性系统的 $H_{\infty}$ 次优问题。仿射非线性 $H_{\infty}$ 次优问题指的是：给定 $\gamma_0 > 0$ ，寻求控制规律 $u = u(\cdot)$ ，使得在此控制器作用下的闭环系统内部稳定，且 $\forall w(\cdot) \in L_2([0, +\infty); \mathbb{R}^{r_1})$ ，相应于 $w(t)$ 的闭环系统的零初态响应 $z_c(t) \stackrel{\mathrm{def}}{=} h(x(t)) + K_{11}(x(t))w(t) + K_{12}(x(t))u(\cdot)$ 满足不等式

$$\int_ {0} ^ {+ \infty} z _ {c} ^ {\mathrm{T}} (t) z _ {c} (t) \mathrm{d} t \leqslant \gamma_ {0} \int_ {0} ^ {+ \infty} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t. \tag {7.5.34}$$

如果这样的控制规律 $u = u(\cdot)$ 存在，则说系统(7.5.29)的非线性 $H_{\infty}$ 次优问题可解.

下面考察非线性 $H_{\infty}$ 次优问题的解。限于篇幅，这里仅就系统 (7.5.29) 中 $K_{11}(x) = 0, h_1^{\mathrm{T}}(x)K_{12}(x) = 0, K_{12}^{\mathrm{T}}(x)K_{12}(x) \stackrel{\mathrm{def}}{=} R_2(x)$ 为正定对称阵，且 $x, w$ 皆可测的全息情况进行论述。将受外干扰的控制系统视为对策系统，而将系统的控制和干扰分别视为对策中的甲方和乙方的策略，于是可用7.4中定量微分对策的思想，方法及某些结果来处理“次优问题”。为此，给定 $\gamma_0 > 0$ ，取性能指标

$$J [ u, w ] = \frac {1}{2} \int_ {0} ^ {+ \infty} \left[ z ^ {\mathrm{T}} (t) z (t) - \gamma_ {0} w (t) ^ {\mathrm{T}} w (t) \right] \mathrm{d} t,$$

并考察定量微分对策问题

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + G _ {1} (x) w + G _ {2} (x) u, \\ z = h _ {1} (x) + K _ {1 1} (x) w + K _ {1 2} (x) u, \\ \min _ {u} \max _ {w} J [ u, w ], (u, w) \in L _ {2} ([ 0, + \infty); \mathbb {R} ^ {r _ {2}}) \times L _ {2} ([ 0, + \infty); \mathbb {R} ^ {r _ {1}}). \end{array} \right. \tag {7.5.35}
$$

根据7.4中HJI方程的有关结论,问题(7.5.35)的反馈形式的最优策略 $(u^{*}(x),w^{*}(x))$ 为

$$
\left\{ \begin{array}{l} u ^ {*} (x) = - R _ {2} ^ {- 1} G _ {2} ^ {\mathrm{T}} (x) \left(\frac {\partial J ^ {*} (x)}{\partial x}\right) ^ {\mathrm{T}}, \\ w ^ {*} (x) = \frac {1}{\gamma_ {0}} G _ {1} ^ {\mathrm{T}} (x) \left(\frac {\partial J ^ {*} (x)}{\partial x}\right) ^ {\mathrm{T}}, \end{array} \right. \tag {7.5.36}
$$

其中 $J^{*}(x)$ 是带终端条件的偏微分方程
