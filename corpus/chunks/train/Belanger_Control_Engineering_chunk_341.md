# Proportional-Derivative Compensation

A proportional-derivative (PD) compensator has the transfer function

$$G _ {c} (s) = k (T s + 1). \tag {6.40}$$

It may be viewed as a limiting form of the lead compensator, as T tends to 0 and $\alpha T$ tends to a finite value. Since $G_{c}$ is not proper, it cannot be realized unless the derivative of the error can be measured as well as the error.

The phase of the compensator at the desired crossover frequency $\omega_{c}$ is

$$\not \prec G _ {c} (j \omega_ {c}) = \tan^ {- 1} \omega_ {c} T. \tag {6.41}$$

To normalize the magnitude at $\omega_{c}$ , we write

$$G _ {c} (s) = \frac {k _ {1}}{\sqrt {\omega_ {c} ^ {2} T ^ {2} + 1}} (T s + 1) \tag {6.42}$$

so that $|G_c(j\omega_c)| = k_1$ .

The design procedure parallels that for the lead. Using Equation 6.42, T is chosen to obtain a desired phase lead at $\omega = \omega_{c}$ . The gain $k_{1}$ is the gain needed to make $k_{1}|L(j\omega_{c})| = 1$ ; i.e., $k_{1} = -|G_{c}(j\omega_{c})|$ db.
