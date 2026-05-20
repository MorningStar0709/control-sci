# Decoupled Command Signal and Disturbance Responses

Consider the process

$$A y = B u + v$$

and the controller

$$R u = T u _ {c} - S y$$

The closed-loop system is characterized by

$$y = \frac {B T}{A _ {c}} u _ {c} + \frac {R}{A _ {c}} v \tag {11.5}u = \frac {A T}{A _ {c}} u _ {c} - \frac {S}{A _ {c}} v$$

where $A_c = AR + BS$ is the closed-loop characteristic polynomial. Assume that no process zeros are canceled, and factor the characteristic polynomial as $A_c = A_oA_m$ . If we choose $T = T'A_o$ , Eqs. (11.5) become

$$y = \frac {B T ^ {\prime}}{A _ {m}} u _ {c} + \frac {R}{A _ {o} A _ {m}} vu = \frac {A T ^ {\prime}}{A _ {m}} u _ {c} - \frac {S}{A _ {o} A _ {m}} v$$

The command signal response is governed by the dynamics of $A_{m}$ , but the disturbance response is governed by the dynamics of $A_{o}A_{m}$ . In this sense it is thus coupling between the command signal response and the disturbance response. In some cases it is desirable that the dynamics of the command signal responses and the disturbance responses are completely decoupled. This can be achieved by requiring that $T = T'A_{o}$ and $R = R'A_{m}$ . The closed-loop system is then characterized by

$$
\begin{array}{l} y = \frac {B T ^ {\prime}}{A _ {m}} u _ {c} + \frac {R ^ {\prime}}{A _ {0}} v \\ u = \frac {A T ^ {\prime}}{A _ {m}} u _ {c} - \frac {S}{A _ {o} A _ {m}} v \\ \end{array}
$$

The Diophantine equation then becomes

$$A A _ {m} R ^ {\prime} + B S = A _ {o} A _ {m}$$

To have a causal controller, we must require that $\deg A_{m} \geq \deg A$ . The minimum-degree causal solution to this equation is such that $\deg S = \deg A + \deg A_{m} - 1$ . Furthermore, $\deg R = \deg A_{m} + \deg A_{o} - \deg A$ . To have a causal controller, we must thus require that $\deg S \leq \deg R$ . This implies that

$$\deg A + \deg A _ {m} - 1 \leq \deg A _ {m} + \deg A _ {o} - \deg A$$

Hence $\deg A_{0} \geq 2\deg A - 1$ . We thus find that the minimum-degree solution that decouples the response to command signals and disturbances is such that

$$\deg A _ {m} = n \quad \deg A _ {o} = 2 n - 1 \quad \deg R = \deg S = 2 n - 1$$

where $n = \deg A$ .

A design of this type can be very useful when there are very noisy measurements and a fast setpoint response is desired.
