$$
\begin{array}{l} \sum_ {i = k} ^ {t} a ^ {- 1} (i, k) = a ^ {- 1} (t, k) + \sum_ {i = k} ^ {t - 1} a ^ {- 1} (i, k) \\ \geqslant \left(1 + \frac {1}{c}\right) \sum_ {i = k} ^ {t - 1} a ^ {- 1} (i, k) \geqslant \dots \\ \geqslant \left(1 + \frac {1}{c}\right) ^ {t - k} a ^ {- 1} (k, k) \\ = \left(\frac {1 + c}{c}\right) ^ {t - k} \\ \end{array}
$$

于是，再次利用不等式 (9.3.4) 得

$$a ^ {- 1} (t, k) \geqslant \frac {1}{c} \left(\frac {1 + c}{c}\right) ^ {t - k}.$$

故

$$a (t, k) \leqslant c \left(\frac {c}{1 + c}\right) ^ {t - k}, \quad \forall t \geqslant k.$$

注意到

$$a (t, k) = \lambda_ {\max} \left\{E \left[ \Phi^ {T} (t, k) \Phi (t, k) \right] \right\},$$

因此式 (9.3.2) 是 $L_{2}$ 指数稳定的。定理证毕。

从上一定理知，为研究方程(9.3.1)的稳定性(有界性)，需要首先研究方程(9.3.2)的指数稳定性．为此引进下述定义．

定义9.3.3 若 $d \times d$ 维随机矩阵序列 $F = \{F_k\}$ 属于下列集合 $S_p$ , 则 $\{F_k\}$ 称为是 $p$ 阶稳定激励的

$$S _ {p} \stackrel {\mathrm{def}} {=} \left\{F: \| \prod_ {j = i + 1} ^ {k} (I - F _ {j}) \| _ {L _ {p}} \leqslant M \lambda^ {k - i}, \forall k \geqslant i, \forall i \geqslant 0, \right.$$

其中 $M > 0, \lambda \in [0,1)$ 是两个常数 $\Bigg\}$ ,

类似地，当 $p = 1, d = 1$ 时，对于一维非负序列 $f \stackrel{\mathrm{def}}{=} \{f_k\}$ 的集合，记为

$$S ^ {0} \stackrel {\text { def }} {=} \left\{f: f _ {k} \in [ 0, 1 ], E \prod_ {j = i + 1} ^ {k} (1 - f _ {j}) \leqslant M \lambda^ {k - i}, \quad \forall k \geqslant i, \forall i \geqslant 0, \right.$$

其中 $M > 0, \lambda \in [0,1)$ 是两个常数

下面我们说明，研究集合 $S_{p}$ 的问题在一定意义下可以转化为研究 $S^{0}$ .

考虑下列递推随机 Lyapunov 方程

$$P _ {k + 1} = (I - F _ {k}) P _ {k} (I - F _ {k}) ^ {\mathrm{T}} + Q _ {k}, \quad P _ {0} > 0, k \geqslant 0, \tag {9.3.5}$$

其中 $Q_{k}>0$ 是正定的随机矩阵序列.

定理9.3.4 设 $\{F_k\}$ 为任意 $d \times d$ 维随机矩阵序列。若由式(9.3.5)所定义的 $\{P_k\}$ 满足：

(i) $\left\{\frac{1}{1 + \|Q_k^{-1}P_{k + 1}\|}\right\} \in S^0;$

(ii) $\sup_{n\geqslant m}\| (\| P_n\| \cdot \| P_m^{-1}\|)\|_{L_p} < \infty ,p\geqslant 1,$

则有 $\{F_k\} \in S_p$ .

证明 对任何 $m \geqslant 0$ , 考虑下列方程:

$$x _ {k + 1} = (I - F _ {k}) x _ {k}, \quad k \in [ m, n - 1 ], n > m,$$

其中 $x_{m}$ 是确定性向量且满足 $\| x_m\| = 1$ ，于是

$$x _ {n} = \prod_ {i = m} ^ {n - 1} (I - F _ {i}) x _ {m}. \tag {9.3.6}$$

记 $B_{k} = I - F_{k}$ ，考虑Lyapunov函数

$$V _ {k} = x _ {k} ^ {\mathrm{T}} P _ {k} ^ {- 1} x _ {k}.$$

我们有

$$V _ {k + 1} = x _ {k + 1} ^ {\mathrm{T}} P _ {k + 1} ^ {- 1} x _ {k + 1} = x _ {k} ^ {\mathrm{T}} B _ {k} ^ {\mathrm{T}} P _ {k + 1} ^ {- 1} B _ {k} x _ {k}. \tag {9.3.7}$$

利用式 (9.3.5) 及矩阵求逆公式 (1.1.8) 得
