# Example 8.2

Compute the Laplace transform of the step function $f ( t ) = A$ for $t > 0$ where A is a constant. The step function $f ( t ) = 0 \mathrm { f o r } t \leq 0$ .

Using the definition of the Laplace transform (Eq. 8.1)

$$
\begin{array}{l} \mathscr {L} \{A \} = \int_ {0} ^ {\infty} A e ^ {- s t} d t \\ = A \left. \frac {e ^ {- s t}}{- s} \right| _ {t = 0} ^ {t = \infty} = \frac {A e ^ {- \infty}}{- s} - \frac {A e ^ {0}}{- s} \\ \end{array}
$$

Hence, the Laplace transform of the step function $f ( t ) = A$ is

$$F (s) = \frac {A}{s}$$

$\operatorname { I f } f ( t )$ is a unit-step function, then A = 1 and $F ( s ) = 1 / s$ .
