# 7.3.1 终值定理

根据式(7.2.6)计算得出系统输出的终值,根据式(7.2.7)得到了稳态误差。请读者重新审视从式(7.2.3)到式(7.2.7)的推导过程,它用到了分式分解法和拉普拉斯逆变换,整个过程比较复杂,尤其是针对高阶的系统,计算量会非常大。为了快速得到系统的稳态值,本节将引入终值定理(Final Value Theorem,FVT)。这一定理将时间趋于无穷时的时域表达与复数域之间联系起来。它的定义如下:如果 $\lim x(t)$ 存在,且 $X(s)=\mathcal{L}[x(t)]$ ,那么

$$\lim _ {t \to \infty} x (t) = \lim _ {s \to 0} s X (s) \tag {7.3.1}$$

请读者注意使用终值定理的前提条件,那就是要求 $\lim_{t\to\infty}x(t)$ 存在。从控制系统的角度来看,即要求 $x(t)$ 最终稳定在一个值上。

对式 $(7.2.3)$ 使用终值定理,可以得到系统输出的终值,即

$$
\begin{array}{l} \lim _ {t \rightarrow \infty} x (t) = \lim _ {s \rightarrow 0} X (s) = \lim _ {s \rightarrow 0} \frac {K _ {\mathrm{P}} r - \alpha C + 7 0 0 0 x _ {0} s}{s (7 0 0 0 s + 1 0 \alpha + K _ {\mathrm{P}})} \\ = \lim _ {s \rightarrow 0} \frac {K _ {\mathrm{P}} r - \alpha C + 7 0 0 0 x _ {0} s}{7 0 0 0 s + 1 0 \alpha + K _ {\mathrm{P}}} = \frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha} \tag {7.3.2} \\ \end{array}
$$

式(7.3.2)的结果和式(7.2.6)的结果一致,但求解过程要方便很多。更重要的是,这个定理不仅简化了求解的中间步骤,也为我们设计控制器消除稳态误差提供了思路。
