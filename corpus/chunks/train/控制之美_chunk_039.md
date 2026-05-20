$$
\begin{array}{l} t = u + \tau \\ \Rightarrow \mathrm{d} t = \mathrm{d} u + \mathrm{d} \tau = \mathrm{d} u \\ \Rightarrow \int_ {\tau} ^ {\infty} f (\tau) g (t - \tau) \mathrm{e} ^ {- s t} \mathrm{d} t = \int_ {0} ^ {\infty} f (\tau) g (u) \mathrm{e} ^ {- s (u + \tau)} \mathrm{d} u \tag {2.2.11} \\ \end{array}
$$

将式 $(2.2.11)$ 代入式 $(2.2.10b)$ ，得到

$$\int_ {0} ^ {\infty} \int_ {\tau} ^ {\infty} f (\tau) g (t - \tau) \mathrm{e} ^ {- s t} \mathrm{d} t \mathrm{d} \tau = \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} f (\tau) g (u) \mathrm{e} ^ {- s (u + \tau)} \mathrm{d} u \mathrm{d} \tau= \int_ {0} ^ {\infty} f (\tau) \mathrm{e} ^ {- s \tau} \mathrm{d} \tau \int_ {0} ^ {\infty} g (u) \mathrm{e} ^ {- s u} \mathrm{d} u = F (s) G (s) \tag {2.2.12}$$

式(2.2.12)说明通过拉普拉斯变换后,复杂的卷积运算变成了简单的乘法运算。

表 2.2.1 列出了常见的拉普拉斯变换公式。

表 2.2.1 常见的拉普拉斯变换公式

<table><tr><td>原函数</td><td>拉普拉斯变换</td><td rowspan="2">收敛域</td></tr><tr><td> $f(t)=\mathcal{L}^{-1}[F(s)]$ </td><td> $F(s)=\mathcal{L}[f(t)]$ </td></tr><tr><td> $\delta(t)$ </td><td>1</td><td> $\infty >s>-\infty$ </td></tr><tr><td>1</td><td> $\frac{1}{s}$ </td><td>s&gt;0</td></tr><tr><td> $e^{-at}$ </td><td> $\frac{1}{s+a}$ </td><td>s&gt;-a</td></tr><tr><td>sin(at)</td><td> $\frac{a}{s^2+a^2}$ </td><td>s&gt;0</td></tr><tr><td>cos(at)</td><td> $\frac{s}{s^2+a^2}$ </td><td>s&gt;0</td></tr><tr><td>sinh(at)</td><td> $\frac{a}{s^2-a^2}$ </td><td>s&gt;|a|</td></tr><tr><td>cosh(at)</td><td> $\frac{s}{s^2-a^2}$ </td><td>s&gt;|a|</td></tr><tr><td> $e^{at}\sin(bt)$ </td><td> $\frac{b}{(s-a)^2+b^2}$ </td><td>s&gt;a</td></tr><tr><td> $e^{at}\cos(bt)$ </td><td> $\frac{s-a}{(s-a)^2+b^2}$ </td><td>s&gt;a</td></tr><tr><td> $e^{at}\sinh(bt)$ </td><td> $\frac{b}{(s-a)^2-b^2}$ </td><td>s-a&gt;|b|</td></tr><tr><td> $e^{at}\cosh(bt)$ </td><td> $\frac{s-a}{(s-a)^2-b^2}$ </td><td>s-a&gt;|b|</td></tr></table>
