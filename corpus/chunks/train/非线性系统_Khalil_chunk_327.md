# 11.2 标准模型的时间尺度特性

奇异扰动引起动力学系统的多时间尺度特性,由系统对外部激励的慢瞬态和快瞬态响应描述。简单说就是慢响应由降阶模型(11.5)逼近,而降阶模型的响应与整个模型(11.1)\~(11.2)响应之间的差异就是快瞬态响应。为了理解这一点,解状态方程

$$\dot {x} = f (t, x, z, \varepsilon), \quad x (t _ {0}) = \xi (\varepsilon) \tag {11.6}\varepsilon \dot {z} = g (t, x, z, \varepsilon), \quad z (t _ {0}) = \eta (\varepsilon) \tag {11.7}$$

其中 $\xi(\varepsilon)$ 和 $\eta(\varepsilon)$ 随 $\varepsilon$ 光滑变化，且 $t_{0} \in [0, t_{1})$ 。设 $x(t, \varepsilon)$ 和 $z(t, \varepsilon)$ 表示方程 (11.6) 和方程 (11.7) 的解。当定义降阶模型 (11.5) 的相应问题时，可以仅指定 n 个初始条件，因为是 n 阶模型。自然保留 x 的初始状态得到降阶问题

$$\dot {x} = f (t, x, h (t, x), 0), \quad x (t _ {0}) = \xi_ {0} \stackrel {\mathrm{def}} {=} \xi (0) \tag {11.8}$$

用 $\bar{x}(t)$ 表示方程(11.8)的解。因为从降阶模型中去掉了变量 z，并由其“准稳态”（quasi-steady-state） $h(t,x)$ 代换，通过解方程(11.8)能得到的有关 z 的信息只是计算

$$\bar {z} (t) \stackrel {\mathrm{def}} {=} h (t, \bar {x} (t))$$

它描述了当 $x = \bar{x}$ 时 $z$ 的准稳态特性。与在 $t_0$ 时刻由给定的 $\eta (\varepsilon)$ 开始的原始变量 $z$ 对比，准稳态 $\bar{z}$ 不能自由地从给定值开始，而且可能在其初始值 $\bar{z}(t_0) = h(t_0,\xi_0)$ 与给定的初始状态 $\eta (\varepsilon)$ 之间存在很大差异，这样 $\bar{z} (t)$ 就可能不是 $z(t,\varepsilon)$ 的一致逼近。最好的结果是估计量

$$z (t, \varepsilon) - \bar {z} (t) = O (\varepsilon)$$

在一个不包括 $t_0$ 的区间内成立，即 $t \in [t_b, t_1]$ ，其中 $t_b > t_0$ 。另一方面，有理由期望估计量

$$x (t, \varepsilon) - \bar {x} (t) = O (\varepsilon)$$

对于所有 $t \in [t_0, t_1]$ 一致成立，因为

$$x (t _ {0}, \varepsilon) - \bar {x} (t _ {0}) = \xi (\varepsilon) - \xi (0) = O (\varepsilon)$$

如果在 $[t_b, t_1]$ 上误差 $z(t, \varepsilon) - \bar{z}(t)$ 确实是 $O(\varepsilon)$ ，则在初始（边界层）区间 $[t_0, t_b]$ 内，变量 $z$ 一定逼近 $\bar{z}$ 。要记住，因为 $\dot{z} = g / \varepsilon$ ，故 $z$ 的速度可能较高。事实上，在方程(11.2)中已经设定$\varepsilon = 0$ ，只要 $g \neq 0$ ，就可以使 $z$ 的瞬态是即时的。根据前面的平衡点稳定性研究，显然不能希望 $z$ 收敛到其准稳态 $\bar{z}$ ，除非满足一定的稳定性条件，这样的条件将由下面的分析给出。

为了便于进行分析,做变量代换

$$y = z - h (t, x) \tag {11.9}$$

将 z 的准稳态移至原点。采用新的变量 $(x, y)$ 之后，整个问题是

$$\dot {x} = f (t, x, y + h (t, x), \varepsilon), x \left(t _ {0}\right) = \xi (\varepsilon) \tag {11.10}\varepsilon \dot {y} = g (t, x, y + h (t, x), \varepsilon) - \varepsilon \frac {\partial h}{\partial t} \tag {11.11}- \varepsilon \frac {\partial h}{\partial x} f (t, x, y + h (t, x), \varepsilon), \quad y (t _ {0}) = \eta (\varepsilon) - h (t _ {0}, \xi (\varepsilon))$$

现在方程(11.11)的准稳态是 y=0，代入方程(11.10)就得到了降价模型(11.8)。为了分析方程(11.11)，应该注意，即使当 $\varepsilon$ 趋于零和 $\dot{y}$ 趋于无限时， $\varepsilon\dot{y}$ 也可以保持有限值。令
