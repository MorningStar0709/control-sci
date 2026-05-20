# Example 5.8 Integral action and robustness

Consider the same problem as in Example 5.7 but assume that in addition we would like to make sure that the sensitivity function is one at the Nyquist frequency. This is achieved by the conditions $R_{d} = z - 1$ and $S_{d} = z + 1$ . The polynomial $X$ is thus of second order and polynomial $Y$ is of first order. The conditions (5.49) become

$$X (1) R ^ {0} (1) - \left(y _ {0} + y _ {1}\right) B (1) = 0X (- 1) S ^ {0} (- 1) - \left(- y _ {0} + y _ {1}\right) B (- 1) = 0$$

Solving these equations for $y_{0}$ and $y_{1}$ gives

$$y _ {0} = \frac {1}{2} \left(\frac {X (1) R ^ {0} (1)}{B (1)} - \frac {X (- 1) S ^ {0} (- 1)}{B (- 1)}\right)y _ {1} = \frac {1}{2} \left(\frac {X (1) R ^ {0} (1)}{B (1)} + \frac {X (- 1) S ^ {0} (- 1)}{B (- 1)}\right)$$
