# 例 9.1 非线性摆的线性化

考虑例 2.5 中单摆运动的非线性方程。推导系统的平衡点并确定相应的小信号线性模型。

解答。运动方程为

$$\ddot {\theta} + \frac {g}{l} \sin \theta = \frac {T _ {\mathrm{c}}}{m l ^ {2}} \tag {9.4}$$

令 $\left[x_{1}\quad x_{2}\right]^{T}=\left[\theta\quad\dot{\theta}\right]^{T}$ ，可将此运动方程写成状态空间的形式：

$$
\dot {x} = \left[ \begin{array}{l} x _ {2} \\ - \omega_ {0} ^ {2} \sin x _ {1} + u \end{array} \right] = \left[ \begin{array}{l} f _ {1} (x, u) \\ f _ {2} (x, u) \end{array} \right] = f (x, u)
$$

其中： $\omega_{0}=\sqrt{\frac{g}{l}}$ ； $u=\frac{T_{c}}{ml^{2}}$ 。为了确定平衡点状态，假设（标准化的）输入扭矩为标称值 $u_{0}=0$ ，则

$$\dot {x} _ {1} = \dot {\theta} = 0\dot {x} _ {2} = \ddot {\theta} = - \frac {g}{l} \sin \theta = 0$$

642

因此，系统的平衡状态为 $\theta_{0}=0$ 和 $\pi$ （也就是，摆分别处于垂直向下和向上的位置）。平衡状态和输入是 $x_{0}=\left[\theta_{0}\quad0\right]^{T}$ ， $u_{0}=0$ ，状态空间矩阵为

$$
\mathbf {A} = \left[ \begin{array}{l l} \frac {\partial f _ {1}}{\partial x _ {1}} & \frac {\partial f _ {1}}{\partial x _ {2}} \\ \frac {\partial f _ {2}}{\partial x _ {1}} & \frac {\partial f _ {2}}{\partial x _ {2}} \end{array} \right] _ {x _ {0}, u _ {0}} = \left[ \begin{array}{c c} 0 & 1 \\ - \omega_ {0} ^ {2} \cos \theta_ {0} & 0 \end{array} \right]

\boldsymbol {B} = \left[ \begin{array}{l} \frac {\partial f _ {1}}{\partial u} \\ \frac {\partial f _ {2}}{\partial u} \end{array} \right] _ {x _ {0}, u _ {0}} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right]
$$

线性系统在 $\theta_{0}=0$ 和 $\pi$ 的特征根分别为 $\pm j\omega_{0}$ 和 $\pm\omega_{0}$ ，正如所料，后一种情况为不稳定的。
