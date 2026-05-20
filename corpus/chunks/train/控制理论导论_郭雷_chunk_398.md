定理5.3.21 设 $T(t)$ 是 $X$ 上的 $C_0$ 半群，生成算子为 $A$ ，并满足 $\| T(t) \| \leqslant M e^{\omega t}$ . 那么下列三个命题等价：

(1) A 满足假设 (H);   
(2) $T(t)$ 可微并满足式 (5.3.49);

(3) 对于任意 $\delta \in (0, \pi/2)$ , $T(t)$ 在扇形区域 $\Sigma_{\delta}$ 中有解析延拓，并且 $\mathrm{e}^{-\omega z} T(z)$ 在 $\Sigma_{\delta}$ 的每个子扇形中是有界的.

证明 同上, 我们可以假定 $\omega = 0$ . 在定理5.3.20中我们已经证明了(1) $\Longrightarrow$ (2).

(2) $\Longrightarrow$ (3). 依据假设， $T(t)$ 无穷次可微，并且从引理5.3.8得

$$T ^ {(n)} (t) = A ^ {n} T (t) = [ A T (t / n) ] ^ {n} = [ T ^ {\prime} (t / n) ] ^ {n}, \quad \forall t > 0, \forall n \geqslant 1.$$

于是从式 (5.3.49) 可得

$$\| T ^ {(n)} (t) \| \leqslant n ^ {n} M _ {2} ^ {n} t ^ {- n}, \quad \forall t > 0, \forall n \geqslant 1.$$

令 $a_{n} = (nM_{2} / t)^{n} / n!$ ，我们有

$$\frac {a _ {n + 1}}{a _ {n}} = \frac {M _ {2}}{t} \left(\frac {n + 1}{n}\right) ^ {n} \rightarrow \frac {\mathrm{e} M _ {2}}{t} \quad (n \rightarrow \infty).$$

因此级数

$$S (z) \stackrel {\text { def }} {=} \sum_ {n = 0} ^ {\infty} \frac {(z - t) ^ {n}}{n !} T ^ {(n)} (t)$$

在圆盘 $D_{t} = \{z\in \mathbb{C}\mid |z|\leqslant M_{2}kt / e\}$ 中一致收敛，这里 $k\in (0,1)$ 如果我们记 $\tan^{-1}(1 / (\mathrm{e}M_2)) = \delta$ ，则 $S(\cdot)$ 是 $\Sigma_{\delta}$ 中的解析函数．为简单起见，我们记 $T(z) = S(z)$ $z\in \Sigma_{\delta}$ 对于任意 $\delta^{\prime}\in (0,\delta)$ ，存在 $k\in (0,1)$ 使得

$$\| T (z) \| \leqslant \sum_ {n = 0} ^ {\infty} \left(\frac {\mathrm{e} M _ {2}}{t}\right) ^ {n} \left(\frac {k t}{\mathrm{e} M _ {2}}\right) ^ {n} = \frac {1}{1 - k}, \quad \forall z \in \overline {{\Sigma}} _ {\delta^ {\prime}},$$

即 $T(t)$ 在 $\overline{\Sigma_{\delta'}}$ 中一致有界. $T(z)$ 在 $\Sigma_{\delta}$ 中的半群性质由 $T(z)$ 的解析性推出.

(3) $\Longrightarrow$ (1). 根据假设, $T(z)$ 在扇形区域 $\Sigma_{\delta}$ 中解析, $\delta \in (0, \pi/2)$ . 我们知道 $A$ 的豫解式 $R(\lambda; A)$ 为

$$R (\lambda ; A) = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) \mathrm{d} t, \quad \forall \operatorname{Re} \lambda > 0. \tag {5.3.50}$$

对于 $\lambda \in \Sigma_{\delta}$ , $\operatorname{Im} \lambda \geqslant 0$ , 将式 (5.3.50) 中积分路径变到直线 $\{t e^{-3i\delta/4} \mid t \geqslant 0\} \subset \Sigma_{\delta}$ , 我们有

$$R (\lambda ; A) = \int_ {0} ^ {\infty} \exp \Big (- \lambda t e ^ {- 3 i \delta / 4} \Big) T \Big (t e ^ {- 3 i \delta / 4} \Big) e ^ {- 3 i \delta / 4} d t.$$

但 $T(z)$ 在任意子区域 $\Sigma_{\delta}$ 中一致有界，故存在 $M_3 > 0$ 使得
