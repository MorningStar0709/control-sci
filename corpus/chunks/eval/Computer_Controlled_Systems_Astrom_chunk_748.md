# Example 12.10 LQG control with unstable process zero

Consider the same system as in Examples 12.8 and 12.9. Instead of using a minimum-variance control law we will now use an LQG strategy. To do this the parameter $\rho$ in the control strategy must be chosen. To guide this choice we will first calculate the variances of the output and control signals obtained for different values of the loss function. The results are shown in Fig. 12.8. The value $\rho = 0$ corresponds to a minimum-variance strategy. This gives a control signal with large variance. Compare with Example 12.9. The variance of the control signal decreases rapidly with increasing $\rho$ . The variance of the output increases slowly.

By choosing a reasonable value of $\rho$ it is possible to have a control strategy that gives an output variance that is only marginally higher than with minimum-variance control and a variance of the control signal that is substantially lower. A reasonable value is $\rho = 1$ . This gives $Ey^{2} = 1.39$ and $Eu^{2} = 0.22$ , which can be compared with minimum-variance control that gives $Ey^{2} = 1.05$ and $Eu^{2} = 14.47$ .

The input- and output signals obtained with $\rho = 1$ are shown in Fig. 12.9. Compare with the corresponding curves for minimum-variance control in Example 12.9. The fluctuations in the output are a little larger, but the fluctuations in the control signal are substantially smaller. This way of applying LQG control where the control weighting is used as a design parameter is very typical.

![](image/4756292f5eb45c33b431c4757031bede4bb4251e42101de853b8efdf5fdb9bb2.jpg)

<details>
<summary>line</summary>

| Weighting ρ | Variance (Solid Line) | Variance (Dashed Line) |
| --- | --- | --- |
| 0.001 | ~1.0 | 10.0 |
| 1 | ~1.5 | ~0.5 |
| 1000 | ~5.0 | ~0.0 |
</details>

Figure 12.8 Variances of input u (dashed line) and output y (solid line) for LQG controllers having different values of the control weighting $\rho$ for the system in Example 12.10
