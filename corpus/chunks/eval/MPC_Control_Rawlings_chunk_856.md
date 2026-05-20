$$\sigma (\xi) = \left(\operatorname{var} (\xi)\right) ^ {1 / 2}$$

Normal distribution. The normal or Gaussian distribution is ubiquitous in applications. It is characterized by its mean, m and variance, $\sigma ^ { 2 }$ , and is given by

$$p _ {\xi} (x) = \frac {1}{\sqrt {2 \pi \sigma^ {2}}} \exp \left(- \frac {1}{2} \frac {(x - m) ^ {2}}{\sigma^ {2}}\right) \tag {A.21}$$

We proceed to check that the mean of this distribution is indeed m and the variance is $\sigma ^ { 2 }$ as claimed and that the density is normalized so that its integral is one. We require the definite integral formulas

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2}} d x = \sqrt {\pi} \\ \int_ {0} ^ {\infty} x ^ {1 / 2} e ^ {- x} d x = \Gamma (3 / 2) = \frac {\sqrt {\pi}}{2} \\ \end{array}
$$

The first formula may also be familiar from the error function in transport phenomena

$$\operatorname{erf} (x) = \frac {2}{\sqrt {\pi}} \int_ {0} ^ {x} e ^ {- u ^ {2}} d u\operatorname{erf} (\infty) = 1$$

We calculate the integral of the normal density as follows

$$\int_ {- \infty} ^ {\infty} p _ {\xi} (x) d x = \frac {1}{\sqrt {2 \pi \sigma^ {2}}} \int_ {- \infty} ^ {\infty} \exp \left(- \frac {1}{2} \frac {(x - m) ^ {2}}{\sigma^ {2}}\right) d x$$

Define the change of variable

$$u = \frac {1}{\sqrt {2}} \left(\frac {x - m}{\sigma}\right)$$

which gives

$$\int_ {- \infty} ^ {\infty} p _ {\xi} (x) d x = \frac {1}{\sqrt {\pi}} \int_ {- \infty} ^ {\infty} \exp (- u ^ {2}) d u = 1$$

and (A.21) does have unit area. Computing the mean gives

$$\mathcal {E} (\xi) = \frac {1}{\sqrt {2 \pi \sigma^ {2}}} \int_ {- \infty} ^ {\infty} x \exp \left(- \frac {1}{2} \frac {(x - m) ^ {2}}{\sigma^ {2}}\right) d x$$

using the same change of variables as before yields

$$\mathcal {E} (\xi) = \frac {1}{\sqrt {\pi}} \int_ {- \infty} ^ {\infty} (\sqrt {2} u \sigma + m) e ^ {- u ^ {2}} d u$$

The first term in the integral is zero because u is an odd function, and the second term produces

$$\mathcal {E} (\xi) = m$$

as claimed. Finally the definition of the variance of $\xi$ gives

$$\operatorname{var} (\xi) = \frac {1}{\sqrt {2 \pi \sigma^ {2}}} \int_ {- \infty} ^ {\infty} (x - m) ^ {2} \exp \left(- \frac {1}{2} \frac {(x - m) ^ {2}}{\sigma^ {2}}\right) d x$$

Changing the variable of integration as before gives

$$\operatorname{var} (\xi) = \frac {2}{\sqrt {\pi}} \sigma^ {2} \int_ {- \infty} ^ {\infty} u ^ {2} e ^ {- u ^ {2}} d u$$

and because the integrand is an even function,
