| X | Y |
| --- | --- |
| 6 | 0.05 |
| 7 | -0.05 |
</details>

图2.4.2

![](image/aee4216d7954a5c6715e9eb8d67f45b50f38ebc79210912ce42ec8df263c977e.jpg)

<details>
<summary>line</summary>

| x | f | r (real(α,d)) |
| --- | --- | --- |
| 7 | 0.5 | -10 |
| 8 | 0.6 | -8 |
| 9 | 0.7 | -6 |
| 10 | 0.8 | -4 |
| 11 | 0.9 | -2 |
| 12 | 1.0 | 0 |
| 13 | 1.1 | 2 |
| 14 | 1.2 | 4 |
| 15 | 1.3 | 6 |
| 16 | 1.4 | 8 |
| 17 | 1.5 | 10 |
| 18 | 1.6 | 12 |
| 19 | 1.7 | 14 |
| 20 | 1.8 | 16 |
</details>

图2.4.3

产生这些高频振荡的根本原因,无论是系统(2.4.1)还是系统(2.4.2),都是不能以有限步到达设定值并停在那里.因为,尽管 $-r\mathrm{sign}\left(x_{1}+\frac{x_{2}\mid x_{2}\mid}{2r}\right)$ 是连续系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = u, | u | \leqslant r \end{array} \right. \tag {2.4.3}
$$

从非零初值到达原点的最速控制综合函数,但是它和线性饱和函数 $-rsat\left(x_{1}+\frac{x_{2}\mid x_{2}\mid}{2r},d\right)$ 都不是离散系统

$$
\left\{ \begin{array}{l} x _ {1} (k + 1) = x _ {1} (k) + h x _ {2} (k) \\ x _ {2} (k + 1) = x _ {2} (k) + h u, \quad | u | \leqslant r \end{array} \right. \tag {2.4.4}
$$

的最速控制综合函数．方程(2.4.3)的数值计算是用这种离散递推公式来进行的.

我们把离散系统（2.4.4）的最速控制综合函数记做 $\mathrm{fhan}(x_{1},x_{2},r,h)$ ，其算法公式如下：

$$
u = \operatorname{fhan} \left(x _ {1}, x _ {2}, r, h\right):
\left\{ \begin{array}{l} d = r h \\ d _ {0} = h d \\ y = x _ {1} + h x _ {2} \\ a _ {0} = \sqrt {d ^ {2} + 8 r | y |} \\ a = \left\{ \begin{array}{l l} x _ {2} + \frac {(a _ {0} - d)}{2} \operatorname{sign} (y), & | y | > d _ {0} \\ x _ {2} + \frac {y}{h}, & | y | \leqslant d _ {0} \end{array} \right. \\ \text { fhan } = - \left\{ \begin{array}{l l} r \operatorname{sign} (a), & | a | > d \\ r \frac {a}{d}, & | a | \leqslant d \end{array} \right. \end{array} \right. \tag {2.4.5}
$$

这里有两个条件语句： $|y| < d_0, |y| \geqslant d_0$ 和 $|a| \leqslant d, |a| > d.$ 利用符号函数的特性去掉这两个条件语句和适当的参数归化可推出如下等价的公式：

记

$$\operatorname{fsg} (x, d) = (\operatorname{sign} (x + d) - \operatorname{sign} (x - d)) / 2$$

那么 $u = \mathrm{fhan}(x_1, x_2, r, h)$ 表示成

$$
\left\{ \begin{array}{l} d = r h ^ {2} \\ a _ {0} = h x _ {2} \\ y = x _ {1} + a _ {0} \\ a _ {1} = \sqrt {d (d + 8 | y |)} \\ a _ {2} = a _ {0} + \operatorname{sign} (y) \left(a _ {1} - d\right) / 2 \\ a = \left(a _ {0} + y\right) \mathrm{fsg} (y, d) + a _ {2} \left(1 - \mathrm{fsg} (y, d)\right) \\ \text {fhan} = - r \left(\frac {a}{d}\right) \mathrm{fsg} (a, d) - r \operatorname{sign} (a) \left(1 - \mathrm{fsg} (a, d)\right) \end{array} \right. \tag {2.4.6}
$$

这个计算公式的具体推导放在本书2.7小节中.

图2.4.4为函数 $x_{3} = \mathrm{fhan}(x_{1},x_{2},r,h_{1})$ ，当 $r = 1,h_1 = 0.3$ 时的曲面图(a）和等高线图(b).
