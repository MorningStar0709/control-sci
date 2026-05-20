# 2.2 Eigenvalues and Eigenvectors

Let $A \in \mathbb { C } ^ { n \times n }$ ; then the eigenvalues of A are the n roots of its characteristic polynomial $p ( \lambda ) = \operatorname* { d e t } ( \lambda I - A )$ . The maximal modulus of the eigenvalues is called the spectral radius, denoted by

$$\rho (A) := \max _ {1 \leq i \leq n} | \lambda_ {i} |$$

if $\lambda _ { i }$ is a root of $p ( \lambda )$ , where, as usual, | · | denotes the magnitude. The real spectral radius of a matrix A, denoted by $\rho _ { R } ( A )$ , is the maximum modulus of the real eigenvalues of A; that is, $\rho _ { R } ( A ) : = \operatorname* { m a x } _ { \lambda _ { i } \in \mathbb { R } } | \lambda _ { i } |$ and $\rho _ { R } ( A ) : = 0$ if A has no real eigenvalues. A nonzero vector $x \in \mathbb { C } ^ { n }$ that satisfies

$$A x = \lambda x$$

is referred to as a right eigenvector of A. Dually, a nonzero vector y is called a left eigenvector of A if

$$y ^ {*} A = \lambda y ^ {*}.$$

In general, eigenvalues need not be real, and neither do their corresponding eigenvectors. However, if A is real and λ is a real eigenvalue of A, then there is a real eigenvector corresponding to λ. In the case that all eigenvalues of a matrix A are real, we will denote $\lambda _ { \mathrm { m a x } } ( A )$ for the largest eigenvalue of A and $\lambda _ { \mathrm { m i n } } ( A )$ for the smallest eigenvalue. In particular, if A is a Hermitian matrix $( \mathrm { i . e . , } A = A ^ { * } )$ , then there exist a unitary matrix U and a real diagonal matrix Λ such that $A = U \Lambda U ^ { * }$ , where the diagonal elements of Λ are the eigenvalues of A and the columns of U are the eigenvectors of A.

Lemma 2.1 Consider the Sylvester equation

$$A X + X B = C, \tag {2.1}$$

where $A \ \in \ \mathbb { F } ^ { n \times n } , \ B \ \in \ \mathbb { F } ^ { m \times m }$ , and $C \in \mathbb { F } ^ { n \times m }$ are given matrices. There exists a unique solution $\boldsymbol { X } \in \mathbb { F } ^ { n \times m }$ if and only if $\lambda _ { i } ( A ) + \lambda _ { j } ( B ) \neq 0 , \forall i = 1 , 2 , . . . , n _ { \mathrm { ~ } }$ , and $j = 1 , 2 , \dots , m$ .

In particular, if $B = A ^ { * }$ , equation $( 2 . 1 )$ is called the Lyapunov equation; and the necessary and sufficient condition for the existence of a unique solution is that $\lambda _ { i } ( A ) + { \bar { \lambda } } _ { j } ( A ) \neq 0 , \forall i , j = 1 , 2 , \dots , n .$ .

Illustrative MATLAB Commands:

$$\gg [ \mathbf {V}, \mathbf {D} ] = \operatorname{eig} (\mathbf {A}) \% A V = V D\gg \mathbf {X} = \text {lyap} (\mathbf {A}, \mathbf {B}, - \mathbf {C}) \quad \% \text {solving Sylvester equation.}$$
