# The Deterministic Case

The deterministic case, where $v(k) = 0$ and $e(k) = 0$ in (11.3), is first considered. The system is thus described by

$$x (k + 1) = \Phi x (k) + \Gamma u (k) \tag {11.16}$$

where $x(0)$ is given. The problem is now to determine the control sequence $u(0), u(1), \ldots, u(N - 1)$ such that the loss function in (11.9) is minimized.

The idea behind the derivation of the control law is to use the principle of optimality and dynamic programming. The principle of optimality states that an optimal policy has the property that whatever the initial state and initial decision are the remaining decisions must be optimal with respect to the state resulting from the first decision. By using this idea and starting from the end time N and going backwards in time, it is possible to determine the best control law for the last step independent of how the state at time N - 1 was reached. The remaining loss-to-go will now depend on the state at time N - 1. Iterating backwards to the initial time k = 0 determines the optimal-control policy. The procedure is called dynamic programming and was introduced by Bellman. The solution is given by the following theorem.

![](image/9796d115b774dedf358d7d8a7db790c67eb26d42478a7dc61b9ee1a7026510b0.jpg)

<details>
<summary>text_image</summary>

V_k
0 k-1 k N Time
Iteration direction
</details>

Figure 11.1 Illustration of the iteration procedure using dynamic programming.

THEOREM 11.1 LQ-CONTROL OF A DETERMINISTIC SYSTEM Consider the system of (11.16). Allow $u(k)$ to be a function of $x(k), x(k - 1), \ldots$ . We introduce

$$
\begin{array}{l} S (k) = \Phi^ {T} S (k + 1) \Phi + Q _ {1} - \left(\Phi^ {T} S (k + 1) \Gamma + Q _ {1 2}\right) \tag {11.17} \\ \times \left(\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}\right) ^ {- 1} \left(\Gamma^ {T} S (k + 1) \Phi + Q _ {1 2} ^ {T}\right) \\ \end{array}
$$

with end condition $S(N) = Q_{0}$ . Assume that $Q_{0}$ is positive semidefinite and that $Q_{2} + \Gamma^{T} S(k)\Gamma$ is positive definite. Then there exists a unique, admissible, control strategy

$$u (k) = - L (k) x (k) \tag {11.18}$$

where

$$L (k) = \left(Q _ {2} + \Gamma^ {T} S (k + 1) \Gamma\right) ^ {- 1} \left(\Gamma^ {T} S (k + 1) \Phi + Q _ {1 2} ^ {T}\right) \tag {11.19}$$

that minimizes the loss (11.9). The minimal value of the loss is

$$\min J = V _ {0} = x ^ {T} (0) S (0) x (0)$$

Further $S(k)$ is positive semidefinite.
