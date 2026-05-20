$$
\frac {\mathrm{d} x}{\mathrm{d} t} = \left[ \begin{array}{l l} 0 & 1 \\ - 1 & 0 \end{array} \right] x. \tag {2.4.6}
$$

易知 $x = 0$ 是它的唯一平衡解, 并且微分方程 (2.4.6) 以 $(0, x_0)$ 为初值的解 $\varphi(t; 0, x_0)$ 为

$$
\varphi (t; 0, x _ {0}) = \left[ \begin{array}{l} x _ {0 1} \cos t + x _ {0 2} \sin t \\ x _ {0 2} \cos t - x _ {0 1} \sin t \end{array} \right], \tag {2.4.7}
$$

这里 $x_0 = [x_{10}, x_{20}]^{\mathrm{T}} \neq 0$

不难看到，对于任给的 $\varepsilon > 0$ ，取 $\delta = \varepsilon$ ，只要 $(x_{10}^2 + x_{20}^2)^{1/2} < \delta$ ，就有

$$\left| \varphi (t; 0, x _ {0}) - 0 \right| = \left(x _ {1 0} ^ {2} + x _ {2 0} ^ {2}\right) ^ {1 / 2} < \varepsilon , \quad \forall t \geqslant 0.$$

所以微分方程 (2.4.6) 的平衡解 $x = 0$ 是稳定的.

但是

$$\lim _ {t \rightarrow + \infty} | \varphi (t; 0, x _ {0}) - 0 | = (x _ {1 0} ^ {2} + x _ {2 0} ^ {2}) ^ {1 / 2} \neq 0,$$

所以它的平衡解 $x = 0$ 不是渐近稳定的.

线性定常微分方程的稳定性有相当完善的理论. 这些理论不仅本身是重要的, 而且是研究非线性微分方程稳定性的重要参照. 考察线性齐次定常向量微分方程

$$\frac {\mathrm{d} x}{\mathrm{d} t} = A x, \tag {2.4.8}$$

其中 $x \in \mathbb{R}^n, A \in \mathbb{R}^{n \times n}$ .

定理 2.4.1(Lyapunov 稳定性定理) $^{[12]}$ 线性定常微分方程 (2.4.8) 的平衡解稳定的充要条件是 A 的所有特征值皆具有非正实部，而且实部为零的特征值是其最小多项式的单根；微分方程 (2.4.8) 的平衡解渐近稳定的充分必要条件是 A 的所有特征值皆具有负实部.

定理2.4.1 把线性齐次定常微分方程 (2.4.8) 的平衡解的稳定性问题与它的系数矩阵 $\pmb{A}$ 的特征值直接联系起来了，这就使得在研究方程 (2.4.8) 的稳定性问题时不必具体求出解的表达式，而只需考察其系数阵即可。 $\pmb{A}$ 的特征值是其特征方程

$$\det (\lambda I _ {n} - A) = \lambda^ {n} + a _ {n - 1} \lambda^ {n - 1} + a _ {n - 2} \lambda^ {n - 2} + \dots + a _ {1} \lambda + a _ {0} = 0 \tag {2.4.9}$$

的根．熟知，当 $n > 3$ 时要求方程(2.4.9)的根并不容易．一个自然的问题是，不通过求解特征方程就能够了解特征值的分布呢？答案是肯定的.

定义2.4.7 一个 $n \times n$ 矩阵 $\pmb{A}$ 称为稳定的，如果其特征值皆具有负实部；稳定矩阵 $\pmb{A}$ 的特征多项式 $\operatorname{det}(\lambda I_n - A)$ 称为稳定多项式或Hurwitz多项式.

定理 2.4.2 多项式 $\varphi_{n}(\lambda)=\lambda^{n}+a_{1}\lambda^{n-1}+a_{2}\lambda^{n-2}+\cdots+a_{n-1}\lambda+a_{n}$ 为稳定多项式的必要条件是它的系数 $a_{1},\cdots,a_{n}$ 都是正的.

为了从多项式 $\varphi_{n}(\lambda)$ 的系数来判断其稳定性，下面考察由 $\varphi_{n}(\lambda)$ 的系数按照一定规则组成的 $n \times n$ 方阵

$$
\boldsymbol {H} _ {n} = \left[ \begin{array}{c c c c c c} a _ {1} & 1 & 0 & 0 & \dots & 0 \\ a _ {3} & a _ {2} & a _ {1} & 1 & \dots & 0 \\ a _ {5} & a _ {4} & a _ {3} & a _ {2} & \dots & 0 \\ a _ {7} & a _ {6} & a _ {5} & a _ {4} & \dots & 0 \\ \vdots & \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & 0 & \dots & a _ {n} \end{array} \right].
$$

方阵 $H_{n}$ 的构成方法是
