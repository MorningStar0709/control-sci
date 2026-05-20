# Example 5.7 Integral action

Assume that a controller $R^{0}$ , $S^{0}$ has been designed and that we want to find a new controller for the same system that has integral action. Assume that the minimum-degree solution of Eq. (5.47) is U = -B and V = A. A new closed-loop pole is introduced at $-x_{1}$ ; hence $X(z) = z + x_{1}$ . The polynomial $Y(z)$ is then simply a scalar $y_{0}$ and Eq. (5.49) become

$$(1 + x _ {1}) R ^ {0} (1) - y _ {0} B (1) = 0$$

This gives $y_0 = (1 + x_1)R^0 (1) / B(1)$ and the new controller becomes

$$R (z) = \left(z + x _ {1}\right) R ^ {0} (z) - \frac {\left(1 + x _ {1}\right) R ^ {0} (1) B (z)}{B (1)}S (z) = \left(z + x _ {1}\right) S ^ {0} (z) + \frac {\left(1 + x _ {1}\right) R ^ {0} (1) A (z)}{B (1)}$$
