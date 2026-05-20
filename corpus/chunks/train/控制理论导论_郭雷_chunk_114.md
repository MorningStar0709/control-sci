其中 K 是一个 $r \times n$ 常值控制增益矩阵，使得 $A + BK$ 是稳定的矩阵。又由坐标变换 (1.8.13) 有

$$
x (t) = \left[ \begin{array}{c c} C _ {1} ^ {- 1} & - C _ {1} ^ {- 1} C _ {2} \\ 0 & I _ {n - m} \end{array} \right] \left[ \begin{array}{l} \overline {{x}} _ {1} (t) \\ \overline {{x}} _ {2} (t) \end{array} \right].
$$

若将 $K$ 分成相应的两部分

$$
\boldsymbol {K} = \left[ \begin{array}{l l} \boldsymbol {K} _ {1} & \boldsymbol {K} _ {2} \end{array} \right],
$$

其中 $K_{1}$ 和 $K_{2}$ 分别为 $r \times m, r \times (n - m)$ 常值矩阵. 则式 (1.8.15) 可写成

$$u (t) = K _ {1} C _ {1} ^ {- 1} y (t) + \left(K _ {2} - K _ {1} C _ {1} ^ {- 1} C _ {2}\right) \bar {x} _ {2} (t). \tag {1.8.16}$$

为使控制规律 (1.8.16) 成为物理上能实现的，必须对 $\overline{x}_2(t)$ 设计观测器.

由于系统(1.8.14)是能观测的，因此由引理1.7.1知 $(\overline{A}_{22},\overline{A}_{12})$ 也是能观测的，从而由定理1.7.3知存在极小阶观测器，即有常值增益矩阵 $G_{2}$ ，使得 $\overline{A}_{22} - G_2\overline{A}_{12}$ 是稳定的矩阵，且极小阶观测器方程为

$$\overline {{{x}}} _ {2 e} (t) = x _ {c} (t) + G _ {2} y (t), \tag {1.8.17}\dot {x} _ {c} (t) = (\overline {{{A}}} _ {2 2} - G _ {2} \overline {{{A}}} _ {1 2}) x _ {c} (t) + (\overline {{{B}}} _ {2} - G _ {2} \overline {{{B}}} _ {1}) u (t) \tag {1.8.18}+ \left[ \left(\overline {{{A}}} _ {2 1} - G _ {2} \overline {{{A}}} _ {1 1}\right) + \left(\overline {{{A}}} _ {2 2} - G _ {2} \overline {{{A}}} _ {1 2}\right) G _ {2} \right] y (t), \tag {1.8.19}$$

其中 $x_{2e}(t)$ 是 $\bar{x}_2(t)$ 的状态估计。取物理上能实现的控制规律为

$$
\begin{array}{l} u (t) = K _ {1} C _ {1} ^ {- 1} y (t) + \left(K _ {2} - K _ {1} C _ {1} ^ {- 1} C _ {2}\right) \bar {x} _ {2 e} (t) \\ = \left[ K _ {1} C _ {1} ^ {- 1} + \left(K _ {2} - K _ {1} C _ {1} ^ {- 1} C _ {2}\right) G _ {2} \right] y (t) \\ + \left(\boldsymbol {K} _ {2} - \boldsymbol {K} _ {1} \boldsymbol {C} _ {1} ^ {- 1} \boldsymbol {C} _ {2}\right) x _ {c} (t). \tag {1.8.20} \\ \end{array}
$$

令

$$
\left\{ \begin{array}{l} \boldsymbol {F} = \boldsymbol {K} _ {1} \boldsymbol {C} _ {1} ^ {- 1} + (\boldsymbol {K} _ {2} - \boldsymbol {K} _ {1} \boldsymbol {C} _ {1} ^ {- 1} \boldsymbol {C} _ {2}) \boldsymbol {G} _ {2}, \\ \boldsymbol {F} _ {c} = \boldsymbol {K} _ {2} - \boldsymbol {K} _ {1} \boldsymbol {C} _ {1} ^ {- 1} \boldsymbol {C} _ {2}, \end{array} \right. \tag {1.8.21}
$$

则由式 (1.8.20) 得

$$u (t) = \boldsymbol {F} _ {\mathrm{c}} x _ {\mathrm{c}} (t) + \boldsymbol {F} y (t). \tag {1.8.22}$$

将这个控制规律代入方程 (1.8.17), 并令
