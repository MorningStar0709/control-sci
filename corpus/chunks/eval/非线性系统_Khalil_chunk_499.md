因而 $\int_0^\infty G(u(t))dt\leqslant \int_0^{t_1}G(g(t))dt + \int_{t_1}^\infty \frac{e^{-t}}{h(0)} dt\leqslant k_1$

所以,引理中第一个积分也是有界的。引理证毕。

为了证明定理 4.16, 设

$$V (t, x) = \int_ {t} ^ {\infty} G (\| \phi (\tau ; t, x) \| _ {2}) d \tau$$

其中 $\phi (\tau ;t,x)$ 是始于 $(t,x)$ 的解， $G$ 是用引理C.1选择的K类函数。为了理解如何选择 $G$ ，我们首先检验

$$\frac {\partial V}{\partial x} = \int_ {t} ^ {\infty} G ^ {\prime} (\| \phi \| _ {2}) \frac {\phi^ {\mathrm{T}}}{\| \phi \| _ {2}} \phi_ {x} d \tau$$

的上界。在定理4.14的证明中看到，假设 $\| \partial f / \partial x\| _2\leqslant L$ ，对 $t$ 一致，说明 $\| \phi_x(\tau ;t,x)\| _2\leqslant$ $\exp [L(\tau -t)]$ ，因此

$$\left\| \frac {\partial V}{\partial x} \right\| _ {2} \leqslant \int_ {t} ^ {\infty} G ^ {\prime} (\| \phi (\tau ; t, x) \| _ {2}) \exp [ L (\tau - t) ] d \tau\leqslant \int_ {t} ^ {\infty} G ^ {\prime} (\beta (\| x \| _ {2}, \tau - t)) \exp [ L (\tau - t) ] d \tau\leqslant \int_ {0} ^ {\infty} G ^ {\prime} (\beta (\| x \| _ {2}, s)) \exp (L s) d s$$

以 $\beta (r_0,s)$ 和 $\exp (Ls)$ 作为引理C.1中的函数 $g$ 和 $h$ ，根据引理把 $G$ 作为K类函数。因此对于所有 $\| x\| _2\leqslant r_0$ ，积分

$$\int_ {0} ^ {\infty} G ^ {\prime} (\beta (\| x \| _ {2}, s)) \exp (L s) d s \stackrel {\text { def }} {=} \alpha_ {4} (\| x \| _ {2})$$

有界,对 x 一致,而且是关于 $\|x\|_{2}$ 的连续严格递增函数,因为对于每个固定的 $s,\beta(\|x\|_{2},s)$ 是关于 $\|x\|_{2}$ 的 K 类函数,因此 $\alpha_{4}$ 是 K 类函数,这就证明了定理中的最后一个不等式。现在考虑

$$V (t, x) = \int_ {t} ^ {\infty} G (\| \phi (\tau ; t, x) \| _ {2}) d \tau\leqslant \int_ {t} ^ {\infty} G (\beta (\| x \| _ {2}, \tau - t)) d \tau = \int_ {0} ^ {\infty} G (\beta (\| x \| _ {2}, s)) d s \stackrel {\text {def}} {=} \alpha_ {2} (\| x \| _ {2})$$

根据引理C.1,对于所有 $\| x\| _2\leqslant r_0$ 最后一个积分是有界的。函数 $\alpha_{2}$ 是K类函数，回顾定理4.14的证明，假设 $\| \partial f / \partial x\| _2\leqslant L$ ，对 $t$ 一致，说明 $\| \phi (\tau ;t,x)\| _2\geqslant \| x\| _2\exp [ - L(\tau -t)]$ 。因此

$$V (t, x) \geqslant \int_ {t} ^ {\infty} G (\| x \| _ {2} e ^ {- L (\tau - t)}) d \tau = \int_ {0} ^ {\infty} G (\| x \| _ {2} e ^ {- L s}) d s\geqslant \int_ {0} ^ {(\ln 2) / L} G \left(\frac {1}{2} \| x \| _ {2}\right) d s = \frac {\ln 2}{L} G \left(\frac {1}{2} \| x \| _ {2}\right) \stackrel {\text {def}} {=} \alpha_ {1} (\| x \| _ {2})$$

显然， $\alpha_{1}(\| x \|_{2})$ 是 $\mathcal{K}$ 类函数，因此对于所有 $\| x \|_{2} \leqslant r_{0}, V$ 满足不等式

$$\alpha_ {1} (\| x \| _ {2}) \leqslant V (t, x) \leqslant \alpha_ {2} (\| x \| _ {2})$$

最后，V 沿系统轨线的导数由下式给出：
