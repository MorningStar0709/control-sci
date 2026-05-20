# EXAMPLE 4.10 Minimum-effort control

Consider the same system as in Example 4.9. The minimum-effort controller is in this case given by

$$\mu = b \frac {1 + a ^ {2} + \cdots + a ^ {2 (d - 1)}}{(- a) ^ {d - 1}} = \frac {b (a ^ {2 d} - 1)}{(- a) ^ {d - 1} (a ^ {2} - 1)}$$

which gives (when $y_{m} = 0$ )

$$u (t) = - \frac {(- a) ^ {d}}{\mu} y (t) = \frac {a ^ {2 d - 1} (a ^ {2} - 1)}{b (a ^ {2 d} - 1)} y (t)$$

The pole of the closed-loop system is

$$p _ {d} = - a + \frac {a ^ {2 d - 1} (a ^ {2} - 1)}{a ^ {2 d} - 1} = - \frac {a ^ {2 d - 1} + a}{a ^ {2 d} - 1}$$

which gives

$$
\begin{array}{l} \lim _ {d \rightarrow \infty} p _ {d} = - a \quad | a | \leq 1 \quad (\text { stable   open - loop   system }) \\ \lim _ {d \rightarrow \infty} p _ {d} = - 1 / a \quad | a | > 1 \quad (\text { unstable   open - loop   system }) \\ \end{array}
$$

For this example the minimum-effort controller gives a better closed-loop system than if the future control is assumed to be constant.
