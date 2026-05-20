$$
\left\{ \begin{array}{l} \mathrm{fh} = \text {fhan} (v _ {1} - v, v _ {2}, r _ {0}, h) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fh} \\ h ^ {*} = \frac {h}{k} \\ e = z _ {1} - y, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h ^ {*}), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h ^ {*}) \\ \text {for} i = 1: k \\ z _ {1} = z _ {1} + h ^ {*} (z _ {2} - \beta_ {0 1} e) \\ z _ {2} = z _ {2} + h ^ {*} (z _ {3} - \beta_ {0 2} \mathrm{fe} + u) \\ z _ {3} = z _ {3} + h ^ {*} (- \beta_ {0 3} \mathrm{fe} _ {1}) \\ \text {end} \\ e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2} \\ u = - \text {fhan} (e _ {1}, c e _ {2}, r, h _ {1}) - z _ {3} \end{array} \right.
$$

(5.5.7)

即在算法(5.5.2)中,估计对象状态和总和扰动的ESO部分,多转 $k(>1)$ 次,以便提高ESO的估计精度.采取这种措施提高自抗扰控制器的控制能力是有一定效果的.

例如，控制器参数为： $\beta_{01}=100,\beta_{02}=200,\beta_{03}=2000,r=1000,c=2,h_{1}=0.05=5h.$ 如果 k=1，即采用标准的自抗扰控制器算法，那么此控制器只能控制 $m\leqslant7$ 的对象，但是取 $k=4\sim12$ 时，能控的对象范围能扩大到 $m\leqslant8$ 了.
