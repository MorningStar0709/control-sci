It can be seen from the root-locus plot of Figure 6–25 that this system is stable only for limited ranges of the value of K—that is, $0 < K < 1 2$ and $7 3 < K < 1 5 4$ . The system becomes unstable for $1 2 < K < 7 3$ and 154<K. (If K assumes a value corresponding to unstable operation, the system may break down or may become nonlinear due to a saturation nonlinearity that may exist.) Such a system is called conditionally stable.

Root-Locus Plot of G(s) = K(s2 + 2s + 4)/[s(s + 4)(s + 6)(s2 + 1.4s + 1)]

![](image/06baef8826c76d05b3dad7ca9140ee63f9eba4545b21d8880c83191344b0330d.jpg)

<details>
<summary>line</summary>

| Real Axis | Imag Axis | K |
| --- | --- | --- |
| -6 | 0 | 12 |
| -4 | 0 | 12 |
| -2 | 0 | 12 |
| 0 | 0 | 12 |
| 0 | 2 | 154 |
| 0 | 4 | 154 |
| 0 | -2 | 12 |
| 0 | -4 | 12 |
| 0 | -5 | 12 |
| 0 | -2 | 73 |
| 0 | -1 | 73 |
| 0 | 0 | 73 |
| 0 | 1 | 73 |
| 0 | 2 | 73 |
| 0 | 3 | 73 |
| 0 | 4 | 73 |
| 0 | 5 | 73 |
</details>

Figure 6–25   
Root-locus plot of conditionally stable system.

In practice, conditionally stable systems are not desirable. Conditional stability is dangerous but does occur in certain systems—in particular, a system that has an unstable feedforward path. Such an unstable feedforward path may occur if the system has a minor loop. It is advisable to avoid such conditional stability since, if the gain drops beyond the critical value for any reason, the system becomes unstable. Note that the addition of a proper compensating network will eliminate conditional stability. [An addition of a zero will cause the root loci to bend to the left. (See Section 6–5.) Hence conditional stability may be eliminated by adding proper compensation.]

Nonminimum-Phase Systems. If all the poles and zeros of a system lie in the lefthalf s plane, then the system is called minimum phase. If a system has at least one pole or zero in the right-half s plane, then the system is called nonminimum phase. The term nonminimum phase comes from the phase-shift characteristics of such a system when subjected to sinusoidal inputs.

Consider the system shown in Figure 6–26(a). For this system

$$G (s) = \frac {K \left(1 - T _ {a} s\right)}{s (T s + 1)} \quad \left(T _ {a} > 0\right), \quad H (s) = 1$$

This is a nonminimum-phase system, since there is one zero in the right-half s plane. For this system, the angle condition becomes
