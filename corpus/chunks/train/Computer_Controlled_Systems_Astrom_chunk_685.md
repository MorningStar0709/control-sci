# 11.4 Linear Quadratic Gaussian Control

In the LQG-control problem, it is assumed that the system is governed by (11.3) and that the loss function is given by (11.9). The admissible controls are assumed to be such that $u(k)$ is a function of $Y_{k-1}$ or of $Y_{k-1}$ and $y(k)$ .

Theorem 11.2 and (11.30) still hold for the case of incomplete state information. Because (11.18) is not an admissible control strategy, the third term in (11.30) cannot be made equal to zero. The solution is given by the following theorem.

THEOREM 11.7 THE SEPARATION THEOREM Consider the system in (11.3). Let the admissible control strategies be such that $u(k)$ is a function of $Y_{k-1}$ . Assume that $S(k)$ is given by (11.17) with initial condition $S(N) = Q_0$ and with $Q_0$ positive semidefinite. If $\Gamma^T S(k)\Gamma + Q_2$ is positive definite then there exists a unique admissible control strategy

$$u (k) = - L (k) \hat {x} (k \mid k - 1) \tag {11.58}$$

that minimizes the expected loss (11.9). The minimum value of the loss function is given by

$$
\begin{array}{l} J = m _ {0} ^ {T} S (0) m _ {0} + \operatorname{tr} S (0) R _ {0} + \sum_ {k = 0} ^ {N - 1} \operatorname{tr} S (k + 1) R _ {1} \tag {11.59} \\ + \sum_ {k = 0} ^ {N - 1} \operatorname{tr} P (k) L ^ {T} (k) \left(\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}\right) L (k) \\ \end{array}
$$

Proof. The theorem follows directly from Theorem 11.2 and (11.22) and that $v(k)$ is independent of $u(k)$ and $x(k)$ . Equation (11.28) gives the value of the loss function.

Remark 1. The difference in the minimal losses given by (11.31) and (11.59) is due to the estimation of the state variables.

Remark 2. It is possible to modify Theorem 11.7 to other admissible control strategies—for instance, the case when $u(k)$ is allowed to be a function of $Y_{k-1}$ and $y(k)$ . It follows from (11.23) that the control law is given by [compare with (11.32)]

$$
\begin{array}{l} u (k) = - L (k) \hat {x} (k \mid k) - L _ {v} (k) \hat {v} (k \mid k) \\ = - L (k) \hat {x} (k \mid k - 1) - \left(L (k) K _ {f} (k) + L _ {v} (k) K _ {v} (k)\right) \left(y (k) - C \hat {x} (k \mid k - 1)\right) \\ = - \left(L (k) - M (k) C\right) \hat {x} (k \mid k - 1) - M (k) y (k) \tag {11.60} \\ \end{array}
$$

where $\hat{v}(k|k)$ is given by (11.50) and where

$$M (k) = L (k) K _ {f} (k) + L _ {v} (k) K _ {v} (k)$$

Further $L(k), L_{v}(k), K_{f}(k)$ , and $K_{v}(k)$ are given by (11.19), (11.24), (11.51), and (11.52), respectively.
