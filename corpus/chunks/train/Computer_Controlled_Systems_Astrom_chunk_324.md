# Example 5.10 Influence of the observer polynomial 2

Consider the same system and the same desired closed-loop response as in Example 5.9. Let the observer polynomial be

$$A _ {o} (z) = z - a$$

The Diophantine equation (5.4) becomes

$$(z - 1) (z + r _ {1}) + 0. 1 (s _ {0} z + s _ {1}) = (z - a) (z - 0. 8)$$

Hence the following conditions are obtained.

$$
\begin{array}{l} - 1 + r _ {1} + 0. 1 s _ {0} = - a - 0. 8 \\ - r _ {1} + 0. 1 s _ {1} = 0. 8 a \\ \end{array}
$$

Because there are two linear equations and three unknowns, one extra condition may be introduced. Choose $r_{1} = -1$ to obtain integral action. This gives

$$
\begin{array}{l} s _ {0} = 1 2 - 1 0 a \\ s _ {1} = 8 a - 1 0 \\ \end{array}
$$

The following expression is obtained for the process output.

$$X (z) = \frac {0 . 2}{z - 0 . 8} U _ {c} (z) + \frac {0 . 1 (z - 1)}{(z - a) (z - 0 . 8)} V (z) - \frac {(1 . 2 - a) z - 1 + 0 . 8 a}{(z - a) (z - 0 . 8)} E (z)$$

The Bode diagrams for the signal transmission from load disturbances and measurement errors to x are shown in Fig. 5.9; compare this with Fig. 5.8. By changing the observer dynamics the closed-loop system will be less sensitive for low-frequency load disturbances. The figure shows that the effects of load disturbances and measurement noise are strongly influenced by the observer polynomial $A_{o}$ . A fast observer (a = 0) gives a very good rejection of load disturbances, but much measurement noise is also injected into the system. With a slow observer (a = 0.9), much less measurement noise is injected into the system but the attenuation of load disturbances is not so good.
