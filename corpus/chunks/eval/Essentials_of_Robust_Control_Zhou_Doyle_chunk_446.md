$$
\left\| \left[ \begin{array}{c} K \\ I \end{array} \right] (I + G _ {r} K) ^ {- 1} \tilde {M} _ {r} ^ {- 1} \right\| _ {\infty} \leq (\delta - \epsilon) ^ {- 1}.
$$

(b) Let $W ( s ) , W ^ { - 1 } ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ be obtained from the following spectral factorization:

$$W ^ {- 1} W ^ {- *} = \tilde {M} _ {r} \tilde {M} _ {r} ^ {*} + \tilde {N} _ {r} \tilde {N} _ {r} ^ {*}.$$

Show that $\left\| W \right\| _ { \infty } \le \frac { 1 } { 1 - \epsilon }$ and $\begin{array} { r } { \left. W ^ { - 1 } \right. _ { \infty } \leq 1 + \epsilon } \end{array}$

(c) Show that

$$
\delta_ {r n} ^ {- 1} := \inf _ {K _ {1}} \left\| \left[ \begin{array}{c} K _ {1} \\ I \end{array} \right] (I + G _ {r} K _ {1}) ^ {- 1} (W \tilde {M} _ {r}) ^ {- 1} \right\| _ {\infty}

= \inf _ {K _ {1}} \left\| \left[ \begin{array}{c} K _ {1} \\ I \end{array} \right] (I + G _ {r} K _ {1}) ^ {- 1} \left[ \begin{array}{c c} I & G _ {r} \end{array} \right] \right\| _ {\infty} \leq \frac {\left\| W ^ {- 1} \right\| _ {\infty}}{\delta - \epsilon} \leq \frac {1 + \epsilon}{\delta - \epsilon}.
$$

and

$$
\left\| \left[ \begin{array}{c} K _ {1} \\ I \end{array} \right] (I + G _ {r} K _ {1}) ^ {- 1} \tilde {M} _ {r} ^ {- 1} \right\| _ {\infty} \leq \delta_ {r n} ^ {- 1} \| W \| _ {\infty}.
$$

(d) With the controller $K _ { 1 }$ given in (c), show that

$$
\left\| \left[ \begin{array}{c} K _ {1} \\ I \end{array} \right] (I + G K _ {1}) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} = \left\| \left[ \begin{array}{c} K _ {1} \\ I \end{array} \right] (I + G K _ {1}) ^ {- 1} \left[ \begin{array}{c c} I & G \end{array} \right] \right\| _ {\infty} \leq \delta_ {\text {red}} ^ {- 1}
$$

where

$$\delta_ {\mathrm{red}} := \frac {\delta_ {r n}}{\| W \| _ {\infty}} - \epsilon \leq \frac {\delta - \epsilon}{\| W ^ {- 1} \| _ {\infty} \| W \| _ {\infty}} - \epsilon \leq \frac {1 - \epsilon}{1 + \epsilon} (\delta - \epsilon) - \epsilon .$$

Note that if $\tilde { N } _ { r }$ and $\tilde { M _ { r } }$ are the kth-order balanced truncation of $\tilde { N }$ and $\tilde { M }$ , then $\delta = \delta _ { r n } = \sqrt { 1 - \sigma _ { 1 } ^ { 2 } } , \delta _ { \mathrm { r e d } } = \delta - \epsilon ,$ , and $\textstyle \epsilon \leq 2 \sum _ { i = k + 1 } ^ { n } \sigma _ { i }$ , where $\sigma _ { i }$ are the Hankel singular values of $\left[ \begin{array} { l l } { \tilde { M } } & { \tilde { N } } \end{array} \right]$ .

(e) Show that
