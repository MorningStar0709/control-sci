# Higher-Order Holds

The zero-order hold can be regarded as an extrapolation using a polynomial of degree zero. For smooth functions it is possible to obtain smaller reconstruction errors by extrapolation with higher-order polynomials. A first-order causal polynomial extrapolation gives

$$f (t) = f \left(t _ {k}\right) + \frac {t - t _ {k}}{t _ {k} - t _ {k - 1}} \left(f \left(t _ {k}\right) - f \left(t _ {k - 1}\right)\right) \quad t _ {k} \leq t < t _ {k + 1}$$

The reconstruction is thus obtained by drawing a line between the two most recent samples. The first-order hold is illustrated in Fig. 7.5.
