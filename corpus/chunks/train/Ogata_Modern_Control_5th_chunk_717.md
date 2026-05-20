Equation (9–113) shows the desired modification in the form of the determinant. This equation gives the form of Sylvester’s interpolation formula when the minimal polynomial of A involves three equal roots. (The necessary modification of the form of the determinant for other cases will be apparent.)

A–9–14. Using Sylvester’s interpolation formula, compute $e ^ { \mathbf { A } t }$ , where

$$
\mathbf {A} = \left[ \begin{array}{c c c} 2 & 1 & 4 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right]
$$

Solution. Referring to Problem A–9–9, the characteristic polynomial and the minimal polynomial are the same for this A. The minimal polynomial (characteristic polynomial) is given by

$$\phi (\lambda) = (\lambda - 2) ^ {2} (\lambda - 1)$$

Note that $\lambda _ { 1 } = \lambda _ { 2 } = 2$ and $\lambda _ { 3 } = 1$ . Referring to Equation (9–112) and noting that $f ( \mathbf { A } )$ in this problem is $e ^ { \mathbf { A } t }$ , we have

$$e ^ {\mathbf {A} t} = \alpha_ {0} (t) \mathbf {I} + \alpha_ {1} (t) \mathbf {A} + \alpha_ {2} (t) \mathbf {A} ^ {2}$$

where $\alpha _ { 0 } ( t ) , \alpha _ { 1 } ( t )$ , and $\alpha _ { 2 } ( t )$ are determined from the equations

$$\alpha_ {1} (t) + 2 \alpha_ {2} (t) \lambda_ {1} = t e ^ {\lambda_ {1} t}\alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {1} + \alpha_ {2} (t) \lambda_ {1} ^ {2} = e ^ {\lambda_ {1} t}\alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {3} + \alpha_ {2} (t) \lambda_ {3} ^ {2} = e ^ {\lambda_ {3} t}$$

Substituting $\lambda _ { 1 } = 2 .$ , and $\lambda _ { 3 } = 1$ into these three equations gives

$$\alpha_ {1} (t) + 4 \alpha_ {2} (t) = t e ^ {2 t}\alpha_ {0} (t) + 2 \alpha_ {1} (t) + 4 \alpha_ {2} (t) = e ^ {2 t}\alpha_ {0} (t) + \alpha_ {1} (t) + \alpha_ {2} (t) = e ^ {t}$$

Solving for $\alpha _ { 0 } ( t ) , \alpha _ { 1 } ( t )$ , and $\alpha _ { 2 } ( t )$ , we obtain

$$\alpha_ {0} (t) = 4 e ^ {t} - 3 e ^ {2 t} + 2 t e ^ {2 t}\alpha_ {1} (t) = - 4 e ^ {t} + 4 e ^ {2 t} - 3 t e ^ {2 t}\alpha_ {2} (t) = e ^ {t} - e ^ {2 t} + t e ^ {2 t}$$

Hence,

$$
e ^ {\mathbf {A} t} = \left(4 e ^ {t} - 3 e ^ {2 t} + 2 t e ^ {2 t}\right) \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] + \left(- 4 e ^ {t} + 4 e ^ {2 t} - 3 t e ^ {2 t}\right) \left[ \begin{array}{c c c} 2 & 1 & 4 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right]

+ \left(e ^ {t} - e ^ {2 t} + t e ^ {2 t}\right) \left[ \begin{array}{c c c} 4 & 1 6 & 1 2 \\ 0 & 4 & 0 \\ 0 & 9 & 1 \end{array} \right]

= \left[ \begin{array}{c c c} e ^ {2 t} & 1 2 e ^ {t} - 1 2 e ^ {2 t} + 1 3 t e ^ {2 t} & - 4 e ^ {t} + 4 e ^ {2 t} \\ 0 & e ^ {2 t} & 0 \\ 0 & - 3 e ^ {t} + 3 e ^ {2 t} & e ^ {t} \end{array} \right]
$$

A–9–15. Show that the system described by
