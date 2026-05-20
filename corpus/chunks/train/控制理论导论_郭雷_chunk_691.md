$$I - \mu F _ {t} = (1 - \mu) P _ {t} P _ {t - 1} ^ {- 1}. \tag {9.4.17}$$

于是对任何 $k \geqslant i > 0$ 有

$$\prod_ {j = i + 1} ^ {k} (I - \mu F _ {j}) = (1 - \mu) ^ {k - i} P _ {k} P _ {i} ^ {- 1}. \tag {9.4.18}$$

进一步，利用矩阵求逆公式从式(9.4.9)可知

$$P _ {t} ^ {- 1} = (1 - \mu) P _ {t - 1} ^ {- 1} + \mu \phi_ {t} \phi_ {t} ^ {\mathrm{T}}, \tag {9.4.19}$$

从而根据假设易见

$$\sup _ {t} \| P _ {t} ^ {- 1} \| _ {L _ {q}} < \infty , \tag {9.4.20}$$

因此，为证 $\{\mu F_j\} \in S_p$ ，只需证明对任意的 $p \geqslant 1$ 都有 $\sup_t \| P_t \|_{L_p} < \infty$ 即可.

对任何 $m \geqslant 0$ 从式 (9.4.9) 知

$$P _ {k - 1} \leqslant \frac {1}{1 - \mu} P _ {k - 2} \leqslant \dots \leqslant \left(\frac {1}{1 - \mu}\right) ^ {h - 1} P _ {m h}, \quad k \in [ m h + 1, (m + 1) h ], \tag {9.4.21}$$

于是再次利用式 (9.4.19) 和矩阵求逆公式 (1.1.8) 知

$$
\begin{array}{l} P _ {k} = [ (1 - \mu) P _ {k - 1} ^ {- 1} + \mu \phi_ {k} \phi_ {k} ^ {\mathrm{T}} ] ^ {- 1} \leqslant [ (1 - \mu) ^ {h} P _ {m h} ^ {- 1} + \mu \phi_ {k} \phi_ {k} ^ {\mathrm{T}} ] ^ {- 1} \\ = \left(\frac {1}{1 - \mu}\right) ^ {h} \left[ P _ {m h} - \frac {\mu P _ {m h} \phi_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {m h}}{(1 - \mu) ^ {h} + \mu \phi_ {k} ^ {\mathrm{T}} P _ {m h} \phi_ {k}} \right] \\ \leqslant \left(\frac {1}{1 - \mu}\right) ^ {h} \left[ P _ {m h} - \frac {\mu P _ {m h} \phi_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {m h}}{[ (1 - \mu) ^ {h} + \mu \lambda_ {\max} (P _ {m h}) ] [ 1 + \| \phi_ {k} \| ^ {2} ]} \right]. \tag {9.4.22} \\ \end{array}
$$

令

$$T _ {m} = \sum_ {k = (m - 1) h + 1} ^ {m h} \operatorname{tr} \left(P _ {k}\right), \tag {9.4.23}a _ {m + 1} = \frac {\mu \operatorname{tr} \left[ P _ {m h} ^ {2} \sum_ {k = m h + 1} ^ {(m + 1) h} \frac {\phi_ {k} \phi_ {k} ^ {\mathrm{T}}}{1 + \| \phi_ {k} \| ^ {2}} \right]}{\left[ (1 - \mu) ^ {h} + \mu \lambda_ {\max} \left(P _ {m h}\right) \right] h \operatorname{tr} \left(P _ {m h}\right)}, \tag {9.4.24}$$

于是对式 (9.4.22) 两边求和得

$$T _ {m + 1} \leqslant (1 - \mu) ^ {- h} [ 1 - a _ {m + 1} ] h \mathrm{tr} (P _ {m h}). \tag {9.4.25}$$

但根据不等式 $P_{k} \leqslant (1 - \mu)^{-1} P_{k-1}$ 知

$$
\begin{array}{l} h \operatorname{tr} \left(P _ {m h}\right) = \sum_ {k = (m - 1) h + 1} ^ {m h} \operatorname{tr} \left(P _ {m h}\right) \leqslant \sum_ {k = (m - 1) h + 1} ^ {m h} (1 - \mu) ^ {- (m h - k)} \operatorname{tr} \left(P _ {k}\right) \\ \leqslant (1 - \mu) ^ {- h + 1} T _ {m}. \\ \end{array}
$$

将此式代入式 (9.4.25) 得

$$T _ {m + 1} \leqslant (1 - \mu) ^ {1 - 2 h} [ 1 - a _ {m + 1} ] T _ {m}. \tag {9.4.26}$$

为了分析此式，我们对任何 $p \geqslant 1$ ，记

$$b _ {m + 1} = (1 - \mu) ^ {(1 - 2 h) p} \left[ 1 - \frac {a _ {m + 1}}{2} \right] I (\operatorname{tr} (P _ {m h}) \geqslant \mu^ {- 1}),$$
