where $s _ { 1 } = \big ( \zeta + \sqrt { \zeta ^ { 2 } - 1 } \big ) \omega _ { n }$ and $s _ { 2 } = ( \zeta - \sqrt { \zeta ^ { 2 } - 1 } ) \omega _ { n }$ Thus, the response. $c ( t )$ includes two decaying exponential terms.

When $\zeta$ is appreciably greater than unity, one of the two decaying exponentials decreases much faster than the other, so the faster-decaying exponential term (which corresponds to a smaller time constant) may be neglected. That is, $\operatorname { i f } - s _ { 2 }$ is located very much closer to the jv axis than $- s _ { 1 }$ Awhich means $\left| { { s } _ { 2 } } \right| \leqslant \left| { { s } _ { 1 } } \right| )$ , then for an approximate solution we may neglect $- s _ { 1 }$ .This is permissible because the effect of $- s _ { 1 }$ on the response is much smaller than that $\mathrm { o f } - s _ { 2 }$ , since the term involving $s _ { 1 }$ in Equation (5–17) decays much faster than the term involving $s _ { 2 }$ . Once the faster-decaying exponential term has disappeared, the response is similar to that of a first-order system, and $C ( s ) / R ( s )$ may be approximated by

$$\frac {C (s)}{R (s)} = \frac {\zeta \omega_ {n} - \omega_ {n} \sqrt {\zeta^ {2} - 1}}{s + \zeta \omega_ {n} - \omega_ {n} \sqrt {\zeta^ {2} - 1}} = \frac {s _ {2}}{s + s _ {2}}$$

This approximate form is a direct consequence of the fact that the initial values and final values of both the original $C ( s ) / R ( s )$ and the approximate one agree with each other.

With the approximate transfer function $C ( s ) / R ( s )$ , the unit-step response can be obtained as

$$C (s) = \frac {\zeta \omega_ {n} - \omega_ {n} \sqrt {\zeta^ {2} - 1}}{(s + \zeta \omega_ {n} - \omega_ {n} \sqrt {\zeta^ {2} - 1}) s}$$

The time response $c ( t )$ is then

$$c (t) = 1 - e ^ {- (\zeta - \sqrt {\zeta^ {2} - 1}) \omega_ {n} t}, \quad \text { for } t \geq 0$$

This gives an approximate unit-step response when one of the poles of $C ( s ) / R ( s )$ can be neglected.

Figure 5–7 Unit-step response curves of the system shown in Figure 5–6.   
![](image/d5669b77029037ebfb922e25aac4fe27d15ef0d6b5337a9d563a6ccf0f91c92e.jpg)

<details>
<summary>line</summary>
