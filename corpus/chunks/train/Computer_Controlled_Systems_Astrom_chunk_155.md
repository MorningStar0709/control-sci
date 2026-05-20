$$B _ {n} (z) = b _ {1} ^ {n} z ^ {n - 1} + b _ {2} ^ {n} z ^ {n - 2} + \dots + b _ {n} ^ {n}$$

and

$$b _ {k} ^ {n} = \sum_ {i = 1} ^ {k} (- 1) ^ {k - i} i ^ {n} \binom {n + 1} {k - i} \quad k = 1, 2, \dots , n$$

Furthermore show that

$$
\begin{array}{l} B _ {1} (z) = 1 \\ B _ {2} (z) = z + 1 \\ B _ {3} (z) = z ^ {2} + 4 z + 1 \\ B _ {4} (z) = z ^ {3} + 1 1 z ^ {2} + 1 1 z + 1 \\ B _ {5} (z) = z ^ {4} + 2 6 z ^ {3} + 6 6 z ^ {2} + 2 6 z ^ {2} + 1 \\ B _ {6} (z) = z ^ {5} + 5 7 z ^ {4} + 3 0 2 z ^ {3} + 3 0 2 z ^ {2} + 5 7 z + 1 \\ \end{array}
$$

2.27 Derive Eq. (2.31) from (2.30).

2.28 Solve the difference equation

$$y (k) = y (k - 1) + y (k - 2) \quad k = 2, 3, \dots$$

when $y(0) = y(1) = 1$ . [The numbers $y(k)$ are called Fibonacci numbers.]

2.29 Determine the poles and zeros (with multiplicity) of the system

$$y (k) - 0. 5 y (k - 1) + y (k - 2) = 2 u (k - 1 0) + u (k - 1 1)$$

2.30 Which of the following discrete-time systems can be obtained by sampling a causal continuous-time system using a zero-order hold?

$$
\begin{array}{l} H _ {1} (q) = \frac {1}{q - 0 . 8} \quad H _ {2} (q) = \frac {1}{q + 0 . 8} \\ H _ {3} (q) = \frac {q - 1}{(q + 0 . 8) ^ {2}} \quad H _ {4} (q) = \frac {2 q ^ {2} - 0 . 7 q - 0 . 8}{q (q - 0 . 8)} \\ \end{array}
$$

2.31 Determine the pulse-transfer operator obtained by sampling

$$G (s) = \frac {2 (s + 2)}{(s + 1) (s + 3)}$$

with h = 0.02.

2.32 Sample the continuous-time system

$$
\frac {d x (t)}{d t} = \left( \begin{array}{l l} 1 & 0 \\ 1 & 1 \end{array} \right) x (t) + \binom {1} {0} u (t - 0. 2)
$$

using the sampling interval h = 0.3. Determine the pulse-transfer operator.

2.33 Consider a linear system with the transfer function

$$G _ {a} (s) = \frac {a}{s + a}$$

Sampling the system gives the pulse-transfer function

$$H _ {a} (z) = \frac {1 - e ^ {- a h}}{z - e ^ {- a h}}$$

Letting $a \to \infty$ , we get

$$G _ {\infty} (s) = \lim _ {a \rightarrow \infty} G _ {n} (s) = 1$$

and

$$H _ {\infty} (z) = \lim _ {a \rightarrow \infty} H _ {a} (z) = \frac {1}{z}$$

Notice that $H_{\infty}(z)$ is not the pulse-transfer function obtained by sampling the system with the pulse-transfer function $G_{\infty}(s)=1$ . Determine conditions on the transfer function $G_{a}(s)$ such that sampling commutes with limit operations.
