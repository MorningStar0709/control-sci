$$T (t) T (s) x = T (t + s) x \rightarrow 0.$$

因此 $T(s)x\in W$ .现在证明 $T^{*}(s)x\in W$ .首先由于 $T^{*}(t)$ 是压缩的，故

$$\left\| T ^ {*} \left(t _ {2}\right) x \right\| ^ {2} = \left\| T ^ {*} \left(t _ {2} - t _ {1}\right) T ^ {*} \left(t _ {1}\right) x \right\| ^ {2} \leqslant \left\| T ^ {*} \left(t _ {1}\right) x \right\| ^ {2}, \quad \forall x \in H, \forall t _ {2} \geqslant t _ {1} \geqslant 0,$$

因此 $\| T^{*}(t)x\|^2$ 对于 $t$ 是非增且下有界的．于是 $\| T^{*}(t)x\|^2$ 当 $t\to \infty$ 时是收敛的.这样，对于任意固定的 $s\geqslant 0$

$$z (t) = \| T ^ {*} (t) x \| ^ {2} - \| T ^ {*} (t + s) x \| ^ {2} \rightarrow 0 \quad (t \rightarrow \infty).$$

另一方面，我们有

$$
\begin{array}{l} z (t) = \left(T ^ {*} (t) x, T ^ {*} (t) x\right) - \left(T (s) T ^ {*} (s) T ^ {*} (t) x, T ^ {*} (t) x\right) \\ = ([ I - T (s) T ^ {*} (s) ] T ^ {*} (t) x, T ^ {*} (t) x) \\ = \left\| [ I - T (s) T ^ {*} (s) ] ^ {\frac {1}{2}} T ^ {*} (t) x \right\| ^ {2}. \\ \end{array}
$$

由此可见， $\forall x\in H,\forall s\geqslant 0,$

$$\lim _ {t \rightarrow \infty} (I - T (s) T ^ {*} (s)) T ^ {*} (t) x = 0.$$

用 $T^{*}(s)$ 乘左端得到

$$T ^ {*} (s) [ I - T (s) T ^ {*} (s) ] T ^ {*} (t) x = [ I - T ^ {*} (s) T (s) ] T ^ {*} (t + s) x.$$

因此 $\forall x\in H,\forall s\geqslant 0,$

$$\lim _ {t \rightarrow \infty} (I - T ^ {*} (s) T (s)) T ^ {*} (t) x = 0.$$

于是 $\forall x\in H,\forall s\geqslant 0,$

$$T (t) \left[ I - T ^ {*} (s) T (s) \right] x \rightarrow 0 \quad (t \rightarrow \infty), \tag {10.3.17}T (t) [ 1 - T (s) T ^ {*} (s) ] x \rightarrow 0 \quad (t \rightarrow \infty). \tag {10.3.18}$$

现在对于任意 $x \in W$ , 由于 $T(t)x \to 0 (t \to \infty)$ , 从式 (10.3.18) 得到

$$T (t) T (s) T ^ {*} (s) x = T (t + s) T ^ {*} (s) x \rightarrow 0 (t \rightarrow \infty),$$

由此推出 $T(t)T^{*}(s)x\to 0 (t\to \infty)$ , 即 $T^{*}(s)x\in W$ . 这样我们证明了, $W$ 和 $W^{\perp}$ 对于任意 $s\geqslant 0$ 约化 $T(s)$ .

(2) 式 (10.3.17) 和式 (10.3.18) 蕴含着

$$\mathcal {R} (J (t)) \subset W, \quad \mathcal {R} (J _ {*} (t)) \subset W, \quad \forall t \geqslant 0. \tag {10.3.19}$$

由于 $J(t)$ 和 $J_{*}(t)$ 是自伴的，我们有

$$\mathcal {R} (J _ {*} (t)) ^ {\perp} = \mathcal {N} (J _ {*} (t)), \quad \mathcal {R} (J (t)) ^ {\perp} = \mathcal {N} (J (t)).$$

因此式 (10.3.19) 等价于

$$W ^ {\perp} \subset \bigcap_ {s \geqslant 0} \left[ \mathcal {N} (J (s)) \cap \mathcal {N} (J _ {*} (s)) \right] = H _ {u}.$$

(3) 设 $x \in W$ . 任意 $y \in H$ 都可以唯一地分解成 $y = y_1 + y_2$ , 其中 $y_1 \in W, y_2 \in W^\perp$ . 于是

$$(T ^ {*} (t) x, y) = (x, T (t) y _ {1}) + (x, T (t) y _ {2}).$$
