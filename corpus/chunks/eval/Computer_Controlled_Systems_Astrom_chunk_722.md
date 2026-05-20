# Example 12.4 Zeros on the unit circle

Consider the process

$$y (k) = e (k) - e (k - 1) \tag {12.22}$$

In this case the polynomial $C(z) = z - 1$ has a zero on the unit circle. Applying the previous methods formally gives the one-step predictor

$$\hat {y} (k + 1 \mid k) = - e (k)$$

Attempting to calculate $e(k)$ from $y(k), y(k - 1), \ldots, y(k_0)$ as was done previously gives

$$e (k) = e \left(k _ {0} - 1\right) + \sum_ {i = k _ {0}} ^ {k} y (i) = e \left(k _ {0} - 1\right) + z (k)$$

The presence of the term $e(k_{0}-1)$ , which does not go to zero as $k_{0}\to-\infty$ , shows the consequences of C being unstable. The Kalman filtering theory can, however, be used to determine the optimal predictor. The signal given by (12.22) can be written as

$$
\begin{array}{l} x (k + 1) = e (k) \\ y (k) = - x (k) + e (k) \\ \end{array}
$$

where $R_{1} = R_{2} = R_{12} = \sigma^{2}$ with the notations used in Sec. 11.3. The Kalman filter is

$$
\begin{array}{l} \hat {x} (k + 1 \mid k) = K (k) \left(y (k) + \hat {x} (k \mid k - 1)\right) \\ P (k + 1) = \frac {\sigma^ {2} P (k)}{P (k) + \sigma^ {2}} \\ K (k) = \frac {\sigma^ {2}}{P (k) + \sigma^ {2}} \\ \end{array}
$$

with the initial conditions

$$
\begin{array}{l} \hat {x} \left(k _ {0} \mid k _ {0} - 1\right) = 0 \\ P \left(k _ {0}\right) = \sigma^ {2} \\ \end{array}
$$

The predictor for the output is

$$\hat {y} (k + 1 \mid k) = - \hat {x} (k + 1 \mid k) = - K (k) \left(y (k) - \hat {y} (k \mid k - 1)\right)$$

Simple calculations give

$$\hat {y} (k + 1 \mid k) = - \frac {1}{k - k _ {0} + 2} \sum_ {n = 0} ^ {k - k _ {0}} (n + 1) y (k _ {0} + n)$$

The optimum predictor is thus a time-varying system. Notice that the influence of the initial condition $y(k_{0})$ goes to zero at the rate $1/(k-k_{0}+2)$ . This is much slower than in the case of stable polynomials C.

It follows from the example that the optimal predictor is a time-varying system if the polynomial C has zeros on the unit circle. Such models should be avoided if time-invariant predictors are desired. Unfortunately, this fact is not always noticed, as Example 12.5 illustrates.
