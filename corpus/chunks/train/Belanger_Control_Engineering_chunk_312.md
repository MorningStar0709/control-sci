If $Re s_{i} \gg \zeta \omega_{0}$ , the extra terms—which translate into terms $e^{-Re s_{i} t} e^{jl_{m} s_{i} t}$ in the time domain—go to zero much faster than the second-order transient, because $e^{-Re s_{i} t} \ll e^{-\zeta \omega_{0} t}$ . After a short initial period, the response is essentially that of the second-order system. In such a case, the paired complex poles near the origin are said to be dominant poles.

In classical design, we often try to achieve a closed-loop system with a pair of dominant poles. The prototype open-loop system is the one whose Root Locus is given in Figure 6.3, with two real poles. The gain is chosen so as to achieve the desired $\zeta$ for the complex closed-loop poles. In general, this idea applies to the extent that other open-loop poles are stable and that they and the open-loop zeros are much farther away from the origin than the two real poles.

![](image/acc69a3a59be029aaea1a83708ec8627c3a1df4df56da66b8241963d8767192f.jpg)

<details>
<summary>text_image</summary>

ζ = .707
45°
</details>

Figure 6.3 Root locus for a system with two real-axis poles

The reader should guard against drawing overly strong conclusions from poles alone. The zeros are important because they help determine the coefficients of the terms in the partial fraction expansion of $y(s)$ . In fact, the pole locations, taken alone, tell us only what to avoid, in general. For example, a system with poles in the hatched region in Figure 6.4 will have a response that may be (i) unstable (RHP poles), (ii) too oscillatory (pole pair with small $\zeta$ ), (iii) slow (poles with small negative real parts). Unfortunately, avoiding the “undesirable” region does not guarantee a good response. The transfer function $(13s+5)/(s+1)(s+5)$ has two well-damped poles, but its step response, shown in Figure 6.5, still has a large overshoot.
