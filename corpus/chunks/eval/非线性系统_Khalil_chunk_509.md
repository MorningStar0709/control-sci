设 $y_{\sigma}(t)$ 是输入为 $u_{\sigma}(t)$ 时， $G(s)$ 的输出， $y_{\sigma}(t)$ 的傅里叶变换为 $Y_{\sigma}(j\omega) = G(j\omega)U_{\sigma}(j\omega) = G(j\omega)H(j\omega)Z_{\sigma}(j\omega)$ ，由帕塞瓦尔定理，得

$$
\begin{array}{l} \left\| y _ {\sigma} \right\| _ {\mathcal {L} _ {2}} ^ {2} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} Z _ {\sigma} ^ {\mathrm{T}} (- j \omega) H ^ {\mathrm{T}} (- j \omega) G ^ {\mathrm{T}} (- j \omega) G (j \omega) H (j \omega) Z _ {\sigma} (j \omega) d \omega \\ = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} H ^ {T} (- j \omega) G ^ {T} (- j \omega) G (j \omega) H (j \omega) | Z _ {\sigma} (j \omega) | ^ {2} d \omega \\ \end{array}
$$

利用 $|Z_{\sigma}(j\omega)|^{2} \geqslant \frac{1}{1 + e^{-\omega_{0}^{2}\sigma / 2}}\left(\frac{\pi\sigma}{2}\right)^{1 / 2}\left[e^{-(\omega - \omega_{0})^{2}\sigma / 2} + e^{-(\omega - \omega_{0})^{2}\sigma / 2}\right] \stackrel {\mathrm{def}}{=} \psi_{\sigma}(\omega)$

可得

$$\| y _ {\sigma} \| _ {\mathcal {L} _ {2}} ^ {2} \geqslant \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} H ^ {\mathrm{T}} (- j \omega) G ^ {\mathrm{T}} (- j \omega) G (j \omega) H (j \omega) \psi_ {\sigma} (\omega) d \omega$$

设 $\sigma$ 趋于无穷, 即可将频谱 $\psi_{\sigma}(\omega)$ 集中在频率 $\omega = \pm \omega_0$ 附近②, 因此当 $\sigma$ 趋于无穷时, 上述不等式的右边逼近

$$H ^ {\mathrm{T}} (- j \omega_ {0}) G ^ {\mathrm{T}} (- j \omega_ {0}) G (j \omega_ {0}) H (j \omega_ {0}) = \| G (j \omega_ {0}) \| _ {2} ^ {2} \geqslant (c _ {2} - \varepsilon) ^ {2}$$

因此可选择一个有限而足够大的 $\sigma$ ，使 $\| y_{\sigma} \|_{\mathcal{L}_2} \geqslant c_2 - 2\varepsilon$ 。然而这与不等式 $\| y_{\sigma} \|_{\mathcal{L}_2} \leqslant c_2 - 3\varepsilon$ 矛盾，这样就证明了 $c_1 = c_2$ 。
