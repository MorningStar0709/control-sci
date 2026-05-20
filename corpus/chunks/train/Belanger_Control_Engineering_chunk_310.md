# 6.2.3 Transient Response

The expression relating the time-domain response of the closed loop to that of the open loop is quite complex. It cannot be used practically to infer closed-loop behavior from the open-loop transient response. Inferences about the closed-loop time response are more easily made from consideration of the pole-zero pattern

The all-pole second-order transfer function is a convenient starting point. Let

$$\frac {y}{y _ {d}} = H _ {d} (s) = \frac {\omega_ {0} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {0} s + \omega_ {0} ^ {2}}, \quad \zeta \geq 0. \tag {6.11}$$

Here, $\zeta$ is the damping factor. For $\zeta = \sqrt{2} / 2$ , $H_{d}$ is the second-order Butterworth low-pass filter.

The poles of $H_{d}(s)$ are

$$s _ {1}, s _ {1} ^ {*} = - \zeta \omega_ {0} \pm j \omega_ {0} \sqrt {1 - \zeta^ {2}}. \tag {6.12}$$

The poles are complex if $0 \leq \zeta < 1$ . Figure 6.1 shows how the poles vary as a function of $\zeta$ . Note that $|s_1| = |s_1^*| = \omega_0$ if the poles are complex.

The unit-step response is calculated from

$$
\begin{array}{l} y (s) = \frac {1}{s} H _ {d} (s) = \frac {\omega_ {0} ^ {2}}{s (s ^ {2} + 2 \zeta \omega_ {0} s + \omega_ {0} ^ {2})} \\ = \frac {1}{s} - \frac {s + 2 \zeta \omega_ {0}}{s ^ {2} + 2 \zeta \omega_ {0} s + \omega_ {0} ^ {2}}. \\ \end{array}
$$

Using a table of Laplace transforms and assuming complex poles,

$$
\begin{array}{l} y (t) = 1 - e ^ {- \zeta \omega_ {0} t} \left(\cos \omega_ {0} \sqrt {1 - \zeta^ {2}} t - \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {0} \sqrt {1 - \zeta^ {2}} t\right) \\ = 1 - \frac {1}{\sqrt {1 - \zeta^ {2}}} e ^ {- \zeta \omega_ {0} t} \cos [ \omega_ {0} \sqrt {1 - \zeta^ {2}} t + \phi ] \tag {6.13} \\ \end{array}
$$

where $\phi = \tan^{-1}\frac{\zeta}{\sqrt{1 - \zeta^2}}.$

Step responses are plotted in Figure 6.2, for a few values of $\zeta$ . The responses are plotted against $\omega_{0}t$ rather than t, to show the scaling effect of $\omega_{0}$ . The larger $\omega_{0}$ , the faster the response; what happens at t = 1 s for $\omega_{0} = 1$ rad/s occurs at t = 1 ms for $\omega_{0} = 1000$ rad/s.

![](image/2a75a9a841ae90e43931dc8783cd88c52f6cab00d8d8e7c354c9307fb83fa9fb.jpg)

<details>
<summary>other</summary>

| Point Label | Frequency (ω₀) |
| --- | --- |
| ζ = 0.1 | -jω₀ |
| ζ = 0.7 | -jω₀ |
| ζ = 1 | -jω₀ |
| ζ = -0.7 | -jω₀ |
| ζ = -1 | -jω₀ |
The diagram is a closed arc in the complex plane, with dashed lines indicating the direction of the phase axis.
</details>
