# 4.5 系统输出被噪声污染时的扩张状态观测器

当系统输出被噪声污染时,要想用扩张状态观测器得到比较好的估计值,需要先滤波处理量测数据,但采用不同的滤波方法会得到不同的估计效果.

设被观测对象为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}, t, w (t)) \\ y = x _ {1} + n (t) \end{array} \right. \tag {4.5.1}
$$

系统输出被一定强度的白噪声 $n(t)$ 所污染.

如果不采用任何滤波处理,那么用这个量测输出所作的扩张

状态观测器方程为

$$
\left\{ \begin{array}{l} e = z _ {1} - y, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} \mathrm{fe}\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {1}\right) \end{array} \right. \tag {4.5.2}
$$

采用最简单的惯性滤波处理量测输出时的扩张状态观测器方程变为

$$
\left\{ \begin{array}{l} y _ {0} = y _ {0} - h \alpha (y _ {0} - y) \\ e = z _ {1} - y _ {0}, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {1} = z _ {1} + h (z _ {2} - \beta_ {0 1} e) \\ z _ {2} = z _ {2} + h (z _ {3} - \beta_ {0 2} \mathrm{fe}) \\ z _ {3} = z _ {3} + h (- \beta_ {0 3} \mathrm{fe} _ {1}) \end{array} \right. \tag {4.5.3}
$$

采用跟踪微分器来进行噪声滤波并用微分信号来进行预测所得到滤波值来建立扩张状态观测器,得

$$
\left\{ \begin{array}{l} \mathrm{fh} = \operatorname{fhan} \left(v _ {1} - y, v _ {2}, r _ {0}, h _ {1}\right) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fh} \\ y _ {0} = v _ {1} + k _ {0} h v _ {2} \\ e = z _ {1} - y _ {0}, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} \mathrm{fe}\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {1}\right) \end{array} \right. \tag {4.5.4}
$$

我们在系统(4.5.1)中取 $(f_{x_{1},x_{2}},t,w(t))=\gamma_{1}\mathrm{sign}(\sin(\omega t))$ ， $n(t)=\gamma_{0}n_{0}$ ，其中 $n_{0}(t)$ 为 $\pm1$ 之间均匀分布的白噪声，然后分别用方程(4.5.2)，方程(4.5.3)，方程(4.5.4)所作的仿真结果如图4.5.1所示。图4.5.1(a)是不作滤波处理的情形，图4.5.1(b)是一阶惯性滤波处理以后的情形，图4.5.1(c)图形显示的是跟踪微分器来进行滤波并加预测处理后所得的观测结果。从图4.5.1中可以看出，用跟踪微分器来进行滤波并加预报处理的效果最好，惯性滤波处理的效果也可以，但信号的相位损失稍大一些。

![](image/82ed5f832f5e401cf80688eb066a7284ffc07311288c113f81ad9457860fd33d.jpg)  
图4.5.1
