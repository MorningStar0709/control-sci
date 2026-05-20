The adaptive controller is a dynamical system with five state variables that can be chosen to be the model output, the parameters, and the sensitivity derivatives. A block diagram of the system is shown in Fig. 5.4. The behavior of the system is now illustrated by a simulation. The parameters are chosen to be a = 1, b = 0.5, and $a_{m} = b_{m} = 2$ , the input signal is a square wave with amplitude 1, and $\gamma = 1$ . Figure 5.5 shows the results of a simulation. Figure 5.6 shows the parameter estimates for different values of the adaptation gain $\gamma$ . Notice that the parameters change most when the command signal changes and that the parameters converge very slowly. For $\gamma = 1$ , the value used in Fig. 5.5, the parameters have the values $\theta_{1} = 3.2$ and $\theta_{2} = 1.2$ at time t = 100. These values are far from the correct values $\theta_{1}^{0} = 4$ and $\theta_{2}^{0} = 2$ . However, the parameters will converge to the true values with increasing time. The convergence rate increases with increasing $\gamma$ , as is shown in Fig. 5.6.

![](image/71189152e8226f184ca642d2c8e3c062b262664aecd3037db7692d927bc1bfb8.jpg)  
Figure 5.5 Simulation of the system in Example 5.2 using an MRAS. The parameter values are a = 1, b = 0.5, $a_{m} = b_{m} = 2$ , and $\gamma = 1$ .

The fact that the control is quite good even at time t = 10 is a reflection of the fact that the parameter estimates are related to each other in a very special way, although they are quite far from their true values. This is illustrated in Fig. 5.7, where parameter $\theta_{2}$ is plotted as a function of $\theta_{1}$ for a simulation with a duration of 500 time units. Figure 5.7 shows that parameters do indeed approach their correct values as time increases. The parameter estimates quickly approach the line $\theta_{2} = \theta_{1} - a/b$ . This line represents parameter values such that the closed-loop system has correct steady-state gain. ☐

![](image/95f2360cbe4d7478860745d1bd7d477d2d90a583a30be40b539d86d7538e99e8.jpg)  
Figure 5.6 Controller parameters $\theta_{1}$ and $\theta_{2}$ for the system in Example 5.2 when $\gamma = 0.2, 1$ and 5.

![](image/5a5c588007a849246e9f7da45c166fc00cb56f5f82a6405cc0db2c880579f272.jpg)

<details>
<summary>line</summary>

| θ₁ | θ₂ |
| --- | --- |
| 0 | 0 |
| 1 | -1 |
| 2 | 0 |
| 3 | 1 |
| 4 | 2 |
</details>

Figure 5.7 Relation between controller parameters $\theta_{1}$ and $\theta_{2}$ when the system in Example 5.2 is simulated for 500 time units. The dashed line shows the line $\theta_{2} = \theta_{1} - a/b$ . The dot indicates the convergence point.
