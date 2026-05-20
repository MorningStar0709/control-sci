Global Properties We now investigate the global properties when the parameters are chosen in such a way that the equilibrium is stable. To get some guidelines for the analysis, we first simulate the system. In Fig. 6.2 we show a phase portrait for the case in which $\alpha = 0.1$ , $\gamma = 0.1$ , $\theta_0 = 1.5$ , $y_0 = 1$ , and $a = 0.9$ . It follows from Eqs. (6.9) that the equations have an equilibrium for $y = 1.0$ and $\hat{\theta} = 2.4$ and from condition (ii) in Eqs. (6.11) that the equilibrium is stable provided that $0 < \gamma < 0.22$ . The equilibrium is thus stable for the chosen value of the adaptation gain. Remember that the system is a discrete-time system. The discrete solution points are connected with straight lines to give a continuous graph. All trajectories shown in the simulation are approaching the equilibrium. Solutions with initial values $\hat{\theta}(0) = 0$ appear to have large excursions, and the trajectory with $\hat{\theta}(0) = 2.5$ seems to be oscillatory. To understand the behavior intuitively, we consider the equations for $y$ and $\hat{\theta}$ separately. It follows from Eqs. (6.8) that if $\hat{\theta}$ is constant, then the motion of $y$ is governed by

$$y (t + 1) = (\theta_ {0} - \hat {\theta}) y (t) + a + y _ {0}$$

This is a first-order difference equation with the equilibrium solution

$$y = f (\hat {\theta}) = \frac {a + y _ {0}}{1 + \hat {\theta} - \theta_ {0}} \tag {6.12}$$

![](image/5732e287e5de13d6f356aef7c369fa4a06371d0dc887ab292863a888e0fab1a9.jpg)

<details>
<summary>line</summary>

| y | θ̂ |
| --- | --- |
| -10 | 0.0 |
| 0 | 2.5 |
| 10 | 1.0 |
| 20 | 0.5 |
</details>

Figure 6.2 Phase portrait for the system in the stable case. Parameter values are $\alpha = 0.1$ , $\gamma = 0.1$ , $\theta_0 = 1.5$ , $y_0 = 1$ , and $\alpha = 0.9$ . The dashed lines indicate the interval $\theta_0 - 1 < \hat{\theta} < \theta_0 + 1$ . The dot is the equilibrium point.

If parameter $\hat{\theta}$ is constant, the solution is stable if

$$\theta_ {0} - 1 < \hat {\theta} < \theta_ {0} + 1$$
