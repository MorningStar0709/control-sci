# Vector-Matrix Algebra

In this appendix we first review the determinant of a matrix, then we define the adjoint matrix, the inverse of a matrix, and the derivative and integral of a matrix.

Determinant of a Matrix. For each square matrix, there exists a determinant.The determinant of a square matrix A is usually written as $| \mathbf { A } |$ or det A. The determinant has the following properties:

1. If any two consecutive rows or columns are interchanged, the determinant changes its sign.   
2. If any row or any column consists only of zeros, then the value of the dererminant is zero.   
3. If the elements of any row (or any column) are exactly k times those of another row (or another column), then the value of the determinant is zero.   
4. If, to any row (or any column), any constant times another row (or column) is added, the value of the determinant remains unchanged.   
5. If a determinant is multiplied by a constant, then only one row (or one column) is multiplied by that constant. Note, however, that the determinant of k times an n\*n matrix A is $k ^ { n }$ times the determinant of A, or

$$\left| k \mathbf {A} \right| = k ^ {n} | \mathbf {A} |$$

This is because

$$
k \mathbf {A} = \left[ \begin{array}{c c c c} k a _ {1 1} & k a _ {1 2} & \ldots & k a _ {1 m} \\ k a _ {2 1} & k a _ {2 2} & \ldots & k a _ {2 m} \\ \vdots & \vdots & & \vdots \\ k a _ {n 1} & k a _ {n 2} & \ldots & k a _ {n m} \end{array} \right]
$$

6. The determinant of the product of two square matrices A and B is the product of determinants, or

$$\left| \mathbf {A} \mathbf {B} \right| = \left| \mathbf {A} \right| \left| \mathbf {B} \right|$$

$\operatorname { I f } \mathbf { B } = n \times$ m matrix and $\mathbf { C } = m \times n$ matrix, then

$$\det (\mathbf {I} _ {n} + \mathbf {B C}) = \det (\mathbf {I} _ {m} + \mathbf {C B})$$

If and D=m\*m matrix, thenA Z 0

$$
\det \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] = \det \mathbf {A} \cdot \det \mathbf {S}
$$

where S=D-CA1 B.

If , thenD Z 0

$$
\det \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] = \det \mathbf {D} \cdot \det \mathbf {T}
$$

where T=A-BD1 C.

If or thenB = 0 C = 0,

$$
\det \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ \mathbf {C} & \mathbf {D} \end{array} \right] = \det \mathbf {A} \cdot \det \mathbf {D}

\det \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {0} & \mathbf {D} \end{array} \right] = \det \mathbf {A} \cdot \det \mathbf {D}
$$
