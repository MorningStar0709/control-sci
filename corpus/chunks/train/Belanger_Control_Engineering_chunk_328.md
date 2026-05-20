# 6.3.2 The Bode Gain-Phase Relationship

The Bode theorem [5] applies to systems that are stable and minimum phase, i.e., with no poles or zeros in the closed RHP. For such systems,

$$\neq G (j \omega) = \frac {\pi}{2} \frac {d}{d u} (\ln | G (j \omega) |) \left| _ {\omega_ {0}} \right.+ \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \left[ \frac {d}{d u} (\ln | G (j \omega) |) - \frac {d}{d u} (\ln | G (j \omega) |) \right. \Bigg | _ {\omega_ {0}} \Bigg ] W (u) d u \tag {6.25}$$

where

$$u = \ln (\omega / \omega_ {0})W (u) = \ln \coth \left| \frac {u}{2} \right|.$$

Since $u = \ln \omega - \ln \omega_{0}$ , the plot of $\ln |G(j\omega)|$ versus u is just the plot of $\ln |G(j\omega)|$ versus $\ln \omega$ shifted to a new abscissa origin, $\ln \omega_{0}$ . The slope of $\ln |G(j\omega)|$ plotted against $\ln \omega$ is the same as that of $\log |G(j\omega)|$ versus $\log \omega$ , and is the slope of the Bode magnitude plot (in decibels) divided by 20.

Figure 6.17 shows the weighting function $W(u)$ . It weighs the contributions of frequencies near $\omega_0$ heavily, with much less emphasis on those frequencies relatively far from $\omega_0$ . If the slope of the Bode magnitude plot is nearly constant in the vicinity of $\omega_0$ , the bracketed term in the integral will be small near $\omega_0$ and the integral itself will be small. The integral will contribute significantly to the phase at frequencies where the slope of the magnitude curve is changing. Because the Bode magnitude plot is basically a set of straight lines, the first term in Equation 6.25 dominates, so

![](image/6be8ed07126cb6e642ad661b763284d29c5907858fdc18171578d0b39c39db01.jpg)

<details>
<summary>line</summary>

| ω/ω₀ | W |
| --- | --- |
| 0.1 | 0.2 |
| 0.2 | 0.4 |
| 0.5 | 1.0 |
| 1.0 | 6.5 |
| 2.0 | 3.0 |
| 5.0 | 1.0 |
| 10.0 | 0.2 |
</details>

Figure 6.17 Weighting function for Bode's theorem

$$\neq G (j \omega_ {0}) \sim 9 0 ^ {\circ} \times \frac {\text { slope of Bode magnitude curve at } \omega_ {0} (\mathrm{db/decade})}{2 0}. \tag {6.26}$$

The practical consequence is this: since the phase must be greater (i.e., less negative) than $-180^{\circ}$ at crossover, the slope of the magnitude curve must be greater than -40 db/decade (less than 40 db/decade in magnitude) for a relatively wide range of frequencies around $\omega_{0}$ . If the crossover frequency is located in a region of approximately constant slope, that slope should be -20 db/decade.
