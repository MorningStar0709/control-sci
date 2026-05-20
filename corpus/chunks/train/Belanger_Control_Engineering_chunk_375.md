$$
\begin{array}{l} \left[ \begin{array}{c c} - z I + A - B K & B \\ C - D K & D \end{array} \right] \left[ \begin{array}{c} \mathbf {v} _ {1} \\ \mathbf {v} _ {2} + K \mathbf {v} _ {1} \end{array} \right] = \left[ \begin{array}{c} (- z I + A) \mathbf {v} _ {1} + B - B K \mathbf {v} _ {1} + B K \mathbf {v} _ {1} \\ C \mathbf {v} _ {1} + D v _ {2} - D K \mathbf {v} _ {1} + D K \mathbf {v} _ {1} \end{array} \right] \\ = \left[ \begin{array}{c} (- z I + A) \mathbf {v} _ {1} + B \mathbf {v} _ {2} \\ C \mathbf {v} _ {1} + D \mathbf {v} _ {2} \end{array} \right] = 0 \\ \end{array}
$$

in view of Equation 7.10. The matrix in Equation 7.11 is rank-deficient with $\zeta = z$ , and $z$ is a zero.

An important property of state feedback is that it preserves controllability. The following theorem states this precisely.

■ Theorem 7.2

A system controlled by state feedback is controllable with $u_{ex}$ as input if, and only if, the open-loop system is controllable.

Proof: Refer to Figure 7.2. Suppose the open-loop system is controllable. Then, for any state $\mathbf{x}_f$ and time $T > 0$ , there exists an input $\mathbf{u}^*(t)$ that takes the state from $\mathbf{x} = \boldsymbol{\theta}$ at $t = 0$ to $\mathbf{x} = \mathbf{x}_f$ at $t = T$ . Let the state evolution under the action of $\mathbf{u}^*(t)$ be $\mathbf{x}^*(t)$ [where, of course, $\mathbf{x}^*(T) = \mathbf{x}_f$ ]. Now, let $\mathbf{u}_{ex}(t) = \mathbf{u}^*(t) + K\mathbf{x}^*(t)$ . Clearly, $\mathbf{u}(t) = \mathbf{u}^{*}(t)$ and $\mathbf{x}(t) = \mathbf{x}^{*}(t)$ , so that the state of the closed-loop system at time $T$ is $\mathbf{x}_f$ . Thus, there exists an input $\mathbf{u}_{ex}(t)$ that takes the state of the closed-loop system from 0 to an arbitrary $\mathbf{x}_f$ at an arbitrary time $T$ , i.e., the closed-loop system is controllable.

If the open-loop system is not controllable, the state can never have a component along an uncontrollable state when driven from $\mathbf{x} = \mathbf{0}$ , regardless of what input $\mathbf{u}(t)$ is applied. This is true no matter how that input is generated, including by state feedback. Therefore, the closed-loop system is also uncontrollable.

From the modal viewpoint, an uncontrollable mode remains uncontrollable with state feedback. Recall that, if $s_i$ is an uncontrollable mode, the corresponding left eigenvector $\mathbf{w}_i^T$ of the system $A$ matrix satisfies $\mathbf{w}_i^T B = 0$ . Now, in such a case,

$$\mathbf {w} _ {i} ^ {T} (A - B K) = s _ {i} \mathbf {w} _ {i} ^ {T} - \mathbf {w} _ {i} ^ {T} B K = s _ {i} \mathbf {w} _ {i} ^ {T}$$

so $s_i$ is also an eigenvalue of the closed-loop system, with the same left eigenvector as before. Since the closed-loop $B$ matrix is still $B$ , and since $\mathbf{w}_i^T B = 0$ , the result follows.

In fact, uncontrollable modes are unchanged not only by state feedback, but by any other means of generating u.
