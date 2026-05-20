$$y (t) = 1 - e ^ {\alpha t} \left(\cos \beta t - \frac {\alpha}{\beta} \sin \beta t\right) \tag {7.72}$$

The “exponential envelope” depends on the real part of the roots, $\alpha = - \zeta \omega _ { n }$ , and the sinusoidal (damped) frequency depends on the imaginary part of the roots, $\beta = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } } = \omega _ { d }$ . The real and imaginary parts (?? and $\beta )$ are functions of damping ratio $\zeta$ and undamped natural frequency $\omega _ { n }$ . Figure 7.19 shows the unit-step response Eq. (7.72) for two cases: both with $\omega _ { n } = 1$ rad/s, and two damping ratios $\zeta = 0 . 2$ and 0.4. Clearly, the damping ratio $\zeta$ affects the peak value of the transient response.

Next, we present the performance equations for a step response. The peak time $t _ { p }$ is the time to reach the peak (maximum) output during the transient response. Figure 7.19 shows that the peak output occurs at one-half of the period of a damped sinusoidal cycle. The period of one cycle is $T _ { \mathrm { p e r i o d } } = 2 \pi / \omega _ { d }$ , where $\omega _ { d } = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ is the damped frequency. Therefore, the peak time is

$$t _ {p} = \frac {\pi}{\omega_ {n} \sqrt {1 - \zeta^ {2}}} \tag {7.73}$$

The peak or maximum output $y _ { \mathrm { m a x } }$ is obtained from the unit-step response Eq. (7.72) at peak time $t = \pi / \omega _ { d }$ , with the substitution $\beta = \omega _ { d }$

$$y _ {\max} = y (t _ {p}) = 1 - e ^ {\alpha \pi / \omega_ {d}} \left(\cos \pi - \frac {\alpha}{\omega_ {d}} \sin \pi\right) \tag {7.74}$$

![](image/a9a9b9e658c6ceff395448b2a2df816d925da7c23633a788d77b9511df307e31.jpg)

<details>
<summary>line</summary>

| Time, s | Damping ratio ζ = 0.2 | Damping ratio ζ = 0.4 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 3 | 1.5 | 1.25 |
| 6 | 0.7 | 0.95 |
| 10 | 1.15 | 1.0 |
| 15 | 1.0 | 1.0 |
| 20 | 1.0 | 1.0 |
| 25 | 1.0 | 1.0 |
</details>

Figure 7.19 Unit-step responses for a second-order system with $\omega _ { n } = 1$ rad/s.

Substituting for the real part of the roots $( \alpha = - \zeta \omega _ { n } )$ and the damped frequency $\omega _ { d } = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ in Eq. (7.74), we obtain the peak unit-step response

$$y _ {\max} = 1 + e ^ {- \zeta \pi / \sqrt {1 - \zeta^ {2}}} \tag {7.75}$$
