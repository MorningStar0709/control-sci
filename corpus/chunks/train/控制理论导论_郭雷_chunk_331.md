显然，对任何 $n \times m$ 矩阵 $\pmb{K}$ , $x_{y} = Ex + K(y - Ey)$ 是用 $y$ 对 $x$ 的线性无偏估计. 所谓无偏，是指 $Ex_{y} = Ex$ .

注意到

$$E [ (I - R _ {y} ^ {+} R _ {y}) (y - E y) ] [ (I - R _ {y} ^ {+} R _ {y}) (y - E y) ] ^ {*} = 0,$$

所以

$$(y - R y) ^ {*} = (y - E y) ^ {*} R _ {y} ^ {+} R _ {y}, \quad \text { a.s. } \tag {4.4.4}$$

由此知

$$R _ {x y} R _ {y} ^ {+} R _ {y} = R _ {x y}. \tag {4.4.5}$$

用式 (4.4.5), 直接验证

$$
\begin{array}{l} E (x - E x - K (y - E y)) (x - E x - K (y - E y)) ^ {*} \\ = R _ {x} - K R _ {y x} - R _ {x y} K ^ {*} + K R _ {y} K ^ {*} \\ = (K - R _ {x y} R _ {y} ^ {+}) R _ {y} (K - R _ {x y} R _ {y} ^ {+}) ^ {*} + R _ {x} - R _ {x y} R _ {y} ^ {+} R _ {y x}, \\ \end{array}
$$

上式右端第一项为非负定阵，所以当 $K = R_{xy}R_y^+$ 时，

$$\hat {x} _ {y} \stackrel {\text { def }} {=} E x + R _ {x y} R _ {y} ^ {+} (y - E y) \tag {4.4.6}$$

是用 $y$ 对 $x$ 的线性无偏最小方差估计，并且此时，估计误差协方差阵为 $R_{x / y}$

$$R _ {x / y} \stackrel {\mathrm{def}} {=} E (x - \hat {x} _ {y}) (x - \hat {x} _ {y}) ^ {*} = R _ {x} - R _ {x y} R _ {y} ^ {+} R _ {y x}. \tag {4.4.7}$$

设 G 和 a 为相应维数的确定性矩阵及向量，容易验证，用 y 对 $z \stackrel{\operatorname{def}}{=} x^{1} + x^{2} + Gy + a$ 的线性无偏最小方差估计为

$$\hat {z} _ {y} = \hat {x} _ {y} ^ {1} + \hat {x} _ {y} ^ {2} + G y + a. \tag {4.4.8}$$

为了把线性无偏最小方差估计写成递推的形式，我们先证如下引理：

引理 4.4.1 设 x, y, z 为三个随机向量，二阶矩都有穷。记 $w \stackrel{\operatorname{def}}{=} \begin{bmatrix} y \\ z \end{bmatrix}$ ， $K = (R_{xz} - R_{xy} R_{y}^{+} R_{yz}) R_{z|y}^{+}$ ，那么

$$\hat {x} _ {w} = \hat {x} _ {y} + K (z - \hat {z} _ {y}). \tag {4.4.9}$$

证明 因为 $E(z - \hat{z}_y)(z - \hat{z}_y)^* = R_{z / y}$ ，所以

$$E [ (I - R _ {z / y} ^ {+} R _ {z / y}) (z - \hat {z} _ {y}) ] [ (I - R _ {z / y} ^ {+} R _ {z / y}) (z - \hat {z} _ {y}) ] ^ {*} = 0,$$

由此知

$$(z - \hat {z} _ {y}) ^ {*} = (z - \hat {z} _ {y}) ^ {*} R _ {z / y} ^ {+} R _ {z / y}.$$

记

$$R _ {x z / y} \stackrel {\text { def }} {=} E (x - \hat {x} _ {y}) (z - \hat {z} _ {y}) ^ {*},$$

则从上式知

$$R _ {x z / y} - R _ {x z / y} R _ {z / y} ^ {+} R _ {z / y} = 0,$$

或

$$E (x - \hat {x} _ {y} - R _ {x z / y} R _ {z / y} ^ {+} (z - \hat {z} _ {y}) ] (z - \hat {z} _ {y}) ^ {*} = 0. \tag {4.4.10}$$

记

$$\tilde {x} = x - \hat {x} _ {y} - R _ {x z / y} R _ {z / y} ^ {+} (z - \hat {z} _ {y}),$$

即

$$\tilde {x} = x - E x - R _ {x y} R _ {y} ^ {+} (y - E y) - R _ {x z / y} ^ {+} R _ {z / y} ^ {+} [ z - E z - R _ {z y} R _ {y} ^ {+} (y - E y) ]. \tag {4.4.11}$$

所以由式 (4.4.5) 知

$$E \tilde {x} (y - E y) ^ {*} = 0. \tag {4.4.12}$$

把式 (4.4.12) 代入式 (4.4.10) 知

$$E \bar {x} (z - E z) ^ {*} = 0,$$

因此

$$E \bar {x} (w - E w) ^ {*} = 0.$$

注意到 $E\bar{x} = 0$ ，便知 $\hat{\bar{x}}_w = 0.$

另一方面，用式(4.4.8)从 $\tilde{x}$ 的表达式(4.4.11)知

$$\tilde {x} _ {w} = \hat {x} _ {w} - E x - R _ {x y} R _ {y} ^ {+} (y - E y) - R _ {x z / y} R _ {z / y} ^ {+} (z - E z - R _ {z y} R _ {y} ^ {+} (y - E y) ], \tag {4.4.13}$$

所以，
