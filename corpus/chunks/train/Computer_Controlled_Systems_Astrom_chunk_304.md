# Improved Response to Disturbances

We will now modify the controller to improve its response to disturbances. For this purpose we will assume that there is a process disturbance v that acts at the process input and measurement noise that acts at the process output e. This is illustrated in the block diagram of Fig. 5.3. The system in Fig. 5.3 is described by the equations.

$$A x = B (u + v)y = x + e \tag {5.32}R u = T u _ {c} - S y$$

Solving for the signals x, y, and u we get

$$x = \frac {B T}{A R + B S} u _ {c} + \frac {B R}{A R + B S} v - \frac {B S}{A R + B S} ey = \frac {B T}{A R + B S} u _ {c} + \frac {B R}{A R + B S} v + \frac {A R}{A R + B S} e \tag {5.33}u = \frac {A T}{A R + B S} u _ {c} - \frac {B S}{A R + B S} v - \frac {A S}{A R + B S} e$$

These equations tell how the closed-loop system responds to command signals and disturbances. We will assume that the design is performed in such a way that the closed-loop system is always stable. The characteristic polynomial $A_{cl} = AR + BS$ then has all its roots inside the unit disc.

First, consider the situation when the load disturbance v is a step. The steady-state response is then given by the static gain. To avoid that there is a steady-state error we must require that the static gain from the disturbance v to x is zero. This means that $B(1)R(1)=0$ . If the process itself has a nonzero gain, that is, if $B(1)\neq0$ then we must require that $R(1)=0$ . This means that z-1 is a factor of $R(z)$ or that the controller is required to have integral action.

Periodic signals with period $n \cdot h$ can be eliminated in a similar way by requiring that $z^{n} - 1$ is a factor of $R(z)$ . This follows from the observation that a signal with period $n \cdot h$ satisfies the difference equation

$$v ((k + n) h) - v (k h) = (q ^ {n} - 1) v (k h) = 0$$

In a similar way a sinusoidal load disturbance with frequency $\omega_{0}$ will not give any steady-state deviation if the polynomial $R(z)$ has the factor $z^{2}-2z\cos\omega_{0}h+1$ . This follows because the sinusoid $\sin\omega_{0}t$ satisfies the difference equation

$$y (k h) - (2 \cos \omega_ {0} h) y (k h - h) + y (k h - 2 h) = 0$$

which can be verified by a direct calculation.
