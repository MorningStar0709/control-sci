$$
\begin{array}{l} \alpha_ {2} + 3 \alpha_ {3} \lambda_ {1} + \dots + \frac {(m - 1) (m - 2)}{2} \alpha_ {m - 1} \lambda_ {1} ^ {m - 3} = \frac {f ^ {\prime \prime} (\lambda_ {1})}{2} \\ \alpha_ {1} + 2 \alpha_ {2} \lambda_ {1} + \dots + (m - 1) \alpha_ {m - 1} \lambda_ {1} ^ {m - 2} = f ^ {\prime} (\lambda_ {1}) \\ \begin{array}{l} \alpha_ {0} + \alpha_ {1} \lambda_ {1} + \alpha_ {2} \lambda_ {1} ^ {2} + \dots + \alpha_ {m - 1} \lambda_ {1} ^ {m - 1} = f (\lambda_ {1}) \\ \alpha_ {0} + \alpha_ {1} \lambda_ {4} + \alpha_ {2} \lambda_ {4} ^ {2} + \dots + \alpha_ {m - 1} \lambda_ {4} ^ {m - 1} = f (\lambda_ {4}) \end{array} \tag {9-111} \\ \end{array}
\alpha_ {0} + \alpha_ {1} \lambda_ {m} + \alpha_ {2} \lambda_ {m} ^ {2} + \dots + \alpha_ {m - 1} \lambda_ {m} ^ {m - 1} = f (\lambda_ {m})
$$

These m simultaneous equations determine the $\alpha _ { k }$ values (where $k = 0 , 1 , 2 , \ldots , m - 1 )$ ). Noting that $\phi ( \mathbf { A } ) = \mathbf { 0 }$ because it is a minimal polynomial, we have $f ( \mathbf { A } )$ as follows:

$$f (\mathbf {A}) = g (\mathbf {A}) \phi (\mathbf {A}) + \alpha (\mathbf {A}) = \alpha (\mathbf {A})$$

Hence, referring to Equation (9–105), we have

$$f (\mathbf {A}) = \alpha (\mathbf {A}) = \alpha_ {0} \mathbf {I} + \alpha_ {1} \mathbf {A} + \alpha_ {2} \mathbf {A} ^ {2} + \dots + \alpha_ {m - 1} \mathbf {A} ^ {m - 1} \tag {9-112}$$

where the $\alpha _ { k }$ values are given in terms of $f ( \lambda _ { 1 } ) , f ^ { \prime } ( \lambda _ { 1 } ) , f ^ { \prime \prime } ( \lambda _ { 1 } ) , f ( \lambda _ { 4 } ) , f ( \lambda _ { 5 } ) , \ldots , f ( \lambda _ { m } )$ . In terms of the determinant equation, $f ( \mathbf { A } )$ can be obtained by solving the following equation:

$$
\left| \begin{array}{c c c c c c c} 0 & 0 & 1 & 3 \lambda_ {1} & \dots & \frac {(m - 1) (m - 2)}{2} \lambda_ {1} ^ {m - 3} & \frac {f ^ {\prime \prime} (\lambda_ {1})}{2} \\ 0 & 1 & 2 \lambda_ {1} & 3 \lambda_ {1} ^ {2} & \dots & (m - 1) \lambda_ {1} ^ {m - 2} & f ^ {\prime} (\lambda_ {1}) \\ 1 & \lambda_ {1} & \lambda_ {1} ^ {2} & \lambda_ {1} ^ {3} & \dots & \lambda_ {1} ^ {m - 1} & f (\lambda_ {1}) \\ 1 & \lambda_ {4} & \lambda_ {4} ^ {2} & \lambda_ {4} ^ {3} & \dots & \lambda_ {4} ^ {m - 1} & f (\lambda_ {4}) \\ . & . & . & . & & . & . \\ . & . & . & . & & . & . \\ . & . & . & . & & . & . \\ 1 & \lambda_ {m} & \lambda_ {m} ^ {2} & \lambda_ {m} ^ {3} & \dots & \lambda_ {m} ^ {m - 1} & f (\lambda_ {m}) \\ \mathbf {I} & \mathbf {A} & \mathbf {A} ^ {2} & \mathbf {A} ^ {3} & \dots & \mathbf {A} ^ {m - 1} & f (\mathbf {A}) \end{array} \right| = \mathbf {0} \tag {9-113}
$$
