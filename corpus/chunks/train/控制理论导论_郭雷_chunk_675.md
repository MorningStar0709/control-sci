# 9.3 时变随机系统稳定性

在自适应系统研究中，常常遇到下列类型的时变随机系统

$$x _ {t + 1} = A _ {t} x _ {t} + \xi_ {t + 1}, \quad t \geqslant 0. \tag {9.3.1}$$

其中 $x_{t}\in \mathbb{R}^{n},A_{t}\in \mathbb{R}^{n\times n},\xi_{t}\in \mathbb{R}^{n}$ 都是随机序列.

易见，方程(9.3.1)的稳定性依赖于其齐次部分

$$x _ {t + 1} = A _ {t} x _ {t}, \quad t \geqslant 0 \tag {9.3.2}$$

的稳定性，而这又实质上是关于随机矩阵无穷乘积的研究.

我们先考虑式 (9.3.2) 的渐近稳定性.

定理9.3.1 (Furstenberg-Kesten) 设 $\{A_t, t \geqslant 1\}$ 是平稳矩阵序列，则极限

$$\lim _ {t \rightarrow \infty} \frac {1}{t} E [ \log \| A _ {t} A _ {t - 1} \dots A _ {1} \| ] = \lambda$$

存在 ( $\lambda$ 不一定是有限数). 进一步, 若 $\{A_{t}\}$ 还是遍历的且 $E[\log^{+}\|A_{1}\|]<\infty$ , 则 $\lambda<\infty$ 且

$$\lim _ {t \rightarrow \infty} \frac {1}{t} \log \| A _ {t} A _ {t - 1} \dots A _ {1} \| = \lambda \quad \text { a.s. }$$

对慢变化的适应算法来讲，常常有 $A_{t} = I - \mu F_{t},\mu \in (0,1]$ .这时当 $\mu$ 很小时，利用定理9.3.1可得如下结果[11]：

定理9.3.2 设 $\{F_t\}$ 是平稳遍历的矩阵序列， $E\| F_1\| < \infty$ 。则对任何 $\mu > 0$ ，下述极限

$$\lambda_ {\mu} \stackrel {\text { def }} {=} \lim _ {t \rightarrow \infty} \frac {1}{t} \log \| (I - \mu F _ {t}) (I - \mu F _ {t - 1}) \dots (I - \mu F _ {1}) \|$$

存在，并且 $\lambda_{\mu} < \infty$ 既不依赖于范数的选取，也不依赖于样本 $\omega$ 。进一步还有

$$\limsup _ {\mu \to 0} \frac {\lambda_ {\mu}}{\mu} \leqslant - \lambda_ {\min} \left(E \left[ \frac {F _ {1} + F _ {1} ^ {\mathrm{T}}}{2} \right]\right).$$

上一定理说明，对 $\forall \alpha < \lambda_{\min}\left(E\left[\frac{F_1 + F_1^{\mathrm{T}}}{2}\right]\right)$ ，对所有充分小的 $\mu > 0$ 和充分大的 $t$ 都有

$$\left\| \left(I - \mu F _ {t}\right) \left(I - \mu F _ {t - 1}\right) \dots \left(I - \mu F _ {1}\right) \right\| \leqslant e ^ {- \mu \alpha t}, \quad \text { a.s. }$$

此时，若 $\alpha > 0$ ，则显然式(9.3.2)的解是渐近稳定的.

当将这一定理用于适应性算法分析时，遇到两个困难。其一是一般来讲，随机矩阵序列 $\{A_t, t \geqslant 1\}$ 往往并不是平稳遍历的；其二，更重要的是，仅仅证明齐次方程 (9.3.2) 以上述指数的速度趋于零，一般还并不能保证方程 (9.3.1) 的稳定性。

为说明这一点，我们先引进下列记号：

定义9.3.1 若随机矩阵序列 $\{A_t, t \geqslant 0\}$ 满足

$$\sup _ {t \geqslant 0} E \| A _ {t} \| ^ {p} < \infty , \quad p > 0,$$

则称其为 $L_{p}$ 稳定的. $A_{t}$ 的 $L_{p}$ 模定义为 $\| A_{t}\|_{L_{p}}\stackrel {\mathrm{def}}{=}\{E\| A_{t}\|^{p}\}^{1 / p}.$

定义 9.3.2 若存在常数 $M > 0, \lambda \in (0,1), p > 0,$ 使方程 (9.3.2) 中的随机矩阵序列 $\{A_{t}, t \geqslant 0\}$ 满足

$$\left\| \prod_ {j = i + 1} ^ {k} A _ {j} \right\| _ {L _ {p}} \leqslant M \lambda^ {k - i}, \quad \forall k \geqslant i > 0,$$

其中

$$
\prod_ {j = i + 1} ^ {k} A _ {j} = \left\{ \begin{array}{l l} A _ {k} \dots A _ {i + 1}, & k > i, \\ I, & k \leqslant i, \end{array} \right.
$$

则称方程 (9.3.2) 是 $L_{p}$ -指数稳定的.
