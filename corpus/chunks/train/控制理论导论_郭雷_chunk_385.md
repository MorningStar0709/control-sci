(2) 设 $\mathrm{e}^{\lambda t} \in \sigma_r(T(t))$ . 首先注意, 若对于某个 $k \in \mathbb{N}$ , 有 $\lambda_k \in \sigma_p(A)$ , 则依据定理5.3.10, $\mathrm{e}^{\lambda t} \in \sigma_p(T(t))$ , 与假设 $\mathrm{e}^{\lambda t} \in \sigma_r(T(t))$ 矛盾. 由此剩下只要证明存在 $k \in \mathbb{N}$ 使得 $\lambda_{k} \in \sigma_{r}(A)$ . 为此我们仅需证明 $\{\lambda_{n}\} \subset \rho(A) \cup \sigma_{c}(A)$ 是不可能的. 事实上, 从式 (5.3.29) 我们有

$$\left(\mathrm{e} ^ {\lambda_ {n} t} I - T ^ {\prime} (t)\right) x = B _ {\lambda_ {n}} \left(\lambda_ {n} I - A\right) x, \quad \forall x \in \mathcal {D} (A), \forall n \in \mathbb {N}. \tag {5.3.32}$$

但依据假设， $\mathrm{e}^{\lambda_{n}t}=\mathrm{e}^{\lambda t}\in\sigma_{r}(T(t))$ ，故式(5.3.32)的左端属于X的某个非稠闭子空间Y．另一方面，若 $\lambda_{n}\in\rho(A)\cup\sigma_{c}(A),\forall n\in\mathbb{N},$ 则 $(\lambda_{n}I-A)$ 的值域在X中稠，从而由式(5.3.32)可知，对于所有 $n\in\mathbb{N},B_{\lambda_{n}}(t)$ 的值域包含在Y中．写出连续函数 $\mathrm{e}^{-\lambda s}T(s)x$ 的Fourier级数，我们有

$$\mathrm{e} ^ {- \lambda s} T (s) x \sim \sum_ {n = - \infty} ^ {\infty} \frac {1}{t} \mathrm{e} ^ {(2 \pi n \mathrm{i} / t) s} B _ {\lambda_ {n}} (t) x. \tag {5.3.33}$$

并且式 (5.3.33) 右端每一项均属于 $Y$ 。注意 $\mathrm{e}^{-\lambda s} T(s)x$ 在 $(0, t)$ 中可微，从而像在经典的数值情形那样，可以证明式 (5.3.33) 的级数对于任意 $0 < s < t$ 弱收敛于 $\mathrm{e}^{-\lambda s} T(s)x$ 。因此 $\mathrm{e}^{-\lambda s} T(s)x \in Y, \forall s \in (0, t)$ 。让 $s \downarrow 0$ 取极限，得到 $x \in \overline{Y}, \forall x \in \mathcal{D}(A)$ 。这不可能，因为 $\overline{Y}$ 是 $X$ 的一真子空间，并且 $\mathcal{D}(A)$ 在 $X$ 中稠。

定理5.3.12 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $A$ 为其生成算子。如果 $\lambda \in \sigma_c(A)$ ， $\lambda_n = \lambda + 2\pi ni / t \notin \sigma_p(A) \cup \sigma_r(a), \forall n \in \mathbb{N}$ ，则 $\mathrm{e}^{\lambda t} \in \sigma_c(T(t))$ 。

证明 依据定理5.3.9, 如果 $\lambda \in \sigma_c(A)$ , 则有 $\mathrm{e}^{\lambda t} \in \sigma(T(t))$ . 若 $\mathrm{e}^{\lambda t} \in \sigma_p(T(t))$ , 则从定理5.3.10可知存在 $k \in \mathbb{N}$ 使得 $\lambda_k \in \sigma_p(A)$ , 从而 $\mathrm{e}^{\lambda t} \notin \sigma_p(T(t))$ . 类似地, 若 $\mathrm{e}^{\lambda t} \in \sigma_r(T(t))$ , 则从定理5.3.11知存在一个 $k \in \mathbb{N}$ 使得 $\lambda_k \in \sigma_r(A)$ , 从而 $\mathrm{e}^{\lambda t} \notin \sigma_r(T(t))$ . 证毕

定理5.3.13 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $A$ 为其生成算子。若 $\lambda \in \sigma_p(A)$ ，则 $N_{\lambda}(A) \subset N_{\mathbf{e}^{\lambda t}}(T(t)), \forall t \geqslant 0$ ，其中
