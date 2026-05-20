# 7.4.3 The Optimal LQ Regulator

The optimal linear-quadratic regulator problem is stated as follows. Given the LTI system

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u}$$

and the initial state $\mathbf{x}(0)$ , calculate the state feedback gain matrix $K$ such that the control law $\mathbf{u}(t) = -K\mathbf{x}(t)$ minimizes the performance index

$$J = \int_ {0} ^ {\infty} \left[ \mathbf {x} ^ {T} (t) Q \mathbf {x} (t) + \mathbf {u} ^ {T} (t) R \mathbf {u} (t) \right] d t$$

where Q and R are symmetric and $Q \geq 0$ , R > 0.

The closed-loop system and performance index are described by Equations 7.20 and 7.21, repeated here for convenience:

$$
\begin{array}{l} \dot {\mathbf {x}} = (A - B K) \mathbf {x} \\ J = \int_ {0} ^ {\infty} \mathbf {x} ^ {T} (t) \left(Q + K ^ {T} R K\right) \mathbf {x} (t) d t. \\ \end{array}
$$

The solution begins with the observation that, in order for the problem to be of practical interest, it must be possible to obtain internal stability with linear state feedback. Thus, the system must be stabilizable; i.e., any unstable modes must be controllable. Controllability of the system guarantees stabilizability, of course, because in that case all modes are controllable.

We now derive a necessary condition to be satisfied by a stabilizing gain to lead to a minimum of J.

■ Theorem 7.6

For a stabilizing gain $K$ to minimize $J$ for all $\mathbf{x}(0)$ , it must satisfy the necessary condition

$$K = R ^ {- 1} B ^ {T} P \tag {7.27}$$

where P satisfies the matrix Riccati equation,

$$A ^ {T} P + P A - P B R ^ {- 1} B ^ {T} P + Q = 0. \tag {7.28}$$

Proof: From the preceding section and Equations 7.20 and 7.21, we have, for any stabilizing K,

$$J (K) = \mathbf {x} ^ {T} (0) P \mathbf {x} (0) \tag {7.29}$$

where P satisfies the matrix Lyapunov equation,

$$(A - B K) ^ {T} P + P (A - B K) = - Q - K ^ {T} R K. \tag {7.30}$$

Let us assume that there exists a gain that minimizes $J$ , and let $K^*$ be that gain. Let $P^*$ be the corresponding $P$ matrix; i.e., let

$$(A - B K ^ {*}) ^ {T} P ^ {*} + P ^ {*} (A - B K ^ {*}) = - Q - K ^ {* T} R K ^ {*}. \tag {7.31}$$
