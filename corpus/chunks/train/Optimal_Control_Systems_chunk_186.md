# 3.5 Infinite-Time LQR System II

In this section, we examine the state regulator system with infinite time interval for a linear time-invariant (LTI) system. Let us consider the

plant as

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t) \tag {3.5.1}$$

and the cost functional as

$$J = \frac {1}{2} \int_ {0} ^ {\infty} [ \mathbf {x} ^ {\prime} (t) \mathbf {Q x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R u} (t) ] d t \tag {3.5.2}$$

where, $\mathbf{x}(t)$ is nth order state vector; $\mathbf{u}(t)$ is rth order control vector; A is nxn-order state matrix; B is rxr-order control matrix; Q is nxn-order, symmetric, positive semidefinite matrix; R is rxr-order, symmetric, positive definite matrix. First of all, let us discuss some of the implications of the time-invariance and the infinite final-time.

1. The infinite time interval case is considered for the following reasons:

(a) We wish to make sure that the state-regulator stays near zero state after the initial transient.   
(b) We want to include any special case of large final time.

2. With infinite final-time interval, to include the final cost function does not make any practical sense. Hence, the final cost term involving $\mathbf{F}(t_{f})$ does not exist in the cost functional (3.5.2).

3. With infinite final-time interval, the system (3.5.1) has to be completely controllable. Let us recall that this controllability condition of the plant (3.5.1) requires that the controllability matrix (see Appendix B)

$$
\left[ \begin{array}{l l} \mathbf {B} & \mathbf {A B} \dots \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right] \tag {3.5.3}
$$

must be nonsingular or contain n linearly independent column vectors. The controllability requirement guarantees that the optimal cost is finite. On the other hand, if the system is not controllable and some or all of those uncontrollable states are unstable, then the cost functional would be infinite since the control interval is infinite. In such situations, we cannot distinguish optimal control from the other controls. Alternatively, we can assume that the system (3.5.1) is completely stabilizable.
