# Criteria

In steady-state regulation it makes sense to express the criteria in terms of the steady-state variances of the output and the control signals. This leads to the performance criterion

$$J = E \{y ^ {2} (t) + \rho u ^ {2} (t) \} \tag {4.3}$$

where E denotes mathematical expectation with respect to the noise process acting on the system. The control law minimizing (4.3) is the linear quadratic

Gaussian (LQG) controller. If $\rho = 0$ , then the resulting controller is called the minimum-variance (MV) controller.

The properties of the control signal when the minimum-variance controller is used depend critically on the sampling interval. A short sampling interval gives large variance in the control signal, and a long sampling interval gives a low variance. Notice that the loss function (4.3) is defined in discrete time, that is, only the behavior at the sampling instances is considered.

To define the design problem, it is also necessary to define the admissible controllers. It will be assumed that $u(t)$ is allowed to be a function of $y(t), y(t - 1), \ldots, u(t - 1), u(t - 2), \ldots$ .
