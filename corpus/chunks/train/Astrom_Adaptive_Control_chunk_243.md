To solve the design problem, it is necessary to solve the spectral factorization problem of Eq. (4.45) and to solve the Diophantine equation Eq. (4.43). The solution to the LQG problem given by Theorem 4.3 is closely related to the pole placement design problem. The solution to the spectral factorization problem gives the desired closed-loop poles. The second part of the algorithm can be interpreted as a pole placement problem.

An alternative solution to the design problem is to use a state space formulation. The process model of Eq. (4.39) can be written in state space form as

$$x (t + 1) = \bar {A} x (t) + \bar {B} u (t) + \bar {K} e (t) \tag {4.46}y (t) = \bar {C} x (t) + e (t)$$

where the matrices $\bar{A}$ , $\bar{B}$ , $\bar{C}$ , and $\bar{K}$ are given in the canonical form

$$
\hat {A} = \left( \begin{array}{c c c c c} - a _ {1} & 1 & 0 & \dots & 0 \\ \vdots & & \ddots & & \\ - a _ {n - 1} & 0 & & \dots & 1 \\ - a _ {n} & 0 & & \dots & 0 \end{array} \right)

\bar {B} = \left( \begin{array}{c c c c c c} 0 & \dots & 0 & b _ {0} & \dots & b _ {m} \end{array} \right) ^ {T}

\bar {C} = \left( \begin{array}{c c c c} 1 & 0 & \dots & 0 \end{array} \right)

\bar {K} = \left( \begin{array}{l l l} c _ {1} - a _ {1} & \dots & c _ {n} - a _ {n} \end{array} \right) ^ {T}
$$

where $m = n - d_{0}$ . The model in Eq. (4.46) is called the innovation model, and $\bar{K}$ is the optimal steady-state gain in the Kalman filter, that is, $\hat{x}(t+1|t) = x(t+1)$ . It is also possible to derive the filter for $\hat{x}(t|t)$ , which is given by

$$\dot {x} (t | t) = \left(q I - \bar {A} + \bar {K} \bar {C}\right) ^ {- 1} (\bar {B} u (t) + \bar {K} y (t))$$

By using the definitions of $\bar{A},\bar{K}$ , and $\bar{C}$ it is easily seen that $\det (qI - \bar{A} +\bar{K}\bar{C}) = C(q)$ . That is, the optimal observer polynomial is equal to $C(q)$ .

Introduce the loss function

$$J _ {x} = E \left\{\sum_ {t = 1} ^ {N} x ^ {T} (t) Q _ {1} x (t) + \rho u ^ {2} (t) + x ^ {T} (N) Q _ {0} x (N) \right\} \tag {4.47}$$

The optimal controller is given by

$$u (t) = - L (t) \hat {x} (t | t) \tag {4.48}$$

where $L(t)$ is a time-varying feedback gain given through a Riccati equation

$$S (t) = \left(\bar {A} - \bar {B} L (t)\right) ^ {T} S (t + 1) \left(\bar {A} - \bar {B} L (t)\right) + Q _ {1} + \rho L ^ {T} (t) L (t) \tag {4.49}L (t) = \left(\rho + \bar {B} ^ {T} S (t + 1) \bar {B}\right) ^ {- 1} \bar {B} ^ {T} S (t + 1) \bar {A}$$

with $S(N) = Q_0$ . The limiting controller

$$\tilde {L} = \lim _ {t \rightarrow \infty} L (t)$$

is such that the closed-loop characteristic equation is

$$P (q) = \det (q - \bar {A} + \ddot {B} \bar {L}) = 0$$

where $P(q)$ is the same as in Eq. (4.44).

The two solutions to the LQG control problem suggest two ways to construct indirect linear quadratic self-tuning regulators. In both algorithms it is first necessary to estimate the A, B, and C polynomials in the process model of Eq. (4.39). This can be done by using the recursive maximum-likelihood method or the extended least-squares method. This leads to the following algorithm.
