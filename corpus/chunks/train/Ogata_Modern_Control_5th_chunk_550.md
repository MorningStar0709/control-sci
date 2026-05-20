# A–7–17. For the standard second-order system

$$\frac {C (s)}{R (s)} = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}$$

show that the bandwidth $\omega _ { b }$ is given by

$$\omega_ {b} = \omega_ {n} \left(1 - 2 \zeta^ {2} + \sqrt {4 \zeta^ {4} - 4 \zeta^ {2} + 2}\right) ^ {1 / 2}$$

Note that $\omega _ { b } / \omega _ { n }$ is a function only of z. Plot a curve of $\omega _ { b } / \omega _ { n }$ versus $\zeta .$

Solution. The bandwidth $\omega _ { b }$ is determined from $| C \big ( j \omega _ { b } \big ) / R \big ( j \omega _ { b } \big ) \big | = - 3$ dB. Quite often, instead of –3 dB, we use –3.01 dB, which is equal to 0.707. Thus,

$$\left| \frac {C (j \omega_ {b})}{R (j \omega_ {b})} \right| = \left| \frac {\omega_ {n} ^ {2}}{(j \omega_ {b}) ^ {2} + 2 \zeta \omega_ {n} (j \omega_ {b}) + \omega_ {n} ^ {2}} \right| = 0. 7 0 7$$

Then

$$\frac {\omega_ {n} ^ {2}}{\sqrt {\left(\omega_ {n} ^ {2} - \omega_ {b} ^ {2}\right) ^ {2} + \left(2 \zeta \omega_ {n} \omega_ {b}\right) ^ {2}}} = 0. 7 0 7$$

from which we get

$$\omega_ {n} ^ {4} = 0. 5 \left[ \left(\omega_ {n} ^ {2} - \omega_ {b} ^ {2}\right) ^ {2} + 4 \zeta^ {2} \omega_ {n} ^ {2} \omega_ {b} ^ {2} \right]$$

![](image/ac4aee993671e92d9f531bcdb996c292c0cdea521f505efdc8c6eff26a20fc4a.jpg)

<details>
<summary>line</summary>

| ζ | ω_b / ω_n |
| --- | --- |
| 0.0 | 1.58 |
| 0.2 | 1.52 |
| 0.4 | 1.38 |
| 0.6 | 1.18 |
| 0.8 | 0.90 |
| 1.0 | 0.65 |
</details>

Figure 7–134 Curve of $\omega _ { b } / \omega _ { n }$ versus $\zeta ,$ where $\omega _ { b }$ is the bandwidth.

By dividing both sides of this last equation by $\omega _ { n } ^ { 4 }$ , we obtain

$$1 = 0. 5 \left\{\left[ 1 - \left(\frac {\omega_ {b}}{\omega_ {n}}\right) ^ {2} \right] ^ {2} + 4 \zeta^ {2} \left(\frac {\omega_ {b}}{\omega_ {n}}\right) ^ {2} \right\}$$

Solving this last equation for $\left( \omega _ { b } / \omega _ { n } \right) ^ { 2 }$ yields

$$\left(\frac {\omega_ {b}}{\omega_ {n}}\right) ^ {2} = - 2 \zeta^ {2} + 1 \pm \sqrt {4 \zeta^ {4} - 4 \zeta^ {2} + 2}$$

Since $\left( \omega _ { b } / \omega _ { n } \right) ^ { 2 } > 0$ , we take the plus sign in this last equation. Then

$$\omega_ {b} ^ {2} = \omega_ {n} ^ {2} \left(1 - 2 \zeta^ {2} + \sqrt {4 \zeta^ {4} - 4 \zeta^ {2} + 2}\right)$$

or

$$\omega_ {b} = \omega_ {n} \left(1 - 2 \zeta^ {2} + \sqrt {4 \zeta^ {4} - 4 \zeta^ {2} + 2}\right) ^ {1 / 2}$$

Figure 7–134 shows a curve relating $\omega _ { b } / \omega _ { n }$ versus $\zeta .$
