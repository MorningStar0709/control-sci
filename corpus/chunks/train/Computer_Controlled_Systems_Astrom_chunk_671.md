# Example 11.3 LQ-control of the double integrator

To illustrate the dependence of the weighting matrices on the closed-loop poles, reconsider Example 11.1. Figure 11.5 shows the poles of the closed-loop system for different values of $\rho$ . For $\rho = 0$ the root locus starts at $z = -1$ and $z = 0$ . As $\rho$ increases the roots move toward the poles of $H(z), z = 1$ .

Theorem 11.3 shows that the LQ-controller gives a stable closed-loop system, that is, all the poles of the closed-loop system are within the unit circle. It is also possible to get the poles inside a circle with a radius less than 1. This is done by introducing the transformation

![](image/c97536260ca555a1df3414762b609edcf406f41750a6cb101cc4a7b0d3725196.jpg)

<details>
<summary>scatter</summary>

| Point | Real axis | Imaginary axis |
| --- | --- | --- |
| (a) | -0.5 | 0 |
| (b) | -0.2 | 0.3 |
| (c) | 0.3 | 0.4 |
| (d) | 0.6 | 0.3 |
</details>

Figure 11.5 Closed-loop poles given by (11.35) when the double integrator is controlled with the optimal controller for $\rho$ varying from 0 to $\infty$ . The stars indicate the closed-loop poles for (a) $\rho = 0.01563$ , (b) $\rho = 0.05$ , (c) $\rho = 0.5$ , and (d) $\rho = 10$ , which are the values used in Fig. 11.2.

$$\Phi \rightarrow \Phi / \bar {r}\Gamma \rightarrow \Gamma / \bar {r}$$

where $\bar{r} < 1$ , and then solving the linear quadratic problem for the system

$$x (k + 1) = \frac {1}{\bar {r}} \Phi x (k) + \frac {1}{\bar {r}} \Gamma u (k)$$

In the z-transform this implies that we make the substitution

$$z \rightarrow z \bar {r}$$

This is further discussed in Sec. 12.6.

Theorem 11.3 shows that the closed-loop system is stable when the LQ-controller is used. It is also possible to determine the gain margin of the closed-loop system. Consider the system of (11.3) with $v(k) = e(k) = 0$ . The pulse-transfer function of the open-loop system is

$$H (z) = C (z I - \Phi) ^ {- 1} \Gamma$$

Assume that only inputs and outputs are penalized in the loss function of $(11.9)$ , that is,

$$Q _ {1} = C ^ {T} C$$

and that $Q_{12} = 0$ . Let the system be controlled by the steady-state LQ state-feedback controller. The controller is then defined by the equations

$$S = \Phi^ {T} S \Phi + Q _ {1} - L ^ {T} R LL = R ^ {- 1} \Gamma^ {T} S \Phi \tag {11.36}R = \Gamma^ {T} S \Gamma + Q _ {2}$$

The algebraic Riccati equation (11.36) can be written

$$Q _ {1} = (z ^ {- 1} I - \Phi) ^ {T} S (z I - \Phi) + (z ^ {- 1} I - \Phi) ^ {T} S \Phi + \Phi^ {T} S (z I - \Phi) + L ^ {T}. R L$$
