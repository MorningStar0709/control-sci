(1) $\operatorname{Re}\langle F\varphi, \varphi \rangle \leqslant 0, \quad \forall \varphi \in H;$   
(2) $\lim_{k\to \infty}\operatorname{Re}\langle F\varphi_k,\varphi_k\rangle = 0\Longrightarrow \lim_{k\to \infty}\| F\varphi_k\| = 0.$

如果 $T(t)$ 是指数稳定的，则由 $A + F$ 生成的 $C_0$ 半群也是指数稳定的.

证明 由于 $F$ 是有界且耗散的, 故 $A + F$ 生成 $H$ 上 $C_0$ 压缩半群. 于是依据定理10.1.6, 为了由 $A + F$ 生成的 $C_0$ 半群是指数稳定的, 我们只需证明 $\mathbb{R} \subset \rho(A + F)$ , 并且

$$\sup \left\{\| R (\mathrm{i} \omega ; A + F) \| \mid \omega \in \mathbb {R} \right\} < \infty .$$

首先证明 $\mathbb{R} \subset \rho(A + F)$ . 若不然, 则存在 $\omega \in \mathbb{R}$ 使得 $\mathrm{i}\omega \in \sigma(A + F)$ . 如果 $\mathrm{i}\omega \in \sigma_p(A + F) \cup \sigma_c(A + F)$ , 则存在序列 $\{\varphi_n\} \subset \mathcal{D}(A)$ 满足 $\|\varphi_k\| = 1$ 和

$$\lim _ {k \rightarrow \infty} \| (A + F) \varphi_ {k} - \mathrm{i} \omega \varphi_ {k} \| = 0.$$

于是

$$\lim _ {k \rightarrow \infty} \operatorname{Re} \left\langle (A + F) \varphi_ {k}, \varphi_ {k} \right\rangle = 0.$$

由于 $A$ 和 $F$ 都是耗散的，故上式意味着 $\lim_{k\to \infty}\mathrm{Re}\langle F\varphi_k,\varphi_k\rangle = 0.$ 因此依据假设(2)，我们有 $\lim_{k\to \infty}\| F\varphi_k\| = 0.$ 这样我们得到

$$\lim _ {k \rightarrow \infty} \| A \varphi_ {k} - \mathrm{i} \omega \varphi_ {k} \| = 0,$$

这表明 $\mathbf{i}\omega \in \sigma(A)$ , 与 $T(t)$ 的指数稳定性相矛盾.

现在如果 $\mathrm{i}\omega \in \sigma_r(A + F)$ , 则依定理5.1.11, $-\mathrm{i}\omega \in \sigma_p(A^* + F^*)$ . 但 $A^* + F^*$ 生成 $H$ 中 $C_0$ 半群 $T^*(t)$ , 并且 $\| T^*(t) \| = \| T(t) \|$ , 这又与 $T(t)$ 的指数稳定性相矛盾. 于是我们证明了 $\mathbb{R} \subset \rho(A + F)$ .

现在我们证明 $\sup \left\{\| R(\mathrm{i}\omega; A + F) \| \mid \omega \in \mathbb{R}\right\} < \infty$ 。事实上，如果不然，则存在两个序列 $\{\omega_k\} \subset \mathbb{R}$ 和 $\{\varphi_k\} \subset \mathcal{D}(A)$ ，满足 $\|\varphi_k\| = 1, \forall k \geqslant 1$ ，和 $\lim_{k \to \infty} \| \mathrm{i}\omega_k\varphi_k - (A +$

$F)\varphi_{k}\| = 0.$ 于是

$$\lim _ {k \rightarrow \infty} \left(\mathrm{i} \omega_ {k} \| \varphi_ {k} \| ^ {2} - \langle (A + F) \varphi_ {k}, \varphi_ {k} \rangle\right) = 0.$$

由此可见

$$\lim _ {k \rightarrow \infty} \left(\operatorname{Re} \langle A \varphi_ {k}, \varphi_ {k} \rangle + \operatorname{Re} \langle F \varphi_ {k}, \varphi_ {k} \rangle\right) = 0.$$

但 $A$ 和 $F$ 都是耗散的，故 $\lim_{k\to \infty}\mathrm{Re}\langle F\varphi_k,\varphi_k\rangle = 0.$ 根据假定(2)， $\lim_{k\to \infty}\| F\varphi_k\| = 0,$ 从而
