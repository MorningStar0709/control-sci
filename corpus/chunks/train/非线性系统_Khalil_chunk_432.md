通常,由(14.41)给出的连续型李雅普诺夫再设计,与不连续控制(14.39)一样都不能稳定原点,但它能保证解一致毕竟有界。由于最终边界 $b(\varepsilon)$ 是 $\varepsilon$ 的K类函数,因此可通过选择足够小的 $\varepsilon$ ,使 $b(\varepsilon)$ 任意小。在极限情况下,当 $\varepsilon$ 趋于零时,可恢复不连续控制器的性能。注意,从分析角度讲,并不要求 $\varepsilon$ 非常小,分析上对 $\varepsilon$ 的限制只是 $\varepsilon < 2\alpha_{3}(\alpha_{2}^{-1}(\alpha_{1}(r)))/(1-\kappa_{0})$ ,当假设全局成立且 $\alpha_{i}(i=1,2,3)$ 是 $K_{\infty}$ 类函数时,这一要求对于任意 $\varepsilon$ 都满足。当然从实践观点出发,希望 $\varepsilon$ 尽可能小,因为我们想要把系统状态限定在原点附近尽可能小的邻域内。在分析中寻求尽可能小的 $\varepsilon$ ,可当不确定项 $\delta$ 在原点为零时,得到更明显的结果。假设存在一个球 $B_{a}=\{\|x\|_{2}\leqslant a\}$ , $a\leqslant r$ ,使得对于所有 $x\in B_{a}$ 下列不等式成立:

$$\alpha_ {3} (\| x \| _ {2}) \geqslant \phi^ {2} (x) \tag {14.44}\eta (t, x) \geqslant \eta_ {0} > 0 \tag {14.45}\rho (t, x) \leqslant \rho_ {1} \phi (x) \tag {14.46}$$

其中， $\phi: R^n \to R$ 是 $x$ 的正定函数。选择 $\varepsilon < b^{-1}(a)$ ，以保证闭环系统的轨线在有限时间内限定在球 $B_a$ 内。当 $\eta(t, x) \|w\|_2 < \varepsilon$ 时，导数 $\dot{V}$ 满足

$$
\begin{array}{l} \dot {V} \leqslant - \alpha_ {3} (\| x \| _ {2}) - \frac {\eta^ {2} (1 - \kappa_ {0})}{\varepsilon} \| w \| _ {2} ^ {2} + \rho \| w \| _ {2} \\ \leqslant - \frac {1}{2} \alpha_ {3} (\| x \| _ {2}) - \frac {1}{2} \phi^ {2} (x) - \frac {\eta_ {0} ^ {2} \left(1 - \kappa_ {0}\right)}{\varepsilon} \| w \| _ {2} ^ {2} + \rho_ {1} \phi (x) \| w \| _ {2} \\ \leqslant - \frac {1}{2} \alpha_ {3} (\| x \| _ {2}) - \frac {1}{2} \left[ \begin{array}{l} \phi (x) \\ \| w \| _ {2} \end{array} \right] ^ {\mathrm{T}} \left[ \begin{array}{c c} 1 & - \rho_ {1} \\ - \rho_ {1} & 2 \eta_ {0} ^ {2} (1 - \kappa_ {0}) / \varepsilon \end{array} \right] \left[ \begin{array}{l} \phi (x) \\ \| w \| _ {2} \end{array} \right] \\ \end{array}
$$

如果 $\varepsilon < 2\eta_0^2 (1 - \kappa_0) / \rho_1^2$ ，该二次型矩阵是正定的。因此，选择 $\varepsilon < 2\eta_0^2 (1 - \kappa_0) / \rho_1^2$ ，有 $\dot{V} \leqslant -\alpha_3 (\| x \|_2) / 2$ 。又由于当 $\eta(t, x) \| w \|_2 \geqslant \varepsilon$ 时，有 $\dot{V} \leqslant -\alpha_3 (\| x \|_2) \leqslant -\alpha_3 (\| x \|_2) / 2$ ，故可推出

$$\dot {V} \leqslant - \frac {1}{2} \alpha_ {3} (\| x \| _ {2})$$

这表明原点是一致渐近稳定的。

推论14.1 假设不仅定理14.3的假设成立,不等式(14.44)到不等式(14.46)也都成立,则对于所有 $\varepsilon < \min \left\{2\eta_0^2 (1 - \kappa_0) / \rho_1^2, b^{-1}(a)\right\}$ , 闭环系统(14.38)的原点是一致渐近稳定的。如果 $\alpha_{i}(r) = k_{i}r^{c}$ , 则原点是指数稳定的。
