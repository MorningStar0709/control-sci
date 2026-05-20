The stability condition in Theorem 7.9 is only sufficient as shown in the following example.

Example 7.3 Note that

$$
\frac {(s - 1) (s - 2)}{(s + 1) (s + 2)} = \left[ \begin{array}{c c c} - 2 & - 2. 8 2 8 4 & - 2 \\ 0 & - 1 & - 1. 4 1 4 2 \\ \hline 2 & 1. 4 1 4 2 & 1 \end{array} \right]
$$

is a balanced realization with Σ = I, and every subsystem of the realization is stable. On the other hand,

$$
\frac {s ^ {2} - s + 2}{s ^ {2} + s + 2} = \left[ \begin{array}{c c c} - 1 & 1. 4 1 4 2 & 1. 4 1 4 2 \\ - 1. 4 1 4 2 & 0 & 0 \\ \hline - 1. 4 1 4 2 & 0 & 1 \end{array} \right]
$$

is also a balanced realization with Σ = I, but one of the subsystems is not stable.

Theorem 7.11 Suppose $G ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ and

$$
G (s) = \left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & C _ {2} & D \end{array} \right]
$$

is a balanced realization with Gramian $\Sigma = \mathrm { { d i a g } ( \Sigma _ { 1 } , \Sigma _ { 2 } ) }$

$$\Sigma_ {1} = \mathrm{diag} (\sigma_ {1} I _ {s _ {1}}, \sigma_ {2} I _ {s _ {2}}, \ldots , \sigma_ {r} I _ {s _ {r}})\Sigma_ {2} = \operatorname{diag} (\sigma_ {r + 1} I _ {s _ {r + 1}}, \sigma_ {r + 2} I _ {s _ {r + 2}}, \dots , \sigma_ {N} I _ {s _ {N}})$$

and

$$\sigma_ {1} > \sigma_ {2} > \dots > \sigma_ {r} > \sigma_ {r + 1} > \sigma_ {r + 2} > \dots > \sigma_ {N}$$

where $\sigma _ { i }$ has multiplicity $s _ { i } , i = 1 , 2 , . . . , N$ and $s _ { 1 } + s _ { 2 } + \cdot \cdot \cdot + s _ { N } = n$ . Then the truncated system

$$
G _ {r} (s) = \left[ \begin{array}{c c} A _ {1 1} & B _ {1} \\ \hline C _ {1} & D \end{array} \right]
$$

is balanced and asymptotically stable. Furthermore,

$$\left\| G (s) - G _ {r} (s) \right\| _ {\infty} \leq 2 (\sigma_ {r + 1} + \sigma_ {r + 2} + \dots + \sigma_ {N})$$

Proof. The stability of $G _ { r }$ follows from Theorem 7.9. We shall first show the one step model reduction. Hence we shall assume $\Sigma _ { 2 } = \sigma _ { N } I _ { s _ { N } }$ . Define the approximation error

$$
\begin{array}{l} E _ {1 1} := \left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & C _ {2} & D \end{array} \right] - \left[ \begin{array}{c c} A _ {1 1} & B _ {1} \\ \hline C _ {1} & D \end{array} \right] \\ = \left[ \begin{array}{c c c c} A _ {1 1} & 0 & 0 & B _ {1} \\ 0 & A _ {1 1} & A _ {1 2} & B _ {1} \\ 0 & A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline - C _ {1} & C _ {1} & C _ {2} & 0 \end{array} \right] \\ \end{array}
$$

Apply a similarity transformation T to the preceding state-space realization with
