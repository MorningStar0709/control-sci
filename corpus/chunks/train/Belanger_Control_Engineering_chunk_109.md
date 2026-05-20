# Example 3.10 (Pendulum on a Cart)

Assess the observability of the inverted pendulum-and-cart system, using the linearized equations of Example 2.9. Study two sensor configurations: $x$ , $v$ , and $\theta$ in the first, and only $x$ and $v$ in the second.

Solution The state equations are

$$
\left[ \begin{array}{c} \dot {x} \\ \dot {v} \\ \dot {\theta} \\ \dot {\omega} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & \frac {- m g}{M} & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & \frac {(M + m) g}{m \ell} & 0 \end{array} \right] \left[ \begin{array}{c} x \\ v \\ \theta \\ \omega \end{array} \right] + \left[ \begin{array}{c} 0 \\ \frac {1}{M} \\ 0 \\ \frac {- 1}{m \ell} \end{array} \right] F.
$$

For the first configuration,

$$
C = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array} \right].
$$

In this case, we need not write the whole observability matrix; we can stop the procedure of constructing $\mathcal{O}$ as soon as we have four independent rows. Since $C$ by itself already has three, we need only find a fourth. We write

$$
\left. \begin{array}{l} \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & \frac {- m g}{M} & 0 \\ 0 & 0 & 0 & 1 \end{array} \right] \end{array} \right\} C
$$

and stop, because the last row and the first three span all four dimensions

With the second configuration,

$$
C = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{array} \right].
$$

We write

$$
\left[ \begin{array}{cccc} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & \frac {- m g}{M} & 0 \\ 0 & 0 & \frac {- m g}{M} & 0 \\ 0 & 0 & 0 & \frac {- m g}{M} \\ \end{array} \right]\left\{ \begin{array}{l}C \\ C A \\ C A ^ {2}. \\ \end{array} \right.
$$

We may stop, since rows 1, 2, 4, and 6 are independent. This system is thus seen to be observable without the angle sensor.

Despite its usefulness, the rank test is not completely satisfactory from a numerical point of view because of the difficulty of establishing the rank of a matrix. The eigenvector test is somewhat easier to implement, and also gives a modal interpretation of observability.

Before introducing the result, we recall the concept of linearly independent functions. The functions $f_{1}(t)$ , $f_{2}(t)$ , $\ldots$ , $f_{n}(t)$ form a linearly independent set over the interval 0 to T, T > 0, if the relation

$$a _ {1} f _ {1} (t) + a _ {2} f _ {2} (t) + \dots + a _ {n} f _ {n} (t) = 0, \quad 0 \leq t \leq T$$
