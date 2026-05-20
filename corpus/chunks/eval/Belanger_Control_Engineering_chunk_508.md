# 8.11 $H^{\infty}$ SOLUTION

One important difference between the $H^{2}$ and $H^{\infty}$ solutions is that, for the latter, we look not for the optimal solution but for a solution (not unique) for which $\|T_{wz}\|_{\infty}<\gamma$ . A search for the minimum is carried out simply by decreasing $\gamma$ until a solution fails to exist.

The solution is taken from $[4, 5]$ . It requires more technical machinery than we can display here, so proofs will not be given. The starting point is the Hamiltonian matrix,

$$
H = \left[ \begin{array}{c c} A & - R \\ - Q & - A ^ {T} \end{array} \right]
$$

with Q and R symmetric but not necessarily positive definite. All submatrices in H are of dimensions $n \times n$ . The matrix H is symplectic and has the property that its eigenvalues are located symmetrically with respect to the j-axis as well as the real axis.

We assume that H has no eigenvalues on the j-axis; this assumption is called the stability condition. We form the $2n \times n$ matrix X with columns from the eigenvectors and generalized eigenvectors of H that correspond to LHP eigenvalues; for complex conjugate pairs, we use the real and imaginary parts. The resulting matrix is partitioned into $n \times n$ matrices $X_{1}$ and $X_{2}$ as follows:

$$
X = \left[ \begin{array}{c} X _ {1} \\ X _ {2} \end{array} \right].
$$

If $X_{1}$ is nonsingular, H is said to satisfy the complementarity condition. If H has no j-axis eigenvalues and $X_{1}^{-1}$ exists, then $P = X_{2}X_{1}^{-1}$ satisfies the Riccati equation,

$$A ^ {T} P + P A - P R P + Q = 0$$

and, in addition, A - RP is a stable matrix. The converse is not true: P may satisfy the Riccati equation and A - RP may be stable without the complementarity and stability conditions being satisfied.

If R > 0 and $Q \geq 0$ , a square-root method can be used to express R as $BB^{T}$ , and the Riccati equation is the familiar one. If, in addition, $(A, B)$ is stabilizable and $(Q^{1/2}, A)$ is detectable, then the complementarity and stability conditions can be shown to hold.

Doyle et al., the major reference [4], gives a solution under the following simplifying assumptions:

$$D _ {1 1} = D _ {2 2} = 0D _ {1 2} ^ {T} D _ {1 2} = D _ {2 1} D _ {2 1} ^ {T} = IB _ {1} D _ {2 1} ^ {T} = D _ {1 2} ^ {T} C _ {1} = 0.$$

These assumptions can be removed and are in computer algorithms. Since we shall not be calculating the solution by hand, we shall use these assumptions to simplify the presentation.
