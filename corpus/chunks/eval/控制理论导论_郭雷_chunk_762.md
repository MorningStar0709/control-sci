$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} (y (t), P _ {\omega} y (t)) = \left(A ^ {*} y (t), P _ {\omega} y (t)\right) + \left(y (t), P _ {\omega} A ^ {*} x (t)\right) \\ + 2 \omega (P _ {\omega} y (t), y (t)) - 2 \| B ^ {*} y (t) \| ^ {2} \\ = - \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- 2 \omega s} \left(T (- s) B B ^ {*} \frac {\mathrm{d}}{\mathrm{d} s} T ^ {*} (- s) y (t), y (t)\right) \mathrm{d} s \\ - \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- 2 \omega s} (y (t), T (- s) B B ^ {*} \frac {\mathrm{d}}{\mathrm{d} s} T ^ {*} (- s) y (t)) \mathrm{d} s \\ + 2 \omega (P _ {\omega} y (t), y (t)) - 2 \| B ^ {*} y (t) \| ^ {2} \\ = - \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- 2 \omega s} \left(\frac {\mathrm{d}}{\mathrm{d} s} B ^ {*} T ^ {*} (- s) y (t), B ^ {*} T ^ {*} (- s) y (t)\right) \mathrm{d} s \\ - \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- 2 \omega s} \left(B ^ {*} T ^ {*} (- s) y (t), \frac {\mathrm{d}}{\mathrm{d} s} B ^ {*} T ^ {*} (- s) y (t)\right) \mathrm{d} s \\ + 2 \omega (P _ {\omega} y (t), y (t)) - 2 \| B ^ {*} y (t) \| ^ {2} \\ = - \int_ {0} ^ {t _ {1}} \frac {\mathrm{d}}{\mathrm{d} s} \| \mathrm{e} ^ {- \omega s} B ^ {*} T ^ {*} (- s) y (t) \| ^ {2} \mathrm{d} s - 2 \| B ^ {*} y (t) \| ^ {2} \\ = - \left\| e ^ {- \omega t _ {1}} B ^ {*} T ^ {*} (- t _ {1}) S ^ {*} (t) y _ {0} \right\| ^ {2} - \left\| B ^ {*} S ^ {*} (t) y _ {0} \right\| ^ {2}. \\ \end{array}
$$

因此根据 $\mathcal{D}(A^{*})$ 在 $H$ 中的稠密性，我们有

$$\| S ^ {*} (t) \| \leqslant M, \quad \forall t \geqslant 0,$$

其中 $M$ 为一正常数. 由于 $T^{A - BB^{*}P_{\omega}^{-1}}(t) = \mathrm{e}^{-\omega t}S(t)$ , 我们有

$$\left\| T ^ {A - B B ^ {*} P _ {\omega} ^ {- 1}} (t) \right\| \leqslant M e ^ {- \omega t}, \quad \forall t \geqslant 0.$$

证毕.

设 $X$ 和 $Y$ 是两个 Banach 空间，假定线性算子 $A$ 生成 $X$ 上的某个 $C_0$ 半群，而 $C \in \mathcal{L}(X, Y)$ 。我们说偶对 $(C, A)$ 是指数能检测的，是指存在 $S \in \mathcal{L}(Y, X)$ 使得由 $A - SC$ 生成的半群 $T^{A - SC}(t)$ 是指数稳定的。

引理10.3.1 设 $A$ 是Hilbert空间 $H$ 上 $C_0$ 半群 $T(t)$ 的生成算子， $C \in \mathcal{L}(H, Y)$ ， $B \in \mathcal{L}(U, H)$ ， $Y$ 为另一个Hilbert空间。假定 $(C, A)$ 是指数能检测的，并且存在一对称非负算子 $P \in \mathcal{L}(H)$ ，一正定算子 $R \in \mathcal{L}(U)$ ，和一有界算子 $K \in \mathcal{L}(H, U)$ ，使得

$$2 \operatorname{Re} (P (A - B K) x, x) + \left(C ^ {*} C x, x\right) + \left(K ^ {*} R K x, x\right) \leqslant 0, \quad \forall x \in \mathcal {D} (A), \tag {10.3.4}$$

那么 $T^{A - BK}(t)$ 是指数稳定的.

证明 为证引理，根据定理10.1.1，只需证明

$$\int_ {0} ^ {\infty} \| T ^ {A - B K} (t) x \| ^ {2} \mathrm{d} t < \infty , \quad \forall x \in H. \tag {10.3.5}$$

由于 $(C, A)$ 是指数能检测的，故存在 $S \in \mathcal{L}(Y, H)$ 使得 $T^{A - SC}(t)$ 是指数稳定的。因此我们可以在 $\mathcal{D}(A)$ 上作分解
