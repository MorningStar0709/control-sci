# A–10–15. Consider the system

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x}$$

where x is a state vector (n-vector) and A is an n\*n constant matrix. We assume that A is nonsingular. Prove that if the equilibrium state x=0 of the system is asymptotically stable (that is, if A is a stable matrix), then there exists a positive-definite Hermitian matrix P such that

$$\mathbf {A} ^ {*} \mathbf {P} + \mathbf {P A} = - \mathbf {Q}$$

where Q is a positive-definite Hermitian matrix.

Solution. The matrix differential equation.

$$\dot {\mathbf {X}} = \mathbf {A} ^ {*} \mathbf {X} + \mathbf {X A}, \quad \mathbf {X} (0) = \mathbf {Q}$$

has the solution

$$\mathbf {X} = e ^ {\mathbf {A} * t} \mathbf {Q} e ^ {\mathbf {A} t}$$

Integrating both sides of this matrix differential equation from t=0 to t=q, we obtain

$$\mathbf {X} (\infty) - \mathbf {X} (0) = \mathbf {A} ^ {*} \left(\int_ {0} ^ {\infty} \mathbf {X} d t\right) + \left(\int_ {0} ^ {\infty} \mathbf {X} d t\right) \mathbf {A}$$

Noting that A is a stable matrix and, therefore, $\mathbf { X } ( \infty ) = \mathbf { 0 }$ we obtain,

$$- \mathbf {X} (0) = - \mathbf {Q} = \mathbf {A} ^ {*} \left(\int_ {0} ^ {\infty} \mathbf {X} d t\right) + \left(\int_ {0} ^ {\infty} \mathbf {X} d t\right) \mathbf {A}$$

Let us put

$$\mathbf {P} = \int_ {0} ^ {\infty} \mathbf {X} d t = \int_ {0} ^ {\infty} e ^ {\mathbf {A} * t} \mathbf {Q} e ^ {\mathbf {A} t} d t$$

Note that the elements of $e ^ { \mathbf { A } t }$ are finite sums of terms like $e ^ { \lambda _ { i } t }$ , $t e ^ { \lambda _ { i } t } \ldots , t ^ { m _ { i } - 1 } e ^ { \lambda _ { i } t }$ where the, $\lambda _ { i }$ are the eigenvalues of A and $m _ { i }$ is the multiplicity of $\lambda _ { i } .$ . Since the $\lambda _ { i }$ possess negative real parts,

$$\int_ {0} ^ {\infty} e ^ {\mathbf {A} ^ {*} t} \mathbf {Q} e ^ {\mathbf {A} t} d t$$

exists. Note that

$$\mathbf {P} ^ {*} = \int_ {0} ^ {\infty} e ^ {\mathbf {A} ^ {*} t} \mathbf {Q} e ^ {\mathbf {A} t} d t = \mathbf {P}$$

Thus P is Hermitian (or symmetric if P is a real matrix). We have thus shown that for a stable A and for a positive-definite Hermitian matrix Q, there exists a Hermitian matrix P such that $\mathbf { A } ^ { * } \mathbf { P } + \mathbf { P } \mathbf { A } = - \mathbf { Q }$ We now need to prove that P is positive definite. Consider the following Her-. mitian form:
