由于函数 $\mathrm{fhan}(x_{1},x_{2},r,h_{1})$ 具有快速并消除颤震的特殊功能，因此用它来进行状态反馈的非线性配置、非线性 PID 和自抗扰控制器中的误差的非线性组合等是很理想的.

总之，在非线性滑动曲线所给出的变结构控制系统中，比直线性滑动线所给出的变结构控制，有很多具有更好动态品质的变结构控制。最速反馈控制系统就是以其开关曲线为滑动曲线的变结构控制系统，是具有比较理想的动态品质的闭环系统。

我们从两个函数 $-rsat(s, \delta)$ 和 $\operatorname{fhan}(x_1, x_2, r, h_1)$ 的等高线图形的比较中可以看出，两个函数取区间 $[-r, r]$ 内部值的区域有很大差异。函数值取线性值的区域的这种差异在数值计算和实际应用中显示出本质上的不同。

为了更有效地把最速反馈函数 $\mathrm{fhan}(x_{1},x_{2},r,h_{1})$ 用于状态反馈中，我们引入阻尼因子 c 来把 $\mathrm{fhan}(x_{1},x_{2},r,h_{1})$ 中的变量 $x_{2}$ 改成 $cx_{2}$ ，得 $\mathrm{fhan}(x_{1},cx_{2},r,h_{1})$ .

把函数(3.3.22)

$$u \left(x _ {1}, x _ {2}\right) = - (r + \Delta r) \operatorname{sign} \left(x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r}\right)$$

可以改写成

$$u \left(x _ {1}, x _ {2}\right) = - (r + \Delta r) \text {sign} \left(x _ {1} + \frac {x _ {2} \sqrt {\frac {r + \Delta r}{r}} \left| x _ {2} \sqrt {\frac {r + \Delta r}{r}} \right|}{2 (r + \Delta r)}\right) \tag {3.3.29}$$

于是令 $r_1 = r + \Delta r, c = \sqrt{\frac{r_1}{r}}$ ，就得

$$u (x _ {1}, x _ {2}) = - r _ {1} \mathrm{sign} \left(x _ {1} + \frac {c x _ {2} | c x _ {2} |}{2 r _ {1}}\right) \tag {3.3.30}$$

对应的离散化形式为 $\mathrm{fhan}(x_{1},cx_{2},r_{1},h_{1})$ :

$$
\left\{ \begin{array}{l} d = r h _ {1} ^ {2}, a _ {0} = h _ {1} c x _ {2}, y = x _ {1} + a _ {0} \\ a _ {1} = \sqrt {d (d + 8 | y |)} \\ a _ {2} = a _ {0} + \operatorname{sign} (y) (a _ {1} - d) / 2 \\ s _ {y} = (\operatorname{sign} (y + d) - \operatorname{sign} (y - d)) / 2 \\ a = (a _ {0} + y - a _ {2}) s _ {y} + a _ {2} \\ s _ {a} = (\operatorname{sign} (a + d) - \operatorname{sign} (a - d)) / 2 \\ \text {fhan} = - r (a / d - \operatorname{sign} (a)) s _ {a} - r \operatorname{sign} (a) \end{array} \right.
$$

为什么参数 c 称作“阻尼因子”呢? 先看看带阻尼项的线性状态反馈 $u(x_{1}, x_{2}) = -x_{1} - cx_{2}$ ，其中 c 为阻尼因子。在这个线性反馈中，控制量取零的状态是直线

$$u \left(x _ {1}, x _ {2}\right) = - x _ {1} - c x _ {2} = 0, x _ {2} = - x _ {1} / c,$$

是以 -1/c 为斜率的，c 越大，直线越接近横轴。在最速状态反馈控制律 $u(x_{1},x_{2})=-r_{1}\mathrm{sign}\left(x_{1}+\frac{cx_{2}\mid cx_{2}\mid}{2r_{1}}\right)$ 中控制量取零的曲线是两个在原点对接的半抛物线组成的曲线

$$x _ {1} + \frac {c x _ {2} | c x _ {2} |}{2 r _ {1}} = 0, x _ {2} = - \frac {\operatorname{sign} (x _ {1})}{c} \sqrt {2 r _ {1} | x _ {1} |}$$

在这里，c 越大，此曲线越贴近横轴。其形状如图 3.3.8 所示。这就是把 c 称作阻尼因子的原因。

![](image/1167707d9d19898cee5915d1856a4cb9cabff2dfabcd269e536f718507233148.jpg)

<details>
<summary>line</summary>

| x | y (c=5) | y (c=1) |
| --- | --- | --- |
| -2 | 2 | - |
| -1 | 1 | 0.5 |
| 0 | 0 | 0 |
| 1 | -1 | -0.5 |
| 2 | -2 | -1.5 |
</details>
