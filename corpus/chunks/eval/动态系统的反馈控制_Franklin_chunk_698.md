# 1. 叠加原理

拉普拉斯变换的一个重要性质就是线性性质，其证明如下：

$$
\begin{array}{l} \mathscr {L} \left\{\alpha f _ {1} (t) + \beta f _ {2} (t) \right\} = \int_ {0} ^ {+ \infty} \left[ \alpha f _ {1} (t) + \beta f _ {2} (t) \right] e ^ {- s t} d t \tag {A.5} \\ = \alpha \int_ {0} ^ {+ \infty} f _ {1} (t) \mathrm{e} ^ {- s t} \mathrm{d} t + \beta \int_ {0} ^ {+ \infty} f _ {2} (t) \mathrm{e} ^ {- s t} \mathrm{d} t \\ = \alpha F _ {1} (s) + \beta F _ {2} (s) \\ \end{array}
$$

线性的扩展属性是一个特例，即，

$$\mathcal {L} \{\alpha f (t) \} = \alpha F (s) \tag {A.6}$$

表 A.1 拉普拉斯变换的性质

<table><tr><td>编号</td><td>拉普拉斯变换</td><td>时域函数</td><td>备注</td></tr><tr><td>-</td><td> $F(s)$ </td><td> $f(t)$ </td><td>变换对</td></tr><tr><td>1</td><td> $\alpha F_{1}(s)+\beta F_{2}(s)$ </td><td> $\alpha f_{1}(t)+\beta f_{2}(t)$ </td><td>叠加性质</td></tr><tr><td>2</td><td> $F(s)e^{-s\lambda}$ </td><td> $f(t-\lambda)$ </td><td>延时性质( $\lambda \geqslant 0$ )</td></tr><tr><td>3</td><td> $\frac{1}{|a|}F\left(\frac{s}{a}\right)$ </td><td> $f(at)$ </td><td>比例性质</td></tr><tr><td>4</td><td> $F(s+a)$ </td><td> $e^{-\alpha t}f(t)$ </td><td>位移性质</td></tr><tr><td>5</td><td> $s^{m}F(s)-s^{m-1}f(0)-s^{m-2}\dot{f}(0)-\cdots-f^{(m-1)}(0)$ </td><td> $f^{(m)}(t)$ </td><td>微分性质</td></tr><tr><td>6</td><td> $\frac{1}{s}F(s)$ </td><td> $\int_{0}^{t}f(\zeta)d\zeta$ </td><td>积分性质</td></tr><tr><td>7</td><td> $F_{1}(s)F_{2}(s)$ </td><td> $f_{1}(t)*f_{2}(t)$ </td><td>卷积性质</td></tr><tr><td>8</td><td> $\lim_{s\to+\infty}sF(s)$ </td><td> $f(0^{+})$ </td><td>初值定理</td></tr><tr><td>9</td><td> $\lim_{s\to0}sF(s)$ </td><td> $\lim_{t\to+\infty}f(t)$ </td><td>终值定理</td></tr><tr><td>10</td><td> $\frac{1}{2\pi\mathrm{j}}\int_{\sigma_{e}-j\infty}^{\sigma_{e}+j\infty}F_{1}(\zeta)F_{2}(s-\zeta)d\zeta$ </td><td> $f_{1}(t)f_{2}(t)$ </td><td>时域乘积定理</td></tr><tr><td>11</td><td> $\frac{1}{2\pi}\int_{-j\infty}^{+j\infty}Y(-j\omega)U(j\omega)d\omega$ </td><td> $\int_{0}^{+\infty}y(t)u(t)dt$ </td><td>巴塞伐尔(Parseval)定理</td></tr><tr><td>12</td><td> $-\frac{\mathrm{d}}{\mathrm{d}s}F(s)$ </td><td> $tf(t)$ </td><td>时域与时间乘积性质</td></tr></table>

表 A.2 拉普拉斯变换表
