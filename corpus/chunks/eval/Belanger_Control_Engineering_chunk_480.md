◆ Property I If $S^{-1}$ exists,

$$\underline {{{{\sigma}}}} (S) = \frac {1}{\overline {{{{\sigma}}}} (S ^ {- 1})}$$

and

$$\overline {{{{\sigma}}}} (S) = \frac {1}{\underline {{{{\sigma}}}} (S ^ {- 1})}. \quad \spadesuit$$

◆ Property II $\det S = \sigma_{1}\sigma_{2} \ldots \sigma_{n}.$ ◆

◆ Property III $\overline{\sigma}(A+B)\leq\overline{\sigma}(A)+\overline{\sigma}(B).$

◆ Property IV $\overline{\sigma}(AB) \leq \overline{\sigma}(A)\overline{\sigma}(B).$ ◆

◆ Property V $\max[\overline{\sigma}(A),\overline{\sigma}(B)]\leq\overline{\sigma}([A\quad B])\leq\sqrt{2}\max[\overline{\sigma}(A),\overline{\sigma}(B)].$

From Equation 8.15, we see that $\overline{\sigma}(S)$ describes the worst-case situation for a given $\| \mathbf{d}\| _2$ . In other words, given that the squares of the magnitudes of the components of the disturbance at a frequency $\omega$ sum to $\| \mathbf{d}\| _2^2$ , the most unfavorable distribution of disturbance components will lead to $\| \mathbf{y}(j\omega)\| _2 = \overline{\sigma}(S(j\omega))\| \mathbf{d}\| _2$ . It follows that $\overline{\sigma}[S(j\omega)]$ is the key scalar quantity describing the maximum amplification of $S(j\omega)$ and plays the role that was given to $|S(j\omega)|$ in the SISO case. The same is true of the other contributions in Equations 8.4, 8.5, and 8.6. For example, the magnitude of the measurement noise contribution at $\omega$ is measured by $\overline{\sigma}[T(j\omega)]\| \mathbf{v}(j\omega)\| _2$ .

Singular values also describe the magnitude of the loop gain. In the SISO case, it was found that $S(j\omega)$ is small and $T(j\omega) \approx 1$ if $|L(j\omega)| \gg 1$ , and that $S(j\omega) \approx 1$ and $T(j\omega) \approx L(j\omega)$ if $|L(j\omega)| \ll 1$ . To arrive at a MIMO equivalent, consider

$$(I + L) \mathbf {w} = \mathbf {w} + L \mathbf {w} \tag {8.16}$$
