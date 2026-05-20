$$G (s) := \int_ {0} ^ {\infty} g (t) e ^ {- s t} d t, \operatorname{Re} (s) > 0,$$

by the definition of $\mathcal { H } _ { \infty }$ norm, we have

$$
\begin{array}{l} \| G \| _ {\infty} = \sup _ {\operatorname{Re} (s) > 0} \left\| \int_ {0} ^ {\infty} g (t) e ^ {- s t} d t \right\| \\ \leq \sup _ {\operatorname{Re} (s) > 0} \int_ {0} ^ {\infty} \| g (t) e ^ {- s t} \| d t \\ \leq \int_ {0} ^ {\infty} \| g (t) \| d t. \\ \end{array}
$$

To prove the last inequality, let $e _ { i }$ be the ith unit vector and define

$$
E _ {1} = \left[ \begin{array}{c c c} e _ {1} & \dots & e _ {s _ {1}} \end{array} \right], \quad E _ {2} = \left[ \begin{array}{c c c} e _ {s _ {1} + 1} & \dots & e _ {s _ {1} + s _ {2}} \end{array} \right], \quad \ldots ,

E _ {N} = \left[ \begin{array}{c c c} e _ {s _ {1} + \dots + s _ {N - 1} + 1} & \dots & e _ {s _ {1} + \dots + s _ {N}} \end{array} \right].
$$

Then $\sum _ { i = 1 } ^ { N } E _ { i } E _ { i } ^ { * } = I$ and

$$
\begin{array}{l} \int_ {0} ^ {\infty} \| g (t) \| d t = \int_ {0} ^ {\infty} \left\| C e ^ {A t / 2} \sum_ {i = 1} ^ {N} E _ {i} E _ {i} ^ {*} e ^ {A t / 2} B \right\| d t \\ \leq \sum_ {i = 1} ^ {N} \int_ {0} ^ {\infty} \left\| C e ^ {A t / 2} E _ {i} E _ {i} ^ {*} e ^ {A t / 2} B \right\| d t \\ \leq \sum_ {i = 1} ^ {N} \int_ {0} ^ {\infty} \left\| C e ^ {A t / 2} E _ {i} \right\| \left\| E _ {i} ^ {*} e ^ {A t / 2} B \right\| d t \\ \leq \sum_ {i = 1} ^ {N} \sqrt {\int_ {0} ^ {\infty} \left\| C e ^ {A t / 2} E _ {i} \right\| ^ {2} d t} \sqrt {\int_ {0} ^ {\infty} \left\| E _ {i} ^ {*} e ^ {A t / 2} B \right\| ^ {2} d t} \leq 2 \sum_ {i = 1} ^ {N} \sigma_ {i} \\ \end{array}
$$

where we have used Cauchy-Schwarz inequality and the following relations:

$$\int_ {0} ^ {\infty} \left\| C e ^ {A t / 2} E _ {i} \right\| ^ {2} d t = \int_ {0} ^ {\infty} \lambda_ {\max} \left(E _ {i} ^ {*} e ^ {A ^ {*} t / 2} C ^ {*} C e ^ {A t / 2} E _ {i}\right) d t = 2 \lambda_ {\max} \left(E _ {i} ^ {*} \Sigma E _ {i}\right) = 2 \sigma_ {i}\int_ {0} ^ {\infty} \left\| E _ {i} ^ {*} e ^ {A t / 2} B \right\| ^ {2} d t = \int_ {0} ^ {\infty} \lambda_ {\max} \left(E _ {i} ^ {*} e ^ {A t / 2} B B ^ {*} e ^ {A ^ {*} t / 2} E _ {i}\right) d t = 2 \lambda_ {\max} \left(E _ {i} ^ {*} \Sigma E _ {i}\right) = 2 \sigma_ {i}$$

✷

Example 7.2 Consider a system

$$
G (s) = \left[ \begin{array}{c c c} - 1 & - 2 & 1 \\ 1 & 0 & 0 \\ \hline 2 & 3 & 0 \end{array} \right]
$$

It is easy to show that the Hankel singular values of $G$ are $\sigma _ { 1 } = 1 . 6 0 6 1$ and $\sigma _ { 2 } = 0 . 8 5 6 1$ . The $\mathcal { H } _ { \infty }$ norm of G is $\| G \| _ { \infty } = 2 . 9 7 2$ and the $\mathcal { L } _ { 1 }$ norm of $g ( t )$ can be computed as

$$\int_ {0} ^ {\infty} | g (t) | d t = h _ {1} + h _ {2} + h _ {3} + h _ {4} + \ldots$$
