# 线性算子半群的定义和基本性质

上述分析启发我们引入如下线性算子半群的定义：

定义5.3.1 设 $X$ 是一Banach空间．从 $X$ 到 $X$ 的一单参数有界线性算子族 $T(t),0\leqslant t < \infty$ ，称为 $X$ 上的一强连续线性算子半群，或简称 $X$ 上的 $C_0$ 半群，是指它满足

(1) $T(0) = I$ ( $I$ 为 $X$ 上的恒等算子);  
(2) $T(t + s) = T(t)T(s), \forall t, s \geqslant 0$ (半群性质):   
(3) $\lim_{t\downarrow 0}\| T(t)x - x\| = 0,\forall x\in X$ (强连续性).

此外，若 $T(t)$ 还满足

(4) $\| T(t)\| \leqslant 1, \forall t\geqslant 0,$

则 $T(t)$ 称为 $X$ 上的 $C_0$ 压缩半群.

$X$ 上的一 $C_0$ 半群 $T(t)$ 称为一致连续的，是指 $T(t)$ 相对于 $t \geqslant 0$ 按 $\mathcal{L}(X)$ 中范数，即按一致算子拓扑是连续的.

例5.3.1 设 $A \in \mathcal{L}(X)$ , 其中 $\mathcal{L}(X)$ 为 $X$ 中有界线性算子全体构成的Banach空间, 则

$$T (t) = \mathrm{e} ^ {A t} = \sum_ {k = 0} ^ {\infty} (t A) ^ {k} / k!, \qquad t \geqslant 0$$

是 $X$ 上的 $C_0$ 半群，而且是一致连续的，即

$$\lim _ {t \rightarrow 0} \| T (t) - I \| = 0.$$

例5.3.2 设 $C[0, \infty]$ 表示 $[0, \infty]$ 上连续函数全体按上确界范数构成的Banach空间．定义 $T(t)$ 为

$$\big (T (t) x \big) (s) = x (t + s), \quad t, s \geqslant 0, x \in C [ 0, \infty ].$$

那么 $T(t)$ 是 $C[0, \infty]$ 上的 $C_0$ 压缩半群.

例5.3.3 设 $p \geqslant 1$ , 在 $L^p(0, \infty)$ 中定义 $T(t)$ 为

$$\big (T (t) x \big) (s) = x (t + s), \quad \forall t, s \geqslant 0, x \in L ^ {p} (0, \infty).$$

那么 $T(t)$ 是 $L^p (0,\infty)$ 上的 $C_0$ 压缩半群.

例5.3.4 在 $L^1 (-\infty ,\infty)$ 中定义 $T(t)$

$$\big (T (t) x \big) (s) = \frac {1}{\sqrt {\pi t}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- (s - \sigma) ^ {2} / t} x (\sigma) \mathrm{d} \sigma , \quad t > 0, s \in \mathbb {R}.$$

那么 $T(t)$ 也是 $L^1 (-\infty ,\infty)$ 上的 $C_0$ 压缩半群．事实上，根据Fubini定理，对于 $x\in L^{1}(-\infty ,\infty)$ 和 $t > 0$ ，我们有

$$
\begin{array}{l} \| T (t) x \| \leqslant \int_ {- \infty} ^ {\infty} d s \int_ {- \infty} ^ {\infty} \frac {1}{\sqrt {\pi t}} e ^ {- (s - \sigma) ^ {2} / t} | x (\sigma) | d \sigma \\ = \int_ {- \infty} ^ {\infty} | x (\sigma) | \mathrm{d} \sigma \int_ {- \infty} ^ {\infty} \frac {1}{\sqrt {\pi t}} \mathrm{e} ^ {- (s - \sigma) ^ {2} / t} \mathrm{d} s \\ = \int_ {- \infty} ^ {\infty} | x (\sigma) | \mathrm{d} \sigma = \| x \|, \\ \end{array}
$$

这表明 $T(\cdot)x \in L^{1}(-\infty, \infty)$ , 并且 $\| T(t) \| \leqslant 1$ .

现在我们验证 $T(t)$ 的 $C_0$ 半群条件．对于 $x \in L^{1}(-\infty, \infty), t, \tau > 0,$ 和 $s \in \mathbb{R}$ ，我们有
