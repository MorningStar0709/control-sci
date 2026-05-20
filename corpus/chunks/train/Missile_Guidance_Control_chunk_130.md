$$n \pi = \omega t _ {\text { peak }} \sqrt {1 - \zeta^ {2}} \Rightarrow t _ {\text { peak }} = \frac {n \pi}{\omega \sqrt {1 - \zeta^ {2}}} \bigg | _ {n = 0, 1, 2, \dots , \infty} \tag {3.68}$$

![](image/39dbde63445104bf6ccde41d05fc7e095c8c2d000761ab84757ede7e47cf9271.jpg)

<details>
<summary>line</summary>

| Time (T) | P_smax |
| --- | --- |
| T_R | 0.63 |
</details>

Fig. 3.20. Roll rate response.

The time of the first overshoot $( \mathrm { i } . \mathrm { e } . , n = 1 )$ is the largest overshoot. Next, we solve for the peak overshoot at $t _ { \mathrm { p e a k } }$ for $n = 1$ :

$$\alpha_ {\text { peak }} = - \alpha_ {0} e ^ {- \frac {\zeta \pi}{\sqrt {1 - \zeta^ {2}}}}. \tag {3.69}$$

Finally, we can solve for $\zeta$ from (3.69), giving

$$\zeta = \frac {\left| l n \left(- \frac {\alpha_ {\text { peak }}}{\alpha_ {0}}\right) \right|}{\sqrt {\pi^ {2} + \left[ l n \left(- \frac {\alpha_ {\text { peak }}}{\alpha_ {0}}\right) \right] ^ {2}}}, \tag {3.70}$$

and for ω from (3.68), yielding

$$\omega = \frac {\pi}{t _ {\text { peak }} \sqrt {1 - \zeta^ {2}}}. \tag {3.71}$$

A few words about the roll axis model are in order. The missile roll dynamics for stability axis roll rate, $P ,$ , can be modeled after the roll approximation of lateral/directional motion. This approximation ignores the coupling effects in the rotary cross terms and in sideslip angle $\beta .$ . The roll approximation for roll rate is given by the following simple transfer function:

$$\frac {P _ {\mathrm{stab}} (s)}{P _ {\mathrm{stab} _ {\mathrm{cmd}}} (s)} = \frac {1}{T _ {R} s + 1}, \tag {3.72}$$

where $T _ { R }$ is the augmented roll mode time constant with units of seconds. It should be noted that this represents the lower-order equivalent system of the full closed-loop airframe. The filter time constant may be found from linear analysis of the entire closed-loop system or by computing it with the augmented stability derivatives. From classical control theory, we note that the roll rate response for a step input command is as illustrated in Figure 3.20.

In Figure 3.20 we note that the time constant $T _ { R }$ corresponds to the time at which the roll rate response reaches 63% of its final value.
