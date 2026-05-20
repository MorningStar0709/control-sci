# 10.5.4 最优轨迹的优化

最优轨迹能够通过优化与参考轨迹的偏差来间接地得到。假设系统达到稳态的最大允许时间为 $t = 3T_{E}$ ，考虑到能量守恒定理，用非保守力做功来表示系统在运动过程中消耗的总能量，目标函数选择为

$$J = \omega \int_ {0} ^ {3 T _ {\mathrm{E}}} | \tau \dot {\theta} | \mathrm{d} t + (1 - \omega) \int_ {0} ^ {3 T _ {\mathrm{E}}} | \operatorname{dis} (t) | \mathrm{d} t \tag {10.14}$$

式中， $\omega$ 为权值； $\tau$ 为控制输入信号； $\mathrm{dis}(t)$ 为实际跟踪轨迹与理想轨迹之间的距离。

通过采用差分进化算法，优化轨迹式（10.13），使目标函数最小，从而获得最优轨迹。差分进化算法的设定参数如下：最大迭代次数 G，种群数 Size，搜索空间的维数 D，放大因子 F，交叉因子 CR。经过差分进化算法可得到一组最优偏差，进而得到最优的离散轨迹如下：

$$\overline {{{\theta}}} _ {\mathrm{op}} = \left[ \overline {{{\theta}}} _ {\mathrm{op}, 0}, \overline {{{\theta}}} _ {\mathrm{op}, 1}, \dots , \overline {{{\theta}}} _ {\mathrm{op}, 2 n - 1}, \overline {{{\theta}}} _ {\mathrm{op}, 2 n} \right] \tag {10.15}$$

为了获得连续型的最优轨迹，采用三次样条插值进行轨迹规划，即利用三次样条插值的方法对离散轨迹进行插值。插值的边界条件如下：

$$\theta_ {\mathrm{op}} (0) = \overline {{\theta}} _ {\mathrm{op}, 0} = \theta_ {0},\theta_ {\mathrm{op}} \left(T _ {\mathrm{E}}\right) = \bar {\theta} _ {\mathrm{op}, 2 n} = \theta_ {\mathrm{d}},\dot {\theta} _ {\mathrm{op}} (0) = \bar {\dot {\theta}} _ {\mathrm{op}, 0} = \dot {\theta} _ {0} = 0,\dot {\theta} _ {\mathrm{op}} \left(T _ {\mathrm{E}}\right) = \dot {\bar {\theta}} _ {\mathrm{op}, 2 n} = \dot {\theta} _ {\mathrm{d}} = 0$$

插值节点为

$$\theta_ {\mathrm{op}} (t _ {j}) = \overline {{\theta}} _ {\mathrm{op}, j}, \quad t _ {j} = \frac {j}{2 n} T _ {\mathrm{E}}, \quad j = 1, 2, \dots , 2 n - 1$$

将插值得到的连续函数 $\theta_{\mathrm{op}}(k)$ 作为关节的最优轨迹。采用 PD 控制算法实现对最优轨迹的跟踪，控制律为

$$\tau = k _ {\mathrm{p}} e + k _ {\mathrm{d}} \dot {e} \tag {10.16}$$

式中 $k_{p}>0$ ; $\dot{k}_{d}>0$ 。

![](image/f3bd16acadb1bb7e32f5afc65009a218f6299be3429b168fa085d3e7f94a6bc2.jpg)
