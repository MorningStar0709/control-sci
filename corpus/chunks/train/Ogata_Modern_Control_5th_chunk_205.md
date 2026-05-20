$$c (t) = \frac {\omega_ {n}}{2 \sqrt {\zeta^ {2} - 1}} e ^ {- (\zeta - \sqrt {\zeta^ {2} - 1}) \omega_ {n} t} - \frac {\omega_ {n}}{2 \sqrt {\zeta^ {2} - 1}} e ^ {- (\zeta + \sqrt {\zeta^ {2} - 1}) \omega_ {n} t}, \quad \text { for } t \geq 0 \tag {5-28}$$

Note that without taking the inverse Laplace transform of $C ( s )$ we can also obtain the time response c(t) by differentiating the corresponding unit-step response, since the unit-impulse function is the time derivative of the unit-step function. A family of unit-impulse response curves given by Equations (5–26) and (5–27) with various values of $\zeta$ is shown in Figure 5–14. The curves $c ( t ) / \omega _ { n }$ are plotted against the dimensionless variable $\omega _ { n } t ,$ and thus they are functions only of $\zeta .$ . For the critically damped and overdamped cases, the unit-impulse response is always positive or zero; that is, $c ( t ) \geq 0$ . This can be seen from Equations (5–27) and (5–28). For the underdamped case, the unit-impulse response $c ( t )$ oscillates about zero and takes both positive and negative values.

![](image/31d40223d21f861ab43bffc78c541f9c3656372fc8bbd7797ee2420896524a1a.jpg)

<details>
<summary>line</summary>

| ωₙt | ζ = 0.1 | ζ = 0.3 | ζ = 0.5 | ζ = 0.7 | ζ = 1.0 |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 2 | 0.8 | 0.6 | 0.4 | 0.3 | 0.2 |
| 4 | 0.2 | 0.1 | 0.0 | -0.2 | -0.4 |
| 6 | -0.2 | -0.1 | -0.1 | -0.1 | -0.1 |
| 8 | 0.4 | 0.2 | 0.1 | 0.0 | -0.1 |
| 10 | -0.2 | -0.1 | -0.1 | -0.1 | -0.1 |
| 12 | -0.2 | -0.1 | -0.1 | -0.1 | -0.1 |
</details>

Figure 5–14   
Unit-impulse response curves of the system shown in Figure 5–6.

Figure 5–15 Unit-impulse response curve of the system shown in Figure 5–6.   
![](image/a9774685ceeefd92dae407a63249f6abaab2bcd441fa06946c4d3d1f9de10715.jpg)

<details>
<summary>line</summary>

| t | c(t) |
| --- | --- |
| 0 | 0 |
| t_p | 0 |
| >t_p | Decreasing from peak to baseline |
</details>

From the foregoing analysis, we may conclude that if the impulse response $c ( t )$ does not change sign, the system is either critically damped or overdamped, in which case the corresponding step response does not overshoot but increases or decreases monotonically and approaches a constant value.

The maximum overshoot for the unit-impulse response of the underdamped system occurs at

$$t = \frac {\tan^ {- 1} \frac {\sqrt {1 - \zeta^ {2}}}{\zeta}}{\omega_ {n} \sqrt {1 - \zeta^ {2}}}, \quad \text { where } 0 < \zeta < 1 \tag {5-29}$$
