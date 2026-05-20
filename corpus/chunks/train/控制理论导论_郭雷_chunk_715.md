$$D _ {n} = \left\{\theta : b _ {1} \geqslant \frac {1}{\sqrt {\log (n + 1)}} \right\}, \quad n \geqslant 1.$$

证明：由 $\hat{\theta}_n^{\mathrm{T}}\phi_n = y_{n + 1}^*$ 所决定的自校正调节器具有与定理9.5.1一样的收敛速度，即 $R_{n} = O(n^{\epsilon}d_{n})$ ，a.s. $\forall \epsilon >0$

9.5.7 仍考虑上题中的系统和条件，但此时 $\hat{\theta}_k$ 由下式所定义：

$$\hat {\theta} _ {k} = \theta_ {k} + P _ {k} ^ {1 / 2} e _ {i _ {k}},$$

其中 $\theta_{k}$ 与 $P_{k}$ 由 LS 算法 (9.5.11)\~(9.5.13) 所定义，而 $\{i_{k}\}$ 是一个取值于 $\{0,1,\cdots,d\}$ 中的整数序列 $(d=p+q)$

$$i _ {k} = \underset {0 \leqslant i \leqslant d} {\operatorname{argmin}} \left| b _ {1 k} + e _ {p + 1} ^ {\mathrm{T}} P _ {k} ^ {1 / 2} e _ {i} \right|$$

其中 $e_0 = 0, e_i$ 是 $d \times d$ 维单位阵 $I$ 的第 $i$ 列。证明：由该 $\{\hat{\theta}_k\}$ 所决定的自校正调节器仍具有上题中的收敛速度。（提示：先证明 $\liminf_{k \to \infty} (\log r_{k-1}) |\hat{b}_{1k}|^2 \neq 0$ ，其中 $r_k$ 由式 (9.5.25) 所定义而 $\hat{b}_{1k}$ 是 $\hat{\theta}_k$ 中对 $b_1$ 的估计值，可参考文献 [16].）

9.5.8 在定理9.5.5的条件下，进一步假设

(i) $A(z)$ 与 $B(z)$ 互质，且 $\left|a_{p}\right| + \left|b_{q}\right|\neq 0;$

(ii) $\{y_i^*\}$ 满足持续激励条件

$$\liminf _ {n \to \infty} \lambda_ {\min} \left\{\frac {1}{n} \sum_ {i = 0} ^ {n} Y ^ {*} Y ^ {* T} \right\} \neq 0,$$

其中 $Y_{i}^{*}\stackrel{\operatorname{def}}{=}[y_{i}^{*},\cdots,y_{i-p-q+1}^{*}]^{T}$ . 证明：LS 自校正调节器 (9.5.15) 具有对数律

$$R _ {n} \sim (p + q) \sigma_ {w} ^ {2} \log n, \quad \text { a.s. }$$

且

$$\left\| \theta_ {n} - \theta \right\| ^ {2} = O \left(\frac {\log \log n}{n}\right), \quad \text { a.s. }$$

其中假定， $\sigma_w^2\stackrel {\mathrm{def}}{=}E[w_{n + 1}^2 |\mathcal{F}_n] > 0.$ （提示：可参考文献[16].）
