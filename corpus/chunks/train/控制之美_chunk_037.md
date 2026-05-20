# 2.2.1 拉普拉斯变换的定义

以图 2.2.1(a) 所示的电路系统为例, 电流的动态微分方程为

$$e (t) = L \frac {\mathrm{d} i (t)}{\mathrm{d} t} + R i (t) \tag {2.2.1}$$

其中， $e(t)$ 表示电压， $i(t)$ 表示电流，L 表示电感，R 表示电阻。

![](image/69388b967f4d6ddbc91b52d0c3cd8ba0f11b6cc18c09c82352e541b160c765d8.jpg)

<details>
<summary>text_image</summary>

e(t)
+
-
L
eL(t)
-
i(t)
R
eR(t)
+
</details>

(a) 电感电阻网络图

![](image/602f4f9c225e75c0ba76eac7b2026123ef80fadbaf877ddcf8e53009b7881e51.jpg)  
(b) 系统框图  
图 2.2.1 电感电阻系统

定义此动态系统的输入为电压 $u(t) = e(t)$ ，输出为电流 $x(t) = i(t)$ ，则式(2.2.1)可以写成

$$u (t) = L \frac {\mathrm{d} x (t)}{\mathrm{d} t} + R x (t) \tag {2.2.2}$$

式(2.2.2)可以用图 2.2.1(b)所示的框图描述。其中,在系统的输入与输出中间有一个转化过程,设为 $g(t)$ 。 $g(t)$ 就是系统的单位冲激响应 $h(t)(g(t)=h(t))$ 。系统的输入 $u(t)$ 、

输出 $x(t)$ 与 $g(t)$ 之间是卷积运算的关系, 即

$$x (t) = u (t) * g (t) = \int_ {0} ^ {t} u (\tau) g (t - \tau) \mathrm{d} \tau \tag {2.2.3}$$

若要分析系统的输出 $x(t)$ , 就需要分析卷积 $u(t) * g(t)$ , 或者求解微分方程。观察式(2.2.2)和式(2.2.3), 直接求解它们的过程会非常复杂, 尤其是处理复杂系统的时候。正是因为如此, 在经典控制理论当中, 一个强大的数学工具被引入进行辅助分析, 这个数学工具就是拉普拉斯变换。通过拉普拉斯变换, 系统的微分方程将转化为代数方程, 卷积运算则会变为乘法运算。现在, 让我们暂时抛开上面的例子, 先来讨论拉普拉斯变换的定义, 等到 2.3 节再重新分析此例。

对一个函数 $f(t)$ 做拉普拉斯变换, 可以将其从时域 $(t)$ 转换到复数域 $(s)$ , 它的定义为

$$\mathcal {L} [ f (t) ] = F (s) = \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t \tag {2.2.4}$$

其中， $s=\sigma+j\omega$ ，是一个复数。

式(2.2.4)中积分下限从0开始。从控制工程的角度来讲,不需要去研究时间0点以前的事情,而是把这部分留给哲学家。考虑一个特例,当 $\sigma=0$ 的时候,拉普拉斯变换变成了 $F(s)=F(j\omega)=\int_{0}^{\infty}f(t)e^{-j\omega t}dt$ 。这是函数 $f(t)$ 的傅里叶变换。因此,傅里叶变换是拉普拉斯变换的一种特殊情况。关于傅里叶级数和傅里叶变换的推导,读者可以参考附录B。

下面请看几个拉普拉斯变换的例子。

例 2.2.1 $L[e^{-at}]=\frac{1}{s+a}$ 。

证：

$$
\begin{array}{l} \mathcal {L} \left[ e ^ {- a t} \right] = \int_ {0} ^ {\infty} e ^ {- a t} e ^ {- s t} d t = \int_ {0} ^ {\infty} e ^ {- (a + s) t} d t \\ = - \frac {1}{s + a} \mathrm{e} ^ {- (a + s) t} \left| _ {0} ^ {\infty} \right. \\ = - \frac {1}{s + a} \lim _ {t \rightarrow \infty} \left(\mathrm{e} ^ {- (a + s) t}\right) - \left(- \frac {1}{s + a} \mathrm{e} ^ {0}\right) \\ = \frac {1}{s + a} \tag {2.2.5} \\ \end{array}
$$

例 2.2.2 $\mathcal{L}[af(t)+bg(t)]=aF(s)+bG(s)$ ，其中，a、b 为常数。

证：略，可用积分基本规则证明。这是拉普拉斯变换的线性叠加性质，说明拉普拉斯变换是线性变换。

例 2.2.3 $\mathcal{L}[\sin at]=\frac{a}{s^{2}+a^{2}}$ 。

证：根据欧拉公式

$$\mathrm{e} ^ {\mathrm{j} a t} = \cos a t + \mathrm{j} \sin a t \tag {2.2.6a}\mathrm{e} ^ {- \mathrm{j} a t} = \cos a t - \mathrm{j} \sin a t \tag {2.2.6b}$$

式(2.2.6a)减式(2.2.6b)，得到
