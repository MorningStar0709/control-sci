# Example 8.3

Compute the Laplace transform of the sinusoidal function $f ( t ) = A$ sin ??t for $t \geq 0$ where A is the constant amplitude and ?? is the constant frequency. The function $f ( t ) = 0$ for $t < 0$ .

Using Eq. (8.1)

$$\mathscr {L} \{A \sin \omega t \} = \int_ {0} ^ {\infty} A \sin \omega t e ^ {- s t} d t$$

We can use Euler’s formula to relate sinusoidal functions to a complex exponential function

$$e ^ {j \omega t} = \cos \omega t + j \sin \omega t$$

or, sin $\omega t = ( e ^ { j \omega t } - \cos \omega t ) / j$ . Using the complex conjugate of Euler’s formula

$$e ^ {- j \omega t} = \cos \omega t - j \sin \omega t$$

we can substitute cos $\omega t = e ^ { - j \omega t } + j$ sin ??t into the previous expression to yield

$$\sin \omega t = \frac {1}{2 j} \big (e ^ {j \omega t} - e ^ {- j \omega t} \big)$$

Using this result the Laplace transform integral becomes

$$
\begin{array}{l} \mathcal {L} \{A \sin \omega t \} = \frac {A}{2 j} \int_ {0} ^ {\infty} \left(e ^ {j \omega t} - e ^ {- j \omega t}\right) e ^ {- s t} d t \\ = \frac {A}{2 j} \int_ {0} ^ {\infty} \left(e ^ {- (s - j \omega) t} - e ^ {- (s + j \omega) t}\right) d t \\ = \frac {A}{2 j} \left[ \left. \frac {e ^ {- (s - j \omega) t}}{- (s - j \omega)} \right| _ {t = 0} ^ {t = \infty} + \left. \frac {e ^ {- (s + j \omega) t}}{(s + j \omega)} \right| _ {t = 0} ^ {t = \infty} \right] \\ = \frac {A}{2 j} \left[ \frac {1}{s - j \omega} - \frac {1}{s + j \omega} \right] \\ \end{array}
$$

Multiplying both terms by the appropriate complex conjugate $( s + j \omega \mathrm { o r } s - j \omega )$ will produce a common denominator and the result is

$$F (s) = \frac {A \omega}{s ^ {2} + \omega^ {2}}$$

which is the Laplace transform of the sine function f (t) = A sin ??t.

In summary, the examples show that computing the Laplace transform of a time function $f ( t )$ requires integrating the product of $f ( t )$ and $e ^ { s t }$ from t = 0 to t = ∞. Once we have computed the Laplace transform of a common time function, we do not need to recalculate it every time it is needed; instead we can consult a table of precomputed Laplace transforms. Table 8.1 summarizes the Laplace transforms of common time functions, including the results from Examples 8.1, 8.2, and 8.3.
