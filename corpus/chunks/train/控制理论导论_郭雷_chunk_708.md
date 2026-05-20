$$\left\| \varphi_ {k} \right\| ^ {2} = O \left(\alpha_ {k} \delta_ {k} \left\| \varphi_ {k} \right\| ^ {2}\right) + O \left(L _ {k} + d _ {k} + \log r _ {k}\right).$$

将式 (9.5.53) 代入此式得

$$\left\| \varphi_ {k} \right\| ^ {2} = O (\alpha_ {k} \delta_ {k} (\log^ {2} r _ {k - 1}) L _ {k}) + O (L _ {k} + d _ {k} \log^ {3} r _ {k}).$$

最后，将此式代入式(9.5.50)知存在常数 $C > 0$ 使

$$y _ {k + 1} ^ {2} \leqslant C f _ {k} L _ {k} + \xi_ {k}, \tag {9.5.55}$$

其中 $f_{k}, \xi_{k}$ 如引理叙述中所定义.

进一步，据 $L_{k}$ 的定义及式(9.5.55)有

$$L _ {k + 1} \leqslant \lambda L _ {k} + y _ {k + 1} ^ {2} \leqslant (\lambda + C f _ {k}) L _ {k} + \xi_ {k}.$$

故引理成立，证毕.

类似于引理9.5.2我们来证明：

引理9.5.4 在引理9.5.3的条件下，有

$$\left\| \varphi_ {n} \right\| ^ {2} = O (r _ {n} ^ {\epsilon} d _ {n}), \quad \text { a.s. } \quad \forall \epsilon > 0,$$

其中 $r_n$ 与 $d_n$ 分别由式 (9.5.25) 与式 (9.5.26) 定义.

证明 据引理9.5.3知

$$
\begin{array}{l} L _ {n + 1} \leqslant \lambda^ {n + 1} \left[ \prod_ {j = 0} ^ {n} \left(1 + \lambda^ {- 1} C f _ {j}\right) \right] L _ {0} \\ + \sum_ {i = 0} ^ {n} \lambda^ {n - i} \left[ \prod_ {j = i + 1} ^ {n} (1 + \lambda^ {- 1} C f _ {j}) \right] \xi_ {i}. \tag {9.5.56} \\ \end{array}
$$

下面来估计乘积 $\prod_{j = i + 1}^{n}(1 + \lambda^{-1}Cf_j)$

首先据定理9.2.1知，对任意 $\epsilon > 0$ ，存在 $\delta > 0$ 使

$$\delta \sum_ {j = 0} ^ {n} \alpha_ {j} \leqslant \epsilon (\log r _ {n}), \quad \forall n.$$

又据式 (9.5.36) 知存在充分大的 $i_0 > 0$ 使

$$\left(\frac {4}{\delta}\right) \left(\frac {C}{\lambda}\right) ^ {1 / 2} \sum_ {j = i} ^ {\infty} \delta_ {j} \leqslant \epsilon , \quad \forall i \geqslant i _ {0}, \tag {9.5.57}$$

于是利用不等式

$$(1 + x y) \leqslant (1 + x) (1 + y), \quad x \geqslant 0, y \geqslant 0$$

及

$$1 + x ^ {2} \leqslant \mathrm{e} ^ {2 x}, \quad x \geqslant 0,$$

知对 $\forall n\geqslant i\geqslant i_0,$
