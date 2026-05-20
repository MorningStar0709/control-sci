# THEOREM 2.7 Persistently exciting signals

The signal $u$ with the property (2.44) is persistently exciting of order $n$ if and only if

$$U = \lim _ {t \rightarrow \infty} \frac {1}{t} \sum_ {k = 1} ^ {t} (A (q) u (k)) ^ {2} > 0 \tag {2.45}$$

for all nonzero polynomials A of degree n - 1 or less.

Proof: Let the polynomial A be

$$A (q) = a _ {0} q ^ {n - 1} + a _ {1} q ^ {n - 2} + \dots + a _ {n - 1}$$

A straightforward calculation shows that

$$U = \lim _ {t \rightarrow \infty} \frac {1}{t} \sum_ {k = 1} ^ {t} (a _ {0} u (k + n - 1) + \dots + a _ {n - 1} u (k)) ^ {2} = a ^ {T} C _ {n} a$$

where $C_{n}$ is the matrix given by Eq. (2.43). If $C_{n}$ is positive definite, the right-hand side is positive for all a, and so is the left-hand side. Conversely, if the left-hand side is positive for all a, so is the right-hand side. ☐

The result is useful in investigating whether special signals are persistently exciting.
