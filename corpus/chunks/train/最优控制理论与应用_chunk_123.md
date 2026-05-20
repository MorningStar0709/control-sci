# 1. 求函数极值的共轭梯度法

设 $F(X)$ 是定义在 $R^n$ 空间中的二次指标函数

$$F (\boldsymbol {X}) = \frac {1}{2} (\boldsymbol {X}, \boldsymbol {Q} \boldsymbol {X}) + \boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {X} + C \tag {7-22}$$

其中， $\boldsymbol{X} = \left( \begin{array}{cc} x_{1} & x_{2} \cdots x_{n} \end{array} \right)^{\mathrm{T}}, \boldsymbol{a}^{\mathrm{T}} = \left( \begin{array}{cc} a_{1} & a_{2} \cdots a_{n} \end{array} \right), C$ 为常数，Q 为正定阵。

$$(X, Q X) = X ^ {T} Q X \tag {7-23}$$

是 X 和 QX 的内积。要求寻找 X 使 $F(X)$ 取极值。

定义 若 $\mathbf{R}^n$ 中两个向量 $X$ 和 $Y$ 满足

$$(X, Q Y) = X ^ {T} Q Y = 0 \tag {7-24}$$

则称 X 和 Y 是 Q 共轭的。Q = I(单位阵) 时，共轭就变为通常的正交。

设向量 $P^{K}, K=0,1,2,\cdots$ 是两两 Q 共轭的，以 $P^{K}$ 为寻找方向，可得共轭梯度法的迭代寻优程序：

$$\boldsymbol {X} ^ {K + 1} = \boldsymbol {X} ^ {K} + \alpha^ {K} \boldsymbol {P} ^ {K} \tag {7-25}$$

与梯度法不同处仅在于用共轭梯度 $P^{K}$ 代替负梯度 $-g^{K}=-(\partial F/\partial X)^{K}$ 。问题是如何产生共轭梯度方向 $P^{K}, K=0,1,2,\cdots$ 。

令 $P^{0} = -g^{0}$ ，即初始时共轭梯度与梯度方向相反、大小相等。以后的共轭梯度可如下递归产生：

$$\boldsymbol {P} ^ {K} = - \boldsymbol {g} ^ {K} + \beta^ {K} \boldsymbol {P} ^ {K - 1} \tag {7-26}$$

$\beta^{K}$ 的值由 $P^{K}$ 和 $P^{K - 1}$ 对 $\pmb{Q}$ 共轭的关系来确定，即

$$\left(\boldsymbol {P} ^ {K}, \boldsymbol {Q} \boldsymbol {P} ^ {K - 1}\right) = \mathbf {0} \tag {7-27}$$

将式(7-26)代入式(7-27)，得

$$
\begin{array}{l} \mathbf {0} = \left(\boldsymbol {P} ^ {K}, \boldsymbol {Q} \boldsymbol {P} ^ {K - 1}\right) = \left(- \boldsymbol {g} ^ {K} + \beta^ {K} \boldsymbol {P} ^ {K - 1}, \boldsymbol {Q} \boldsymbol {P} ^ {K - 1}\right) \\ = - \left(\boldsymbol {g} ^ {K}, \boldsymbol {Q} \boldsymbol {P} ^ {K - 1}\right) + \beta^ {K} \left(\boldsymbol {P} ^ {K - 1}, \boldsymbol {Q} \boldsymbol {P} ^ {K - 1}\right) \\ \end{array}
$$

故

$$\boldsymbol {\beta} ^ {K} = \frac {\left(\boldsymbol {g} ^ {K} , \boldsymbol {Q} \boldsymbol {P} ^ {K - 1}\right)}{\left(\boldsymbol {P} ^ {K - 1} , \boldsymbol {Q} \boldsymbol {P} ^ {K - 1}\right)} \tag {7-28}$$

$\beta^{\kappa}$ 称为共轭系数。

用式(7-28)计算 $\beta^K$ 是不方便的，因为要用到二阶导数阵 $Q$ 。由式(7-22)和(7-23)知

$$\boldsymbol {Q} = \left(\frac {\partial^ {2} F (\boldsymbol {X})}{\partial x _ {i} \partial x _ {j}}\right) 1 \leqslant i, j \leqslant n \tag {7-29}$$

$x_{i}, x_{j}$ 分别为 $X$ 的第 $i$ 个和第 $j$ 个分量，右端表示由 $\pmb{Q}$ 的第 $i$ 行第 $j$ 列元素构成的矩阵。计算这个二阶导数阵非常困难。为此，有必要推导不用 $\pmb{Q}$ 来计算 $\beta^{K}$ 的公式。在这个推导中要用到共轭梯度的下列性质：

性质 1 若 $\{P^{0}, P^{1}, \cdots, P^{n-1}\}$ 是 $R^{n}$ 空间中彼此 Q 共轭的向量，则它们是线性独立的。
