# 6.5 Bode’s Sensitivity Integral

In this section, we consider the design limitations imposed by the bandwidth constraints and the right-half plane poles and zeros using Bode’s sensitivity integral and Poisson integral. Let L be the open-loop transfer function with at least two more poles than zeros and let $p _ { 1 } , p _ { 2 } , \ldots , p _ { m }$ be the open right-half plane poles of L. Then the following Bode’s sensitivity integral holds:

$$\int_ {0} ^ {\infty} \ln | S (j \omega) | d \omega = \pi \sum_ {i = 1} ^ {m} \mathrm{Re} (p _ {i}) \tag {6.15}$$

In the case where L is stable, the integral simplifies to

$$\int_ {0} ^ {\infty} \ln | S (j \omega) | d \omega = 0 \tag {6.16}$$

These integrals show that there will exist a frequency range over which the magnitude of the sensitivity function exceeds one if it is to be kept below one at other frequencies, as illustrated in Figure 6.12. This is the so-called water bed effect.

![](image/c88ca638ea9f1a96f2ee7b2a08924740658864c6187dddf1db13f9c171cd1184.jpg)  
Figure 6.12: Water bed effect of sensitivity function

Suppose that the feedback system is designed such that the level of sensitivity reduction is given by

$$| S (j \omega) | \leq \epsilon < 1, \quad \forall \omega \in [ 0, \omega_ {l} ]$$

where $\epsilon > 0$ is a given constant.

Bandwidth constraints in feedback design typically require that the open-loop transfer function be small above a specified frequency, and that it roll off at a rate of more than one pole-zero excess above that frequency. These constraints are commonly needed to ensure stability robustness despite the presence of modeling uncertainty in the plant model, particularly at high frequencies. One way of quantifying such bandwidth constraints is by requiring the open-loop transfer function to satisfy

$$| L (j \omega) | \leq \frac {M _ {h}}{\omega^ {1 + \beta}} \leq \tilde {\epsilon} < 1, \quad \forall \omega \in [ \omega_ {h}, \infty)$$

where $\omega _ { h } > \omega _ { l }$ , and $M _ { h } > 0 , \beta > 0$ are some given constants.

Note that for $\omega \geq \omega _ { h }$

$$| S (j \omega) | \leq \frac {1}{1 - | L (j \omega) |} \leq \frac {1}{1 - \frac {M _ {h}}{\omega^ {1 + \beta}}}$$

and
