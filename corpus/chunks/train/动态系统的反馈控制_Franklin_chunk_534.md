# 8.3.1 图斯蒂法

图斯蒂法是一种数字化方法，其目的是把一个问题作为一种数值积分。假设

$$\frac {U (s)}{E (s)} = D _ {\mathrm{c}} (s) = \frac {1}{s}$$

这是一个积分式，因此有

$$u (k T) = \int_ {0} ^ {k T - T} e (t) \mathrm{d} t + \int_ {k T - T} ^ {k T} e (t) \mathrm{d} t \tag {8.14}$$

上式可改写为

$$u (k T) = u (k T - T) + \text { 在最后一个周期 } T \text { 内 } e (t) \text { 下面的面积 } \tag {8.15}$$

其中：T 为采样周期。

对于图斯蒂法，每一步的任务就是使用梯形积分法，也就是将两个采样点之间的 $e(t)$

用一条直线近似代替(见图8.7)。将 $u(kT)$ 和 $u(kT-T)$ 分别简写为 $u(k)$ 和 $u(k-1)$ ，则可将式(8.15)转化为

$$u (k) = u (k - 1) + \frac {T}{2} [ e (k - 1) + e (k) ] \tag {8.16}$$

或者对上式进行 $z$ 变换，有

$$\frac {U (z)}{E (z)} = \frac {T}{2} \left(\frac {1 + z ^ {- 1}}{1 - z ^ {- 1}}\right) = \frac {1}{\frac {2}{T} (\frac {1 - z ^ {- 1}}{1 + z ^ {- 1}})} \tag {8.17}$$

对 $D_{c}(s)=a/(s+a)$ 应用相同的积分近似法，得

![](image/b58bfdf12ae6a0576fc99f9681aa91dcb7867b4f61433982f153f476466861da.jpg)

<details>
<summary>line</summary>

| t | e(t) |
| --- | --- |
| kT-T | Peak |
| kT | Peak |
</details>

图 8.7 图斯蒂法的梯形积分

$$D _ {\mathrm{d}} (z) = \frac {a}{\frac {2}{T} \left(\frac {1 - z ^ {- 1}}{1 + z ^ {- 1}}\right) + a}$$

事实上就是对每一处 s 做如下替换：

$$s = \frac {2}{T} (\frac {1 - z ^ {- 1}}{1 + z ^ {- 1}})$$

得到一个基于梯形积分公式的 $D_{\mathrm{d}}(z)$ 。这就是图斯蒂法也称作双线性近似法的原因。通过运用图斯蒂法来处理一个简单的传递函数也需要大量的代数运算，而运用Matlab中的c2d函数可快速实现这一过程，下一个例子可说明这个问题。
