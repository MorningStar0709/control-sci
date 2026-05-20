Unstable Local Equilibria We now investigate what happens when parameters are such that the local equilibrium is unstable. We first observe that the instabilities may occur by violating any of the conditions given in Eqs. (6.11). Analyzing how the eigenvalues change with the parameters shows that the eigenvalue passes the unit circle with complex values if condition (i) is violated, through z = -1 if condition (ii) is violated and through z = 1 if condition (iii) is violated. We consider the situation in which the value of the adaptation gain is too large. Increasing the gain means that the solution will become unstable with period 2. Consider the case in which $\theta_{0} = 1$ , $\alpha = 0.1$ , $y_{0} = 1$ , and $\alpha = 0.9$ . The equilibrium is y = 1 and $\theta = 1.9$ . It follows from the stability criterion that the equilibrium is stable if $\gamma < 0.22$ . With $\gamma - 0.5$ the linearized closed-loop system is unstable. Figure 6.3 shows a simulation of the system. The behavior of the system is typical for the case with unmodeled dynamics. The output y and the parameter estimate $\hat{\theta}$ appear to approach their equilibrium values. The equilibrium is unstable and a diverging oscillation with period 2 appears when y and $\hat{\theta}$ come sufficiently close to their equilibrium. The variables then oscillate with large excursions. When this happens, the modeling error becomes less significant, and the process output y and the parameter estimate $\hat{\theta}$ approach their equilibrium values. The process then repeats all over again. The phenomenon that has been observed in many adaptive systems is called bursting.

![](image/d41667207ef7c3662881abd8cd12ffca3376a942bf1e66966043527b36d1e5c8.jpg)

<details>
<summary>line</summary>

| Time | y | θ̂ |
| --- | --- | --- |
| 0 | 3.0 | 1.5 |
| 50 | 1.0 | 2.5 |
| 100 | 2.5 | 2.5 |
| 150 | 1.0 | 2.5 |
| 200 | 1.0 | 2.5 |
</details>

Figure 6.3 Simulation of a simple adaptive controller with unmodeled dynamics. The equilibrium values of y and $\hat{\theta}$ are indicated by solid straight lines. The true parameter value $\theta_{0}$ is indicated by a dashed straight line.
