# 4.5 线性定常系统的稳定自由运动的衰减性能的估计

对于线性定常系统，利用李亚普诺夫判据不但可判断其原点平衡状态是否为渐近稳定，而且还可对稳定的自由运动即 $\phi(t; x_{0}, t_{0})$ 趋向原点平衡状态的收敛快慢作出估计。由于这种估计可以在不必求出自由运动的解 $\phi(t; x_{0}, t_{0})$ 的情况下来作出，所以为估计稳定自由运动的衰减性能提供了一种间接的方法。

衰减系数 考察线性定常自治系统

$$\dot {x} = A x, \quad x (0) = x _ {0}, t \geqslant 0 \tag {4.80}$$

设原点 x = 0 为唯一的平衡状态，且为渐近稳定。则据此可知，系统的零输入响应也即由任一初始状态 $x_0$ 出发的自由运动轨线 $\phi(t; x_0, 0)$ ，将随着时间 $t$ 的增加而趋于原点 $x = 0$ 。从物理的直观上容易理解，伴随着运动的收敛趋向于 $x = 0$ ，其相应的能量也随之衰减到零。而且，若初始能量愈小且能量衰减的速率愈大，则运动收敛趋向于原点平衡状态就愈快；反之，则运动收敛得就愈慢。正如前几节中所指出过的，在系统的渐近稳定性判别中所引入的李亚普诺夫函数 $V(x)$ 就是一种“能量”，而 $\dot{V}(x)$ 则为“能量”随时间变化的速率。当系统为渐近稳定时， $V(x)$ 为正定，而 $\dot{V}(x)$ 为负定，因此可引入如下定义的一个正实数

$$\eta = - \frac {\dot {V} (\boldsymbol {x})}{V (\boldsymbol {x})} \tag {4.81}$$

来表征系统自由运动的衰减性能，并将其称为衰减系数。显然， $V(x)$ 愈小且 $\dot{V}(x)$ 的绝对值愈大则 $\eta$ 愈大，从而自由运动衰减得愈快；反之，则 $\eta$ 愈小，相应地自由运动衰减得愈慢。

进一步,对式(4.81)由 t=0 到 t 进行积分,可得到:

$$
\begin{array}{l} - \int_ {0} ^ {t} \eta d t = \int_ {0} ^ {t} \frac {\dot {V} (\boldsymbol {x})}{V (\boldsymbol {x})} d t = \int_ {s _ {0}} ^ {x} \frac {1}{V (\boldsymbol {x})} d V (\boldsymbol {x}) \\ = \ln V (\boldsymbol {x}) - \ln V \left(\boldsymbol {x} _ {0}\right) = \ln \frac {V (\boldsymbol {x})}{V \left(\boldsymbol {x} _ {0}\right)}. \tag {4.82} \\ \end{array}
$$

于是，由此就可导出

$$V (\boldsymbol {x}) = V \left(\boldsymbol {x} _ {0}\right) e ^ {- \int_ {0} ^ {t} \eta d t} \tag {4.83}$$

一般地说,直接由(4.83)是难以进行估计的。为此,取

$$\eta_ {\min} = \min _ {s} \left[ - \frac {\dot {V} (\boldsymbol {x})}{V (\boldsymbol {x})} \right] = \text {常数} \tag {4.84}$$

并将其代入(4.83)，可以进而得到：

$$V (\boldsymbol {x}) \leqslant V \left(\boldsymbol {x} _ {0}\right) e ^ {- \int_ {0} ^ {t} \eta_ {\min} d t} = V \left(\boldsymbol {x} _ {0}\right) e ^ {- \eta_ {\min} t} \tag {4.85}$$

这表明，一旦确定出 $\eta_{\min}$ ，则就可定出 $V(x)$ 随时间 $t$ 的衰减上界。而且，对于线性定常系统， $V(x)$ 是 $x$ 的一个二次型函数，因此也可由此定出自由运动 $\phi(t; x_0, 0)$ 随时间 $t$ 的衰减上界。

计算 $\eta_{\mathrm{min}}$ 的关系式 对于线性定常系统(4.80)，当系统为渐定稳定时，对任意给定的正定对称阵 $Q$ ，李亚普诺夫方程

$$A ^ {T} P + P A = - Q \tag {4.86}$$

的解阵 $P$ 存在唯一且为正定。并且， $V(x) = x^T P x$ 为正定， $\dot{V}(x) = -x^T Q x$ 为负定。同时，把 $\eta_{\min}$ 规范化地规定为

$$
\begin{array}{l} \eta_ {\min} = \min _ {x} \left[ - \frac {\dot {V} (x)}{V (x)} \right] = \min _ {x} \left[ \frac {x ^ {T} Q x}{x ^ {T} P x} \right] \\ = \min _ {\boldsymbol {x}} \left\{\boldsymbol {x} ^ {T} Q \boldsymbol {x}, \boldsymbol {x} ^ {T} P \boldsymbol {x} = 1 \right\} \tag {4.87} \\ \end{array}
$$
