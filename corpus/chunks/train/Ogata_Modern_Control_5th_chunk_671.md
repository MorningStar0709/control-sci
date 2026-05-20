$$e ^ {\mathbf {A} t} = \alpha_ {0} (t) \mathbf {I} + \alpha_ {1} (t) \mathbf {A} + \alpha_ {2} (t) \mathbf {A} ^ {2} + \dots + \alpha_ {m - 1} (t) \mathbf {A} ^ {m - 1} \tag {9-48}$$

and determining the $\alpha _ { k } ( t ) ( k = 0 , 1 , 2 , \ldots , m - 1 )$ by solving the following set of m equations for the $\alpha _ { k } ( t )$ :

$$
\begin{array}{l} \alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {1} + \alpha_ {2} (t) \lambda_ {1} ^ {2} + \dots + \alpha_ {m - 1} (t) \lambda_ {1} ^ {m - 1} = e ^ {\lambda_ {1} t} \\ \alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {2} + \alpha_ {2} (t) \lambda_ {2} ^ {2} + \dots + \alpha_ {m - 1} (t) \lambda_ {2} ^ {m - 1} = e ^ {\lambda_ {2} t} \\ \alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {m} + \alpha_ {2} (t) \lambda_ {m} ^ {2} + \dots + \alpha_ {m - 1} (t) \lambda_ {m} ^ {m - 1} = e ^ {\lambda_ {m} t} \\ \end{array}
$$

matrix and has distinct eigenvalues, then the number of $\alpha _ { k } ( t ) ^ { } \mathrm { s }$ to be $m = n$ . If A involves multiple eigenvalues, but its minimal polynomial has ots, however, then the number m of $\alpha _ { k } ( t ) ^ { \ast } \mathrm { s }$ to be determined is less than n.

Case 2: Minimal Polynomial of A Involves Multiple Roots. As an example, consider the case where the minimal polynomial of A involves three equal roots $\left( \lambda _ { 1 } = \lambda _ { 2 } = \lambda _ { 3 } \right)$ and has other roots $\left( \lambda _ { 4 } , \lambda _ { 5 } , \ldots , \lambda _ { m } \right)$ that are all distinct. By applying Sylvester’s interpolation formula, it can be shown that $e ^ { \mathbf { A } t }$ can be obtained from the following determinant equation:

$$
\left| \begin{array}{c c c c c c c} 0 & 0 & 1 & 3 \lambda_ {1} & \dots & \frac {(m - 1) (m - 2)}{2} \lambda_ {1} ^ {m - 3} & \frac {t ^ {2}}{2} e ^ {\lambda_ {1} t} \\ 0 & 1 & 2 \lambda_ {1} & 3 \lambda_ {1} ^ {2} & \dots & (m - 1) \lambda_ {1} ^ {m - 2} & t e ^ {\lambda_ {1} t} \\ 1 & \lambda_ {1} & \lambda_ {1} ^ {2} & \lambda_ {1} ^ {3} & \dots & \lambda_ {1} ^ {m - 1} & e ^ {\lambda_ {1} t} \\ 1 & \lambda_ {4} & \lambda_ {4} ^ {2} & \lambda_ {4} ^ {3} & \dots & \lambda_ {4} ^ {m - 1} & e ^ {\lambda_ {4} t} \\ . & . & . & . & \dots & . & . \\ . & . & . & . & \dots & . & . \\ . & . & . & . & \dots & . & . \\ 1 & \lambda_ {m} & \lambda_ {m} ^ {2} & \lambda_ {m} ^ {3} & \dots & \lambda_ {m} ^ {m - 1} & e ^ {\lambda_ {m} t} \\ \mathbf {I} & \mathbf {A} & \mathbf {A} ^ {2} & \mathbf {A} ^ {3} & \dots & \mathbf {A} ^ {m - 1} & e ^ {\mathbf {A} t} \end{array} \right| = \mathbf {0} \tag {9-49}
$$

Equation (9–49) can be solved for $e ^ { \mathbf { A } t }$ by expanding it about the last column.
