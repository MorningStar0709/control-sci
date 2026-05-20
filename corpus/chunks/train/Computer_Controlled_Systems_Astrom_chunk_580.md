# Example 9.9 Numerical precision required for PI-control

Consider the formula for updating the integral in a PI-controller:

$$i (k h + h) = i (k h) + e (k h) \cdot h / T _ {i}$$

If the sampling period is 0.03 s and the integration time is 15 min = 900 s, the ratio $h/T_{i}$ becomes $3 \cdot 10^{-5}$ , which corresponds to about 15 bits. To avoid that the quantity $e(kh)h/T_{i}$ is rounded it is thus necessary to make the computations with a longer word length. This is the reason why the integral term is often implemented in 24-bit representation in dedicated PI-controllers.

The examples show that a rapid sampling requires a high precision in the coefficients.
