# 例7.14 摆的控制律

假设有一个频率是 $\omega_0$ 的摆，其状态空间描述为

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - \omega_ {0} ^ {2} & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u \tag {7.71}
$$

寻找控制律将系统的两个闭环极点都置为 $-2\omega_{0}$ ，也就是说，希望将自然频率加倍，将阻尼比 $\zeta$ 从0增加到1。

解答。由式(7.70)，我们知道

$$\alpha_ {c} (s) = \left(s + 2 \omega_ {0}\right) ^ {2} \tag {7.72a}= s ^ {2} + 4 \omega_ {0} s + 4 \omega_ {0} ^ {2} \tag {7.72b}$$

式(7.69)告诉我们

$$
\det [ s \mathbf {I} - (\mathbf {A} - \mathbf {B K}) ] = \det \left\{\left[ \begin{array}{l l} s & 0 \\ 0 & s \end{array} \right] - \left(\left[ \begin{array}{c c} 0 & 1 \\ - \omega_ {0} ^ {2} & 0 \end{array} \right] - \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] [ K _ {1} K _ {2} ]\right) \right\}
$$

或者

$$s ^ {2} + K _ {2} s + \omega_ {0} ^ {2} + K _ {1} = 0 \tag {7.73}$$

令式(7.72b)和式(7.73)中 s 的同次幂系数相等，满足如下方程组：

$$K _ {2} = 4 \omega_ {0}\omega_ {0} ^ {2} + K _ {1} = 4 \omega_ {0} ^ {2}$$

因此

$$K _ {1} = 3 \omega_ {0} ^ {2}K _ {2} = 4 \omega_ {0}$$

所以，更简洁的控制律形式为

$$
\pmb {K} = \left[ \begin{array}{l l} K _ {1} & K _ {2} \end{array} \right] = \left[ \begin{array}{l l} 3 \omega_ {0} ^ {2} & 4 \omega_ {0} \end{array} \right]
$$

图 7.13 给出了闭环系统对初始条件 $x_{1}=1.0$ ， $x_{2}=0.0$ 及 $\omega_{0}=1$ 的响应曲线。当系统的两个根都为 s=-2 时，可以得到非常理想的阻尼响应曲线。利用 Matlab 命令 impulse 可以生成该曲线。

当系统的阶数高于 3 时，使用例 7.14 的方法计算增益就会非常繁琐。然而，当状态变量方程具有特殊的 “标准” 形式时，这对于求解增益的计算过程又变得极其简单了。便于控制规律设计的一种标准形是能控标准形，在7.4.1小节曾讨论过。考虑如下的一个三阶系统 $^{①}$ ：

![](image/bc1d3721ca26dac41c3f0c0a5d3a69459c93785379266d03ebfca3e8442c8ddd.jpg)

<details>
<summary>line</summary>

| 时间/s | x₁ | u/4 | x₂ |
| --- | --- | --- | --- |
| 0 | 1.0 | -0.2 | -0.8 |
| 1 | 0.4 | 0.2 | -0.6 |
| 2 | 0.1 | 0.1 | -0.3 |
| 3 | 0.0 | 0.0 | -0.1 |
| 4 | 0.0 | 0.0 | 0.0 |
| 5 | 0.0 | 0.0 | 0.0 |
| 6 | 0.0 | 0.0 | 0.0 |
| 7 | 0.0 | 0.0 | 0.0 |
</details>

图 7.13 带全状态反馈的无阻尼振荡器的脉冲响应 $\omega_{0}=1$

$$\ddot {y} + a _ {1} \ddot {y} + a _ {2} \dot {y} + a _ {3} y = b _ {1} \ddot {u} + b _ {2} \dot {u} + b _ {3} u \tag {7.74}$$

其相应的传递函数为

$$G (s) = \frac {Y (s)}{U (s)} = \frac {b _ {1} s ^ {2} + b _ {2} s + b _ {3}}{s ^ {3} + a _ {1} s ^ {2} + a _ {2} s + a _ {3}} = \frac {b (s)}{a (s)} \tag {7.75}$$

设引入一个辅助变量(称为部分状态) $\xi$ ，它与 $a(s)$ 和 $b(s)$ 的关系如图7.14a所示。从U到 $\xi$ 的传递函数为

$$\frac {\xi (s)}{U (s)} = \frac {1}{a (s)} \tag {7.76}$$

或者

$$\dddot {\xi} + a _ {1} \ddot {\xi} + a _ {2} \dot {\xi} + a _ {3} \xi = u \tag {7.77}$$

将式 $(7.77)$ 重新整理为
