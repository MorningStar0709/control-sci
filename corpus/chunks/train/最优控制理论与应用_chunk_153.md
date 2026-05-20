# 8.2 连续随机线性调节器问题

不加证明地列出下面的结果,设连续随机线性系统为

$$\dot {\boldsymbol {X}} (t) = \boldsymbol {A} (t) \boldsymbol {X} (t) + \boldsymbol {B} (t) \boldsymbol {U} (t) + \boldsymbol {G} (t) \boldsymbol {W} (t) \tag {8-59}\mathbf {Z} (t) = \mathbf {H} (t) \mathbf {X} (t) + \mathbf {V} (t) \tag {8-60}$$

其中， $W(t)$ 和 $V(t)$ 为零均值高斯白噪声，且

$$
\left. \begin{array}{l} E [ \boldsymbol {W} (t) ] = 0, E [ \boldsymbol {W} (t) \boldsymbol {W} ^ {\mathrm{T}} (\tau) ] = \boldsymbol {Q} (t) \delta (t - \tau) \\ E [ \boldsymbol {V} (t) ] = 0, E [ \boldsymbol {V} (t) \boldsymbol {V} ^ {\mathrm{T}} (\tau) ] = \boldsymbol {R} (t) \delta (t - \tau) \end{array} \right\} \tag {8-61}
E [ \boldsymbol {W} (t) \boldsymbol {V} ^ {\mathrm{T}} (\tau) ] = 0 \tag {8-62}
$$

指标函数为

$$
\begin{array}{l} J = E \left\{\boldsymbol {X} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {P} \boldsymbol {X} \left(t _ {\mathrm{f}}\right) + \right. \\ \int_ {t _ {0}} ^ {t _ {1}} \left[ \boldsymbol {X} ^ {\mathrm{T}} (t) \overline {{{\boldsymbol {Q}}}} (t) \boldsymbol {X} (t) + \boldsymbol {U} ^ {\mathrm{T}} (t) \overline {{{\boldsymbol {R}}}} (t) \boldsymbol {U} (t) \right] \mathrm{d} t \Bigg \} \tag {8-63} \\ \end{array}
$$

这里用 Q、R 表示噪声方差阵，为避免混淆将加权阵改为 $\overline{Q}, \overline{R}$ 。

上述问题称为连续系统的线性高斯二次型问题(LQG 问题)。和离散的情况相同,根据分离定理,最优控制系统由两部分组成:一部分是确定性最优控制器;另一部分是与其串联的最优线性滤波器。最优控制可写成

$$\boldsymbol {U} (t) = - \boldsymbol {L} (t) \hat {\boldsymbol {X}} (t) \tag {8-64}$$

反馈增益与确定性最优控制一样(参考第5章式(5-16)),即

$$\boldsymbol {L} (t) = \overline {{{\boldsymbol {R}}}} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) \tag {8-65}$$

$K(t)$ 满足下面的矩阵黎卡提微分方程(参考第5章式(5-14),注意这里 $K(t)$ 不是卡尔曼滤波增益)

$$
\begin{array}{l} \dot {\boldsymbol {K}} (t) = - \boldsymbol {K} (t) \boldsymbol {A} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) + \\ \boldsymbol {K} (t) \boldsymbol {B} (t) \overline {{\boldsymbol {R}}} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) - \overline {{\boldsymbol {Q}}} (t) \tag {8-66} \\ \end{array}
$$

图8-2表示连续随机线性系统最优控制的方块图。

![](image/f1888e18bb1b1f65421b48263a9e68b816c13568b453b16967d303bf2c36416d.jpg)

<details>
<summary>flowchart</summary>
