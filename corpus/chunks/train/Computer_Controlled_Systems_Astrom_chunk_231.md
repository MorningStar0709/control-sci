Figure 4.2 Responses of the closed-loop system in Example 4.4. The initial condition is $x^{T}(0) = [1 - 1]$ , and the parameter values are $\omega h = 0.44$ and $\zeta = 0.707$ . The outputs for sampling periods $\omega = 0.5$ (dashed-dotted), $\omega = 1$ (dashed), and $\omega = 2$ (solid) are shown in (a), and the corresponding control signals are shown in (b), (c), and (d), respectively.

The expression shows that the magnitude of the control signal increases with increasing $\omega$ . Thus an increase in the speed of the response of the system will require an increase in the control signals. If the bounds on the control signal and typical disturbances are known, it is possible to determine reasonable values of $\omega$ . The consequences of different choices of $\omega$ when $x_{0} = 1$ and $v_{0} = 1$ are illustrated in Fig. 4.2. A larger $\omega$ gives a faster system but also larger control signals.

The selection of sampling periods for open-loop systems was discussed in Sec. 2.9. It was suggested that the sampling period can be chosen such that

$$N _ {r} \approx 4 - 1 0$$

where $N_{r}$ is the number of samples per rise time. Applying the same rule to closed-loop systems we find that the sampling period should be related to the desired behavior of the closed-loop system. It is convenient to introduce the parameter N defined by

$$N = \frac {2 \pi}{\omega h \sqrt {1 - \zeta^ {2}}} \tag {4.16}$$

This parameter gives the number of samples per period of dominating mode of the closed-loop system. Figure 4.3 shows the transient of the system for different values of N. There are small differences between the responses for N > 10. The responses obtained for N > 20 are indistinguishable in the graph.
