| θ̂₁ | θ̂₂ |
| --- | --- |
| -20 | 0 |
| -10 | 10 |
| 0 | 20 |
| 10 | 10 |
| 20 | 0 |
</details>

![](image/5b9cdb64b0e3ed92140aa13e3ca5ed8b29d3865f3befe1dab1b087a3bfafe0b9.jpg)

<details>
<summary>contour</summary>

| θ̂₁ | θ̂₂ |
| --- | --- |
| -20 | 0 |
| -10 | 5 |
| 0 | 10 |
| 10 | 15 |
| 20 | 20 |
</details>

Figure 6.16 Phase plane of the controller parameters (a) in the nominal case of $G(s) = 2/(s + 1)$ and (b) in the case of unmodeled dynamics Eq. (6.63). The dashed lines are the equilibrium sets of the parameters in the nominal case.

It is usually difficult to go beyond the local analysis. However, in this particular case it is possible to obtain the global properties of the averaged equation. Outside the equilibrium set of Eq. (6.64), the averaged equations (Eqs. 6.65) can be divided to give

$$\frac {d \bar {\theta} _ {2}}{d \bar {\theta} _ {1}} = - \frac {G (0) \bar {\theta} _ {1}}{1 + \bar {\theta} _ {2} G (0)}$$

This differential equation has the solution

$$\bar {\theta} _ {2} ^ {2} + \frac {2}{G (0)} \bar {\theta} _ {2} + \bar {\theta} _ {1} ^ {2} = \text { const }$$

The parameters of the averaged equations will thus move along circular paths with the center at $(0, -1/G(0))$ . The motion is clockwise for $\bar{\theta}_{2} > \bar{\theta}_{1} - 1/G(0)$ and counterclockwise for $\bar{\theta}_{2} < \bar{\theta}_{1} - 1/G(0)$ . The motion slows down and stops when the parameters reach the equilibrium set

$$\left\{\bar {\theta} _ {1}, \bar {\theta} _ {2} | \hat {\theta} _ {1} > 0, \bar {\theta} _ {2} = \bar {\theta} _ {1} - 1 / G (0) \right\}$$
