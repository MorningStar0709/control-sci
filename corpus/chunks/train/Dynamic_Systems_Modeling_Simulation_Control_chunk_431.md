# Final-value theorem

As the name implies, the final-value theorem relates the steady-state (final) value of the time function $f ( \infty )$ with its Laplace transform $F ( s )$ . The final-value theorem is

$$f (\infty) = \lim _ {t \to \infty} f (t) = \lim _ {s \to 0} s F (s) \tag {8.10}$$

Therefore, we can use Eq. (8.10) and the Laplace transform $F ( s )$ to compute the steady-state value of the corresponding time response $f ( t )$ . It is important to remember that the final-value theorem holds only for cases where the time function $f ( t )$ reaches a steady-state (constant) value as time $t  \infty$ . In general, the time function $f ( t )$ does not reach a single steady-state value if its Laplace transform $F ( s )$ contains poles on the imaginary axis (with the exception of a single pole at $s = 0 )$ or in the right-half of the complex plane. As a simple example, consider the sinusoidal function $f ( t ) = \sin 3 t$ that clearly does not reach a single, constant steady-state value as time $t \to \infty$ . Table 8.1 shows that the Laplace transform of sin 3t is $F ( s ) =$ $3 / ( s ^ { 2 } + 9 )$ , which has two poles $( \mathrm { a t } s = \pm j 3 )$ that lie on the imaginary axis and hence the final-value theorem does not apply.
