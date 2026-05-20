Now we proceed to the torque expression. There are no torque components due to $\Delta y$ , $\Delta\dot{y}$ , and $\Delta u$ . If $\Delta y = \Delta\dot{y} = \Delta\dot{\theta} = \Delta u = 0$ and $\Delta\theta \neq 0$ , the bar is displaced by $L\Delta\theta/2$ at each end, causing spring forces of magnitude $KL\Delta\theta/2$ . The net torque is $-2KL^{2}\Delta\theta/4$ . Similarly, the net torque due to $\Delta\dot{\theta}$ is $-DL^{2}\Delta\dot{\theta}/2$ . Therefore,

$$\Delta T = - \frac {K}{2} L ^ {2} \Delta \theta - \frac {D}{2} L ^ {2} \Delta \dot {\theta}$$

and the state equations of the linearized system are

$$
\begin{array}{l} \Delta \dot {y} = \Delta v \\ \Delta \dot {\theta} = \Delta \omega \\ \Delta \dot {v} = - 2 \frac {K}{M} \Delta y - 2 \frac {D}{M} \Delta v + 1 \frac {1}{M} \Delta u \\ \Delta \dot {\omega} = - \frac {K L ^ {2}}{2 J} \Delta \theta - \frac {D L ^ {2}}{2 J} \Delta \omega \\ \end{array}
$$

or, in vector-matrix form,

$$
\frac {d}{d t} \left[ \begin{array}{l} \Delta y \\ \Delta \theta \\ \Delta v \\ \Delta \omega \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ - \frac {2 K}{M} & 0 & - \frac {2 D}{M} & 0 \\ 0 & - \frac {K L ^ {2}}{2 J} & 0 & - \frac {D L ^ {2}}{2 J} \end{array} \right] \left[ \begin{array}{l} \Delta y \\ \Delta \theta \\ \Delta v \\ \Delta \omega \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ \frac {1}{M} \\ 0 \end{array} \right] \Delta u.
$$
