$$\sum_ {i = 1} ^ {n} \sigma_ {i} = \sum_ {i = 1} ^ {n} \lambda_ {i} (P) = \mathrm{trace} (P) = \sum_ {i = 1} ^ {n} \frac {b _ {i}}{2 a _ {i}} = \frac {1}{2} G (0) = \frac {1}{2} \| G \| _ {\infty}$$

In particular, let $a _ { i } = b _ { i } = \alpha ^ { 2 i } ,$ ; then $P = Q  \textstyle { \frac { 1 } { 2 } } I _ { n } ( \mathrm { i . e . , } \sigma _ { j }  \textstyle { \frac { 1 } { 2 } }$ as $\alpha  \infty )$ . This example also shows that even when the Hankel singular values are extremely close, they may not be regarded as repeated singular values.

The model reduction bound can also be loose for systems with Hankel singular values close to each other.

Example 7.5 Consider the balanced realization of a fourth-order system:

$$
G (s) = \frac {(s - 0 . 9 9) (s - 2) (s - 3) (s - 4)}{(s + 1) (s + 2) (s + 3) (s + 4)}
= \left[ \begin{array}{c c c c c} - 9. 2 e + 0 0 & - 5. 7 e + 0 0 & - 2. 7 e + 0 0 & 1. 3 e + 0 0 & - 4. 3 e + 0 0 \\ 5. 7 e + 0 0 & - 8. 1 e - 0 7 & - 6. 4 e - 0 1 & 1. 5 e - 0 6 & 1. 3 e - 0 3 \\ - 2. 7 e + 0 0 & 6. 4 e - 0 1 & - 7. 9 e - 0 1 & 7. 1 e - 0 1 & - 1. 3 e + 0 0 \\ - 1. 3 e + 0 0 & 1. 5 e - 0 6 & - 7. 1 e - 0 1 & - 2. 7 e - 0 6 & - 2. 3 e - 0 3 \\ \hline 4. 3 e + 0 0 & 1. 3 e - 0 3 & 1. 3 e + 0 0 & - 2. 3 e - 0 3 & 1. 0 e + 0 0 \end{array} \right]
$$

with Hankel singular values given by

$$\sigma_ {1} = 0. 9 9 9 8, \quad \sigma_ {2} = 0. 9 9 8 8, \quad \sigma_ {3} = 0. 9 9 6 3, \sigma_ {4} = 0. 9 9 2 3.$$

The approximation errors and the estimated bounds are listed in the following table. The table shows that the actual error for an rth-order approximation is almost the same as $2 \sigma _ { r + 1 }$ , which would be the estimated bound if we regard $\sigma _ { r + 1 } = \sigma _ { r + 2 } = \cdot \cdot \cdot = \sigma _ { 4 }$ . In general, it is not hard to construct an nth-order system so that the rth-order balanced model reduction error is approximately $2 \sigma _ { r + 1 }$ but the error bound is arbitrarily close to $2 ( n - r ) \sigma _ { r + 1 }$ . One method to construct such a system is as follows: Let $G ( s )$ b e a stable all-pass function, that is, $G ^ { \sim } ( s ) G ( s ) = I$ . Then there is a balanced realization for G so that the controllability and observability Gramians are $P = Q = I $ . Next, make a very small perturbation to the balanced realization, then the perturbed system has a balanced realization with distinct singular values and $P = Q \approx I $ . This perturbed system will have the desired properties.
