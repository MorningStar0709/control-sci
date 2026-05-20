$$
\begin{array}{l} C _ {s} (s) = \frac {1}{s + j \omega} [ (s + j \omega) R (s) G (s) | _ {s = - j \omega} ] + \frac {1}{s - j \omega} [ (s - j \omega) R (s) G (s) | _ {s = j \omega} ] \\ = \frac {A}{s + \mathrm{j} \omega} \frac {\cos \varphi - \mathrm{j} \sin \varphi}{- 2 \mathrm{j}} G (- \mathrm{j} \omega) + \frac {A}{s - \mathrm{j} \omega} \frac {\cos \varphi + \mathrm{j} \sin \varphi}{2 \mathrm{j}} G (\mathrm{j} \omega) \tag {5-11} \\ \end{array}
$$

设

$$G (\mathrm{j} \omega) = \frac {a (\omega) + \mathrm{j} b (\omega)}{c (\omega) + \mathrm{j} d (\omega)} = | G (\mathrm{j} \omega) | \mathrm{e} ^ {\mathrm{j} / G (\mathrm{j} \omega)} \tag {5-12}$$

因为 $G(s)$ 的分子和分母多项式为实系数，故式(5-12)中的 $a(\omega)$ 和 $c(\omega)$ 为关于 $\omega$ 的偶次幂实系数多项式， $b(\omega)$ 和 $d(\omega)$ 为关于 $\omega$ 的奇次幂实系数多项式，即 $a(\omega)$ 和 $c(\omega)$ 为 $\omega$ 的偶函数， $b(\omega)$ 和 $d(\omega)$ 为 $\omega$ 的奇函数。鉴于

$$\mid G (\mathrm{j} \omega) \mid = \left(\frac {b ^ {2} (\omega) + a ^ {2} (\omega)}{c ^ {2} (\omega) + d ^ {2} (\omega)}\right) ^ {\frac {1}{2}}. \tag {5-13}\underline {{{G (\mathrm{j} \omega)}}} = \arctan \frac {b (\omega) c (\omega) - a (\omega) d (\omega)}{a (\omega) c (\omega) + d (\omega) b (\omega)} \tag {5-14}$$

因而

$$G (- \mathrm{j} \omega) = \frac {a (\omega) - \mathrm{j} b (\omega)}{c (\omega) - \mathrm{j} d (\omega)} = | G (\mathrm{j} \omega) | \mathrm{e} ^ {- \mathrm{j} / G (\mathrm{j} \omega)} \tag {5-15}$$

再由式(5-11)得

$$C _ {s} (s) = \frac {A | G (\mathrm{j} \omega) |}{s + \mathrm{j} \omega} \frac {\mathrm{e} ^ {- \mathrm{j} (\varphi + \angle G (\mathrm{j} \omega))}}{- 2 \mathrm{j}} + \frac {A | G (\mathrm{j} \omega) |}{s - \mathrm{j} \omega} \frac {\mathrm{e} ^ {\mathrm{j} (\varphi + \angle G (\mathrm{j} \omega))}}{2 \mathrm{j}}c _ {s} (t) = A \mid G (\mathrm{j} \omega) \mid \frac {\mathrm{e} ^ {\mathrm{j} (\omega t + \varphi + \underline {{{G}}} (\mathrm{j} \omega))} - \mathrm{e} ^ {- \mathrm{j} (\omega t + \varphi + \underline {{{G}}} (\mathrm{j} \omega)}}{2 \mathrm{j}}= A \mid G (\mathrm{j} \omega) \mid \sin [ \omega t + \varphi + \underline {{{G (\mathrm{j} \omega)}}} ] \tag {5-16}$$

式(5-16)与式(5-5)相比较,得

$$
\left\{ \begin{array}{l} A (\omega) = | G (\mathrm{j} \omega) | \\ \varphi (\omega) = \underline {{G (\mathrm{j} \omega)}} \end{array} \right. \tag {5-17}
$$
