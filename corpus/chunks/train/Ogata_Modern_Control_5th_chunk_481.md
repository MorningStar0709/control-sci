$$\omega_ {d} = \omega_ {n} \sqrt {1 - \zeta^ {2}} \tag {7-19}$$

On the other hand, the maximum overshoot $M _ { p }$ for the unit-step response is given by Equation (5–21), or

$$M _ {p} = e ^ {- (\zeta / \sqrt {1 - \zeta^ {2}}) \pi} \tag {7-20}$$

This maximum overshoot occurs in the transient response that has the damped natural frequency $\omega _ { d } = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ The maximum overshoot becomes excessive for values of. $\zeta < 0 . 4$ .

Since the second-order system shown in Figure 7–73 has the open-loop transfer function

$$G (s) = \frac {\omega_ {n} ^ {2}}{s (s + 2 \zeta \omega_ {n})}$$

for sinusoidal operation, the magnitude of $G ( j \omega )$ becomes unity when

$$\omega = \omega_ {n} \sqrt {\sqrt {1 + 4 \zeta^ {4}} - 2 \zeta^ {2}}$$

which can be obtained by equating $\left| G ( j \omega ) \right|$ to unity and solving for v. At this frequency, the phase angle of $G ( j \omega )$ is

$$\underline {{G (j \omega)}} = - \underline {{j \omega}} - \underline {{j \omega + 2 \zeta \omega_ {n}}} = - 9 0 ^ {\circ} - \tan^ {- 1} \frac {\sqrt {\sqrt {1 + 4 \zeta^ {4}} - 2 \zeta^ {2}}}{2 \zeta}$$

Thus, the phase margin $\gamma$ is

$$
\begin{array}{l} \gamma = 1 8 0 ^ {\circ} + \underline {{G (j \omega)}} \\ = 9 0 ^ {\circ} - \tan^ {- 1} \frac {\sqrt {\sqrt {1 + 4 \zeta^ {4}} - 2 \zeta^ {2}}}{2 \zeta} \\ = \tan^ {- 1} \frac {2 \zeta}{\sqrt {\sqrt {1 + 4 \zeta^ {4}} - 2 \zeta^ {2}}} \tag {7-21} \\ \end{array}
$$

Equation (7–21) gives the relationship between the damping ratio $\zeta$ and the phase margin $\gamma .$ (Notice that the phase margin g is a function only of the damping ratio z.)

Figure 7–74 Curve g (phase margin) versus z for the system shown in Figure 7–73.   
![](image/99b124becc8531d681f32c029d0b7d0c3d886c941bac78df87abdbc94e9774dd.jpg)

<details>
<summary>line</summary>

| ζ | γ |
| --- | --- |
| 0.0 | 0° |
| 0.4 | ~30° |
| 0.8 | ~60° |
| 1.2 | ~75° |
| 1.6 | ~85° |
| 2.0 | ~90° |
</details>

In the following, we shall summarize the correlation between the step transient response and frequency response of the standard second-order system given by Equation (7–16):

1. The phase margin and the damping ratio are directly related.Figure 7–74 shows a plot of the phase margin g as a function of the damping ratio $\zeta .$ . It is noted that for the standard second-order system shown in Figure 7–73,the phase margin $\gamma$ and the damping ratio $\zeta$ are related approximately by a straight line for $0 \leq \zeta \leq 0 . 6$ , as follows:
