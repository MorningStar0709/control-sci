$$
\left\{ \begin{array}{l} x _ {2} + \frac {\sqrt {h ^ {r} r ^ {2} + 8 r | y |} - h r}{2} \text {sign} (y) = - h r \text {sign} (y) (\text {过点} a _ {s i} \text {的对接抛物线}) \\ x _ {2} + \frac {\sqrt {h ^ {r} r ^ {2} + 8 r | y |} - h r}{2} \text {sign} (y) = h r \text {sign} (y) (\text {过点} b _ {s i} \text {的对接抛物线}) \\ x _ {2} + \frac {\sqrt {h ^ {r} r ^ {2} + 8 r | y |} - h r}{2} \text {sign} (y) = 0 (\text {过点} c _ {s i} \text {的对接抛物线}) \end{array} \right. \tag {2.7.10}
$$

现在，在等时区 $G(2)$ 之外，即由不等式 $\left|x_{1}+hx_{2}\right|=\left|y\right|\geqslant hr$ 限定的区域内，定义函数

$$a \left(x _ {1}, x _ {2}, r, h\right) = x _ {2} + \frac {\sqrt {h ^ {2} r ^ {2} + 8 r | y |} - h r}{2} \operatorname{sign} (y), | y | \geqslant h r \tag {2.7.11}$$

那么有

$$
\left\{ \begin{array}{l} a (x _ {1}, x _ {2}, r, h) \mid_ {a _ {+ i}, \delta_ {+ i}, i \geqslant 2} = - h r \\ a (x _ {1}, x _ {2}, r, h) \mid_ {a _ {- i}, \delta_ {- i}, i \geqslant 2} = h r \\ a (x _ {1}, x _ {2}, r, h) \mid_ {c _ {+ i}, c _ {- i}, i \geqslant 2} = 0 \end{array} \right. \tag {2.7.12}
$$

用 $\widetilde{I}^{+},\widetilde{I}^{-},\widetilde{I}^{0}$ 分别记等式

$$
\begin{array}{l} a \left(x _ {1}, x _ {2}, r, h\right) = - h r; \\ a \left(x _ {1}, x _ {2}, r, h\right) = h r; \\ a \left(x _ {1}, x _ {2}, r, h\right) = 0 \tag {2.7.13} \\ \end{array}
$$

所确定的曲线,那么,在等时区 $G(2)$ 之外,曲线 $\widetilde{\Gamma}^{+},\widetilde{\Gamma}^{-},\widetilde{\Gamma}^{0}$ 分别和折线 $\Gamma^{+},\Gamma^{-},\Gamma^{0}$ ,在折点上完全重合,而且有

$$
\left\{ \begin{array}{l} a (x _ {1}, x _ {2}, r, h) \leqslant - h r (\text {点} (x _ {1}, x _ {2}) \text {在曲线} \hat {\Gamma} ^ {+} \text {的下方}) \\ a (x _ {1}, x _ {2}, r, h) \geqslant h r (\text {点} (x _ {1}, x _ {2}) \text {在曲线} \hat {\Gamma} ^ {-} \text {的上方}) \\ | a (x _ {1}, x _ {2}, r, h) | \leqslant h r (\text {点} (x _ {1}, x _ {2}) \text {在曲线} \hat {\Gamma} ^ {+} \text {和} \hat {\Gamma} ^ {-} \text {限定的区域}) \end{array} \right. \tag {2.7.14}
$$

于是定义函数

$$
\operatorname{sat} (x, \delta) = \left\{ \begin{array}{l l} \operatorname{sign} (x), & | x | > \delta \\ \frac {x}{\delta}, & | x | \leqslant \delta \end{array} \right.
$$

时，在等时区 $G(2)$ 之外，即当 $|y| \geqslant hr$ 时，快速最优控制函数可近似（由于折线 $\Gamma^{+}, \Gamma^{-}$ 和曲线 $\widetilde{\Gamma}^{+}, \widetilde{\Gamma}^{-}$ 之间有一点微小差别）地定义为

$$u = - r \operatorname{sat} (a (x _ {1}, x _ {2}, r, h), h r), | y | \geqslant h r \tag {2.7.15}$$

下面考察等时区 $G(2)$ 内的快速最优控制综合函数．等时区 $G(2)$ 的表达式为
