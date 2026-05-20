$$A B _ {\lambda} ^ {\prime} (t) x = B _ {\lambda} ^ {\prime} (t) A x, \quad \forall x \in \mathcal {D} (A).$$

于是如果 $x \in \mathcal{D}(A)$ , 则

$$B _ {\lambda} ^ {\prime} (t) (\lambda I - A) x = (\lambda I - A) B _ {\lambda} ^ {\prime} (t) x.$$

如果 $\lambda \mathrm{e}^{\lambda t}\in \rho (AT(t))$ ，则 $F_{\lambda}(t)\in \mathcal{L}(X)$ ，并且从式(5.3.40）可得

$$(\lambda I - A) B _ {\lambda} ^ {\prime} (t) F _ {\lambda} (t) ^ {- 1} x = x, \quad \forall x \in X.$$

因此，利用 $B_{\lambda}^{\prime}(t)$ 和 $F_{\lambda}(t)$ 之间（从而 $B_{\lambda}^{\prime}(t)$ 和 $F_{\lambda}(t)^{-1}$ 之间）的可交换性，我们得到

$$B _ {\lambda} ^ {\prime} (t) F _ {\lambda} (t) ^ {- 1} (\lambda I - A) x = x, \quad \forall x \in \mathcal {D} (A).$$

于是 $B_{\lambda}^{\prime}(t)F_{\lambda}(t)^{-1}$ 是 $(\lambda I - A)$ 的逆，从而 $\lambda \in \rho(A)$ . 但这不可能，因此必定有 $\lambda e^{\lambda t} \in \sigma(AT'(t))$ . 证毕.

定理5.3.18 设 $T(t)$ 是Banach空间 $X$ 上由 $A$ 生成的 $C_0$ 半群，满足 $\| T(t)\| \leqslant M\mathrm{e}^{\omega t}, t \geqslant 0$ . 假定 $T(t)$ 对于 $t > t_0$ 可微，那么存在常数 $a \in \mathbb{R}, b > 0$ 和 $C > 0$ 使得

$$\rho (A) \supset \Sigma = \left\{\lambda \in \mathbb {C} \mid \operatorname{Re} \lambda \geqslant a - b \log | \operatorname{Im} \lambda | \right\}, \tag {5.3.41}\| R (\lambda ; A) \| \leqslant C | \operatorname{Im} \lambda |, \quad \forall \lambda \in \Sigma , \operatorname{Re} \lambda \leqslant \omega . \tag {5.3.42}$$

证明 任取一固定的 $t_1 > t_0$ ，显然 $AT(t_1)$ 是有界算子。令 $\mu(t_1) = \|AT(t_1)\|$ ，从引理5.3.9得

$$\sigma (A) \subset \left\{\lambda \in \mathbb {C} \mid \lambda e ^ {\lambda t} \in \sigma (A T (t _ {1})) \right\} \subset \left\{\lambda \in \mathbb {C} \mid | \lambda e ^ {\lambda t _ {1}} | \leqslant \mu (t _ {1}) \right\}.$$

因此

$$\rho (A) \supset \left\{\lambda \in \mathbb {C} \mid \operatorname{Re} \lambda > t _ {1} ^ {- 1} \log \mu (t _ {1}) - t _ {1} ^ {- 1} \log | \operatorname{Im} \lambda | \right\}.$$

对于固定的 $\delta > 0$ ，令

$$\Sigma = \left\{\lambda \in \mathbb {C} \mid \operatorname{Re} \lambda > t _ {1} ^ {- 1} (\log (1 + \delta)) \mu (t _ {1}) - t _ {1} ^ {- 1} \log | \operatorname{Im} \lambda | \right\}.$$

显然 $\Sigma \subset \rho(A)$ , 这就证明了式 (5.3.41). 为证式 (5.3.42), 在式 (5.3.40) 中用 $R(\lambda; A)x$ 代替 $x$ , 我们得到

$$\lambda \mathrm{e} ^ {\lambda t} R (\lambda ; A) x = A T (t) R (\lambda ; A) x + T (t) x + \lambda \int_ {0} ^ {t} \mathrm{e} ^ {\lambda (t - s)} T (s) x \mathrm{d} s.$$

在上式中取 $t = t_{1}$ 和 $\lambda = \sigma +\mathrm{i}\tau \in \Sigma$ ，我们得到如下估计：
