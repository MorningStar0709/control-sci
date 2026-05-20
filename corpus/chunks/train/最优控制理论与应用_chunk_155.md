# 1. 对象状态方程

汽车可看成纯惯性环节,其传递函数为

$$\boldsymbol {G} _ {P} (s) = \frac {\boldsymbol {X} (s)}{\boldsymbol {U} (s)} = \frac {K v}{s ^ {2}} \tag {8-67}$$

令 $x_{1} = x, x_{2} = \dot{x}_{1}$ , 则汽车的状态方程为

$$\dot {X} = A X + B U + W \tag {8-68}$$

其中

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], \quad \boldsymbol {B} = \left[ \begin{array}{l} 0 \\ K _ {v} \end{array} \right], \quad \boldsymbol {W} = \left[ \begin{array}{l} 0 \\ w \end{array} \right]
$$

根据实例,干扰力 W 为服从正态分布的白噪声

$$
E [ \boldsymbol {W} (t) ] = 0, \quad E [ \boldsymbol {W} (t) \boldsymbol {W} ^ {\mathrm{T}} (\tau) ] = Q \delta (t - \tau)
Q = \left[ \begin{array}{c c} 0 & 0 \\ 0 & q \end{array} \right]
$$

$K_{\nu}$ 和 $q$ 为常数。

2. 量测方程

$$\boldsymbol {Z} = \boldsymbol {H} \boldsymbol {X} + \boldsymbol {V} \tag {8-69}$$

其中， $H=[1\quad0]$ ，V为正态分布的噪声， $E[V(t)]=0$ $E[V(t)V^{\mathrm{T}}(\tau)]=r\delta(t-\tau)$ 且干扰 W 和测量噪声 V 不相关，即

$$E [ \boldsymbol {V} (t) \boldsymbol {W} ^ {\mathrm{T}} (\tau) ] = 0$$

3. 性能指标

$$J = E \left[ \int_ {0} ^ {\infty} \left(a x _ {1} ^ {2} + b u ^ {2}\right) \mathrm{d} t \right] \tag {8-70}$$

其中,第一项表示对汽车侧向位移的约束,第二项则表示对控制量 U 的约束。

4. 最优控制的设计

这是线性二次型高斯问题,可以应用分离定理。因不是无限长时间定常系统调节器问题,可以用稳态控制增益,即

$$u = - \boldsymbol {L} \hat {\boldsymbol {X}} \tag {8-71}\boldsymbol {L} = \overline {{\boldsymbol {R}}} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} \tag {8-72}$$

其中 $K$ 满足矩阵黎卡提代数方程

$$- \boldsymbol {K} \boldsymbol {A} - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {K} + \boldsymbol {K} \boldsymbol {B} \overline {{\boldsymbol {R}}} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} - \overline {{\boldsymbol {Q}}} = \mathbf {0} \tag {8-73}$$

这里，

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \quad \boldsymbol {K} = \left[ \begin{array}{c c} K _ {1 1} & K _ {1 2} \\ K _ {1 2} & K _ {2 2} \end{array} \right] \quad \overline {{{\boldsymbol {Q}}}} = \left[ \begin{array}{l l} a & 0 \\ 0 & 0 \end{array} \right]

\boldsymbol {B} = \left[ \begin{array}{l} 0 \\ K _ {V} \end{array} \right] \quad \overline {{\boldsymbol {R}}} = b
$$

把这些值代黎卡提方程(8-73)，得
