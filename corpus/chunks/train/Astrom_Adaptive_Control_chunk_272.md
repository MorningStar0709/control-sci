The input $u_{c}$ is a sinusoid with frequency 1 rad/s, and the parameter values are k = 1 and $k_{0} = 2$ . Figure 5.3 shows that the parameter converges toward the correct value reasonably fast when the adaptation gain is $\gamma = 1$ and that the process output approaches the model output. Figure 5.3 also shows that the convergence rate depends on the adaptation gain. It is thus important to know a reasonable value of this parameter. Intuitively, we may expect that parameters converge slowly for small $\gamma$ and that the convergence rate increases with $\gamma$ . Simulation experiments indicate that this is true for small values of $\gamma$ but also that the behavior is quite unpredictable for large $\gamma$ . ☐

![](image/d62d0236e07e27c7bdecee41130139ca94ac0c3838b34bd24952aa89538104bd.jpg)  
Figure 5.3 Simulation of an MRAS for adjusting a feedforward gain. The process (solid line) and the model (dashed line) outputs are shown in the upper graph for $\gamma = 1$ . The controller parameter is shown in the lower graph when the adaptation gain $\gamma$ has the values 0.5, 1, and 2.

An example of a practical problem that fits this formulation is control of robots with unknown load, in which the process transfer function from the motor current to the angular velocity is

$$G (s) = \frac {k _ {I}}{J s}$$

where $k_{I}$ is the current to torque constant and J is the unknown moment of inertia. Another example is the dynamics of a CD player, in which the sensitivity of the laser diode is the unknown process parameter.

A remark on notation In analyzing the MRAS with time-varying parameters it is important to consider the fact that the parameter $\theta$ is time-varying. The expression

$$G (p) (\theta u)$$

where $p = d / dt$ is the differential operator should be interpreted as the differential operator $G(p)$ acting on the signal $\theta u$ . When $\theta$ is time-varying, this is different from $\theta G(p)u$ . For example, if $G(p) = p$ , we have

$$G (p) (\theta u) = p (\theta u) = \theta \frac {d u}{d t} + \frac {d \theta}{d t} u = \theta (p u) + u (p \theta)$$

Care must thus be taken in manipulating expressions and block diagrams.

Notice that no approximations were needed in Example 5.1. When the MIT rule is applied to more complicated problems, however, it is necessary to use approximations to obtain the sensitivity derivatives. This is illustrated by another example.
