导弹的横向加速度 $a_{M}$ 为一控制量。一般将控制信号加给舵机，舵面偏转后产生弹体攻角 $\alpha$ ，而后产生横向加速度 $a_{M}$ 。如果忽略舵机和弹体的惯性，而且假设控制量的单位与加速度单位相同，则可用控制量 u 来表示 $-a_{M}$ ，也就是令

$$\boldsymbol {u} = - \boldsymbol {a} _ {M} \tag {12-8}$$

所以式(12-7)为

$$\dot {\boldsymbol {x}} _ {2} = \boldsymbol {a} _ {T} + \boldsymbol {u} \tag {12-9}$$

这样可得导弹运动状态方程为

$$\dot {\boldsymbol {x}} _ {1} = \boldsymbol {x} _ {2} \tag {12-10}\dot {\boldsymbol {x}} _ {2} = \boldsymbol {u} + \boldsymbol {a} _ {T} \tag {12-11}$$

可写成矩阵的形式：

$$\dot {\boldsymbol {X}} = \boldsymbol {A} \boldsymbol {X} + \boldsymbol {B} \boldsymbol {u} + \boldsymbol {D} \boldsymbol {a} _ {T} \tag {12-12}$$

式中，

$$
\boldsymbol {X} = \left[ \begin{array}{l} \boldsymbol {x} _ {1} \\ \boldsymbol {x} _ {2} \end{array} \right], \boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], \boldsymbol {B} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right], \boldsymbol {D} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \tag {12-13}
$$

如果不考虑目标的机动, 即 $a_{T}=0$ , 则在这种情况下, 式 (12-12) 变成

$$\dot {\boldsymbol {X}} = \boldsymbol {A} \boldsymbol {X} + \boldsymbol {B} \boldsymbol {u} \tag {12-14}$$

下面来考虑式(12-4)，该式可写成

$$\dot {\boldsymbol {y}} = - \left(\boldsymbol {V} _ {M} - \boldsymbol {V} _ {T}\right) \tag {12-15}$$

其中， $V_{M}-V_{T}=V_{C}$ 表示导弹相对目标的接近速度。由于 q, $\theta$ 和 $\theta_{T}$ 的值都比较小，y 可近似表示导弹与目标之间的距离。设 $t_{f}$ 为导弹与目标的遭遇时刻（即导弹与目标相碰撞或两者之间的距离为最短的时刻），则在某一瞬时 t，导弹与目标的距离 y 可近似用下式表示：

$$\mathbf {y} (t) = \left(\mathbf {V} _ {M} - \mathbf {V} _ {T}\right) \left(t _ {\mathrm{f}} - t\right) = \mathbf {V} _ {C} \left(t _ {\mathrm{f}} - t\right) \tag {12-16}$$

又考虑到对于导弹制导来说,最基本的要求是脱靶量越小越好,因此,应该选择最优控制量 u,使得下面的指标函数为最小。

$$J = \left[ \boldsymbol {x} _ {T} \left(t _ {\mathrm{f}}\right) - \boldsymbol {x} _ {M} \left(t _ {\mathrm{f}}\right) \right] ^ {2} + \left[ \boldsymbol {y} _ {T} \left(t _ {\mathrm{f}}\right) - \boldsymbol {y} _ {M} \left(t _ {\mathrm{f}}\right) \right] ^ {2} \tag {12-17}$$

然而，当要求一个反馈形式的控制时，按上式列出的问题很难求解。所以以 $t = t_{\mathrm{f}}$ 时刻，即 $\pmb {y}(t_{\mathrm{f}}) = \pmb{V}_{C}(t_{\mathrm{f}} - t_{\mathrm{f}}) = \mathbf{0}$ 时的 $\pmb{x}_1(t_{\mathrm{f}})$ 值作为脱靶量，要求 $\pmb{x}_1(t_{\mathrm{f}})$ 值越小越好。另外，由于舵偏角受到限制，导弹结构能够承受的最大载荷也受到限制，所以控制信号 $\pmb{u}$ 也应该受到限制。因此，选择以下形式的二次型指标函数：
