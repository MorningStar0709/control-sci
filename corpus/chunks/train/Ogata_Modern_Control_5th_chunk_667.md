From this equation, we see that A and $\mathbf { B } _ { i } \left( i = 1 , 2 , \ldots , n \right)$ commute. Hence, the product of $\left( \lambda \mathbf { I } - \mathbf { A } \right)$ and ad $\left( \lambda \mathbf { I } - \mathbf { A } \right)$ becomes zero if either of these is zero. If A is substituted for l in this last equation, then clearly $\lambda \mathbf { I } - \mathbf { A }$ becomes zero. Hence, we obtain

$$\mathbf {A} ^ {n} + a _ {1} \mathbf {A} ^ {n - 1} + \dots + a _ {n - 1} \mathbf {A} + a _ {n} \mathbf {I} = \mathbf {0}$$

This proves the Cayley–Hamilton theorem, or Equation (9–44).

Minimal Polynomial. Referring to the Cayley–Hamilton theorem, every $n \times n$ matrix A satisfies its own characteristic equation. The characteristic equation is not, however, necessarily the scalar equation of least degree that A satisfies.The least-degree polynomial having A as a root is called the minimal polynomial. That is, the minimal polynomial of an $n \times n$ matrix A is defined as the polynomial $\phi ( \lambda )$ of least degree,

$$\phi (\lambda) = \lambda^ {m} + a _ {1} \lambda^ {m - 1} + \dots + a _ {m - 1} \lambda + a _ {m}, \quad m \leq n$$

such that $\phi ( \mathbf { A } ) = \mathbf { 0 } , \mathrm { o r }$

$$\phi (\mathbf {A}) = \mathbf {A} ^ {m} + a _ {1} \mathbf {A} ^ {m - 1} + \dots + a _ {m - 1} \mathbf {A} + a _ {m} \mathbf {I} = \mathbf {0}$$

The minimal polynomial plays an important role in the computation of polynomials in an $n \times n$ matrix.

Let us suppose that $d ( \lambda )$ a polynomial in l, is the greatest common divisor of all the, elements of $\operatorname { a d j } ( \lambda \mathbf { I } - \mathbf { A } )$ We can show that if the coefficient of the highest-degree term. in l of $d ( \lambda )$ is chosen as 1, then the minimal polynomial $\phi ( \lambda )$ is given by

$$\phi (\lambda) = \frac {| \lambda \mathbf {I} - \mathbf {A} |}{d (\lambda)} \tag {9-45}$$

[See Problem A–9–8 for the derivation of Equation $( 9 - 4 5 ) . ]$

It is noted that the minimal polynomial $\phi ( \lambda )$ of an $n \times n$ matrix A can be determined by the following procedure:
