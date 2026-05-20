# Example 10.2 Predictor for a ramp signal

A predictor for a ramp can be constructed by calculating the slope from the past and the current observations and making a linear extrapolation, which can be expressed by the formula

$$
\begin{array}{l} \hat {y} ((k + m) h \mid k h) = y (k h) + m (y (k h) - y (k h - h)) \\ = (1 + m) y (k h) - m y (k h - h) \\ \end{array}
$$

This predictor has an initial error for $t = h, 2h, \ldots, mh$ . After that it predicts the signal without error.
