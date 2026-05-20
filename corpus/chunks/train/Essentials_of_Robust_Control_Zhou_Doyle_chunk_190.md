# 7.6 Problems

Problem 7.1 Use the following relation

$$\frac {d}{d t} \left(e ^ {A t} Q e ^ {A ^ {*} t}\right) = A e ^ {A t} Q e ^ {A ^ {*} t} + e ^ {A t} Q e ^ {A ^ {*} t} A$$

to show that $\textstyle P = \int _ { 0 } ^ { \infty } e ^ { A t } Q e ^ { A ^ { * } t }$ dt solves

$$A P + P A ^ {*} + Q = 0$$

if A is stable.

Problem 7.2 Let $G ( s ) \in \mathcal { H } _ { \infty }$ and let $g ( t )$ be the inverse Laplace transform of $G ( s )$ . Let $h _ { i } , i = 1 , 2 , \ldots$ . be the variations of the step response of G. Show that

$$\int_ {0} ^ {\infty} | g (t) | d t = h _ {1} + h _ {2} + h _ {3} + h _ {4} + \dots$$

Problem 7.3 Let $Q \geq 0$ be the solution to

$$Q A + A ^ {*} Q + C ^ {*} C = 0$$

Suppose Q has m zero eigenvalues. Show that there is a nonsingular matrix T such that

$$
\left[ \begin{array}{c c} T A T ^ {- 1} & T B \\ \hline C T ^ {- 1} & D \end{array} \right] = \left[ \begin{array}{c c c} A _ {1 1} & 0 & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & 0 & D \end{array} \right], \quad A _ {2 2} \in \mathbb {R} ^ {m \times m}.
$$

Apply the above result to the following state-space model:

$$
A = \left[ \begin{array}{r r r} - 4 & - 7 & - 2 \\ 1 & 0 & 0 \\ - 1 & 1 & 0 \end{array} \right], B = \left[ \begin{array}{r r} 1 & 2 \\ 0 & - 1 \\ 0 & 2 \end{array} \right], C = \left[ \begin{array}{r r r} 0 & 2 & 1 \\ 1 & 1 & 0 \end{array} \right], D = 0
$$

Problem 7.4 Let

$$G (s) = \sum_ {i = 1} ^ {5} \frac {\alpha^ {2 i}}{s + \alpha^ {2 i}}$$

Find a balanced realization for each of the following α:

$$\alpha = 2, 4, 2 0, 1 0 0.$$

Discuss the behavior of the Hankel singular values as $\alpha \to \infty$ .

Problem 7.5 Find a transformation so that $T P T ^ { * } = \Sigma ^ { 2 } , ( T ^ { * } ) ^ { - 1 } Q T ^ { - 1 } = I$ . (This realization is called output normalized realization.)

Problem 7.6 Consider the model reduction error:

$$
\begin{array}{r l r} {E _ {1 1}} & = & {\left[ \begin{array}{c c c c} A _ {1 1} & 0 & A _ {1 2} / 2 & B _ {1} \\ 0 & A _ {1 1} & - A _ {1 2} / 2 & 0 \\ A _ {2 1} & - A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline 0 & - 2 C _ {1} & C _ {2} & 0 \end{array} \right] =: \left[ \begin{array}{c c} A _ {e} & B _ {e} \\ \hline C _ {e} & 0 \end{array} \right].} \end{array}
$$

Show that

$$
\tilde {P} = \left[ \begin{array}{c c c} {\Sigma_ {1}} & 0 & \\ {0} & {\sigma_ {N} ^ {2} \Sigma_ {1} ^ {- 1}} & 0 \\ {0} & 0 & {2 \sigma_ {N} I _ {s _ {N}}} \end{array} \right]
$$

satisfies

$$A _ {e} \tilde {P} + \tilde {P} A _ {e} ^ {*} + B _ {e} B _ {e} ^ {*} + \frac {1}{4 \sigma_ {N} ^ {2}} \tilde {P} C _ {e} ^ {*} C _ {e} \tilde {P} = 0.$$
