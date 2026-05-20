# Frequency-Domain Properties of Kalman Filters

Modeling is very important when design problems are solved using optimization techniques because the optimal regulator, or the optimal filter, is just a transformation of the model. It is thus useful to understand the properties of this transformation. In this section some insight into the design of Kalman filters is provided by analyzing the frequency-domain characteristics of a stationary Kalman filter. Consider the problem of estimating the state of the system

$$x (k + 1) = \Phi_ {1} x (k) + v (k)$$

based on noisy observations

$$y (k) = C _ {1} x (k) + n (k)$$

where the noise n is given by

$$n (k) = C _ {2} z (k) + e (k)z (k + 1) = \Phi_ {2} z (k) + w (k)$$

In these models, $v(k)$ , $e(k)$ , and $w(k)$ are sequences of uncorrelated random variables. The steady-state Kalman filter for one-step prediction of x is given by

$$
\binom {\hat {x} (k + 1)} {\hat {z} (k + 1)} = \left( \begin{array}{c c} \Phi_ {1} & 0 \\ 0 & \Phi_ {2} \end{array} \right) \binom {\hat {x} (k)} {\hat {z} (k)} + \binom {K _ {1}} {K _ {2}} \left(y (k) - C _ {1} \hat {x} (k) - C _ {2} \hat {z} (k)\right)
$$

or

$$
\binom {\hat {x} (k + 1)} {\hat {z} (k + 1)} = \left( \begin{array}{c c} \Phi_ {1} - K _ {1} C _ {1} & - K _ {1} C _ {2} \\ - K _ {2} C _ {1} & \Phi_ {2} - K _ {2} C _ {2} \end{array} \right) \binom {\hat {x} (k)} {\hat {z} (k)} + \binom {K _ {1}} {K _ {2}} y (k) \tag {11.56}
$$

The Kalman filter is thus characterized by the pulse-transfer function from y to $\hat{x}$ and $\hat{z}$ :

$$
H (z) = \left( \begin{array}{c c} I & 0 \end{array} \right) \left( \begin{array}{c c} z I - \Phi_ {1} + K _ {1} C _ {1} & K _ {1} C _ {2} \\ K _ {2} C _ {1} & z I - \Phi_ {2} + K _ {2} C _ {2} \end{array} \right) ^ {- 1} \binom {K _ {1}} {K _ {2}} \tag {11.57}
$$

A frequency-response plot of the transfer function shows how the filter attenuates different frequencies. It is very useful to determine the frequency responses of the filter when designing Kalman filters. The properties of the frequency response will, in general, depend on the model in a complicated way. There are, however, some general properties that may be understood without detailed calculations.

LEMMA 11.1 TRANSMISSION ZEROS OF THE KALMAN FILTER The transmission zeros of the pulse-transfer function (11.57) of the stationary Kalman filter are given by

$$\det (z I - \Phi_ {2}) = 0$$
