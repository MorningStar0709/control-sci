# EXAMPLE 7.2 Integrator with time-varying gain

Consider an integrator in which the gain is changing. Let the process be described by

$$y (t) - y (t - 1) = b (t) u (t - 1) + e (t)$$

where

$$b (t + 1) = \varphi_ {b} b (t) + R _ {1} v (t)$$

The errors e and v are zero-mean Gaussian white noise with the standard deviations $R_{2}$ and 1, respectively. Further, it is assumed that $u_{c} = 0$ . The certainty equivalence controller is given by

$$u (t) = - \frac {1}{\hat {b} (t + 1)} y (t)$$

and the cautious controller is

$$u (t) = - \frac {\hat {b} (t + 1)}{\hat {b} ^ {2} (t + 1) + p _ {b} (t + 1)} y (t)$$

The gain in the cautious controller has been reduced by a factor

$$\frac {\hat {b} ^ {2}}{\hat {b} ^ {2} + p _ {b}}$$

compared with the certainty equivalence controller. Notice that the gain approaches zero when the uncertainty increases.
