$$
\mathbf {S} ^ {- 1} = \left[ \begin{array}{r r r} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 1 & - 2 & 1 \end{array} \right]
$$

Then it can be seen that

$$
\begin{array}{l} \mathbf {S} ^ {- 1} \mathbf {A} \mathbf {S} = \left[ \begin{array}{r r r} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 1 & - 2 & 1 \end{array} \right] \left[ \begin{array}{r r r} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & - 3 & 3 \end{array} \right] \left[ \begin{array}{r r r} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 2 & 1 \end{array} \right] \\ = \left[ \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right] = \mathbf {J} \\ \end{array}
$$

Noting that

$$
e ^ {\mathbf {J} t} = \left[ \begin{array}{c c c} e ^ {t} & t e ^ {t} & \frac {1}{2} t ^ {2} e ^ {t} \\ 0 & e ^ {t} & t e ^ {t} \\ 0 & 0 & e ^ {t} \end{array} \right]
$$

we find

$$
\begin{array}{l} e ^ {\mathbf {A} t} = \mathbf {S} e ^ {\mathbf {J} t} \mathbf {S} ^ {- 1} \\ = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 2 & 1 \end{array} \right] \left[ \begin{array}{c c c} e ^ {t} & t e ^ {t} & \frac {1}{2} t ^ {2} e ^ {t} \\ 0 & e ^ {t} & t e ^ {t} \\ 0 & 0 & e ^ {t} \end{array} \right] \left[ \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 1 & - 2 & 1 \end{array} \right] \\ = \left[ \begin{array}{c c c} e ^ {t} - t e ^ {t} + \frac {1}{2} t ^ {2} e ^ {t} & t e ^ {t} - t ^ {2} e ^ {t} & \frac {1}{2} t ^ {2} e ^ {t} \\ \frac {1}{2} t ^ {2} e ^ {t} & e ^ {t} - t e ^ {t} - t ^ {2} e ^ {t} & t e ^ {t} + \frac {1}{2} t ^ {2} e ^ {t} \\ t e ^ {t} + \frac {1}{2} t ^ {2} e ^ {t} & - 3 t e ^ {t} - t ^ {2} e ^ {t} & e ^ {t} + 2 t e ^ {t} + \frac {1}{2} t ^ {2} e ^ {t} \end{array} \right] \\ \end{array}
$$

Computation of $e ^ { \mathbf { A } t } \colon$ Method 2. The second method of computing $e ^ { \mathbf { A } t }$ uses the Laplace transform approach. Referring to Equation (9–36), $e ^ { \mathbf { A } t }$ can be given as follows:

$$e ^ {\mathbf {A} t} = \mathcal {L} ^ {- 1} \left[ (s \mathbf {I} - \mathbf {A}) ^ {- 1} \right]$$

Thus, to obtain $e ^ { \mathbf { A } t }$ first invert the matrix This results in a matrix whose(sI - A)., elements are rational functions of s. Then take the inverse Laplace transform of each element of the matrix.

EXAMPLE 9–7 Consider the following matrix A:

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 2 \end{array} \right]
$$

Compute $e ^ { \mathbf { A } t }$ by use of the two analytical methods presented previously.

Method 1. The eigenvalues of A are 0 and $- 2 \left( \lambda _ { 1 } = 0 , \lambda _ { 2 } = - 2 \right)$ A necessary transformation. matrix P may be obtained as

$$
\mathbf {P} = \left[ \begin{array}{c c} 1 & 1 \\ 0 & - 2 \end{array} \right]
$$

Then, from Equation $( 9 - 4 6 ) , e ^ { \mathbf { A } t }$ is obtained as follows:
