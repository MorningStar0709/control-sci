Since the peak time corresponds to the first peak overshoot, $\omega _ { d } t _ { p } = \pi$ Hence.

$$t _ {p} = \frac {\pi}{\omega_ {d}} \tag {5-20}$$

The peak time $t _ { p }$ corresponds to one-half cycle of the frequency of damped oscillation.

Maximum overshoot $M _ { p } { \mathrm { : } }$ : The maximum overshoot occurs at the peak time or at $t = t _ { p } = \pi / \omega _ { d }$ . Assuming that the final value of the output is unity, $M _ { p }$ is obtained from Equation (5–12) as

$$
\begin{array}{l} M _ {p} = c (t _ {p}) - 1 \\ = - e ^ {- \zeta \omega_ {n} (\pi / \omega_ {d})} \left(\cos \pi + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \pi\right) \\ = e ^ {- \left(\sigma / \omega_ {d}\right) \pi} = e ^ {- \left(\zeta / \sqrt {1 - \zeta^ {2}}\right) \pi} \tag {5-21} \\ \end{array}
$$

The maximum percent overshoot is $e ^ { - ( \sigma / \omega _ { d } ) \pi } \times 1 0 0 \%$

If the final value $c ( \infty )$ of the output is not unity, then we need to use the following equation:

$$M _ {p} = \frac {c (t _ {p}) - c (\infty)}{c (\infty)}$$

Settling time $t _ { s } \mathrm { : }$ : For an underdamped second-order system, the transient response is obtained from Equation (5–12) as

$$c (t) = 1 - \frac {e ^ {- \zeta \omega_ {n} t}}{\sqrt {1 - \zeta^ {2}}} \sin \left(\omega_ {d} t + \tan^ {- 1} \frac {\sqrt {1 - \zeta^ {2}}}{\zeta}\right), \quad \text { for } t \geq 0$$

Figure 5–10 Pair of envelope curves for the unitstep response curve of the system shown in Figure 5–6.   
![](image/67bb2cae823468bec90103cbf12572c7eda65c380cdac1793e768618ea87e332.jpg)

<details>
<summary>line</summary>

| t | c(t) for curve 1 | c(t) for curve 2 |
| --- | --- | --- |
| 0 | 0 | 0 |
| T | ~1.5 | ~0.8 |
| 2T | ~1.2 | ~0.9 |
| 3T | ~1.0 | ~0.95 |
| 4T | 1.0 | 1.0 |
</details>

The curves $1 \pm \left( e ^ { - \zeta \omega _ { n } t } / \sqrt { 1 - \zeta ^ { 2 } } \right)$ are the envelope curves of the transient response to a unit-step input. The response curve $c ( t )$ always remains within a pair of the envelope curves, as shown in Figure 5–10. The time constant of these envelope curves is $1 / \zeta \omega _ { n }$ .
