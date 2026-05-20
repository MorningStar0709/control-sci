# 1. 时域信号

时域信号 $\boldsymbol{u}(t)$ 可理解为从 $(-∞, +∞)$ 到实数 R 的一个函数，设 $u(t)$ 是勒贝格可测函数，下面给出关于函数空间的一些定义。

定义1 对于正数 $p \in [1, +\infty)$ , 元素 $\pmb{u}(\cdot)$ 为勒贝格可测函数, 且满足

$$\int_ {- \infty} ^ {+ \infty} | \boldsymbol {u} (t) | ^ {p} \mathrm{d} t < + \infty$$

的函数空间,称为 $L_{p}(-\infty, +\infty)$ 空间。其中 $L_{p}(-\infty, +\infty)$ 空间中,常用的函数空间有

$$
\begin{array}{l} L _ {1} (- \infty , + \infty): \int_ {- \infty} ^ {+ \infty} | u (t) | d t <   + \infty \\ L _ {2} (- \infty , + \infty): \int_ {- \infty} ^ {+ \infty} | u (t) | ^ {2} d t <   + \infty \\ L _ {\infty} (- \infty , + \infty): \underset {t \in (- \infty , + \infty)} {\text { esssup }} | u (t) | <   + \infty \\ \end{array}
$$

其中，esssup 表示真上确界。所谓函数在点集 Q 上的真上确界是指它在 Q 中除某个零测度集外的上确界。对于连续函数，其上确界就是真上确界。

在 $L_{p}(-\infty, +\infty)$ 空间中，所有对 $t < 0$ 除去在测度为零的集合上均为零的函数的全体所构成的集合记为 $L_{p}[0, +\infty)$ 。 $L_{p}[0, +\infty)$ 是 $L_{p}(-\infty, +\infty)$ 的一个闭空间，因为实际信号均满足 $t \geqslant 0$ ，所以这里讨论的信号均属于 $L_{p}[0, +\infty)$ 空间。需要说明的是：对于函数空间中的元素 $\pmb{u}(t)$ 可以是单个的函数，也可以是向量函数。

对于时域信号 $u(t)$ ，常用的范数有：

1 - 范数： $\| \pmb{u} \|_{1} = \int_{-\infty}^{+\infty} |\pmb{u}(t)| \, \mathrm{d}t$

2 - 范数： $\| \pmb{u} \|_{2} = \left( \int_{-\infty}^{+\infty} \pmb{u}^{2}(t) \, \mathrm{d}t \right)^{\frac{1}{2}}$

$\infty - \text{范数:} \quad \| u \|_{\infty} = \underset{t \in (-\infty, +\infty)}{\operatorname{esssup}} |u(t)|$

应当指出：2-范数的平方实际上是对信号能量的一种度量，而 $\infty$ 范数则是对信号幅值上界的度量。因此， $L_{2}[0, +\infty)$ 中的信号属能量有限信号，如单位脉冲信号（幅值不受限）；而 $L_{\infty}[0, +\infty)$ 中的信号则属于幅值有限信号，如单位阶跃信号（能量不受限）。可见， $L_{2}[0, +\infty)$ 和 $L_{\infty}[0, +\infty)$ 以及 $L_{1}[0, +\infty)$ 空间并不是完全等价的。
