当误差是 $O(\varepsilon)$ 时, 对于给定数值 $\varepsilon$ , 如何确定近似误差 $x(t, \varepsilon) - x_0(t)$ 的数值呢? 遗憾的是, 不能把所说的 $O(\varepsilon)$ 数量级转换为误差的数值边界。已知误差为 $O(\varepsilon)$ 意味着其范数小于 $k|\varepsilon|, k$ 为正常数, 与 $\varepsilon$ 无关。但是我们不知道 $k$ 的值是多少, 它可能是 1, 10 或任何正数①。 $k$ 与 $\varepsilon$ 无关, 保证了边界 $k|\varepsilon|$ 随着 $|\varepsilon|$ 减小而单调减小。因此对于足够小的 $|\varepsilon|$ , 误差将会很小。更准确地讲, 若给定任意容差 $\delta$ , 就可以知道对于所有 $|\varepsilon| < \delta / k$ , 误差的范数将小于 $\varepsilon$ 。如果这个范围太小而不能覆盖对 $\delta$ 有影响的数值, 就需要更高阶的逼近以扩展有效范围。对于所有 $|\varepsilon| < \sqrt{\delta / k_2}$ , $O(\varepsilon^2)$ 逼近将满足相同的 $\delta$ 容差, 而对于所有 $|\varepsilon| < (\delta / k_3)^{1/3}$ , $O(\varepsilon^3)$ 逼近也将满足相同的 $\delta$ 容差, 等等。尽管常数 $k_1, k_2$ 和 $k_3$ 不必相等, 这些间隔长度在不断增加, 由于容差 $\delta$ 一般都远小于 1 。另一种找出更高阶逼近的方法是, 对于给定的“足够小”的 $\varepsilon$ ，当 $n > m$ 时， $O(\varepsilon^n)$ 的误差将小于 $O(\varepsilon^m)$ 的误差，因为

$$\frac {k _ {1} | \varepsilon | ^ {n}}{k _ {2} | \varepsilon | ^ {m}} < 1, \forall | \varepsilon | < \left(\frac {k _ {2}}{k _ {1}}\right) ^ {1 / (n - m)}$$

假如函数 $f$ 和 $\eta$ 足够光滑，可以直接得到方程(10.1)和方程(10.2)的高阶逼近。假设对于 $(t,x,\varepsilon)\in [t_0,t_1]\times D\times [-\varepsilon_0,\varepsilon_0],f$ 和 $\eta$ 具有关于 $(x,\varepsilon)$ 的直到 $N$ 阶的连续偏导数，为了得到 $x(t,\varepsilon)$ 的高阶逼近，构造一个有限项泰勒级数

$$x (t, \varepsilon) = \sum_ {k = 0} ^ {N - 1} x _ {k} (t) \varepsilon^ {k} + \varepsilon^ {N} R _ {x} (t, \varepsilon) \tag {10.5}$$

这里需要做两件事,一件事是计算 $x_0, x_1, \cdots, x_{N-1}$ , 在此过程中, 要证明这些项有严格定义。另一件事是证明余项 $R_x$ 有严格定义, 且在 $[t_0, t_1]$ 上有界, 这样就确定了 $\sum_{k=0}^{N-1} x_k(t) \varepsilon^k$ 是 $x(t, \varepsilon)$ 的一个 $O(\varepsilon^N)(N$ 阶)逼近。根据泰勒定理①, 对初始状态 $O(\varepsilon^N)$ 的光滑性要求保证了 $\eta(\varepsilon)$ 存在一个有限项泰勒级数, 即

$$\eta (\varepsilon) = \sum_ {k = 0} ^ {N - 1} \eta_ {k} \varepsilon^ {k} + \varepsilon^ {N} R _ {\eta} (\varepsilon)$$

因此有 $x_{k}(t_{0}) = \eta_{k}, k = 0,1,2,\dots ,N - 1$

将式(10.5)代入式(10.1)得

$$
\begin{array}{l} \sum_ {k = 0} ^ {N - 1} \dot {x} _ {k} (t) \varepsilon^ {k} + \varepsilon^ {N} \dot {R} _ {x} (t, \varepsilon) = f (t, x (t, \varepsilon), \varepsilon) \stackrel {\mathrm{def}} {=} h (t, \varepsilon) \\ = \sum_ {k = 0} ^ {N - 1} h _ {k} (t) \varepsilon^ {k} + \varepsilon^ {N} R _ {h} (t, \varepsilon) \tag {10.6} \\ \end{array}
$$
