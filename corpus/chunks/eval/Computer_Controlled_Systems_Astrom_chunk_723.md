# Example 12.5 How to model offsets

The model

$$A (q) y (k) = C (q) e (k) + b$$

where b is an unknown constant, represents a signal with an offset. The constant b can be eliminated by taking differences. Hence,

$$(q - 1) A (q) y (k) = (q - 1) C (q) e (k)$$

The common factor q - 1 can be eliminated by regarding $\Delta y(k) = (q - 1)y(k)$ as the output. The model

$$A (q) \Delta y (k) = (q - 1) C (q) e (k) = \bar {C} (q) e (k)$$

is then obtained. In this model the polynomial $\tilde{C}$ apparently has a zero on the unit circle. This model is, however, not very desirable because the optimal predictor is a time-varying system. It is much better to model an offset as a Wiener process. This leads to a process model with $A(1) = 0$ that is unstable with a stationary predictor.

Other reasons for avoiding models where the polynomial $C(z)$ has zeros close to the unit circle are given in Sec. 12.6.
