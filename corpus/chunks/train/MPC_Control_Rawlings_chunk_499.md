$$
\begin{array}{l} \operatorname * {P r} (P _ {s} (x; s)) = \left\{ \begin{array}{l l} \binom {s} {i} P (x) ^ {i} (1 - P (x)) ^ {s - i}, & P _ {s} = \frac {i}{s}, \quad i = 0, \dots , s \\ 0, & \text { otherwise } \end{array} \right. \\ - \infty <   x <   \infty \tag {4.40} \\ \end{array}
$$

These probabilities are calculated as follows. For $P _ { s }$ to take on value zero, for example, all of the samples $x _ { i }$ must be greater than x. The probability that any $x _ { i }$ is greater than x is $1 - P ( x )$ . Because the samples are mutually independent, the probability that all s samples are greater than x is $( 1 - P ( x ) ) ^ { s }$ , which is the i = 0 entry of (4.40). Similarly, for $P _ { s }$ to have value $i / s ,$ , i samples must be less than x and $s - i$ samples must be greater than x. This probability is given by $\binom { s } { i } P ( x ) ^ { i } ( 1 - ^ { ^ { \circ } } P ( x ) ^ { s - i } )$ , in which $P ( x ) ^ { i } ( 1 - P ( x ) ^ { s - i } )$ is the probability of having a sample with i values less than x and $s - i$ values greater than x, and $\binom { s } { i }$ accounts for the number of ways such a sample can be drawn from a set of s samples. Figure 4.10 shows the distribution of $P _ { s }$ for a sample size $s = 5$ at the mean, $P ( x ) = 0 . 5$ . Notice the maximum probability occurs near the value $P _ { s } = P ( { \boldsymbol { x } } )$ but the probability distribution is fairly wide with only 5 samples. The number of samples is increased to 50 in Figure 4.11, and three different x values are shown, at which $P ( x ) =$ 0.05, 0.5, 0.95. The peak for each $P _ { s }$ distribution is near the value $P ( x )$ , and the distribution is much narrower for 50 samples. The sampled density $P _ { s } ( x ; s )$ becomes arbitrarily sharply distributed with value $P ( x )$

![](image/9c0a253b360939e5b935a36de4a9788a03403712f19c790bf3b0cff5de9b750d.jpg)

<details>
<summary>bar</summary>

| Ps Range | Pr(Ps) |
| --- | --- |
| 0.00 - 0.05 | 0.26 |
| 0.05 - 0.10 | 0.22 |
| 0.10 - 0.15 | 0.14 |
| 0.15 - 0.20 | 0.07 |
| 0.20 - 0.25 | 0.03 |
| 0.25 - 0.30 | 0.01 |
| 0.30 - 0.35 | 0.02 |
| 0.35 - 0.40 | 0.04 |
| 0.40 - 0.45 | 0.08 |
| 0.45 - 0.50 | 0.11 |
| 0.50 - 0.55 | 0.13 |
| 0.55 - 0.60 | 0.12 |
| 0.60 - 0.65 | 0.09 |
| 0.65 - 0.70 | 0.06 |
| 0.70 - 0.75 | 0.04 |
| 0.75 - 0.80 | 0.03 |
| 0.80 - 0.85 | 0.02 |
| 0.85 - 0.90 | 0.14 |
| 0.90 - 0.95 | 0.22 |
| 0.95 - 1.00 | 0.26 |
</details>
