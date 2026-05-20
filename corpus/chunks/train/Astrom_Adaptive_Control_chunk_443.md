# Analysis of a Simple MRAS

A simple model-reference adaptive system for a process of first order was derived in Example 5.2 by using the MIT rule. In Example 5.7 the same problem was considered, and an MRAS was obtained by using Lyapunov's stability theory. We now use averaging theory to investigate the properties of the controller. In designing the adaptive controller it is assumed that the nominal transfer function of the process is

$$G (s) = \frac {b}{s + a} \tag {6.56}$$

which is not necessarily the true transfer function of the process. The desired closed-loop system has the transfer function

$$G _ {m} (s) = \frac {b _ {m}}{s + a _ {m}}$$

A model-reference adaptive control law was derived in Example 5.7 by using Lyapunov theory. A block diagram of the closed-loop system is given in

Fig. 5.11. The system is described by the equations

$$
\begin{array}{l} \frac {d \hat {\theta} _ {1}}{d t} = - \gamma u _ {c} e \\ \frac {d \hat {\theta} _ {2}}{d t} = \gamma y e \tag {6.57} \\ \end{array}
e = y \dots y _ {m}y = G (p) uy _ {m} = G _ {m} (p) u _ {c}u = \hat {\theta} _ {1} u _ {c} \cdot \hat {\theta} _ {2} y
$$

where $u_{r}$ is the reference signal, u is the process input, y is the process output, $y_{m}$ is the output of the reference model, e is the error, $\hat{\theta}_{1}$ is the adjustable feedforward gain, and $\hat{\theta}_{2}$ is the adjustable feedback gain.

It is not possible to give a complete analysis of Eqs. (6.57) for general reference signals; approximations must be made even in a simple case like this. We now investigate the adaptive system when the reference signal is sinusoidal. The equilibrium points are first explored, and the behavior in their neighborhood is then investigated by averaging and linearization.
