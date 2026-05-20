$$a _ {m + 1} = \frac {\operatorname{tr} \left[ \left(P _ {m h} + h \mu Q\right) ^ {2} \sum_ {k = m h + 1} ^ {(m + 1) h} \frac {\mu \phi_ {k} \phi_ {k} ^ {\mathrm{T}}}{1 + \mu \| \phi_ {k} \| ^ {2}} \right]}{h (R + 1) [ 1 + \lambda_ {\max} \left(P _ {m h} + h \mu Q\right) ] \operatorname{tr} \left(P _ {m h} + h \mu Q\right)}. \tag {9.4.33}$$

事实上，据式(9.4.12)易见

$$P _ {k - 1} \leqslant P _ {k - 2} + \mu Q \leqslant \dots \leqslant P _ {m h} + h \mu Q \tag {9.4.34}$$

对所有 $k \in [mh + 1, (m + 1)h]$ 都成立。于是利用矩阵求逆公式 (1.1.8) 知对任何 $k \in [mh + 1, (m + 1)h]$ 有

$$
\begin{array}{l} P _ {k} = \left(P _ {k - 1} ^ {- 1} + R ^ {- 1} \mu \phi_ {k} \phi_ {k} ^ {\mathrm{T}}\right) ^ {- 1} + \mu Q \\ \leqslant \left[ \left(P _ {m h} + h \mu Q\right) ^ {- 1} + R ^ {- 1} \mu \phi_ {k} \phi_ {k} ^ {\mathrm{T}} \right] ^ {- 1} + \mu Q \\ = P _ {m h} - \frac {\mu \left(P _ {m h} + h \mu Q\right) \phi_ {k} \phi_ {k} ^ {\mathrm{T}} \left(P _ {m h} + h \mu Q\right)}{R + \mu \phi_ {k} ^ {\mathrm{T}} \left(P _ {m h} + h \mu Q\right) \phi_ {k}} + \mu (h + 1) Q \\ \leqslant P _ {m h} - \frac {\left(P _ {m h} + h \mu Q\right) \frac {\mu \phi_ {k} \phi_ {k} ^ {\mathrm{T}}}{1 + \mu \| \phi_ {k} \| ^ {2}} \left(P _ {m h} + h \mu Q\right)}{(R + 1) \left[ 1 + \lambda_ {\max} \left(P _ {m h} + \mu h Q\right) \right]} + \mu (h + 1) Q. \\ \end{array}
$$

将上式两边求和并注意式 (9.4.31) 及式 (9.4.33) 得

$$T _ {m + 1} \leqslant h \operatorname{tr} \left(P _ {m h}\right) - a _ {m + 1} h \operatorname{tr} \left(P _ {m h}\right) + h (h + 1) \mu \operatorname{tr} Q. \tag {9.4.35}$$

再次利用式 (9.4.31) 及式 (9.4.34) 得

$$
\begin{array}{l} h \operatorname{tr} \left(P _ {m h}\right) = \sum_ {k = (m - 1) h + 1} ^ {m h} \operatorname{tr} \left(P _ {m h}\right) \leqslant \sum_ {k = (m - 1) h + 1} ^ {m h} \operatorname{tr} \left\{P _ {k} + (m h - k) \mu Q \right\} \\ \leqslant T _ {m} + \frac {1}{2} h (h + 1) \mu \operatorname{tr} Q. \\ \end{array}
$$

将此式代入式 (9.4.35) 即可得式 (9.4.32).

进一步，利用 $a_{m + 1}$ 的定义，易见 $a_{m + 1} \in \left[0, \frac{1}{1 + R}\right]$ 且

$$E \left[ a _ {m + 1} \mid \mathcal {F} _ {m h} \right] \geqslant \frac {(1 + h) \mu^ {2} \| Q \| \lambda_ {m}}{d (R + 1) (1 + h \mu \| Q \|)}, \tag {9.4.36}$$

其中 $d$ 是矩阵 $P_{k}$ 的行数，该不等式的证明利用了初等不等式

$$\operatorname{tr} (P ^ {2}) \geqslant d ^ {- 1} (\operatorname{tr} P) ^ {2}, \quad \forall P \in \mathbb {R} ^ {d \times d}, P \geqslant 0$$

及 $\frac{x}{1 + x}$ 是 $x\in [0,\infty)$ 的增函数性质.

由于 $\lambda_{m} \in \left[0, \frac{h}{1 + h}\right]$ 且 $\{\lambda_{m}\} \in S^{0}$ , 故据命题9.3.1及命题9.3.2知 $\{a_{m}\} \in S^{0}$ , 即存在 $\lambda \in (0,1)$ 及 $M > 0$ 使
