# EXAMPLE 5.5 Stability depends on the signal amplitudes

Consider the system in Example 5.1. Let the transfer function $G$ be given by

$$G (s) = \frac {1}{s ^ {2} + a _ {1} s + a _ {2}}$$

Equation (5.13) then becomes

$$s ^ {3} + a _ {1} s ^ {2} + a _ {2} s + \mu = 0$$

where $\mu = \gamma y_{m}^{o}u_{c}^{o}k$ . The equation has all its roots in the left half-plane if

$$\gamma y _ {m} ^ {o} u _ {c} ^ {o} k < a _ {1} a _ {2} \tag {5.15}$$

Since this inequality involves the magnitude of the command signal, it may happen that the equilibrium solution corresponding to one command signal is stable and the solution corresponding to another command signal is unstable. This is illustrated by the simulation results shown in Fig. 5.8, where parameters are chosen so that $k = a_1 = a_2 = 1$ . In the simulation the adaptation rate $\gamma$ was adjusted to give a good response when $u_c$ is a square wave with unit amplitude. In this case we have $u_c^o = y_m^o = 1$ , and inequality (5.15) gives the stability condition $\gamma < 1$ . A reasonable value of $\gamma$ is $\gamma = 0.1$ , which was used in the simulation. Figure 5.8 shows clearly that the convergence rate depends on the magnitude of the command signal. Notice that the solution is unstable when the amplitude of $u_c$ is 3.5. The approximate model predicts instability for $u_c$ larger than 3.16. Also notice that the response is intolerably slow for low amplitudes of $u_c$ .

![](image/83f0ccf28ac67d2290e1cf116168a49ac63c732a2960cebaed2f22d16375cd2c.jpg)  
Figure 5.8 Simulation of the MRAS in Example 5.5. The command signal is a square wave with the amplitude (a) 0.1, (b) 1, and (c) 3.5. The model output $y_{m}$ is a dashed line; the process output is a solid line. The following parameters are used: $k = a_{1} = a_{2} = \theta^{0} = 1$ , and $\gamma = 0.1$ .

The example indicates clearly that the choice of adaptation gain is crucial and that the value chosen depends on the signal levels. Because of this it seems natural to modify the algorithm so that it does not depend on the signal levels. To do this, we will write the MIT rule as

$$\frac {d \theta}{d t} = \gamma \varphi e$$

where we have introduced $\varphi = -\partial e / \partial \theta$ . Introduce the following modified adjustment rule:

$$\frac {d \theta}{d t} = \frac {\gamma \varphi e}{\alpha + \varphi^ {T} \varphi} \tag {5.16}$$
