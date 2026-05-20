# 2.6.3 求函数极值

一个输入 - 输出关系是由如下函数关系描述.

$$y = f (x) \tag {2.6.10}$$

式中：x 为输入量；y 为输出量．而且函数 $f(x)$ 的形式是未知的.

求极值点的典型的递推算法为

$$x _ {k + 1} = x _ {k} - \lambda \frac {\mathrm{d} y}{\mathrm{d} x} \Big | _ {x = x _ {k}}, \lambda > 0 \tag {2.6.11}$$

如果点 $x_{k}$ 上函数 $f(x)$ 的导数 $\frac{\mathrm{d}f}{\mathrm{d}x} > 0$ ，那么下一步 $x$ 值 $x_{k+1}$ 大于现在的 $x$ 值 $x_{k}$ ，反之，下一步 $x$ 值 $x_{k+1}$ 小于现在的 $x$ 值 $x_{k}$ ，这样 $x$ 逐渐接近使函数 $f(x)$ 取极小值的 $x^{*}$ .

在这里,我们不知道函数 $y=f(x)$ 的表达式,只能实时获取输入-输出量 $x(t),y(t)$ 无法直接获取导数 $\frac{\mathrm{dy}}{\mathrm{dx}}$ 的信息，从而不能直接利用迭代公式(2.6.11).但是，如果把 $\frac{\mathrm{dy}}{\mathrm{dx}}$ 改写成

$$\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {\frac {\mathrm{d} y}{\mathrm{d} t}}{\frac {\mathrm{d} x}{\mathrm{d} t}} = \frac {\dot {y}}{\dot {x}} \tag {2.6.12}$$

那么我们就可以利用跟踪微分器来分别处理出 $\dot{x}$ 和 $\dot{y}$ ，不用函数表达式 $y = f(x)$ 也能确定出 $\frac{\mathrm{dy}}{\mathrm{dx}}$ ，从而可以用迭代公式(2.6.11)来求极值点了。

用公式(2.6.12)和迭代公式(2.6.11)求极值的具体算法如下：

记 h 为采样步长, $x(k) = x(kh)$ , $y(k) = y(kh)$

输入数据

$$x (t), t = h, 2 h, 3 h, \dots$$

来获取输出数据

$$y (t), t = h, 2 h, 3 h, \dots$$

把 $x(k)$ 送入跟踪微分器 TD1

$$
\left\{ \begin{array}{l} x _ {1} (k + 1) = x _ {1} (k) + h x _ {2} (k) \\ x _ {2} (k + 1) = x _ {2} (k) + h \text {fhan} (x _ {1} (k) - x (k), x _ {2} (k), r, h) \end{array} \right.
$$

跟踪 $x(k)$ 的信号 $x_{1}(k)$ 及其微分信号 $x_{2}(k)$ .

把 $y(k)$ 送入跟踪微分器 TD2

$$
\left\{ \begin{array}{l} y _ {1} (k + 1) = y _ {1} (k) + h y _ {2} (k) \\ y _ {2} (k + 1) = y _ {2} (k) + h \text {fhan} \left(y _ {1} (k) - y (k), y _ {2} (k), r, h\right) \end{array} \right.
$$

跟踪 $y(k)$ 的信号 $y_{1}(k)$ 及其微分信号 $y_{2}(k)$ .

当 $x_{2}(k)\neq 0$ 时，有

$$\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {\dot {y}}{\dot {x}} \approx \frac {y _ {2} (k)}{x _ {2} (k)}$$

于是式 $(2.6.12)$ 变成

$$x (k + 1) = x (k) - \lambda \frac {y _ {2} (k)}{x _ {2} (k)} \tag {2.6.13}$$

例 设 $y = 1 + |x|^n$ ，显然其极小点 $x^* = 0$ ，而极小值 $y^* = 1$ 。上述算法中的各参数取如下：步长 $h = 0.01$ ；TD 的速度因子 $r = 1000$ ；迭代修正因子 $\lambda = 0.002$ ；初值 $x(0) = 1$ 。图 2.6.7 显示的是函数 $y$ 中的幂次分别取 0.5, 1.0, 2.0, 3.0 时的寻优结果。这些结果表明，尽管函数性质差异较大（前两种情形，在极值点函数不可微），但用同一种算法，同一组参数，所给出的寻优结果是相当满意的。

![](image/e8db3796ab6a6a77ea3c9c9fdff38ac21f20571eda6820d91d27e8952c859021.jpg)

<details>
<summary>line</summary>

| X-Axis | y | x |
| --- | --- | --- |
| 0 | 1.5 | 0 |
| 20 | 1.5 | 0 |
| 40 | 1.5 | 0 |
| 60 | 1.5 | 0 |
| 80 | 1.5 | 0 |
</details>

图2.6.7
