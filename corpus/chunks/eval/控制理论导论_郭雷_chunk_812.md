# 温和发展算子

定义 10.6.1 设 X 是一 Banach 空间. 记 $\Delta = \{(t, s) \mid 0 \leqslant s \leqslant t < \infty\}$ ，那么 $S(\cdot, \cdot): \Delta \to \mathcal{L}(X)$ 叫做 X 上的温和发展算子，是指它满足

(1) $S(t,t) = I,\quad \forall t\geqslant 0;$   
(2) $S(t,\tau)S(\tau ,s) = S(t,s),0\leqslant s\leqslant \tau \leqslant t <   \infty ;$   
(3) $S(\cdot, s)$ 在 $[s, \infty)$ 上强连续，而 $S(t, \cdot)$ 在 $[0, t]$ 上强连续.

容易看出，对于任意固定的 $t_1 > 0$ ，从(3)我们有

$$\sup \{\| S (t, s) \| \mid 0 \leqslant s \leqslant t \leqslant t _ {1} \} < \infty .$$

如果 $T(t)$ 是 $X$ 上的 $C_0$ 半群，则显然 $T(t - s)$ 是 $X$ 上的温和发展算子.

有关温和发展算子的一般理论，读者可参阅文献 [32]. 这里我们仅考虑由 $A + B(t)$ 生成的发展算子，这里 $B(\cdot): \mathbb{R}^{+} \to \mathcal{L}(X)$ 是强连续的.

受 $C_0$ 半群中有界算子扰动启发，我们构造满足如下积分方程的温和发展算子：对于 $0 \leqslant s \leqslant t < \infty$ 和任意 $x \in X$

$$S (t, s) x = T (t - s) x + \int_ {s} ^ {t} T (t - \tau) B (\tau) S (\tau , s) x \mathrm{d} \tau . \tag {10.6.1}$$

式 (10.6.1) 中的温和发展算子 $S(t, s)$ 与算子 $A + B(t)$ 有关，它是由如下迭代格式通过极限得到的：

$$S _ {0} (t, s) x = T (t - s) x. \quad \forall x \in X, \tag {10.6.2}S _ {n} (t, s) x = \int_ {s} ^ {t} T (t - \tau) B (\tau) S _ {n - 1} (\tau , s) x \mathrm{d} \tau , \tag {10.6.3}$$

和

$$S (t, s) = \sum_ {n = 0} ^ {\infty} S _ {n} (t, s). \tag {10.6.4}$$

定理 10.6.1 设 $T(t)$ 是 Banach 空间 X 上由闭稠定线性算子生成的 $C_{0}$ 半群， $B(\cdot):\mathbb{R}^{+}\to\mathcal{L}(X)$ 是强连续的。那么由式 (10.6.2)\~(10.6.4) 构造的 $S(t,s)$ 是 X 上的温和发展算子，并且是式 (10.6.1) 的唯一解。

证明 设 $\| T(t) \| \leqslant M_1 e^{\omega t}$ , 并且对于任意固定的 $t_1 > 0$ , 记 $M_2 = \sup \{ \| B(t) \| \mid 0 \leqslant t \leqslant t_1 \}$ . 通过归纳法容易证明

$$\| S _ {n} (t, s) \| \leqslant M _ {1} ^ {n + 1} M _ {2} ^ {n} \mathrm{e} ^ {\omega t} (t - s) ^ {n} / n!, \quad \forall 0 \leqslant s \leqslant t \leqslant t _ {1}, \forall n \geqslant 0.$$

因此式 (10.6.4) 中的级数在 $0 \leqslant s \leqslant t \leqslant t_1$ 中按一致算子拓扑收敛。现在我们证明由式 (10.6.4) 定义的 $S(t, s)$ 是 $X$ 上一温和发展算子。事实上，性质 (1) 是显然的。为证性质 (2)，对于 $0 \leqslant s \leqslant \tau \leqslant t \leqslant t_1$ 和 $x \in X$ ，从式 (10.6.1) 我们得到

$$
\begin{array}{l} S (t, \tau) S (\tau , s) x - S (t, s) x = T (t - \tau) S (\tau , s) x - S (t, s) x \\ + \int_ {\tau} ^ {t} T (t - \xi) B (\xi) S (\xi , \tau) S (\tau , s) x d \xi \\ = \int_ {\tau} ^ {t} T (t - \xi) B (\xi) S (\xi , \tau) S (\tau , s) x d \xi - \int_ {\tau} ^ {t} T (t - \xi) B (\xi) S (\xi , s) x d \xi \\ = \int_ {\tau} ^ {t} T (t - \xi) B (\xi) [ S (\xi , \tau) S (\tau , s) - S (\xi , s) ] x d \xi . \\ \end{array}
$$

若令 $f(t) \stackrel{\mathrm{def}}{=} \mathrm{e}^{\omega t} \| S(t, \tau) S(\tau, s) x - S(t, s) x \|$ ，则从上式可得

$$f (t) \leqslant M _ {1} M _ {2} \int_ {\tau} ^ {t} f (\xi) \mathrm{d} \xi .$$
