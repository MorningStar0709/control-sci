$$
\begin{array}{l} \left\| G _ {1} (\cdot) G _ {2} (\cdot) \right\| _ {\infty} = \sup _ {u \neq 0} \frac {\left\| G _ {1} (\cdot) G _ {2} (\cdot) u \right\| _ {2}}{\left\| u \right\| _ {2}} \\ = \sup _ {u \neq 0} \frac {\left\| G _ {1} (\cdot) y \right\| _ {2}}{\left\| y \right\| _ {2}} \cdot \frac {\left\| G _ {2} (\cdot) u \right\| _ {2}}{\left\| u \right\| _ {2}} \\ \leqslant \| G _ {1} (\cdot) \| _ {\infty} \sup _ {u \neq 0} \frac {\| G _ {2} (\cdot) u \| _ {2}}{\| u \| _ {2}} = \| G _ {1} (\cdot) \| _ {\infty} \| G _ {2} (\cdot) \| _ {\infty}. \\ \end{array}
$$

引理6.1.3 设 $G(\cdot) \in RH_{\infty}^{n \times m}$ , 且 $W(\cdot) \in RH_{\infty}$ 为可逆元. 若

$$\| G (\cdot) W (\cdot) \| _ {\infty} \leqslant 1, \tag {6.1.9}$$

则

$$\bar {\sigma} \{G (\mathrm{j} \omega) \} \leqslant | W ^ {- 1} (\mathrm{j} \omega) |, \quad \forall \omega \in \mathbb {R}. \tag {6.1.10}$$

证明 因为 $W(s)$ 为标量函数，故

$$\sigma \{G (\mathrm{j} \omega) W (\mathrm{j} \omega) \} - | W (\mathrm{j} \omega) | \sigma \{G (\mathrm{j} \omega) \}.$$

再根据式 (6.1.9), 有

$$\bar {\sigma} \{G (\mathrm{j} \omega) W (\mathrm{j} \omega) \} = | W (\mathrm{j} \omega) | \bar {\sigma} \{G (\mathrm{j} \omega) \} \leqslant 1, \quad \forall \omega \in \mathbb {R}.$$

因此式 (6.1.10) 得证.

注6.1.1 如果我们将信号的 $L_{2}$ 范数解释为该信号所具有的能量，那么由引理6.1.1可知， $H_{\infty}$ 范数表达了该系统在传递信号的过程中，输出与输入信号的能量增益的最大值。因此我们可以通过抑制系统的 $H_{\infty}$ 范数来达到抑制系统对输入信号的响应的目的。 $H_{\infty}$ 干扰抑制 (Disturbance Attenuation[8]) 以及 $H_{\infty}$ 干扰近似解耦 (Almost Disturbance Decoupling[13]) 等控制方法就是利用了 $H_{\infty}$ 范数的这一特性。

注6.1.2 考察由已知环节 $G(\cdot) \in RH_{\infty}^{m \times r}$ 和未知环节 $\Delta(\cdot) \in RH_{\infty}^{r \times m}$ 构成的如图6.1.1所示的反馈系统。根据小增益定理（参见文献[3])可知，若该系统的开环传递函数满足 $\| G(\cdot)\Delta(\cdot)\|_{\infty} < 1$ ，则系统是稳定的。因此，如果未知环节 $\Delta(s)$ 的幅频特性的界函数已知，即存在有理函数 $R(s)$ 使得 $\bar{\sigma}\{\Delta(j\omega)\} \leqslant |R(j\omega)|, \forall \omega \in \mathbb{R}$ ，且

$$\left\| G (\cdot) R (\cdot) \right\| _ {\infty} < 1,$$

那么由于 $R$ 是标量函数，有 $\| G(\cdot)R(\cdot)\|_{\infty} = \| G(\cdot)\|_{\infty}\| R(\cdot)\|_{\infty}$ ，且根据引理6.1.2有

$$\| G (\cdot) \Delta (\cdot) \| _ {\infty} \leqslant \| G (\cdot) \| _ {\infty} \| \Delta (\cdot) \| _ {\infty} \leqslant \| G (\cdot) \| _ {\infty} \| R (\cdot) \| _ {\infty} < 1, \tag {6.1.11}$$

所以该系统对于任意 $\Delta(s) (\bar{\sigma} \{\Delta(j\omega)\} \leqslant |R(j\omega)|)$ 是鲁棒稳定的.
