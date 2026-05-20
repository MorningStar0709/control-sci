# 紧算子半群

在实际应用中，一类重要的 $C_0$ 半群就是所谓的紧半群类.

定义5.3.4 Banach空间 $X$ 上的 $C_0$ 半群 $T(t)$ 称为对 $t > t_0$ 是紧的，是指对于任意 $t > t_0, T(t)$ 是 $X$ 上紧算子； $T(t)$ 称为紧半群，是指 $T(t)$ 对于任意 $t > 0$ 是紧算子.

定理5.3.14 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群．如果 $T(t)$ 对于 $t > t_0$ 是紧的，则 $T(t)$ 对于 $t > t_0$ 是按算子拓扑连续的.

证明 根据定理 5.3.1, 存在常数 $M > 0$ 使得 $\|T(s)\| \leqslant M, \forall s \in [0,1]$ . 对于 $t > t_0$ , $U(t) = \{T(t)x \mid \|x\| \leqslant 1\}$ 是 $X$ 中的紧子集. 于是对于任意给定的 $\varepsilon > 0$ , 存在 $x_1, \cdots, x_N \in X$ 使得 $U(t) \subset \bigcup_{k=1}^{N} B(T(t)x_k; \varepsilon/2(M+1))$ , 其中 $B(x;r)$ 表示 $X$ 中以 $x$ 为中心半径 $r$ 的开球. 利用 $T(t)$ 的强连续性, 存在常数 $h_0, 0 < h \leqslant 1$ 使得

$$\| T (t + h) x _ {k} - T (t) x _ {k} \| < \varepsilon / 2, \quad 1 \leqslant k \leqslant N, 0 \leqslant h \leqslant h _ {0}.$$

设 $x \in \bar{B}(0;1)$ 且 $0 \leqslant h \leqslant h_0$ , 则存在元 $x_k, 1 \leqslant k \leqslant N$ , 使得 $\|T(t)x - T(t)x_k\| < \varepsilon / 2(M + 1)$ . 因此我们有

$$
\begin{array}{l} \| T (t + h) x - T (t) x \| \leqslant \| T ^ {\prime} (h) \| \| T (t) x - T (t) x _ {k} \| + \\ + \| T (t + h) x _ {k} - T (t) x _ {k} \| + \| T (t) x _ {k} - T (t) x \| <   \varepsilon , \\ \end{array}
$$

这表明对于 $t > t_0, T(t)$ 按一致算子拓扑是连续的. 证毕.

定理5.3.15 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $A$ 为其生成算子，则 $T(t)$ 是紧半群当且仅当 $T(t)$ 对于 $t > 0$ 按一致算子拓扑连续，并且 $A$ 有紧豫解式.

证明 首先假定 $T(t)$ 是紧半群，于是根据定理5.3.14, $T(t)$ 对于 $t > 0$ 按一致算子拓扑是连续的。设 $\| T(t)\| \leqslant Me^{\omega t},\forall t\geqslant 0,$ 我们有

$$R (\lambda ; A) = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) \mathrm{d} t, \qquad \mathrm{Re} \lambda > \omega , \tag {5.3.34}$$

其中积分是按一致算子拓扑收敛的．设 $\varepsilon > 0, \operatorname{Re} \lambda > \omega$ ，则

$$R _ {\varepsilon} (\lambda) = \int_ {\varepsilon} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) \mathrm{d} t$$

是紧算子．但

$$\| R (\lambda ; A) - R _ {\varepsilon} (\lambda) \| \leqslant \int_ {0} ^ {\varepsilon} \mathrm{e} ^ {- \operatorname{Re} \lambda t} \| T (t) \| \mathrm{d} t \leqslant M \varepsilon ,$$

故 $R(\lambda; A)$ 是紧算子.

现在假定 $A$ 有紧豫解式，并且 $T(t)$ 对于 $t > 0$ 按一致算子拓扑是连续的。于是式(5.3.34)成立，并且

$$\lambda R (\lambda ; A) T (t) - T (t) = \lambda \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda s} (T (t + s) - T (t)) \mathrm{d} s.$$

设 $\lambda > \max \{0, \omega\}$ , 则对于任意 $\delta > 0$ , 我们有
