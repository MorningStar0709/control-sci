# Nonminimum-Phase Systems

When the system is nonminimum phase, it is not possible to place some of the closed-loop poles at the zeros of the B polynomial. It can be shown that the optimal controller minimizing Eq. (4.3) with $\rho = 0$ gives the following closed-loop characteristic equation:

$$q ^ {d _ {0} \dots 1} B ^ {\dagger} (q) B ^ {*} (q) C (q) = 0$$

that is, the process zeros outside the unit disc, $B^{-}(q)$ , are replaced by the zeros defined by the reciprocal polynomial, $B^{-*}(q)$ . See Åström and Wittenmark (1990) in the references at the end of the chapter. The controller

$$u (t) = - \frac {S}{R} y (t)$$

is now obtained from the Diophantine equation

$$q ^ {d _ {0} - 1} B ^ {+} B ^ {- *} C = A R + B S \tag {4.17}$$

Compare Eq. (4.16).
