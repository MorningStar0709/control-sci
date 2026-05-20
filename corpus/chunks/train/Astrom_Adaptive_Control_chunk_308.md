# THEOREM 5.5 MRAS using the Lyapunov rule

Consider the problem of adapting a feedforward gain. Assume that the transfer function G is strictly positive real. Then the parameter adjustment rule

$$\frac {d \theta}{d t} = - \gamma u _ {\mathrm{c}} e \tag {5.40}$$

where $\gamma$ is a positive constant, makes the output error $e$ in Eqs. (5.36) go to zero.

The control law of Eq. (5.40) is very similar to the control law obtained by the MIT rule, Eq. (5.5). This is illustrated in Fig. 5.14, which shows block diagrams of both systems. The only difference between the systems is that the connection to the first multiplier comes from the model output for the MIT rule and from the command signal for the Lyapunov rule. This seemingly small difference has major consequences, however.

A remark on the assumptions It may seem strange that such drastically different behaviors can be obtained by minor modifications of the system. It also seems strange that it is possible to use arbitrarily high adaptation gains. This is because the assumption that a transfer function is positive real is very strong. It follows from Definition 5.5 that $\operatorname{Re} G(i\omega) \geq 0$ if the transfer function $G(s)$ is positive real. This means that the Nyquist curve of G is in the right half-plane. Such a system is stable under proportional feedback with arbitrarily high gain. The closed-loop system can be made arbitrarily insensitive to the gain variations. The result is of limited practical value because of the strong assumptions that are made.
