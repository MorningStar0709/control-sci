# Example 12.1 Modification of the polynomial $C$

Consider the polynomial

$$C (z) = z + 2$$

which has the zero z = -2 outside the unit disc. Consider the signal

$$n (k) = C (q) e (k)$$

where $e(k)$ is a sequence of uncorrelated random variables with zero mean and unit variance. The spectral density of n is given by

$$\phi (e ^ {i \omega h}) = \frac {1}{2 \pi} C (e ^ {i \omega h}) C (e ^ {- i \omega h})$$

Because

$$
\begin{array}{l} C (z) C \left(z ^ {- 1}\right) = (z + 2) \left(z ^ {- 1} + 2\right) = (1 + 2 z ^ {- 1}) (1 + 2 z) \\ = (2 z + 1) (2 z ^ {- 1} + 1) = 4 (z + 0. 5) (z ^ {- 1} + 0. 5) \\ \end{array}
$$

the signal n may also be represented as

$$n (k) = C ^ {*} (q) e (k)$$

where

$$C ^ {*} (z) = 2 z + 1$$

is the reciprocal of the polynomial $C(z)$ (see Sec. 2.6).

If the calculations of (12.4) give a polynomial $C(q)$ that has zeros outside the unit disc, the polynomial $C$ is factored as

$$\boldsymbol {C} = \boldsymbol {C} ^ {+} \boldsymbol {C} ^ {-}$$

where $C^{-}$ contains all factors with zeros outside the unit disc. The polynomial C is then replaced by $C^{+}C^{-*}$ .
