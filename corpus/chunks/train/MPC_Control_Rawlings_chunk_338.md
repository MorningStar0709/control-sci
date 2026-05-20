# 3.1.1 Types of Uncertainty

Robust control concerns control of systems that are uncertain in some sense so that predicted behavior based on the nominal system is not identical to actual behavior. Uncertainty may arise in different ways. The system may have an additive disturbance that is unknown, the state of the system may not be perfectly known, or the model of the system that is used to determine control may be inaccurate.

A system with additive disturbance satisfies the following difference equation

$$x ^ {+} = f (x, u) + w$$

The disturbance w in constrained optimal control problems is usually assumed to be bounded since it is impossible to ensure that a system with unbounded disturbances satisfies the usual state and control constraints. More precisely, we usually assume that w satisfies the constraint $w \in \mathbb { W }$ where W is a compact subset of $\mathbb { R } ^ { n }$ containing the origin.

The situation in which the state is not perfectly measured may be treated in several ways. In the stochastic optimal control literature, where the measured output is $\boldsymbol { y } = \boldsymbol { C } \boldsymbol { x } + \boldsymbol { \nu }$ and the disturbance w and measurement noise v are usually assumed to be Gaussian white noise processes, the state or hyperstate of the optimal control problem is the conditional density of the state x at time k given prior measurements $\{ y ( 0 ) , y ( 1 ) , \dotsc , y ( k - 1 ) \}$ . Because this density is usually difficult to compute and use, except in the linear case when it is provided by the Kalman filter, a suboptimal procedure is often adopted. In this suboptimal approach, the state x is replaced by its estimate xˆ in a control law determined under the assumption that the state is accessible. This procedure is usually referred to as certainty equivalence, a term that was originally employed for the linear quadratic Gaussian (LQG) or similar cases when this procedure did not result in loss of optimality. When $f ( \cdot )$ is linear, the evolution of the state estimate $\hat { x }$ may be expressed by a difference equation

$$\hat {x} ^ {+} = f (\hat {x}, u) + \xi$$

in which $\xi$ is the innovation process. In controlling $\hat { x }$ , we should ensure that the actual state x, which, if the innovation process is bounded, lies in a bounded, possibly time-varying neighborhood of $\hat { x }$ , satisfies the constraints of the optimal control problem.
