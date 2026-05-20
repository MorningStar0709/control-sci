# 5.1.2 模糊系统的逼近精度

万能逼近定理表明模糊系统是除多项函数逼近器、神经网络之外的一个新的万能逼近器。模糊系统较之其他逼近器的优势在于它能够有效地利用语言信息的能力。万能逼近定理是模糊逻辑系统用于非线性系统建模的理论基础，同时也从根本上解释了模糊系统在实际中得到成功应用的原因。

万能逼近定理 $^{[12]}$ 令 $f(x)$ 为式(5.2)中的二维模糊系统, $g(x)$ 为式(5.1)中的未知函数, 如果 $g(x)$ 在 $U = [\alpha_{1}, \beta_{1}] \times [\alpha_{1}, \beta_{2}]$ 上是连续可微的, 则模糊系统的逼近精度为

$$\| g - f \| _ {\infty} \leqslant \left\| \frac {\partial g}{\partial x _ {1}} \right\| _ {\infty} h _ {1} + \left\| \frac {\partial g}{\partial x _ {2}} \right\| _ {\infty} h _ {2} \tag {5.3}$$

其中 $h_{i}=\max_{1\leqslant j\leqslant N_{i}-1}\left|e_{i}^{j+1}-e_{i}^{j}\right|(i=1,2)$ (5.4)

式中，无穷维范数 $\| \cdot \|_{\infty}$ 定义为函数上界，即 $\| d(x)\|_{\infty} = \sup_{x\in U}|d(x)|,e_i^j$ 为 $x_{i}$ 在第 $A_{i}^{j}$ 个模糊集上的中间值或边界值， $j = 1$ 和 $j = N_{i}$ 时为边界值。

由式(5.4)可知:假设 $x_{i}$ 的模糊集的个数为 $N_{i}$ ，其变化范围的长度为 $L_{i}$ ，则模糊系统的逼近精度满足 $h_{i}=\frac{L_{i}}{N_{i}-1}$ ，即 $N_{i}=\frac{L_{i}}{h_{i}}+1$ 。

由该定理可得到以下结论：

①形如式(5.2)的模糊系统是万能逼近器，对任意给定的 $\varepsilon > 0$ ，都可将 $h_1$ 和 $h_2$ 选得足够小，使 $\left\| \frac{\partial g}{\partial x_1} \right\|_{\infty} h_1 + \left\| \frac{\partial g}{\partial x_2} \right\|_{\infty} h_2 < \varepsilon$ 成立，从而保证 $\sup_{x \in U} |g(x) - f(x)| = \| g - f \|_{\infty} < \varepsilon$ 。

② 通过对每个 $x_{i}$ 定义更多的模糊集可以得到更为准确的逼近器, 即规则越多, 所产生的模糊系统越有效。

③为了设计一个具有预定精度的模糊系统，必须知道 $g(x)$ 关于 $x_{1}$ 和 $x_{2}$ 的导数边界，即 $\left\|\frac{\partial g}{x_{1}}\right\|_{\infty}$ 和 $\left\|\frac{\partial g}{x_{2}}\right\|_{\infty}$ 。同时，在设计过程中，还必须知道 $g(x)$ 在 $x=(e_{1}^{i_{1}}, e_{2}^{i_{2}})(i_{1}=1,2,\cdots,N_{1}; i_{2}=1,2,\cdots,N_{2})$ 处的值。
