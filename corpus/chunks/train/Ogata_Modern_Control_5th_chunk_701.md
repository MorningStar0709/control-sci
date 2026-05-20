$$
\begin{array}{l} (s \mathbf {I} - \mathbf {A}) ^ {- 1} = \left[ \begin{array}{c c} s + 1 & 0. 5 \\ - 1 & s \end{array} \right] ^ {- 1} = \frac {1}{s ^ {2} + s + 0 . 5} \left[ \begin{array}{c c} s & - 0. 5 \\ 1 & s + 1 \end{array} \right] \\ = \left[ \begin{array}{c c} \frac {s + 0 . 5 - 0 . 5}{(s + 0 . 5) ^ {2} + 0 . 5 ^ {2}} & \frac {- 0 . 5}{(s + 0 . 5) ^ {2} + 0 . 5 ^ {2}} \\ \frac {1}{(s + 0 . 5) ^ {2} + 0 . 5 ^ {2}} & \frac {s + 0 . 5 + 0 . 5}{(s + 0 . 5) ^ {2} + 0 . 5 ^ {2}} \end{array} \right] \\ \end{array}
$$

we have

$$
\boldsymbol {\Phi} (t) = e ^ {\mathbf {A} t} = \mathscr {L} ^ {- 1} \left[ (s \mathbf {I} - \mathbf {A}) ^ {- 1} \right]
= \left[ \begin{array}{c c} e ^ {- 0. 5 t} (\cos 0. 5 t - \sin 0. 5 t) & - e ^ {- 0. 5 t} \sin 0. 5 t \\ 2 e ^ {- 0. 5 t} \sin 0. 5 t & e ^ {- 0. 5 t} (\cos 0. 5 t + \sin 0. 5 t) \end{array} \right]
$$

Since x(0)=0 and k=1, referring to Equation (9–96), we have

$$
\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + \mathbf {A} ^ {- 1} \left(e ^ {\mathbf {A} t} - \mathbf {I}\right) \mathbf {B} k= \mathbf {A} ^ {- 1} \left(e ^ {\mathbf {A} t} - \mathbf {I}\right) \mathbf {B}
= \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 2 \end{array} \right] \left[ \begin{array}{c} 0. 5 e ^ {- 0. 5 t} (\cos 0. 5 t - \sin 0. 5 t) - 0. 5 \\ e ^ {- 0. 5 t} \sin 0. 5 t \end{array} \right]

= \left[ \begin{array}{c} e ^ {- 0. 5 t} \sin 0. 5 t \\ - e ^ {- 0. 5 t} (\cos 0. 5 t + \sin 0. 5 t) + 1 \end{array} \right]
$$

Hence, the output y(t) can be given by

$$
y (t) = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] = x _ {1} = e ^ {- 0. 5 t} \sin 0. 5 t
$$

A–9–8. The Cayley–Hamilton theorem states that every $n \times n$ matrix A satisfies its own characteristic equation. The characteristic equation is not, however, necessarily the scalar equation of least degree that A satisfies. The least-degree polynomial having A as a root is called the minimal polynomial. That is, the minimal polynomial of an $n \times n$ matrix A is defined as the polynomial $\phi ( \lambda )$ of least degree,

$$\phi (\lambda) = \lambda^ {m} + a _ {1} \lambda^ {m - 1} + \dots + a _ {m - 1} \lambda + a _ {m}, \quad m \leq n$$

such that $\phi ( \mathbf { A } ) = \mathbf { 0 } , \mathrm { o r }$

$$\phi (\mathbf {A}) = \mathbf {A} ^ {m} + a _ {1} \mathbf {A} ^ {m - 1} + \dots + a _ {m - 1} \mathbf {A} + a _ {m} \mathbf {I} = \mathbf {0}$$

The minimal polynomial plays an important role in the computation of polynomials in an $n \times n$ matrix.
