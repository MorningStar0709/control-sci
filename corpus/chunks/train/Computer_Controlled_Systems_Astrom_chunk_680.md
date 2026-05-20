# Example 11.5 Kalman filter for a first order system

Consider the scalar system

$$
\begin{array}{l} x (k + 1) = x (k) \\ y (k) = x (k) + e (k) \\ \end{array}
$$

![](image/c7c16b79fa1022c1afe43b07a84ca333092eff72bba119a739b398e8163ad49c.jpg)  
Figure 11.7 Estimation error for the system in Example 11.5 when starting from $x(0) = -2$ , and when using $\sigma = 1$ and (a) $K = 0.01$ , (b) $K = 0.05$ , and (c) the optimal gain of (11.49).

where e has standard deviation $\sigma$ and $x(0)$ has the variance 0.5. The state is thus constant and has to be reconstructed from noisy measurements. The Kalman filter is given by

$$\hat {x} (k + 1 \mid k) = \hat {x} (k \mid k - 1) + K (k) \left(y (k) - \hat {x} (k \mid k - 1)\right) \tag {11.48}K (k) = \frac {P (k)}{\sigma^ {2} + P (k)} \quad \text { and } \quad P (k + 1) = \frac {\sigma^ {2} P (k)}{\sigma^ {2} + P (k)} \tag {11.49}$$

The variance and the gain are decreasing with time. Figure 11.7 shows realizations of the estimation error when the Kalman filter is used and when (11.48) is used with constant gain. A large fixed gain gives a rapid initial decrease in the error, while the steady-state variance is large. A small fixed gain gives a slow decrease in the error, but a better performance in steady state.
