# 4.2 状态观测器观测误差的讨论

下面在假定参数 b 已知的情况下, 讨论状态观测器

$$
\left\{ \begin{array}{l} e _ {1} = z _ {1} - y \\ \dot {z} _ {1} = z _ {2} - \beta_ {0 1} e _ {1} \\ \dot {z} _ {2} = - \beta_ {0 2} | e _ {1} | ^ {\frac {1}{2}} \text {sign} (e _ {1}) + b u \end{array} \right. \tag {4.2.1}
$$

对系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}) + b u \\ y = x _ {1} \end{array} \right. \tag {4.2.2}
$$

状态的估计误差.

先假定函数 $f(x_{1},x_{2}) = w_{0} = \mathrm{const}$ ，即对象为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = w _ {0} + b u \\ y = x _ {1} \end{array} \right.
$$

对此建立如下状态观测器为

$$
\left\{ \begin{array}{l} e = z _ {1} - x _ {1} \\ \dot {z} _ {1} = z _ {2} - \beta_ {0 1} e \\ \dot {z} _ {2} = - \beta_ {0 2} \mathrm{fal} \left(e, \frac {1}{2}, \delta\right) + b u \end{array} \right.
$$

那么这两个系统的误差系统为

$$
\left\{ \begin{array}{l} e _ {1} = z _ {1} - x _ {1}, e _ {2} = z _ {2} - x _ {2} \\ \dot {e} _ {1} = e _ {2} - \beta_ {0 1} e _ {1} \\ \dot {e} _ {2} = w _ {0} - \beta_ {0 2} \mathrm{fal} \left(e _ {1}, \frac {1}{2}, \delta\right) \end{array} \right.
$$

这个误差系统进入稳态时,有

$$w _ {0} - \beta_ {0 2} \operatorname{fal} \left(e _ {1}, \frac {1}{2}, \delta\right) = e _ {2} - \beta_ {0 1} e _ {1} = 0$$

由此误差系统的稳态误差为

$$e _ {1} = \left(\frac {w _ {0}}{\beta_ {0 2}}\right) ^ {2}, e _ {2} = \beta_ {0 1} e _ {1} = \beta_ {0 1} \left(\frac {w _ {0}}{\beta_ {0 2}}\right) ^ {2}$$

因此只要 $\beta_{02}$ 足够大于 $w_{0}$ ，这些稳态误差与量 $\left(\frac{w_{0}}{\beta_{02}}\right)^{2}$ ，是同一个数量级，比起线性观测时的稳态误差的量级 $\left(\frac{w_{0}}{\beta_{02}}\right)$ 好得多。因为当 $\beta_{02} \gg w_{0}$ 时，有关系式 $\left(\frac{w_{0}}{\beta_{02}}\right) \gg \left(\frac{w_{0}}{\beta_{02}}\right)^{2}$ 。

当 $f(x_{1},x_{2})$ 为一般的非线性函数时，取如下形式李亚普诺夫函数

$$V \left(e _ {1}, e _ {2}\right) = A \mid e _ {1} \mid^ {\frac {3}{2}} - B e _ {1} e _ {2} + C e _ {2} ^ {2} \tag {4.2.3}$$

这时有
