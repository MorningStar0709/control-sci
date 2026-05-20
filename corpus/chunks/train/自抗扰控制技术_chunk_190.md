# 5.4 自抗扰控制器的仿真研究

用上面给出的自抗扰控制器算法对如下对象进行仿真研究.

对象形式为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f \left(x _ {1}, \dot {x} _ {2}, t\right) + w (t) + b u \\ y = x _ {1} \end{array} \right. \tag {5.4.1}
$$

式中，参数 b 假定已知 b = 1.0.

要采用的 ADRC 具体算法为

$$
\left\{ \begin{array}{l} \mathrm{fh} = \operatorname{fhan} (v _ {1} - v _ {0}, v _ {2}, r _ {0}, h) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h f h \quad \text {安排过渡过程，} \\ e = z _ {1} - y, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {1} = z _ {1} + h (z _ {2} - \beta_ {0 1} e) \\ z _ {2} = z _ {2} + h (z _ {3} - \beta_ {0 2} \mathrm{fe} + u) \\ z _ {3} = z _ {3} + h (- \beta_ {0 3} \mathrm{fe} _ {1}) \text {估计状态和扰动，} \\ e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2} \\ u _ {0} = - \operatorname{fhan} (e _ {1}, c e _ {2}, r, h _ {1}) \quad \text {误差反馈，} \\ u = u _ {0} - z _ {3} \quad \text {扰动补偿，} \end{array} \right.
$$

(5.4.2)

这里涉及两个非线性函数 $\mathrm{fhan}(x_{1},x_{2},r,h)$ 和 $\mathrm{fal}(x,\alpha,d)$ ，其定义已在前面给出.

假定作用于对象(5.4.1)的未知加速度 $f(x_{1},x_{2},t)$ 有如下10种不同形式：

(1) $f(x_{1},x_{2},t)=\gamma_{1}\cos(\omega_{1}t)x_{1}+\gamma_{2}\cos(\omega_{2}t)x_{2}+\omega(t)$   
(2) $f(x_{1},x_{2},t)=\gamma_{1}\cos(\omega_{1}t)\mid x_{1}\mid x_{1}+\gamma_{2}\cos(\omega_{2}t)\mid x_{2}\mid x_{2}+\omega(t)$   
(3) $f(x_{1},x_{2},t)=\gamma_{1}(\cos(\omega_{1}t)\mid x_{1}\mid-1)x_{1}+\gamma_{2}\cos(\omega_{2}t)x_{2}+\omega(t)$   
(4) $f(x_{1},x_{2},t)=\gamma_{1}\cos(\omega_{1}t)x_{1}+\gamma_{2}\cos(\omega_{2}t)(3-x_{1}^{2})x_{2}+\omega(t)$   
(5) $f(x_{1},x_{2},t)=\gamma_{1}\cos(\omega_{1}t)\mathrm{sign}(x_{1})\sqrt{|x_{1}|}+\gamma_{2}\cos(\omega_{2}t)$

$$\operatorname{sign} \left(x _ {2}\right) \sqrt {\left| x _ {2} \right|} + \omega (t)$$

(6) $f(x_{1},x_{2},t)=\gamma_{1}\cos(\omega_{1}t)\mid x_{1}\mid^{0.6}+\gamma_{2}\cos(\omega_{2}t)\mid x_{2}\mid^{0.2}+\omega(t)$   
(7) $f(x_{1},x_{2},t)=\gamma_{1}\mathrm{sign}(x_{1}+\gamma_{2}\mathrm{sign}(x_{2}))+\omega(t)$   
(8) $f(x_{1},x_{2},t)=\gamma_{1}\cos(\omega_{1}t)\frac{1}{1+x_{1}^{2}}+$

$$\gamma_ {2} \cos (\omega_ {2} t) x _ {1} | x _ {2} | + \omega (t)$$

(9) $f(x_{1},x_{2},t)=\gamma_{1}\cos(\omega_{1}t)\frac{1}{(1+|x_{1}|)^{2}}+$

$$\gamma_ {2} \exp \left(\cos \left(\omega_ {2} t\right) \frac {1 + \left| x _ {1} \right|}{1 0}\right) + \omega (t)$$
