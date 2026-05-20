which is justified because $C_{c}$ is nonsingular (the controllable canonical form is controllable). The matrix T is nonsingular since it is the product of two $n \times n$ nonsingular matrices.

From Equations 7.12 and 7.13,

$$\mathbf {y} = \mathbf {x} = T \mathbf {z}\mathbf {z} = T ^ {- 1} \mathbf {x}$$

and

$$\dot {\mathbf {z}} = T ^ {- 1} A T \mathbf {z} + T ^ {- 1} \mathbf {b} u$$

Comparison of this with Equation 7.13 yields the desired result.

■ Theorem 7.3

(Pole-placement theorem) Given an $n$ th-order, controllable system $(A, \mathbf{b})$ and a monic $n$ th-order polynomial $p(s)$ , there exists a unique gain vector $\mathbf{k}^T$ such that the characteristic polynomial of $A - \mathbf{bk}^T$ is $p(s)$ .

Proof: We begin with the controllable canonical form,

$$
A _ {c} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \dots & \dots & \dots & \dots & \dots \\ 0 & 0 & \dots & 0 & 1 \\ - a _ {0} & - a _ {1} & \dots & \dots & - a _ {n - 1} \end{array} \right], \quad \mathbf {b} _ {c} = \left[ \begin{array}{l} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right].
$$

Let $\kappa^T$ be a row vector of dimension $n$ . Then

$$
A _ {c} - \mathbf {b} _ {c} \boldsymbol {\kappa} ^ {T} = \left[ \begin{array}{c c c c} 0 & 1 & \dots & 0 \\ 0 & 0 & \dots & 0 \\ \dots & \dots & \dots & \dots \\ 0 & 0 & \dots & 1 \\ - a _ {0} - \kappa_ {1} & - a _ {1} - \kappa_ {2} & \dots & - a _ {n - 1} - \kappa_ {n} \end{array} \right].
$$

Since this matrix is in companion form, its characteristic polynomial is written directly as

$$p _ {c} (s) = s ^ {n} + \left(a _ {n - 1} + \kappa_ {n}\right) s ^ {n - 1} + \dots + \left(a _ {1} + \kappa_ {2}\right) s + \left(a _ {0} + \kappa_ {1}\right). \tag {7.15}$$

It is clear that the components of $\kappa$ can be picked to obtain any desired $n$ th-order, monic polynomial.

By Lemma 7.1, there exists a nonsingular $n \times n$ matrix $T$ such that $A = TA_{c}T^{-1}$ , $\mathbf{b} = T\mathbf{b}_{c}$ . Thus,

$$T (A _ {c} - \mathbf {b} _ {c} \kappa^ {T}) T ^ {- 1} = A - \mathbf {b k} ^ {T}$$

where

$$\mathbf {k} ^ {T} = \kappa^ {T} T ^ {- 1}. \tag {7.16}$$

The characteristic polynomials of $A_{c}-b_{c}\kappa^{T}$ and $A-b\kappa^{T}$ are the same, because similarity transformations preserve eigenvalues. Therefore, since there is a unique $\kappa^{T}$ that results in $p_{c}(s)=p(s)$ , $k^{T}$ is also unique. ■

We now present an algorithm for pole placement, based on Lemma 7.1 and Theorem 7.3. From Equation 7.16,

$$\mathbf {k} ^ {T} T = \kappa^ {T}.$$
