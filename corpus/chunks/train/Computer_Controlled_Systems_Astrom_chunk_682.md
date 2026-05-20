# Example 11.6 Kalman filter and prediction

Consider the first-order system

$$y (k) + a y (k - 1) = e (k) + c e (k - 1) \tag {11.55}$$

where $e$ has standard deviation $\sigma$ . Further assume that $|c| < 1$ . A state-space representation of (11.55) is given by

$$x (k + 1) = - a x (k) + e (k)y (k) = (c - a) x (k) + e (k)$$

In this case $R_{1} = R_{2} = R_{12} = \sigma^{2}$ . The Kalman filter in steady state is given by

$$K = \frac {\sigma^ {2} - a P (c - a)}{(c - a) ^ {2} P + \sigma^ {2}}P = a ^ {2} P + \sigma^ {2} - \frac {\left(\sigma^ {2} - a P (c - a)\right) ^ {2}}{(c - a) ^ {2} P + \sigma^ {2}}$$

It is easy to verify that the solution is P = 0 and K = 1. The one-step-ahead predictor of x is given by

$$\hat {x} (k + 1 \mid k) = - a \hat {x} (k \mid k - 1) + y (k) - (c - a) \hat {x} (k \mid k - 1)= - c \hat {x} (k \mid k - 1) + y (k)$$

Further, in steady state, the one-step-ahead prediction of the output is given by

$$\hat {y} (k + 1 \mid k) = (c - a) \hat {x} (k + 1 \mid k)= \frac {c - a}{1 + c q ^ {- 1}} y (k)$$

If $|c| > 1$ then (11.55) first has to be transformed to a new representation using spectral factorization to get a stable $C$ -polynomial.
