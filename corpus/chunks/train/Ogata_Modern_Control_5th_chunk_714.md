$$
\left| \begin{array}{c c c c c c} 1 & \lambda_ {1} & \lambda_ {1} ^ {2} & \dots & \lambda_ {1} ^ {m - 1} & f (\lambda_ {1}) \\ 1 & \lambda_ {2} & \lambda_ {2} ^ {2} & \dots & \lambda_ {2} ^ {m - 1} & f (\lambda_ {2}) \\ \cdot & \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & \cdot & \dots & \cdot & \cdot \\ 1 & \lambda_ {m} & \lambda_ {m} ^ {2} & \dots & \lambda_ {m} ^ {m - 1} & f (\lambda_ {m}) \\ \mathbf {I} & \mathbf {A} & \mathbf {A} ^ {2} & \dots & \mathbf {A} ^ {m - 1} & f (\mathbf {A}) \end{array} \right| = \mathbf {0}
$$

This formula for the determination of f(A) applies to the case where the minimal polynomial of A involves only distinct roots.

Suppose that the minimal polynomial of A involves multiple roots. Then the rows in the determinant that correspond to the multiple roots become identical, and therefore modification of the determinant in Equation (9–104) becomes necessary.

Modify the form of Sylvester’s interpolation formula given by Equation (9–104) when the minimal polynomial of A involves multiple roots. In deriving a modified determinant equation, assume that there are three equal roots $\left( \lambda _ { 1 } = \lambda _ { 2 } = \lambda _ { 3 } \right)$ in the minimal polynomial of A and that there are other roots $\left( \lambda _ { 4 } , \lambda _ { 5 } , \ldots , \lambda _ { m } \right)$ that are distinct.

Solution. Since the minimal polynomial of A involves three equal roots, the minimal polynomial $\phi ( \lambda )$ can be written as

$$
\begin{array}{l} \phi (\lambda) = \lambda^ {m} + a _ {1} \lambda^ {m - 1} + \dots + a _ {m - 1} \lambda + a _ {m} \\ = \left(\lambda - \lambda_ {1}\right) ^ {3} \left(\lambda - \lambda_ {4}\right) \left(\lambda - \lambda_ {5}\right) \dots \left(\lambda - \lambda_ {m}\right) \\ \end{array}
$$

An arbitrary function $f ( \mathbf { A } )$ of an $n \times n$ matrix A can be written as

$$f (\mathbf {A}) = g (\mathbf {A}) \phi (\mathbf {A}) + \alpha (\mathbf {A})$$

where the minimal polynomial $\phi ( \mathbf { A } )$ is of degree m and $\alpha ( \mathbf { A } )$ is a polynomial in A of degree $m - 1$ or less. Hence we have

$$f (\lambda) = g (\lambda) \phi (\lambda) + \alpha (\lambda)$$

where $\alpha ( \lambda )$ is a polynomial in l of degree m-1 or less, which can thus be written as

$$\alpha (\lambda) = \alpha_ {0} + \alpha_ {1} \lambda + \alpha_ {2} \lambda^ {2} + \dots + \alpha_ {m - 1} \lambda^ {m - 1} \tag {9-105}$$

In the present case we have
