# 7.4.2 The Matrix Lyapunov Equation

If the system $\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}$ is controlled under the state feedback law $\mathbf{u} = -K\mathbf{x}$ , the closed-loop system is given by

$$\dot {\mathbf {x}} = (A - B K) \mathbf {x} \tag {7.20}$$

and the performance index of Equation 7.19 is

$$
\begin{array}{l} J = \int_ {0} ^ {\infty} [ \mathbf {x} ^ {T} (t) Q \mathbf {x} (t) + \mathbf {u} ^ {T} (t) R \mathbf {u} (t) ] d t \\ = \int_ {0} ^ {\infty} [ \mathbf {x} ^ {T} (t) Q \mathbf {x} (t) + \mathbf {x} ^ {T} (t) K ^ {T} R K \mathbf {x} (t) ] d t \\ = \int_ {0} ^ {\infty} \mathbf {x} ^ {T} (t) [ Q + K ^ {T} R K ] \mathbf {x} (t) d t. \tag {7.21} \\ \end{array}
$$

In view of Equations 7.20 and 7.21, we shall solve the following problem. Given

$$\dot {\mathbf {x}} = A \mathbf {x} \tag {7.22}$$

where $A$ is stable, calculate

$$J = \int_ {0} ^ {\infty} \mathbf {x} ^ {T} (t) S \mathbf {x} (t) d t \tag {7.23}$$

where $S$ is symmetric and positive semidefinite or definite. If we can solve this problem, then we merely substitute $A - BK$ for $A$ , and $Q + K^T RK$ for $S$ , to solve the problem defined by Equations 7.20 and 7.21. The solution is given by the following theorem.

■ Theorem 7.4 Let A have all its eigenvalues in the open LHP and let S be a symmetric, positive definite or semidefinite matrix. Then, for $\mathbf{x}(0) = \mathbf{x}_{0}$ ,

$$J = \int_ {0} ^ {\infty} \mathbf {x} ^ {T} (t) S \mathbf {x} (t) d t = \mathbf {x} _ {0} ^ {T} P \mathbf {x} _ {0}$$

where $P$ is a symmetric, positive definite or semidefinite matrix satisfying the matrix Lyapunov equation,

$$A ^ {T} P + P A = - S. \tag {7.24}$$

Proof: With $\mathbf{x}(0) = \mathbf{x}_0$ , we have $\mathbf{x}(t) = e^{At}\mathbf{x}_0$ and

$$
\begin{array}{l} J = \int_ {0} ^ {\infty} \mathbf {x} _ {0} ^ {T} e ^ {A ^ {T} t} S e ^ {A t} \mathbf {x} _ {0} d t \\ = \mathbf {x} _ {0} ^ {T} \left[ \int_ {0} ^ {\infty} e ^ {A ^ {T} t} S e ^ {A t} d t \right] \mathbf {x} _ {0} \\ = \mathbf {x} _ {0} ^ {T} P \mathbf {x} _ {0} \\ \end{array}
$$

with

$$P = \int_ {0} ^ {\infty} e ^ {A ^ {T} t} S e ^ {A t} d t. \tag {7.25}$$

Since $A$ is stable, $e^{At}$ has only negative exponential terms, so the integral of Equation 7.25 exists. To see that $P$ is symmetric, we calculate

$$P ^ {T} = \int_ {0} ^ {\infty} (e ^ {A t}) ^ {T} S (e ^ {A t}) d t = \int_ {0} ^ {\infty} e ^ {A ^ {T} t} S e ^ {A t} d t = P.$$

The matrix P is at least semidefinite, because

$$\mathbf {x} _ {0} ^ {T} P \mathbf {x} _ {0} = J = \int_ {0} ^ {\infty} \mathbf {x} ^ {T} (t) S \mathbf {x} (t) d t \geq 0$$
