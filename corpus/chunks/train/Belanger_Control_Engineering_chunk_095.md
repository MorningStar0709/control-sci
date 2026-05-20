# 3.4.2 Poles and Zeros

From Equation 3.19, the transfer function is written as

$$H (s) = C (s I - A) ^ {- 1} B + D.$$

This is a matrix of dimensions $m \times r$ . To obtain the element $H_{ij}(s)$ , we write $C$ in terms of its rows and $B$ in terms of its columns:

$$
H (s) = \left[ \begin{array}{c} \mathbf {c} _ {1} ^ {T} \\ \mathbf {c} _ {2} ^ {T} \\ \vdots \\ \mathbf {c} _ {m} ^ {T} \end{array} \right] (s I - A) ^ {- 1} \left[ \begin{array}{l l l l} \mathbf {b} _ {1} & \mathbf {b} _ {2} & \dots & \mathbf {b} _ {r} \end{array} \right] + D.
$$

By the rules of matrix multiplication, we see that

$$H _ {i j} (s) = \mathbf {c} _ {i} ^ {T} (s I - A) ^ {- 1} \mathbf {b} _ {j} + d _ {i j}. \tag {3.28}$$

This is written as

$$H _ {i j} (s) = \frac {\mathbf {c} _ {i} ^ {T} A d j (s I - A) \mathbf {b} _ {j} + d _ {i j} \det (s I - A)}{\det (s I - A)}.$$

The matrix $Adj(sI - A)$ is a matrix of polynomials of order $n - 1$ at most. Pre- or postmultiplication by a vector results in weighted sums of such polynomials, so that $\mathbf{c}_i^T Adj(sI - A)\mathbf{b}_i$ is a polynomial of degree $n - 1$ at most. The denominator, $\det(sI - A)$ , is a polynomial of degree $n$ .

The numerator of $H_{ij}(s)$ is of degree n because of the term $d_{ij}\det(sI-A)$ ; $H_{ij}(s)$ [and $H(s)$ ] is said to be proper because its numerator and denominator have the same degree. If D=0, $H_{ij}(s)$ [and $H(s)$ ] is strictly proper because the degree of the numerator is less than that of the denominator. It is not possible for the matrix transfer function of an LTI system represented by state equations to have an excess of zeros over poles.

The denominator of $H_{ij}$ is $\det(sI - A)$ . Since the roots of the denominator are the eigenvalues of A, it follows that all poles of $H(s)$ are eigenvalues of A. The converse does not necessarily hold. If $\det(sI - A)$ has a factor $(s - s_i)^k$ , where k is the multiplicity of $s_i$ , it is possible that all $H_{ij}(s)$ also contain this factor in their numerators, in which case cancellation takes place and $s_i$ is not a pole.

Note that B, C, and D do not influence the pole locations at all. They do, however, influence the zeros, because they enter in the numerators. The reader will recall that, for a scalar-valued $H(s)$ , $s_{0}$ is a zero if $H(s_{0}) = 0$ . For the multi-input, multi-output (MIMO) case, we define a transmission zero as a complex number $s_{0}$ that satisfies

$$H (s _ {0}) \mathbf {w} = \mathbf {0} \tag {3.29}$$

for some $\mathbf{w} \neq \mathbf{0}$ .
