Analysis of the simplest particle filter. The simplest particle filter has well-known weaknesses that limit its use as a practical method for state estimation. The variances in both the particle locations and the filter weights can increase without bound as time increases and more measurements become available. Consider first the particle locations. For even the simple linear model with Gaussian noise, we have

$$x _ {i} (k + 1) = A x _ {i} (k) + B u (k) + G w _ {i} (k)x _ {i} (0) \sim N (\overline {{x}} (0), Q _ {0}) \quad w _ {i} (k) \sim N (0, Q)$$

which gives the following statistical properties for the particle locations

$$x _ {i} (k) \sim N (\overline {{x}} (k), \overline {{P}} (k)) \quad i = 1, \dots , s\overline {{{x}}} (k) = A \overline {{{x}}} (k - 1) + B u (k)\overline {{{P}}} (k) = A \overline {{{P}}} (k - 1) A ^ {\prime} + G Q G ^ {\prime} \tag {4.52}$$

If A is not strictly stable, the variance of the samples locations, P (k), increases without bound despite the availability of the measurement at every time. In this simplest particle filter, one is expecting the particle weights to carry all the information in the measurements. As we will see in the upcoming example, this idea does not work and after a few time iterations the resulting state estimates are useless.

To analyze the variance of the resulting particle weights, it is helpful to define the following statistical properties and establish the following identities. Consider two random variables A and B. Conditional expectations of A and functions of A and conditional variance of A are defined as

$$\mathcal {E} (A | B) := \int p _ {A | B} (a | b) a d a\mathcal {E} (A ^ {2} | B) := \int p _ {A | B} (a | b) a ^ {2} d a\mathcal {E} (g (A) | B) := \int p _ {A | B} (a | b) g (a) d a\operatorname{var} (A | B) := \mathcal {E} (A ^ {2} | B) - \mathcal {E} ^ {2} (A | B)$$

in which we assume as usual that B’s marginal is nonzero so the conditional density is well defined. We derive a first useful identity

$$E (E (g (A) | B)) = E (g (A)) \tag {4.53}$$
