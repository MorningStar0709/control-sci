$$
\begin{array}{l} E e ^ {i \gamma^ {\mathrm{T}} w} = \exp \left\{\mathrm{i} [ \lambda^ {\mathrm{T}}, \mu^ {\mathrm{T}} ] \left[ \begin{array}{c} E x \\ E y \end{array} \right] - \frac {1}{2} [ \lambda^ {\mathrm{T}}, \mu^ {\mathrm{T}} ] \left[ \begin{array}{c c} R _ {x} & 0 \\ 0 & R _ {y} \end{array} \right] \left[ \begin{array}{c} \lambda \\ \mu \end{array} \right] \right\} \\ = \exp \left(\mathrm{i} \lambda^ {\mathrm{T}} E x - \frac {1}{2} \lambda^ {\mathrm{T}} R _ {x} \lambda + \mathrm{i} \mu^ {\mathrm{T}} E y - \frac {1}{2} \mu^ {\mathrm{T}} R _ {y} \mu\right) \\ = E \mathrm{e} ^ {\mathrm{i} \lambda^ {\mathrm{T}} \lambda} \cdot E \mathrm{e} ^ {\mathrm{i} \mu^ {\mathrm{T}} \mu} \\ \end{array}
$$

由定理 4.2.1, 知 x 和 y 独立.

对条件正态的结论证明也完全类似；

ii) 只要计算 $Aw + b$ 的特征函数及在 $z$ 条件下， $A(z)w + b(z)$ 的条件特征函数就可以看出定理结论正确.

下面的引理表示，在正态及条件正态时，最小方差估计是线性估计.

引理4.4.5 i) 设 $\begin{bmatrix} x \\ y \end{bmatrix}$ 正态，那么

$$E (x | y) = E x + R _ {x y} R _ {y} ^ {+} (y - E y), \tag {4.4.25}E (x - E (x | y)) (x - E (x | y)) ^ {\mathrm{T}} = R _ {x} - R _ {x y} R _ {y} ^ {+} R _ {y x} \stackrel {\text { def }} {=} R _ {x} ^ {y}, \tag {4.4.26}$$

$x - E(x|y)$ 和 $y$ 独立，并且 $x - E(x|y)$ 正态，在 $y$ 条件下， $x$ 是期望为 $E(x|y)$ 协方差阵为 $R_x^y$ 的条件正态向量；

ii) 设在 $y$ 条件下， $\left[ \begin{array}{c}x\\ z \end{array} \right]$ 为条件正态，那么

$$
E (x \mid y, z) = E (x \mid y) + R _ {x, z} ^ {y} \left(R _ {z} ^ {y}\right) ^ {+} (z - E (z \mid y)), \tag {4.4.27}
\begin{array}{l} R _ {x} ^ {z, y} \stackrel {\text { def }} {=} E [ (x - E (x | z y)) (x - E (x | z, y)) ^ {\mathrm{T}} | z, y ] \\ = R _ {x} ^ {y} - R _ {x, z} ^ {y} \left(R _ {z} ^ {y}\right) ^ {+} R _ {z x} ^ {y}. \tag {4.4.28} \\ \end{array}
$$

在 $y$ 条件， $x - E(x|z, y)$ 和 $z$ 条件独立，并且条件正态。在 $(z, y)$ 条件下， $x$ 是期望为 $E(x|z, y)$ ，协方差阵为 $R_x^{z, y}$ 的正态向量。

证明 i) 用式 (4.4.5) 知

$$E [ x - E x - R _ {x y} R _ {y} ^ {+} (y - E y) ] [ y - E y ] ^ {\mathrm{T}} = 0.$$

因此

$$E [ x - E x - R _ {x y} R _ {y} ^ {+} (y - E y) ] y ^ {\mathrm{T}} = 0.$$

据引理4.4.4知 $x - Ex - R_{xy}R_y^+ (y - Ey)$ 和 $y$ 独立，所以

$$E [ (x - E x - R _ {x y} R _ {y} ^ {+} (y - E y)) | y ] = E [ x - E x - R _ {x y} R _ {y} ^ {+} (y - E y) ] = 0.$$

于是就得式 (4.4.25), 因此式 (4.4.26) 和式 (4.4.27) 一样地得到.

注意到 $x - E(x|y)$ 和 $y$ 独立并正态，
