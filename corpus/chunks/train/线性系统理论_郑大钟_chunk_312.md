其中 $\{\mu_{1},\cdots,\mu_{a}\}$ 为右克罗内克尔指数， $\{\nu_{1},\cdots,\nu_{\theta}\}$ 为左克罗内克尔指数。再知， $L_{\mu_{i}}$ 为下形的 $\mu_{i}\times(\mu_{i}+1)$ 矩阵：

$$
L _ {\mu_ {j}} = \left[ \begin{array}{c c c c} s & - 1 & & \\ \ddots & \ddots & \ddots & \\ & \ddots & \ddots & \\ & s & - 1 \end{array} \right] \tag {8.82}
$$

因此，必可找到 $(\mu_{i} + 1)$ 维多项式列向量 $p(s)$ ，使成立

$$
L _ {\mu_ {i}} \boldsymbol {p} (s) = \left[ \begin{array}{c c c c c} s & - 1 & & \\ & \ddots & \ddots & \\ & & \ddots & \ddots & \\ & & s & - 1 \end{array} \right] \left[ \begin{array}{l} s ^ {k} \\ s ^ {k + 1} \\ \vdots \\ s ^ {k + \mu_ {i}} \end{array} \right] = 0. \tag {8.83}
$$

并且，当 $k = 0$ 时， $\pmb{p}(s)$ 为满足(8.83)的一个最小次数多项式向量。于是，在此基础上，我们就可对矩阵束 $(sE - A)$ 来构造如下的一组线性无关的多项式列向量：

$$
f _ {1} (s) = V \left[ \begin{array}{c} 1 \\ s \\ \vdots \\ s ^ {\mu_ {1}} \\ - - - \\ 0 \\ \vdots \\ \vdots \\ \vdots \\ \vdots \\ 0 \end{array} \right], \quad f _ {2} (s) = V \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ - - - \\ 1 \\ s \\ \vdots \\ s ^ {\mu_ {2}} \\ - - - \\ 0 \\ \vdots \\ 0 \end{array} \right], \dots , \quad f _ {a} (s) = V \left[ \begin{array}{c} 0 \\ \vdots \\ \vdots \\ \vdots \\ 0 \\ - - - \\ 1 \\ s \\ \vdots \\ s ^ {\mu_ {a}} \end{array} \right] \tag {8.84}
$$

并且，进而有

$$
(s E - A) f _ {i} (s) = U ^ {- 1} U (s E - A) V \left[ \begin{array}{c} 0 \\ \vdots \\ \vdots \\ 0 \\ - \frac {}{} 1 \\ s \\ \vdots \\ s ^ {\mu_ {i}} \\ - \frac {}{} 0 \\ \vdots \\ \vdots \\ 0 \end{array} \right] = U ^ {- 1} \left[ \begin{array}{c c c c} L _ {\mu_ {i}} & & & 0 \\ & L _ {\mu_ {j}} & & \\ & & L _ {\mu_ {o}} & \\ - & & & - \\ & 0 & & * \\ & & & \end{array} \right] \left[ \begin{array}{c} 0 \\ \vdots \\ \vdots \\ 0 \\ - \frac {}{} 1 \\ s \\ \vdots \\ s ^ {\mu_ {i}} \\ - \frac {}{} 0 \\ \vdots \\ \vdots \\ 0 \end{array} \right]
= 0, i = 1, 2, \dots , \alpha \tag {8.85}
$$

其中，“\*”表示克罗内克尔形中余下的各分块阵的总体。这表明，式(8.84)中定义的 $\alpha$ 个线性无关的多项式列向量 $\{f_1(s),\dots ,f_a(s)\}$ 为（ $sE - A$ ）的右零空间的一个多项式基，且如前面所已指出的那样，其次数 $\{\mu_1,\dots ,\mu_a\}$ 是最小的。因此就证明了， $G(s)$ 的右最小指数即等于（ $sE - A$ ）的右克罗内克尔指数。同理，也可证明左最小指数等于左克罗内克尔指数。于是结论得证。

一个推论 下面,我们对零空间的最小多项式基,来给出一个重要的推论。

推论 给定如下的一个满列秩的多项式矩阵 $F(s)$ :

$$F (s) = \left[ f _ {1} (s), f _ {2} (s), \dots , f _ {\alpha} (s) \right] \tag {8.86}$$

其列次数满足如下非降关系式:

$$\mu_ {1} \leqslant \mu_ {2} \leqslant \dots \leqslant \mu_ {a} \tag {8.87}$$

则下述三种说法是等价的：

(1) $\{f_{1}(s), f_{2}(s), \cdots, f_{n}(s)\}$ 是由其张成的一个有理分式向量空间的一个最小多项式基。

(2) $F(s)$ 是列既约的和不可简约的。

(3) $F(s)$ 有最小阶。

证 按照多项式基的阶数的定义, 可知(1)和(3)间的等价性是显然的。下面, 只来证明(1)和(2)间的等价性。
