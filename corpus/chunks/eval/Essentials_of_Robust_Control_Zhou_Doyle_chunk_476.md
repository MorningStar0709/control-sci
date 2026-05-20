# 17.5 Controller Order Reduction

The controller order-reduction procedure described in Chapter 15 can, of course, be applied to the loop-shaping controller design in Chapter 16 and the gap or ν-gap metric optimization here. However, the controller order-reduction in the loop-shaping controller design, or gap metric, or ν-gap metric optimization is especially simple. The following theorem follows immediately from Theorems 17.7 and 17.10.

Theorem 17.11 Let $P _ { 0 }$ be a nominal plant and $K _ { 0 }$ be a stabilizing controller such that $b _ { P _ { 0 } , K _ { 0 } } \leq b _ { \mathrm { o b t } } ( P _ { 0 } )$ . Let $K _ { 0 } = U V ^ { - 1 }$ be a normalized coprime factorization and let $\hat { U } , \hat { V } \in \mathcal { R } \mathcal { H } _ { \infty }$ be such that

$$
\left\| \left[ \begin{array}{c} U \\ V \end{array} \right] - \left[ \begin{array}{c} \hat {U} \\ \hat {V} \end{array} \right] \right\| _ {\infty} \leq \varepsilon .
$$

Then $K : = \hat { U } \hat { V } ^ { - 1 }$ stabilizes P0 $i f \varepsilon < b _ { P _ { 0 } , K _ { 0 } }$ . Furthermore,

$$\arcsin b _ {P, K} \geq \arcsin b _ {P _ {0}, K _ {0}} - \arcsin \varepsilon - \arcsin \beta$$

for all $\{ P : \delta _ { \nu } ( P , P _ { 0 } ) \leq \beta \}$ .

Hence to reduce the controller order one only needs to approximate the normalized coprime factors of the controller. An algorithm for finding the best approximation is also presented in Vinnicombe [1993a, 1993b].
