$$
e ^ {\mathbf {J} t} = \left[ \begin{array}{c c c c c c c} e ^ {\lambda_ {1} t} & t e ^ {\lambda_ {1} t} & \frac {1}{2} t ^ {2} e ^ {\lambda_ {1} t} & & & & 0 \\ 0 & e ^ {\lambda_ {1} t} & t e ^ {\lambda_ {1} t} & & & & \\ 0 & 0 & e ^ {\lambda_ {1} t} & & & & \\ \hline & & & e ^ {\lambda_ {4} t} & t e ^ {\lambda_ {4} t} & & \\ & & & 0 & e ^ {\lambda_ {4} t} & & \\ \hline & & & & & e ^ {\lambda_ {6} t} & 0 \\ 0 & & & & & 0 & e ^ {\lambda_ {7} t} \end{array} \right]
$$

A–9–12. Consider the following polynomial in l of degree $m - 1$ , where we assume $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { m }$ to be distinct:

$$p _ {k} (\lambda) = \frac {\left(\lambda - \lambda_ {1}\right) \cdots \left(\lambda - \lambda_ {k - 1}\right) \left(\lambda - \lambda_ {k + 1}\right) \cdots \left(\lambda - \lambda_ {m}\right)}{\left(\lambda_ {k} - \lambda_ {1}\right) \cdots \left(\lambda_ {k} - \lambda_ {k - 1}\right) \left(\lambda_ {k} - \lambda_ {k + 1}\right) \cdots \left(\lambda_ {k} - \lambda_ {m}\right)}$$

where $k = 1 , 2 , \ldots , m$ . Notice that

$$
p _ {k} (\lambda_ {i}) = \left\{ \begin{array}{l l} 1, & \text { if } i = k \\ 0, & \text { if } i \neq k \end{array} \right.
$$

Then the polynomial f(l) of degree $m - 1$ ,

$$
\begin{array}{l} f (\lambda) = \sum_ {k = 1} ^ {m} f \left(\lambda_ {k}\right) p _ {k} (\lambda) \\ = \sum_ {k = 1} ^ {m} f (\lambda_ {k}) \frac {(\lambda - \lambda_ {1}) \cdots (\lambda - \lambda_ {k - 1}) (\lambda - \lambda_ {k + 1}) \cdots (\lambda - \lambda_ {m})}{(\lambda_ {k} - \lambda_ {1}) \cdots (\lambda_ {k} - \lambda_ {k - 1}) (\lambda_ {k} - \lambda_ {k + 1}) \cdots (\lambda_ {k} - \lambda_ {m})} \\ \end{array}
$$

takes on the values $f { \left( \lambda _ { k } \right) }$ at the points $\lambda _ { k }$ . This last equation is commonly called Lagrange’s interpolation formula. The polynomial $f ( \lambda )$ of degree $m - 1$ is determined from m independent data $f \bigl ( \lambda _ { 1 } \bigr ) , \dot { f } \bigl ( \lambda _ { 2 } \bigr ) , \ldots , \dot { f } \bigl ( \lambda _ { m } \bigr )$ . That is, the polynomial $f ( \lambda )$ passes through m points $f ( \lambda _ { 1 } ) , f { \bigl ( } \lambda _ { 2 } { \bigr ) } , \ldots , f { \bigl ( } \lambda _ { m } { \bigr ) }$ . Since $f ( \lambda )$ is a polynomial of degree $m - 1$ , it is uniquely determined. Any other representations of the polynomial of degree $m - 1$ can be reduced to the Lagrange polynomial f(l).

Assuming that the eigenvalues of an $n \times n$ matrix A are distinct, substitute A for l in the polynomial $p _ { k } ( \lambda )$ . Then we get
