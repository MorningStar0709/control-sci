# 12.1 Stabilizing Solution and Riccati Operator

Assume that H has no eigenvalues on the imaginary axis. Then it must have n eigenvalues in Re $s < 0$ and n in Re $s > 0 .$ . Consider the n-dimensional invariant spectral subspace, X (H), corresponding to eigenvalues of H in Re $s < 0$ . By finding a basis for $\ X _ { - } ( H )$ , stacking the basis vectors up to form a matrix, and partitioning the matrix, we get

$$
\mathcal {X} _ {-} (H) = \mathrm{Im} \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right]
$$

where $X _ { 1 } , X _ { 2 } \ \in \ \mathbb { C } ^ { n \times n } . \quad ( X _ { 1 }$ and $X _ { 2 }$ can be chosen to be real matrices.) If $X _ { 1 }$ is nonsingular or, equivalently, if the two subspaces

$$
\mathcal {X} _ {-} (H), \quad \mathrm{Im} \left[ \begin{array}{c} 0 \\ I \end{array} \right] \tag {12.3}
$$

are complementary, we can set $X : = X _ { 2 } X _ { 1 } ^ { - 1 }$ . Then X is uniquely determined by H $( \mathrm { i . e . , } \ H \longmapsto X$ is a function, which will be denoted Ric). We will take the domain of Ric, denoted dom(Ric), to consist of Hamiltonian matrices H with two properties: H has no eigenvalues on the imaginary axis and the two subspaces in equation(12.3) are complementary. For ease of reference, these will be called the stability property and the complementarity property, respectively. This solution will be called the stabilizing solution. Thus, $X = \operatorname { R i c } ( H )$ and

$$\operatorname{Ric}: \operatorname{dom} (\operatorname{Ric}) \subset \mathbb {R} ^ {2 n \times 2 n} \longmapsto \mathbb {R} ^ {n \times n}.$$

Remark 12.1 It is now clear that to obtain the stabilizing solution to the Riccati equation, it is necessary to construct bases for the stable invariant subspace of H. One way of constructing this invariant subspace is to use eigenvectors and generalized eigenvectors of H. Suppose $\lambda _ { i }$ is an eigenvalue of H with multiplicity k (then $\lambda _ { i + j } = \lambda _ { i }$ for all $j = 1 , \ldots , k - 1 )$ , and let $v _ { i }$ be a corresponding eigenvector and $v _ { i + 1 } , \ldots , v _ { i + k - 1 }$ be the corresponding generalized eigenvectors associated with $v _ { i }$ and $\lambda _ { i }$ . Then vj are related by

$$
\begin{array}{l} (H - \lambda_ {i} I) v _ {i} \quad = 0 \\ (H - \lambda_ {i} I) v _ {i + 1} = v _ {i} \\ (H - \lambda_ {i} I) v _ {i + k - 1} = v _ {i + k - 2}, \\ \end{array}
$$
