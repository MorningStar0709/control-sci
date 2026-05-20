# C. 11 证明引理 6. 1

充分性:假设引理的条件都满足,由于 $G(s)$ 是赫尔维茨矩阵,则存在正常数 $\delta$ 和 $\mu^{*}$ ,使得对于所有 $\mu < \mu^{*}, G(s - \mu)$ 所有元素的极点的实部都小于 $-\delta$ 。要证明 $G(s)$ 是严格正实矩阵,只需证明对于所有 $\omega \in R, G(j\omega - \mu) + G^{\mathrm{T}}(-j\omega - \mu)$ 是半正定的。设 $\{A, B, C, D\}$ 是 $G(s)$ 的最小实现,则

$$
\begin{array}{l} G (s - \mu) = D + C (s I - \mu I - A) ^ {- 1} B \\ = D + C (s I - A) ^ {- 1} (s I - A) (s I - \mu I - A) ^ {- 1} B \tag {C.30} \\ = D + C (s I - A) ^ {- 1} (\mu I + s I - \mu I - A) (s I - \mu I - A) ^ {- 1} B \\ = G (s) + \mu N (s) \\ \end{array}
$$

其中 $N(s) = C(sI - A)^{-1}(sI - \mu I - A)^{-1}B$

由于 A 和 $(A + \mu I)$ 是赫尔维茨矩阵, 对 $\mu$ 一致, 所以存在 $k_{0} > 0$ , 使

$$\sigma_ {\max} [ N (j \omega) + N ^ {T} (- j \omega) ] \leqslant k _ {0}, \forall \omega \in R \tag {C.31}$$

而且 $\lim_{\omega \to \infty}\omega^2 N(j\omega)$ 存在，因此，存在 $k_{1} > 0$ 和 $\omega_{1} > 0$ ，使

$$\omega^ {2} \sigma_ {\max} [ N (j \omega) + N ^ {\mathrm{T}} (- j \omega) ] \leqslant k _ {1}, \quad \forall | \omega | \geqslant \omega_ {1} \tag {C.32}$$

如果 $G(\infty) + G^{\mathrm{T}}(\infty)$ 是正定的，则存在 $\sigma_0 > 0$ ，使

$$\sigma_ {\min} \left[ G (j \omega) + G ^ {\mathrm{T}} (- j \omega) \right] \geqslant \sigma_ {0}, \forall \omega \in R \tag {C.33}$$

由式(C.30)、式(C.31)和式(C.33)，得

$$\sigma_ {\min} \left[ G (j \omega - \mu) + G ^ {\mathrm{T}} (- j \omega - \mu) \right] \geqslant \sigma_ {0} - \mu k _ {0}, \forall \omega \in R$$

选择 $\mu < \sigma_0 / k_0$ ，保证 $G(j\omega -\mu) + G^{\mathrm{T}}(-j\omega -\mu)$ 对于所有 $\omega \in R$ 是正定的，如果 $G(\infty) + G^{\mathrm{T}}(\infty)$ 是奇异的，引理的第三个条件保证了 $G(j\omega) + G^{\mathrm{T}}(-j\omega)$ 有 $q$ 个奇异值，满足 $\lim_{\omega \to \infty}\sigma_i(\omega) > 0$ ，以及有 $p - q$ 个奇异值，满足 $\lim_{\omega \to \infty}\sigma_i(\omega) = 0$ 和 $\lim_{\omega \to \infty}\omega^2\sigma_i(\omega) > 0$ 。因此存在 $\sigma_{1} > 0,\omega_{2} > 0$ ，使

$$\omega^ {2} \sigma_ {\min} [ G (j \omega) + G ^ {\mathrm{T}} (- j \omega) ] \geqslant \sigma_ {1}, \forall | \omega | \geqslant \omega_ {2} \tag {C.34}$$

由式(C.30)、式(C.32)和式(C.34)，可得

$$\omega^ {2} \sigma_ {\min} [ G (j \omega - \mu) + G ^ {\mathrm{T}} (- j \omega - \mu) ] \geqslant \sigma_ {1} - \mu k _ {1}, \quad \forall | \omega | \geqslant \omega_ {3} \tag {C.35}$$

其中 $\omega_{3} = \max \{\omega_{1},\omega_{2}\}$ 。在紧频率区间 $[- \omega_{3},\omega_{3}]$ 上，有

$$\sigma_ {\min} \left[ G (j \omega) + G ^ {T} (- j \omega) \right] \geqslant \sigma_ {2} > 0 \tag {C.36}$$

因此，由式(C.30)、式(C.31)和式(C.36)，可得
