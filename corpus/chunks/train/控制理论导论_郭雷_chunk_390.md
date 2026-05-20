# 可微半群

定义5.3.5 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $T(t)$ 称为在 $t_0 \geqslant 0$ 处可微，是指 $T(t)$ 在 $t_0$ 处按一致算子拓扑（即在 $\mathcal{L}(X)$ 中）可微。 $T(t)$ 称为可微，是指它对于任意 $t > 0$ 是可微的。

注5.3.2 如果 $T(t)$ 对于任意 $t \geqslant 0$ 是可微的，则 $\mathcal{D}(A) = X$ ，其中 $A$ 是 $T(t)$ 的生成算子，因此 $A \in \mathcal{L}(X)$ . 此外，当 $T(t)$ 在 $t_0$ 可微时， $T(t)$ 对于任意 $t \geqslant t_0$ 也可微。今后我们用 $T'(t_0)$ 表示 $T(t)$ 在 $t_0$ 处按一致算子拓扑的微商。

引理5.3.7 设 $T(t)$ 是Banach空间 $X$ 上由 $A$ 生成的 $C_0$ 半群．假定 $T(t)$ 对于 $t > t_0$ 可微，则有

(1) $T'(t) = AT(t), \forall t > t_0; \quad T'(t) = T'(t_1)T(t - t_1), \forall t > t_1 > t_0;$   
(2) $T(t)x\in \mathcal{D}(A),\forall x\in X,t > t_0;$   
(3) 当 $t > nt_0$ ( $n \in \mathbb{N}$ ) 时, $T(t)$ 是 $n$ 次可微的, 并且

$$T ^ {(n)} (t) = A ^ {n} T (t), \quad \forall t > n t _ {0}.$$

证明 (1) 和 (2) 是显然的. 今证 (3). 我们只需考虑 $n = 2$ 的情形, $n > 2$ 的情形可以用关于 $n$ 的归纳法证明. 对于任意 $t > 2t_0$ , 我们有

$$
\begin{array}{l} \lim _ {h \rightarrow 0} \frac {1}{h} \left(T ^ {\prime} (t + h) - T ^ {\prime} (t)\right) = \lim _ {h \rightarrow 0} A T (t / 2) \frac {1}{h} \left(T (t / 2 + h) - T (t / 2)\right) \\ = A T (t / 2) T ^ {\prime} (t / 2) = A ^ {2} T (t), \\ \end{array}
$$

这里我们已经利用了 $AT(t / 2)$ 的有界性. 证毕.

推论5.3.2 设 $T(t)$ 是Banach空间 $X$ 上的可微 $C_0$ 半群，那么 $T(t)$ 对于任意 $t > 0$ 在 $\mathcal{L}(X)$ 中无穷次可微.

引理5.3.8 设 $T(t)$ 是Banach空间 $X$ 上的可微 $C_0$ 半群，那么

$$T ^ {(n)} (t) = (A T (t / n)) ^ {n} = (T ^ {\prime} (t / n)) ^ {n}, \quad \forall n \geqslant 1. \tag {5.3.39}$$

证明 我们用关于 $n$ 的归纳法来证明。对于 $n = 1$ ，结论从引理5.3.7推出。假定式(5.3.39)对于 $n$ 成立，则当 $t \geqslant s$ 时我们有

$$T ^ {(n)} (t) = (A T (t / n)) ^ {n} - T (t - s) (A T (s / n)) ^ {n}.$$

对上式相对于 $t$ 微商得到

$$T ^ {(n + 1)} (t) = A T (t - s) (A T (s / n)) ^ {n}.$$

在上式中取 $s = nt / (n + 1)$ ，即得对应 $n + 1$ 的结论。证毕

为了刻画对于 $t > t_0$ 可微的 $C_0$ 半群生成算子的特性，我们还须要一个引理.

引理5.3.9 设 $T(t)$ 是Banach空间 $X$ 上由 $A$ 生成的 $C_0$ 半群. 如果 $T(t)$ 对于 $t > t_0$ 可微, 并且 $\lambda \in \sigma(A)$ , 那么 $\lambda e^{\lambda t} \in \sigma(AT(t))$ .

证明 设 $B_{\lambda}(t)$ 由式 (5.3.27) 定义. 对于固定的 $x \in X$ , 显然 $B_{\lambda}(t)x$ 相对 $t$ 是可微的, 并且

$$\frac {\mathrm{d}}{\mathrm{d} t} B _ {\lambda} (t) x = T (t) x + \lambda B _ {\lambda} (t) x \stackrel {\text { def }} {=} B _ {\lambda} ^ {\prime} (t) x.$$

注意 $B_{\lambda}^{\prime}(t) \in \mathcal{L}(X)$ . 现在对于 $t > t_0$ , 相对 $t$ 微商 (5.3.28), 我们得到

$$\lambda \mathrm{e} ^ {\lambda t} x - A T (t) x = (\lambda I - A) B _ {\lambda} ^ {\prime} (t) x, \quad \forall x \in X. \tag {5.3.40}$$

记 $F_{\lambda}(t)x = \lambda \mathrm{e}^{\lambda t}x - AT(t)x$ 。对于 $t > 0$ ，显然 $F_{\lambda}(t) \in \mathcal{L}(X)$ ， $B_{\lambda}'(t)$ 和 $F_{\lambda}(t)$ 可交换，并且
