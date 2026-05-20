# 9–5 SOME USEFUL RESULTS IN VECTOR-MATRIX ANALYSIS

In this section we present some useful results in vector-matrix analysis that we use in Section 9–6. Specifically, we present the Cayley–Hamilton theorem, the minimal polynomial, Sylvester’s interpolation method for calculating $e ^ { \mathbf { A } t }$ and the linear independence, of vectors.

Cayley–Hamilton Theorem. The Cayley–Hamilton theorem is very useful in proving theorems involving matrix equations or solving problems involving matrix equations.

Consider an n\*n matrix A and its characteristic equation:

$$\left| \lambda \mathbf {I} - \mathbf {A} \right| = \lambda^ {n} + a _ {1} \lambda^ {n - 1} + \dots + a _ {n - 1} \lambda + a _ {n} = 0$$

The Cayley–Hamilton theorem states that the matrix A satisfies its own characteristic equation, or that

$$\mathbf {A} ^ {n} + a _ {1} \mathbf {A} ^ {n - 1} + \dots + a _ {n - 1} \mathbf {A} + a _ {n} \mathbf {I} = \mathbf {0} \tag {9-44}$$

To prove this theorem, note that is a polynomial in l of degree n-1.adj(lI - A) That is,

$$\operatorname{adj} (\lambda \mathbf {I} - \mathbf {A}) = \mathbf {B} _ {1} \lambda^ {n - 1} + \mathbf {B} _ {2} \lambda^ {n - 2} + \dots + \mathbf {B} _ {n - 1} \lambda + \mathbf {B} _ {n}$$

where $\mathbf { B } _ { 1 } = \mathbf { I } .$ Since.

$$(\lambda \mathbf {I} - \mathbf {A}) \operatorname{adj} (\lambda \mathbf {I} - \mathbf {A}) = [ \operatorname{adj} (\lambda \mathbf {I} - \mathbf {A}) ] (\lambda \mathbf {I} - \mathbf {A}) = | \lambda \mathbf {I} - \mathbf {A} | \mathbf {I}$$

we obtain

$$
\begin{array}{l} \left| \lambda \mathbf {I} - \mathbf {A} \right| \mathbf {I} = \mathbf {I} \lambda^ {n} + a _ {1} \mathbf {I} \lambda^ {n - 1} + \dots + a _ {n - 1} \mathbf {I} \lambda + a _ {n} \mathbf {I} \\ = (\lambda \mathbf {I} - \mathbf {A}) \left(\mathbf {B} _ {1} \lambda^ {n - 1} + \mathbf {B} _ {2} \lambda^ {n - 2} + \dots + \mathbf {B} _ {n - 1} \lambda + \mathbf {B} _ {n}\right) \\ = \left(\mathbf {B} _ {1} \lambda^ {n - 1} + \mathbf {B} _ {2} \lambda^ {n - 2} + \dots + \mathbf {B} _ {n - 1} \lambda + \mathbf {B} _ {n}\right) (\lambda \mathbf {I} - \mathbf {A}) \\ \end{array}
$$
