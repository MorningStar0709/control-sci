Since we can only realize controllers that have proper or strictly proper transfer functions, we must impose a condition to ensure that this will be so. We shall normally require $\lim_{s\to\infty}T(s)=0$ , so that $\lim_{s\to\infty}S(s)=1$ . Suppose that, for large s,

$$T (s) \rightarrow \frac {k _ {T}}{s ^ {N _ {T}}}, \quad P (s) \rightarrow \frac {k _ {P}}{s ^ {N _ {P}}}$$

where $N_{T}(N_{P})$ is the number of poles of $T(P)$ minus the number of zeros of $T(P)$ , i.e., the excess of poles over zeros of $T(P)$ . Then

$$F (s) \rightarrow k s ^ {N _ {P} - N _ {T}}.$$

For $F(s)$ to be at least proper, we must have $N_P - N_T \leq 0$ . To summarize: Let $T(s)$ be strictly proper. Then $F(s)$ is proper (strictly proper) if the excess of poles over zeros of $T(s)$ is equal to (greater than) that of $P(s)$ .

It is possible to express this as a requirement on $S(s)$ , should it be the design parameter. Let

$$T (s) = \frac {b _ {m} s ^ {m} + b _ {m - 1} s ^ {m - 1} + \cdots + b _ {0}}{s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {0}}$$

where $m = n - N_T$ , $0 \leq N_T \leq n$ . Then

(4.38)

$$
\begin{array}{l} S (s) = 1 - T (s) \\ = \frac {s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {m + 1} s ^ {m + 1} + \left(a _ {m} - b _ {m}\right) s ^ {n} + \cdots + \left(a _ {0} - b _ {0}\right)}{s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {0}}. \\ S (s) = 1 - T (s) \\ = \frac {s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {m + 1} s ^ {m + 1} + \left(a _ {m} - b _ {m}\right) s ^ {n} + \cdots + \left(a _ {0} - b _ {0}\right)}{s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {0}}. \\ \end{array}
$$

Equation 4.38 reveals that the leading $N_{T}$ coefficients of the numerator and denominator of $S(s)$ are identical; a transfer function $S(s)$ constructed in this way will lead to a $T(s)$ with a pole excess of $N_{T}$ .
