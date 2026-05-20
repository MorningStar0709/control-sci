# An Interpretation

Theorem 12.4 establishes the relation between LQG-control and pole-placement control because the polynomial $C(z)$ is the observer polynomial $A_{o}(z)$ and $P(z)$ is the polynomial $A_{c}(z)$ . The LQG-controller may thus be considered as a pole-placement controller where the observer polynomial $A_{o}(z)$ is obtained from the noise characteristics and the polynomial $A_{o}(z)$ from the solution to an optimization problem. The solution to the optimization problem also tells what solution of the Diophantine equation we should choose.

![](image/ee7775985a384c3ce61fd960257df6ea549b252fccbc7b87f16c2b4053e7f87c.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0.0 | 5.0 |
| 10 | -2.0 | 4.8 |
| 20 | 1.5 | 5.2 |
| 30 | -1.8 | 4.9 |
| 40 | 2.2 | 5.1 |
| 50 | -3.5 | 4.7 |
| 60 | 1.8 | 5.3 |
| 70 | -2.5 | 4.6 |
| 80 | 2.8 | 5.4 |
| 90 | -1.2 | 4.8 |
| 100 | 1.0 | 5.0 |
</details>

Figure 12.9 Simulation of the for the system in Example 12.10 using the LQG-controller with $\rho = 1$ . The output obtained with the minimum-variance controller ( $\rho = 0$ ) is shown in dashed. Also compare with Fig. 12.6.
