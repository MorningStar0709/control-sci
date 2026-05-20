It is noted that, just as in case 1, solving Equation (9–49) for $e ^ { \mathbf { A } t }$ is the same as writing

$$e ^ {\mathbf {A} t} = \alpha_ {0} (t) \mathbf {I} + \alpha_ {1} (t) \mathbf {A} + \alpha_ {2} (t) \mathbf {A} ^ {2} + \dots + \alpha_ {m - 1} (t) \mathbf {A} ^ {m - 1} \tag {9-50}$$

and determining the $\alpha _ { k } ( t ) ^ { \ast } \mathrm { s } ( k = 0 , 1 , 2 , \dots , m - 1 )$ from

$$\alpha_ {2} (t) + 3 \alpha_ {3} (t) \lambda_ {1} + \dots + \frac {(m - 1) (m - 2)}{2} \alpha_ {m - 1} (t) \lambda_ {1} ^ {m - 3} = \frac {t ^ {2}}{2} e ^ {\lambda_ {1} t}\alpha_ {1} (t) + 2 \alpha_ {2} (t) \lambda_ {1} + 3 \alpha_ {3} (t) \lambda_ {1} ^ {2} + \dots + (m - 1) \alpha_ {m - 1} (t) \lambda_ {1} ^ {m - 2} = t e ^ {\lambda_ {1} t}\alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {1} + \alpha_ {2} (t) \lambda_ {1} ^ {2} + \dots + \alpha_ {m - 1} (t) \lambda_ {1} ^ {m - 1} = e ^ {\lambda_ {1} t}\alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {4} + \alpha_ {2} (t) \lambda_ {4} ^ {2} + \dots + \alpha_ {m - 1} (t) \lambda_ {4} ^ {m - 1} = e ^ {\lambda_ {4} t}\alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {m} + \alpha_ {2} (t) \lambda_ {m} ^ {2} + \dots + \alpha_ {m - 1} (t) \lambda_ {m} ^ {m - 1} = e ^ {\lambda_ {m} t}$$

The extension to other cases where, for example, there are two or more sets of multiple roots will be apparent. Note that if the minimal polynomial of A is not found, it is possible to substitute the characteristic polynomial for the minimal polynomial. The number of computations may, of course, be increased.

EXAMPLE 9–8 Consider the matrix

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 2 \end{array} \right]
$$

Compute $e ^ { \mathbf { A } t }$ using Sylvester’s interpolation formula.

From Equation (9–47), we get

$$
\left| \begin{array}{c c c} 1 & \lambda_ {1} & e ^ {\lambda_ {1} t} \\ 1 & \lambda_ {2} & e ^ {\lambda_ {2} t} \\ \mathbf {I} & \mathbf {A} & e ^ {\mathbf {A} t} \end{array} \right| = \mathbf {0}
$$

Substituting 0 for $\lambda _ { 1 }$ and $^ { - 2 }$ for $\lambda _ { 2 }$ in this last equation, we obtain

$$
\left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & - 2 & e ^ {- 2 t} \\ \mathbf {I} & \mathbf {A} & e ^ {\mathbf {A} t} \end{array} \right| = \mathbf {0}
$$

Expanding the determinant, we obtain

$$- 2 e ^ {\mathbf {A} t} + \mathbf {A} + 2 \mathbf {I} - \mathbf {A} e ^ {- 2 t} = \mathbf {0}$$

or
