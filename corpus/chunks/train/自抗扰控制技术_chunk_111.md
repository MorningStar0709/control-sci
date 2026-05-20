$$\frac {\partial s}{\partial x _ {1}} = 1,\frac {\partial s}{\partial x _ {2}} = \frac {x _ {2}}{r} \mathrm{sign} (x _ {2}) = \frac {| x _ {2} |}{r},\dot {s} = \left(x _ {2} - \frac {r _ {1}}{r} \mid x _ {2} \mid \left(\operatorname{sign} (s) - \frac {w}{r _ {1}}\right)\right) \tag {3.3.17}$$

于是由于 $s = |s|\mathrm{sign}(s),x_2 = |x_2|\mathrm{sign}(x_2)$

$$s \dot {s} = s \left(x _ {2} - \frac {r _ {1}}{r} \mid x _ {2} \mid (\operatorname{sign} (s) - \frac {w}{r _ {1}})\right) =\mid s \mid \mid x _ {2} \mid \left(\operatorname{sign} (s) \left(\operatorname{sign} \left(x _ {2}\right) + \frac {w}{r}\right) - \frac {r _ {1}}{r}\right)$$

于是有

$$\left(1 + \frac {| w |}{r}\right) > \operatorname{sign} (s) \left(\operatorname{sign} \left(x _ {2}\right) + \frac {w}{r}\right)$$

欲使不等式

$$\frac {r _ {1}}{r} > \operatorname{sign} (s) \left(\operatorname{sign} \left(x _ {2}\right) + \frac {w}{r}\right)$$

成立，只要假定扰动范围满足不等式

$$\mid w \mid \leqslant r _ {2}, r + r _ {2} < r _ {1} \tag {3.3.18}$$

就有

$$s \dot {s} < 0 \tag {3.3.19}$$

这说明,当条件(3.3.18)得到满足时,由曲线(3.3.14)定义的滑动曲线(开关曲线)上的所有点,都满足“到达条件”(3.3.19)(图3.3.3).

![](image/e5e18b2a0d5d3b3be6ea5aadec6cfea03952350655d4fd58117f9a20f125d5c4.jpg)

<details>
<summary>contour</summary>

| x | y |
| --- | --- |
| -2.0 | 2.0 |
| -1.5 | 1.5 |
| -1.0 | 1.0 |
| -0.5 | 0.5 |
| 0.0 | 0.0 |
| 0.5 | -0.5 |
| 1.0 | -1.0 |
| 1.5 | -1.5 |
| 2.0 | -2.0 |
</details>

图3.3.3

进一步,变结构控制系统

$$
\left\{ \begin{array}{l} x _ {1} = x _ {2} \\ \dot {x} _ {2} = - r _ {1} \operatorname{sign} (s) + w \end{array} \right. \mid w \mid \leqslant r _ {2}, \tag {3.3.20}
$$

的第二个方程右段加速度满足如下不等式：

$$- \left(r _ {1} + r _ {2}\right) < | - r _ {1} \operatorname{sign} (s) + w | < - \left(r _ {1} - r _ {2}\right), s > 0\left(r _ {1} - r _ {2}\right) < \left| - r _ {1} \operatorname{sign} (s) + w \right| < \left(r _ {1} + r _ {2}\right), s < 0$$

其绝对值总是大于 $r_{1}-r_{2}>0$ ，而轨线到达滑动曲线之前其加速度不会变号，因此从开关曲线以外的初始点出发的轨线总是以有限时间到达滑动曲线s=0。而在滑动曲线上，轨线的速度方向是按菲利波夫的定义，由滑动线两侧轨线速度方向的凸组合来决定，即

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = \alpha (r _ {1} + w) + (1 - \alpha) (- r _ {1} + w) \end{array} \Rightarrow \left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r _ {1} (1 - 2 \alpha) + w \end{array} \right. \right.
$$

其中， $\alpha$ 是由相切条件
