# 6.3.2 非线性扩张观测器

将被扩张的系统的状态观测器称为扩张观测器，韩京清所设计的非线性扩张观测器表示为 $^{[3]}$

$$e = z _ {1} - y\dot {z} _ {1} = z _ {2} - \beta_ {1} e \tag {6.5}\dot {z} _ {2} = z _ {3} - \beta_ {2} \operatorname{fal} (e, \alpha_ {1}, \delta) + b u\dot {z} _ {3} = - \beta_ {3} \operatorname{fal} (e, \alpha_ {2}, \delta)$$

式中， $\beta_{i}>0(i=1,2,3)$ ； $\alpha_{1}=0.5$ ； $\alpha_{2}=0.25$ 。饱和函数 $fal(e,\alpha,\delta)$ 的作用为抑制信号抖振，表示为

$$
f a l (e, \alpha , \delta) = \left\{ \begin{array}{l l} \frac {e}{\delta^ {1 - \alpha}}, & | e | \leqslant \delta \\ | e | ^ {\alpha} \operatorname{sgn} (e), & | e | > \delta \end{array} \right. \tag {6.6}
$$

则有 $z_{1}(t)\rightarrow x_{1}(t),\quad z_{2}(t)\rightarrow x_{2}(t),\quad z_{3}(t)\rightarrow x_{3}(t) = f_{1}(x_{1},x_{2}) + (b - b_{0})u(t)$ 。

观测器式（6.5）中，变量 $z_{3}(t)$ 称为被扩张的状态。可见，通过非线性扩张观测器式（6.5），可实现对被控对象式（6.3）的位置、速度和未知部分的观测。在实际控制工程中，可采用本观测器实现无需速度测量的控制，并可实现对未知不确定性和外加干扰的补偿。

由于扩张观测器只用到对象的名义模型信息，而没有用到描述对象的函数 $f(\cdot)$ 信息，因此，该观测器具有很好的工程应用价值。由非线性扩张观测器的表达式中的非线性切换部分可见，当误差较大时，通过对其绝对值进行开方使其切换增益降低，防止产生超调；当误差较小时，通过对其绝对值进行开方使其切换增益增大，加快收敛过程。

![](image/1ffba959f9b32883632eca940ef9c7171e52681af4af66ae04e30578748fdad3.jpg)
