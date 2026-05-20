since the integrand is nonnegative. (S is positive semidefinite or definite.)

We now show that $P$ satisfies the matrix Lyapunov equation. Using Equation 7.25, we write

$$\dot {A} ^ {T} P + P A = \int_ {0} ^ {\infty} \left[ A ^ {T} e ^ {A ^ {T} t} S e ^ {A t} + e ^ {A ^ {T} t} S e ^ {A t} A \right] d t.$$

Recall that $(d / dt)e^{At} = Ae^{At} = e^{At}A$ , since $A$ and $e^{At}$ commute. Then

$$\frac {d}{d t} \bigg [ e ^ {A ^ {T} t} S e ^ {A t} \bigg ] = A ^ {T} e ^ {A ^ {T} t} S e ^ {A t} + e ^ {A ^ {T} t} S e ^ {A t} A$$

so that

$$
\begin{array}{l} A ^ {T} P + P A = \int_ {0} ^ {\infty} \frac {d}{d t} \biggl [ e ^ {A ^ {T} t} S e ^ {A t} \biggr ] d t \\ = \left. e ^ {A ^ {T} t} \right. S e ^ {A t} \big | _ {0} ^ {\infty} \\ = - S \\ \end{array}
$$

because $\lim_{t\to \infty}e^{At} = 0$ by stability, and $e^{A0} = I$ . That establishes the desired result.

Under certain conditions, the existence of a positive definite or semidefinite P that satisfies the matrix Lyapunov equation guarantees internal stability. That is the matter addressed by the following theorem. Before presenting the theorem, let us state one mathematical fact: a symmetric positive definite or positive semidefinite matrix S can always be written as a matrix product $S = (S^{1/2})^{T} S^{1/2}$ , where $S^{1/2}$ is called the square root of S. The matrix $S^{1/2}$ is not unique, and good algorithms to generate a square root of a particular structure exist, e.g., Cholesky decomposition algorithms [4].

■ Theorem 7.5

Suppose a $P \geq 0$ exists that satisfies the matrix Lyapunov equation, with $S \geq 0$ . Also suppose that the pair $(A, S^{1/2})$ is detectable, from the output $y = S^{1/2}x$ . Then the system $\dot{x} = Ax$ is internally stable.

Proof: We define the Lyapunov function,

$$V = \mathbf {x} ^ {T} P \mathbf {x}.$$

We calculate

$$\dot {V} = \dot {\mathbf {x}} ^ {T} P \mathbf {x} + \mathbf {x} ^ {T} P \dot {\mathbf {x}}$$

which, since $\dot{\mathbf{x}} = A\mathbf{x}$ , becomes

$$
\begin{array}{l} \dot {V} = \mathbf {x} ^ {T} A ^ {T} P \mathbf {x} + \mathbf {x} ^ {T} P A \mathbf {x} \\ = \mathbf {x} ^ {T} (A ^ {T} P + P A) \mathbf {x} = - \mathbf {x} ^ {T} S \mathbf {x} \\ = - \mathbf {x} ^ {T} (S ^ {1 / 2}) ^ {T} S ^ {1 / 2} \mathbf {x} = - (S ^ {1 / 2} \mathbf {x}) ^ {T} (S ^ {1 / 2} \mathbf {x}) = - \| S ^ {1 / 2} \mathbf {x} \| ^ {2}. \tag {7.26} \\ \end{array}
$$
