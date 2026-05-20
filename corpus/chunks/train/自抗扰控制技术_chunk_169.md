$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}) + b u \\ y = x _ {1} \end{array} \right. \tag {4.7.11}
$$

如何选取步长 h 来积分扩张状态观测器(4.7.4)?

(2) 对给定的对象(4.7.11)，如何确定其“时间尺度” $\rho$ ?  
(3)“时间尺度” $\rho$ 和步长h的关系又是什么?  
（4）相应于“时间尺度” $\rho=1$ 的系统的扩张状态观测器参数 $\beta_{01},\beta_{02},\beta_{03}$ 又是什么？

关于前两个问题, 先考察用欧拉法积分一阶常微分方程 (4.7.11) 时的误差分析.

设有一阶常微分方程

$$\dot {x} = f (x), x (0) = x ^ {0} \tag {4.7.12}$$

其解可表示成

$$x (t) = x ^ {0} + \int_ {0} ^ {t} f (x (\tau)) \mathrm{d} \tau$$

但用欧拉法积分 m 步的值为

$$x (t) = x ^ {0} + h \sum_ {i = 0} ^ {m} f (x (i h))$$

其第 $m$ 步时的误差为

![](image/a4b608d58fee96890c42f44ccc3da39275f9e5cbfda8fae472c835730a35541c.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 0.0000 |
| 0.5 | 0.2500 |
| 1.0 | 0.5000 |
| 1.5 | 0.7500 |
| 2.0 | 0.8500 |
| 2.5 | 0.8000 |
| 3.0 | 0.6500 |
| 3.5 | 0.4500 |
| 4.0 | 0.2500 |
| 4.5 | 0.0500 |
| 5.0 | -0.2500 |
| 5.5 | -0.4500 |
| 6.0 | -0.6500 |
</details>

图4.7.12

$$
\begin{array}{l} \int_ {0} ^ {\infty h} f (t) \mathrm{d} t - h \sum_ {0} ^ {m} f (i h) \approx h \sum_ {0} ^ {m} [ \max _ {\tau \in I _ {i}} f (x (\tau)) - \min _ {\tau \in I _ {i}} f (x (\tau)) ] \leqslant \\ 2 m h \max | f (x (\tau)) | <   e \\ \end{array}
$$

这就是说,以固定步长 h,用欧拉法积分引出的误差要小于给定的误差 e,步长 h 要满足

$$h < \frac {e}{2 m M}, M = \max | f (x (\tau)) |$$

是与 $\max |f(x)|$ 成反比.当 $\pmb{x}$ 为向量时，也有

$\boldsymbol{x}(t)=\boldsymbol{x}^{0}+\int_{0}^{t}f(\boldsymbol{x}(\tau))\mathrm{d}\tau$ 与近似值 $\boldsymbol{x}(t)=\boldsymbol{x}^{0}+h\sum_{i=0}^{m}f(\boldsymbol{x}(ih))$ 它们之间的误差也是

$$
h \left[ \max f (\boldsymbol {x} (\tau)) - \min f (\boldsymbol {x} (\tau)) \right] <   2 m h \max f (\boldsymbol {x} (\tau)) <   \left[ \begin{array}{l} e \\ e \\ \vdots \\ e \end{array} \right]
$$

其中， $\max f=\begin{bmatrix}\max f_{1}\\ \max f_{2}\\\vdots\\ \max f_{n}\end{bmatrix},\min f=\begin{bmatrix}\min f_{1}\\ \min f_{2}\\\vdots\\ \min f_{n}\end{bmatrix},$

令

$$M = \max \left\{\max \left| f _ {1} \right|, \max \left| f _ {2} \right|, \dots , \max \left| f _ {n} \right| \right\},$$

那么 $2mhM < e, h < \frac{e}{2mM}$

在这里，量

$$\rho = \frac {1}{M} \tag {4.7.13}$$

决定着表示系统快慢的一种尺度,所以我们用它来定义一阶系统(4.7.12)的“时间尺度”是合适的.数值积分这个方程所需的积分步长h是与时间尺度 $\rho$ 成正比

$$h = k \rho \tag {4.7.14}$$

对二阶系统的初值问题

$$
\left\{ \begin{array}{l l} \dot {x} _ {1} = x _ {2}, & x _ {1} (0) = x _ {1} ^ {0} \\ \dot {x} _ {2} = f (t), & x _ {2} (0) = x _ {2} ^ {0} \end{array} \right. \tag {4.7.15}
$$
