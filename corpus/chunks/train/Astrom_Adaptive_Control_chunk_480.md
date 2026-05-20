# THEOREM 6.9 Limiting sampled-data zeros

Let $G(s)$ be a rational function

$$G (s) = K \frac {(s - z _ {1}) (s - z _ {2}) , \dots , (s - z _ {m})}{(s - p _ {1}) (s - p _ {2}) , \dots , (s - p _ {n})} \tag {6.88}$$

and let $H(z)$ be the corresponding pulse transfer function. Assume that $m < n$ . As the sampling period $h \to 0$ , $m$ zeros of $H$ go to 1 as $\exp(z_i h)$ , and the remaining $n - m - 1$ zeros of $H$ go to the zeros of $B_{n - m}(z)$ , where $B_k(z)$ is the polynomial

$$B _ {k} (z) = b _ {1} ^ {k} z ^ {k - 1} + b _ {2} ^ {k} z ^ {k - 2} + \dots + b _ {k} ^ {k} \tag {6.89}$$

and

$$b _ {i} ^ {k} = \sum_ {l = 1} ^ {i} (- 1) ^ {i - l} l ^ {k} \binom {k + 1} {i - l} \quad i = 1, \dots , k \tag {6.90}$$

The first polynomials $B_{k}$ are

$$B _ {1} (z) = 1B _ {2} (z) = z + 1B _ {3} (z) = z ^ {2} + 4 z + 1$$

![](image/0efe35c42e2ab58db89af4f49c75bcd879e5bc1696d0a351e30a7c37a82f9562.jpg)

This theorem is proved in Åström et al. (1984). It implies that direct methods for adaptive control that require that the plant be minimum-phase cannot be used with too short a sampling period. When very fast sampling is required, a continuous-time representation may then be preferable. Another possibility is to describe the system in the delta operator, defined by

$$\delta = \frac {q - 1}{h}$$

or in Tustin's operator:

$$\Delta = \frac {1}{2 h} \frac {q - 1}{q + 1}$$

This yields parameterizations that give a much better resolution at q = 1. The $\delta$ operator gives a description that is equivalent to the q operator description. The advantage of the transformation is that the $\delta$ operator description has better numerical properties when the sampling is fast. All the poles of the q operator form are clustered around the point q = 1. This gives rise to numerical sensitivity. For the $\delta$ operator it can be shown that the limiting value

$$\lim _ {h \rightarrow 0} \frac {B _ {h} (\delta)}{A _ {h} (\delta)} = \frac {B _ {0} (\delta)}{A _ {0} (\delta)}$$

is such that the coefficients in $B_{0}$ and $A_{0}$ are the same as the coefficients in the continuous-time transfer function. This implies that the structure of the transfer function in the $\delta$ operator is essentially the same as that of the continuous-time transfer function, provided that the sampling period is sufficiently short.
