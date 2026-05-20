# 2.9.3 Unreachable Setpoints

In process control, steady-state optimization is often employed to determine an optimal setpoint, and MPC to steer the state of the system to this setpoint. Because of nonzero process disturbances and discrepancies between the models employed for steady-state optimization and for control, the optimal setpoint may be unreachable. Often an unreachable setpoint is then replaced by a reachable steady-state target that is closest to it. This standard procedure is suboptimal, however, and does not minimize tracking error. We show in this section that by defining performance relative to the unreachable setpoint rather than to the closest reachable target, it is possible to achieve improved performance. Standard MPC theory can no longer be used to analyze stability, however, because the value function for the new problem does not necessarily decrease along trajectories of the controlled system. With an infinite horizon, the cost function for the optimal control problem that yields MPC is unbounded.

Suppose the system to be controlled is described by

$$x ^ {+} = A x + B u$$

with control constraint $u \in \mathbb { U }$ , in which U is convex and compact. The setpoint pair $( x _ { \mathrm { s p } } , u _ { \mathrm { s p } } )$ is not necessarily reachable. The cost function $V ( \cdot )$ for the optimal control problem is

$$V _ {N} (x, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i))$$

in which $x ( i ) : = \phi ( i ; x , { \bf u } )$ , the solution of the dynamic system at time i if the initial state at time 0 is x and the control sequence is $\mathbf { u } : = \{ u ( 0 ) , u ( 1 ) , \ldots , u ( N - 1 ) \}$ . The stage cost $\ell ( \cdot )$ is defined to be a quadratic function of the distance from the setpoint

$$\ell (x, u) := (1 / 2) \big (| x - x _ {\mathrm{sp}} | _ {Q} ^ {2} + | u - u _ {\mathrm{sp}} | _ {R} ^ {2} \big)$$

in which Q and R are positive definite. For simplicity of exposition, a terminal constraint $x ( N ) = x _ { s }$ , in which $x _ { s }$ is defined subsequently, is included in the optimal control problem $\mathbb { P } _ { N } ( x )$ whose solution yields the model predictive controller; problem $\mathbb { P } _ { N } ( x )$ is therefore defined by

$$V _ {N} ^ {0} (x) = \min _ {\mathbf {u}} \left\{V _ {N} (x, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x) \right\}$$

in which the control sequence constraint set $\mathcal { U } _ { N } ( x )$ is defined by
