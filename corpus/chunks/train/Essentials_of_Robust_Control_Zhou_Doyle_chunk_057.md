# 2.4 Invariant Subspaces

Let $A : \mathbb { C } ^ { n } \longmapsto \mathbb { C } ^ { n }$ be a linear transformation, λ be an eigenvalue of A, and x be a corresponding eigenvector, respectively. Then $A x = \lambda x$ and $A ( \alpha x ) = \lambda ( \alpha x )$ for any $\alpha \in \mathbb { C } .$ . Clearly, the eigenvector x defines a one-dimensional subspace that is invariant with respect to premultiplication by A since $A ^ { k } x = \lambda ^ { k } x , \forall k$ . In general, a subspace $S \subset \mathbb { C } ^ { n }$ is called invariant for the transformation A, or A-invariant, if $A x \in S$ for every $x \in S$ . In other words, that S is invariant for A means that the image of S under A is contained in $S \colon A S \subset S$ . For example, {0}, Cn, KerA, and ImA are all A-invariant subspaces.

As a generalization of the one-dimensional invariant subspace induced by an eigenvector, let $\lambda _ { 1 } , \ldots , \lambda _ { k }$ be eigenvalues of A (not necessarily distinct), and let $x _ { i }$ be the corresponding eigenvectors and the generalized eigenvectors. Then $S = \operatorname { s p a n } \{ x _ { 1 } , \ldots , x _ { k } \}$ is an A-invariant subspace provided that all the lower-rank generalized eigenvectors are included. More specifically, let $\lambda _ { 1 } = \lambda _ { 2 } = \cdot \cdot \cdot = \lambda _ { l }$ be eigenvalues of A, and let $x _ { 1 } , x _ { 2 } , \ldots , x _ { l }$ be the corresponding eigenvector and the generalized eigenvectors obtained through the following equations:

$$(A - \lambda_ {1} I) x _ {1} = 0(A - \lambda_ {1} I) x _ {2} = x _ {1}(A - \lambda_ {1} I) x _ {l} = x _ {l - 1}.$$

Then a subspace S with $x _ { t } \in S$ for some $t \leq l$ is an A-invariant subspace only if all lowerrank eigenvectors and generalized eigenvectors of $x _ { t }$ are in $S \ ( { \mathrm { i . e . , ~ } } x _ { i } \in S , \ \forall 1 \leq i \leq t )$ . This will be further illustrated in Example 2.1.

On the other hand, if S is a nontrivial subspace1 and is A-invariant, then there is $x \in S$ and λ such that $A x = \lambda x$ .

An A-invariant subspace $S \subset \mathbb { C } ^ { n }$ is called a stable invariant subspace if all the eigenvalues of A constrained to $S$ have negative real parts. Stable invariant subspaces will play an important role in computing the stabilizing solutions to the algebraic Riccati equations in Chapter 12.

Example 2.1 Suppose a matrix A has the following Jordan canonical form:
