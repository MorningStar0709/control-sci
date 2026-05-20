![](image/384ba37367c4dfbedace30fc41d2c91b2fbbeeee3acbd53d7424d621b23b4b60.jpg)

This alternative formula is useful when doing the hand calculation or when computing from the frequency response of the plants since it does not need to compute the normalized coprime factorizations.

Example 17.5 Consider two plants $P _ { 1 } = 1$ and $P _ { 2 } = 1 / s$ . Then wno det $\left( 1 + P _ { 2 } ^ { \sim } P _ { 1 } \right) =$ wno $[ ( s - 1 ) / s ] = 1$ , as shown in Figure $\mathrm { 1 7 . 3 ( a ) }$ , and wno det $( 1 + P _ { 2 } ^ { \sim } P _ { 1 } ) + \eta ( P _ { 1 } ) -$ $\eta ( P _ { 2 } ) - \eta _ { 0 } ( P _ { 2 } ) = 0$ . On the other hand, wno det $( 1 + P _ { 1 } ^ { \sim } P _ { 2 } ) + \eta ( P _ { 2 } ) - \eta ( P _ { 1 } ) =$ wno $( s + 1 ) / s = 0 .$ , as shown in Figure 17.3(b).

![](image/2357f2d14c9ca965677f30866ecada1ce2e02354d44f027ba1a13adab731e136.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -5 | 7 |
| 0 | 10 |
</details>

![](image/0a85865d88669a27d1f13e103f94bf3d86a04a14a371daca3a660b65eed467f4.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 10.0 |
| 5 | 5.0 |
| 10 | 0.0 |
| 15 | -5.0 |
| 20 | -10.0 |
</details>

Figure 17.3: $\frac { s - 1 } { s }$ and s + 1 $\frac { s + 1 } { s }$ evaluated on Γ

Similar to the gap metric, it is shown by Vinnicombe [1993a, 1993b] that the ν-gap metric can also be characterized as an optimization problem (however, we shall not use it for computation).

Theorem 17.7 Let $P _ { 1 } = N _ { 1 } M _ { 1 } ^ { - 1 }$ and $P _ { 2 } = N _ { 2 } M _ { 2 } ^ { - 1 }$ be normalized right coprime factorizations. Then

$$
\begin{array}{l} \delta_ {\nu} (P _ {1}, P _ {2}) = \inf _ {Q, Q ^ {- 1} \in \mathcal {L} _ {\infty}} \left\| \left[ \begin{array}{c} M _ {1} \\ N _ {1} \end{array} \right] - \left[ \begin{array}{c} M _ {2} \\ N _ {2} \end{array} \right] Q \right\| _ {\infty}. \\ \mathrm{wno} \det (Q) = 0 \\ \end{array}
$$

Moreover, $\delta _ { g } ( P _ { 1 } , P _ { 2 } ) b _ { \mathrm { o b t } } ( P _ { 1 } ) \leq \delta _ { \nu } ( P _ { 1 } , P _ { 2 } ) \leq \delta _ { g } ( P _ { 1 } , P _ { 2 } )$ .

It is now easy to see that

$$
\begin{array}{l} \{P: \delta_ {\nu} (P _ {0}, P) <   r \} \\ \supset \left\{P = (N _ {0} + \Delta_ {N}) (M _ {0} + \Delta_ {M}) ^ {- 1}: \left[ \begin{array}{c} \Delta_ {N} \\ \Delta_ {M} \end{array} \right] \in \mathcal {H} _ {\infty}, \left\| \left[ \begin{array}{c} \Delta_ {N} \\ \Delta_ {M} \end{array} \right] \right\| _ {\infty} <   r \right\}. \\ \end{array}
$$

Define
