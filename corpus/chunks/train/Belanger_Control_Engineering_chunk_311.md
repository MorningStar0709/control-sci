Figure 6.1 Location of second-order system poles

![](image/5b11262e3b6505d3a4023fa4624eb93717c5966f9dca1f5f1c918bf0226d6880.jpg)

<details>
<summary>line</summary>

| ωt | Output (ζ=0.1) | Output (.707) | Output (.0.9) |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 2 | 1.7 | 1.4 | 0.8 |
| 4 | 1.6 | 1.0 | 0.9 |
| 6 | 0.5 | 0.8 | 0.9 |
| 8 | 1.4 | 1.1 | 0.9 |
| 10 | 1.3 | 1.1 | 0.9 |
| 12 | 0.7 | 0.9 | 0.9 |
| 14 | 1.2 | 1.0 | 0.9 |
| 16 | 1.2 | 1.0 | 0.9 |
| 18 | 1.0 | 1.0 | 0.9 |
| 20 | 0.9 | 1.0 | 0.9 |
</details>

Figure 6.2 Step responses, second-order Butterworth transfer function

The shape of the response depends only on $\zeta$ . Values of $\zeta$ near zero lead to fast rise time but large overshoot and long settling time; values near 1 yield small overshoots but slow rise time. The Butterworth value $\zeta = \sqrt{2}/2$ is often used as a good compromise between speed and stability. Process control applications often use $\zeta = 0.2155$ , the so-called quarter-cycle damping value (see Problem 6.5).

It can be shown [3] that the local maxima occur at times $t_{k}$ given by

$$t _ {k} = \frac {\pi + 2 k \pi}{\omega_ {0} \sqrt {1 - \zeta^ {2}}}, \quad k = 0, 1, 2, \dots \tag {6.14}$$

The highest maximum is the first one, for $k = 0$ ; therefore, the peak time $T_{p}$ is

$$T _ {p} = \frac {\pi}{\omega_ {0} \sqrt {1 - \zeta^ {2}}}. \tag {6.15}$$

The peak overshoot, obtained by evaluating $y(t)$ for $t = T_{p}$ , is

$$\text { peak overshoot } = 1 0 0 e ^ {- \zeta \pi / \sqrt {1 - \zeta^ {2}}}. \tag {6.16}$$

As for the settling time $T_{s}$ , it is approximately equal to the time at which the magnitude of the cosine in Equation 6.13 becomes 0.05; i.e., $T_{s}$ satisfies

$$\frac {1}{\sqrt {1 - \zeta^ {2}}} e ^ {- \zeta \omega_ {0} T _ {s}} = 0. 0 5$$

or, taking logarithms,

$$T _ {s} = \frac {1}{\zeta \omega_ {0}} \left(3 + \ln \frac {1}{\sqrt {1 - \zeta^ {2}}}\right). \tag {6.17}$$

Equations 6.16 and 6.17 support the conclusion reached by examination of Figure 6.2.

Of course, the all-pole second-order system is a special case. It is a useful special case, because a practical system often has a complex pole pair relatively close to the origin, with other stable poles and zeros farther away. The transfer function, expressed in partial fractions, would have the form

$$H _ {d} (s) = \frac {k \omega_ {0} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {0} s + \omega_ {0} ^ {2}} + \sum_ {i} \frac {A _ {i}}{s + s _ {i}}.$$
