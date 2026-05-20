# 5.1.4 一个跟踪微分器和状态观测器实现的“线性PID”

把上述处理系统输出信号 y 的部分改成状态观测器, 得到计算控制量的如下公式:

$$
\left\{ \begin{array}{l} f _ {0} = - r _ {0} \left(r _ {0} \left(v _ {1} - v\right) + \sqrt {3} v _ {2}\right) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h f _ {0} \\ e = z _ {1} - y \\ \mathrm{fe} = \operatorname{fal} \left(e, \frac {1}{2}, \delta\right) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(- \beta_ {0 2} \mathrm{fe}\right) \\ e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2}, e _ {0} = \int_ {0} ^ {t} e _ {1} (\tau) \mathrm{d} \tau \\ u = \beta_ {0} e _ {0} + \beta_ {1} e _ {1} + \beta_ {2} e _ {2} \end{array} \right. \tag {5.1.14}
$$

用这个公式算出的控制量 u 来控制非线性对象

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {1} ^ {3} + x _ {2} ^ {2} + \operatorname{sign} \left(\sin \left(\frac {1}{2} t\right)\right) + u \\ y = x _ {1} \end{array} \right. \tag {5.1.15}
$$

的仿真结果如图 5.1.7 所示.

![](image/d3b92ea89f59b31543dfb6fc0ca1fdbc1bbd90d4508cbeb1da2d149d64a837f6.jpg)

<details>
<summary>line</summary>

| x | u |
| --- | --- |
| 0 | 0 |
| 2 | -1 |
| 4 | -3 |
| 6 | -4 |
| 8 | -4 |
| 10 | -4 |
| 12 | -4 |
| 14 | -4 |
| 16 | -4 |
| 18 | -4 |
| 20 | -4 |
</details>

图 5.1.7

这里状态观测器中的参数 $\beta_{02}$ 不大到一定程度, 输出的微分信号跟不上, 控制效果不会好.
