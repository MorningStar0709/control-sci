# Example 2.18 Stability of inverse system changes with sampling

The transfer function

$$G (s) = \frac {6 (1 - s)}{(s + 2) (s + 3)}$$

has an unstable zero s = 1. Sampling the system gives a discrete-time pulse-transfer function with a zero:

$$z _ {1} = - \frac {8 e ^ {- 2 h} - 9 e ^ {- 3 h} + e ^ {- 5 h}}{1 - 9 e ^ {- 2 h} + 8 e ^ {- 3 h}}$$

For $h \approx 1.25, z_{1} = -1$ ; for larger h, the zero is always inside the unit circle and the sampled system has a stable inverse.
