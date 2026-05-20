| x | x1 | x2 | f^sign(sim(0.5)); w=3cos(0.5) |
| --- | --- | --- | --- |
| 0 | 4 | 4 | -1 |
| 4 | 6 | 6 | -1 |
| 8 | 8 | 8 | -1 |
| 12 | 10 | 10 | -1 |
| 16 | 12 | 12 | -1 |
| 20 | 14 | 14 | -1 |
The chart displays three curves: x1, x2, and f^sign(sim(0.5)), all under the condition h=0.01, βm=100, βm=300, βm=1000. The y-axis ranges from -2 to 100. The x-axis is labeled with integer values of 4, 6, 8, 10, 12, 14, 16, 18, and 20. The y-axis is labeled as 'x', and the x-axis is labeled as 'β'. The function values are estimated based on the given formula.
</details>

图4.3.2

在进行数值仿真时,为了避免高频颤振现象的出现,我们把函数 $|e|^{\alpha}\text{sign}(e)$ 改造成原点附近具有线性段的连续的幂次函数

$$
\operatorname{fal} (e, \alpha , \delta) = \left\{ \begin{array}{l l} \frac {e}{\delta^ {\alpha - 1}}, & | e | \leqslant \delta \\ | e | ^ {\alpha} \operatorname{sign} (e), & | e | > \delta \end{array} \right.
$$

式中： $\delta$ 为线性段的区间长度，如图4.3.3所示。利用符号函数，函数 $\operatorname{fal}(e, \alpha, \delta)$ 也可以写成

$$s = \frac {\operatorname{sign} (e + \delta) - \operatorname{sign} (e - \delta)}{2};\operatorname{fal} (e, \alpha , \delta) = \frac {e}{\delta^ {1 - \alpha}} s + | e | ^ {\alpha} \operatorname{sign} (e) (1 - s)$$

式中： $2\delta$ 为 $\operatorname{fal}(e,\alpha ,\delta)$ 函数中线性段区间长度.

在上面例子中我们是在参数 $b = 3$ 和信号 $u = \cos \left(\frac{t}{2}\right)$ 为已知的假定下所作的仿真结果. 如果参数 $b = 3$ 和信号 $u = \cos \left(\frac{t}{2}\right)$ 未知, 那么在扩张状态观测器中不能用这个参数和信号, 扩张状态观测器只能建成

$$
\left\{ \begin{array}{l} e = z _ {1} - y, \mathrm{fe} = \operatorname{fal} \left(e, \frac {1}{2}, \delta\right), \mathrm{fe} _ {1} = \operatorname{fal} \left(e, \frac {1}{4}, \delta\right) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} \mathrm{fe}\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {1}\right) \end{array} \right. \tag {4.3.18}
$$

![](image/851860c67f64195daac75762d1e79e63dacf77feba0060830f3e881e632c028d.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -2.0 | -1.5 |
| -1.5 | -1.0 |
| -1.0 | -0.5 |
| -0.5 | 0.0 |
| 0.0 | 0.5 |
| 0.5 | 1.0 |
| 1.0 | 1.5 |
| 1.5 | 1.8 |
| 2.0 | 2.0 |
</details>

图4.3.3

用这个扩张状态观测器不仅很好地跟踪系统状态 $x_{1}, x_{2}$ ，还很好地跟踪系统中的未知函数 $\operatorname{asign}(\sin(\omega t)) + 3\cos\left(\frac{t}{2}\right)$ . 跟踪系统 (4.3.13) 的仿真结果如图 4.3.4 所示.

如果系统(4.3.2)的函数 $f(x_{1},x_{2})$ 可分解为

![](image/74f29208ea37da025b525dd69c627631813b848afaab367bfc0196c1a5d14da5.jpg)

<details>
<summary>line</summary>
