# A.5 Pseudo-Inverse

The solution of $A x = y$ when A is invertible is $x = A ^ { - 1 }$ y where $A ^ { - 1 }$ is the inverse of A. Often an approximate inverse of $y = A x$ is required when A is not invertible. This is yielded by the pseudo-inverse $A ^ { \dagger }$ of $A ;$ if $A \in \mathbb { R } ^ { m \times n }$ , then $A ^ { \dag } \in \mathbb { R } ^ { n \times m }$ . The properties of the pseudo-inverse are illustrated in Figure A.2 for the case when $A \in \mathbb { R } ^ { 2 \times 2 }$ where both $\mathcal { R } ( A )$ and ${ \mathcal { N } } ( A )$ have dimension 1. Suppose we require a solution to the equation $A x \ : = \ : y$ . Since every $x \in \mathbb { R } ^ { 2 }$ is mapped into $\mathcal { R } ( A )$ , we see that a solution may only be obtained if $y \in \mathcal { R } ( A )$ . Suppose this is not the case, as in Figure A.2. Then the closest point, in the Euclidean sense, to $_ y$ in $\mathcal { R } ( A )$ is the point $y ^ { * }$ which is the orthogonal projection of y onto ${ \mathcal { R } } ( A ) , { \mathrm { i . e . , } } y - y ^ { * }$ is orthogonal to $\mathcal { R } ( A )$ . Since $y ^ { * } \in \mathcal { R } ( A )$ , there exists a point in $\mathbb { R } ^ { 2 }$ that A maps into $y ^ { * }$ . Now A maps any point of the form $x + h$ where $h \in { \mathcal { N } } ( A )$ into $A ( x + h ) = A x + A h = A x$ so that there must exist a point $x ^ { * } \in ( \mathcal { N } ( A ) ) ^ { \perp } \ = \ \mathcal { R } ( A ^ { \prime } )$ such that $A x ^ { * } = y ^ { * }$ , as shown in Figure A.2. All points of the form $x = x ^ { * } + h$ where $h \in { \mathcal { N } } ( A )$ are also mapped into $y ^ { * } ; x ^ { * }$ is the point of least norm that satisfies $A x ^ { * } = y ^ { * }$ where $y ^ { * }$ is that point in $\mathcal { R } ( A )$ closest, in the Euclidean sense, to y.

![](image/4775046289dd4ebe3206232d549a82dd1d89370caecc1e06b80e9fb253f34767.jpg)

<details>
<summary>text_image</summary>

Ax = b
ℝⁿ
ℝᵐ
ℝ(A')
r
A′
A
ℝ(A)
r
0
N(A)
n - r
0
N(A')
m - r
</details>

Figure A.1: The four fundamental subspaces of matrix A (after (Strang, 1980, p.88)). The dimension of the range of A and $A ^ { \prime }$ is $r ,$ the rank of matrix A. The nullspace of A and range of $A ^ { \prime }$ are orthogonal as are the nullspace of $A ^ { \prime }$ and range of A. Solutions to $A x = b$ exist for all b if and only if $m = r$ (rows independent). A solution to $A x = b$ is unique if and only if n = r (columns independent).
