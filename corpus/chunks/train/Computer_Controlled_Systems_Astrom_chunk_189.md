# Trajectory Following

From the preceding definitions and calculations, it is possible to determine a control sequence such that a desired state can be reached after at most n steps of time. Does reachability also imply that it is possible to follow a given trajectory in the state space? Assume that any $x(k)$ is given and that it is necessary to get to $x(k+1)$ . From (3.16) it can be seen that this is possible only if $\Gamma$ has rank n, that is, it is necessary but not sufficient to have n input signals. For a single-input-single-output system it is, in general, possible to reach desired states only at each nth sample point, provided that the desired pointe are known n steps ahead.

It is easier to make the output follow a given trajectory. Assume that the trajectory is given by $u_{c}(k)$ . The control signal u then should satisfy

$$y (k) = \frac {B (q)}{A (q)} u (k) = u _ {c} (k)$$

or

$$u (k) = \frac {A (q)}{B (q)} u _ {c} (k) \tag {3.20}$$

Assume that there are d steps of delay in the system. The generation of $u(k)$ is then causal only if the desired trajectory is known d steps ahead. The control signal then can be generated in real time. The control signal thus is obtained by sending the desired output trajectory through the inverse system A/B. Equation (3.20) has a unique solution if the signal $u_{c}(k)$ is such that there exists a $k_{0}$ such that $u(k)=0$ for all $k<k_{0}$ (compare with Sec. 2.6). The signal u is bounded if $u_{c}$ is bounded and if the system has a stable inverse.
