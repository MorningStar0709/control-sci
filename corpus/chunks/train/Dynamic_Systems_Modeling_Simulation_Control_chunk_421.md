# Example 8.1

Compute the Laplace transform of the exponential function $f ( t ) = A e ^ { - a t }$ for $t \geq 0$ where A and a are constants. The function $f ( t ) = 0$ for $t < 0$ .

Using the definition of the Laplace transform (Eq. 8.1)

$$
\begin{array}{l} \mathscr {L} \{A e ^ {- a t} \} = \int_ {0} ^ {\infty} A e ^ {- a t} e ^ {- s t} d t \\ = A \int_ {0} ^ {\infty} e ^ {- (a + s) t} d t \\ = A \left. \frac {e ^ {- (s + a) t}}{- (s + a)} \right| _ {t = 0} ^ {t = \infty} = \frac {A e ^ {- \infty}}{- (s + a)} - \frac {A e ^ {0}}{- (s + a)} \\ \end{array}
$$

Hence, the Laplace transform of the exponential function $f ( t ) = A e ^ { - a t }$ is

$$F (s) = \frac {A}{s + a}$$
