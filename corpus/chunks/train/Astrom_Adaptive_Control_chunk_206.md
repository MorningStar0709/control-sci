# EXAMPLE 4.1 Modification of the polynomial C

Consider the polynomial

$$C (z) = z + 2$$

which has the zero z = -2 outside the unit disc. Consider the signal

$$v (t) = C (q) e (t)$$

where $\{e(t)\}$ is a sequence of uncorrelated random variables with zero mean and unit variance. The spectral density of v is given by

$$\Phi (e ^ {i \omega h}) = \frac {1}{2 \pi} C (e ^ {i \omega h}) C (e ^ {- i \omega h})$$

Because

$$
\begin{array}{l} C (z) C \left(z ^ {- 1}\right) = (z + 2) \left(z ^ {- 1} + 2\right) = (1 + 2 z ^ {- 1}) (1 + 2 z) \\ = (2 z + 1) \left(2 z ^ {- 1} + 1\right) \\ = 4 (z + 0. 5) \left(z ^ {- 1} + 0. 5\right) \\ \end{array}
$$

the signal v may also be represented as

$$v (t) = C ^ {*} (q) e (t)$$

where

$$\mathbf {C} ^ {*} (z) = 2 z + 1$$

is the reciprocal of the polynomial $C(z)$ (see Section 3.2).

If the calculations (4.2) give a polynomial C that has zeros outside the unit disc, the polynomial is factored as

$$C = C ^ {+} C$$

where $C^{-}$ contains all factors with zeros outside the unit disc. The C polynomial is then replaced by $C^{+}C^{-*}$ . The model (4.1) is an innovations representation. It will be shown later that $e(t)$ is the innovation or the error in predicting the signal $y(t)$ over one sampling period. The C polynomial can be interpreted as the characteristic polynomial of the estimator or predictor.
