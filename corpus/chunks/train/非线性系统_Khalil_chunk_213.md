$$
\begin{array}{l} Z (j \omega) + Z ^ {\mathrm{T}} (- j \omega) = [ I + \gamma_ {2} G (j \omega) ] [ I - \gamma_ {2} G (j \omega) ] ^ {- 1} \\ + \left[ I - \gamma_ {2} G ^ {\mathrm{T}} (- j \omega) \right] ^ {- 1} \left[ I + \gamma_ {2} G ^ {\mathrm{T}} (- j \omega) \right] \\ = \left[ I - \gamma_ {2} G ^ {\mathrm{T}} (- j \omega) \right] ^ {- 1} \left[ 2 I - 2 \gamma_ {2} ^ {2} G ^ {\mathrm{T}} (- j \omega) G (j \omega) \right] \\ \times [ I - \gamma_ {2} G (j \omega) ] ^ {- 1} \\ \end{array}
$$

因此,当且仅当 $\sigma_{\min}\left[I-\gamma_{2}^{2}G^{\mathrm{T}}(-j\omega)G(j\omega)\right]>0,\quad\forall\omega\in R$

时， $Z(j\omega) + Z^{\mathrm{T}}(-j\omega)$ 对于所有的 $\omega$ 是正定的。现在，当 $\gamma_{1}\gamma_{2} < 1$ 时有

$$
\begin{array}{l} \sigma_ {\min} \left[ I - \gamma_ {2} ^ {2} G ^ {\mathrm{T}} (- j \omega) G (j \omega) \right] \geqslant 1 - \gamma_ {2} ^ {2} \sigma_ {\max} \left[ G ^ {\mathrm{T}} (- j \omega) \right] \sigma_ {\max} [ G (j \omega) ] \\ \geqslant 1 - \gamma_ {1} ^ {2} \gamma_ {2} ^ {2} > 0 \\ \end{array}
$$

最终有 $Z(\infty) + Z^{\mathrm{T}}(\infty) = 2I$ 。因此引理6.1的全部条件都满足，我们得出以下结论：如果 $\gamma_{1}\gamma_{2} < 1$ ，则 $Z(s)$ 是严格正实的，系统是绝对稳定的。这是一个鲁棒性结论，说明用一个满足式(7.9)的非线性特性作为反馈环节，与赫尔维茨传递函数构成的闭环系统，如果 $\gamma_{2}$ 足够小，则不影响系统的稳定性③。

在 $p = 1$ 的标量情况下，定理7.1的条件可以用图解法通过检验 $G(j\omega)$ 的奈奎斯特曲线验证。当 $\psi \in [\alpha, \beta]$ ，其中 $\alpha < \beta$ 时，如果标量传递函数

$$Z (s) = \frac {1 + \beta G (s)}{1 + \alpha G (s)}$$

是严格正实的,则系统绝对稳定。为了验证 $Z(s)$ 是严格正实的,可以应用引理 6.1: 如果 $Z(s)$ 为赫尔维茨的,且

$$\mathrm{Re} \left[ \frac {1 + \beta G (j \omega)}{1 + \alpha G (j \omega)} \right] > 0, \forall \omega \in [ - \infty , \infty ] \tag {7.10}$$

则 $Z(s)$ 是严格正实的。要把条件(7.10)与 $G(j\omega)$ 的奈奎斯特曲线联系起来, 必须根据参数 $\alpha$ 的符号区分三种不同的情况。考虑第一种情况, $\beta > \alpha > 0$ 。此时, 条件(7.10)可重写为

$$
\begin{array}{l} \det G \neq 0 \Leftrightarrow \sigma_ {\min} [ G ] > 0 \\ \sigma_ {\max} [ G ^ {- 1} ] = 1 / \sigma_ {\min} [ G ], \text {   if   } \sigma_ {\min} [ G ] > 0 \\ \sigma_ {\min} [ I + G ] \geqslant 1 - \sigma_ {\max} [ G ] \\ \sigma_ {\max} \left[ G _ {1} G _ {2} \right] \leqslant \sigma_ {\max} \left[ G _ {1} \right] \sigma_ {\max} \left[ G _ {2} \right] \\ \end{array}
\mathrm{Re} \left[ \frac {\frac {1}{\beta} + G (j \omega)}{\frac {1}{\alpha} + G (j \omega)} \right] > 0, \forall \omega \in [ - \infty , \infty ] \tag {7.11}
$$
