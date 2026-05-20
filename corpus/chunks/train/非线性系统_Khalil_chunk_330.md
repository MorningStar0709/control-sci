边界层问题 $\frac{dy}{d\tau} = -y, y(0) = \eta_0 + \xi_0$

有唯一解 $\hat{y} (\tau) = (\eta_0 + \xi_0)\exp (-\tau)$

根据定理11.1,对于所有 $t\in[0,1]$ ,有

$$x - [ t - 1 + (1 + \xi_ {0}) \exp (- t) ] = O (\varepsilon)z - \left[ (\eta_ {0} + \xi_ {0}) \exp \left(\frac {- t}{\varepsilon}\right) + 1 - (1 + \xi_ {0}) \exp (- t) \right] = O (\varepsilon)$$

z 的 $O(\varepsilon)$ 逼近清楚地表现出二时间尺度特性。它以快瞬态 $(\eta_{0} + \xi_{0})\exp(-t/\varepsilon)$ 开始，称为解的边界层部分。在这个瞬态衰减后，z 继续接近 $[1 - (1 + \xi_{0})\exp(-t)]$ ，这是解的慢变（准稳态）部分。二时间尺度特性只对 z 有意义，而 x 主要是慢特性。事实上，x 有一个快（边界层）瞬态，但它是 $O(\varepsilon)$ 。由于系统是线性的，可以通过模态分析（modal analysis）使它具有描述其二时间尺度特征。很容易看出，系统有一个慢特征值 $\lambda_{1}$ ，它接近于降阶模型特征值的 $O(\varepsilon)$ ，即 $\lambda_{1} = -1 + O(\varepsilon)$ ；系统还有一个快特征值 $\lambda_{2} = \lambda/\varepsilon$ ，其中 $\lambda$ 是接近于边界层模型特征值的 $O(\varepsilon)$ ，即 $\lambda_{2} = [-1 + O(\varepsilon)]/\varepsilon$ 。x 和 z 的精确解是慢模式 $\exp(\lambda_{1}t)$ 、快模式 $\exp(\lambda t/\varepsilon)$ 以及由于输入 $u(t) = t$ 引起的稳态分量的线性组合。通过模态分解的实际计算，可以验证在 x 上快模式的系数是 $O(\varepsilon)$ 。一般来讲，这对线性系统是可行的（见习题 11.14）。
