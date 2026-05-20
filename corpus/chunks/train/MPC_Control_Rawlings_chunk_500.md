Figure 4.11: Probability density Pr $\left( P _ { s } \left( x ; s \right) \right)$ for three different x corresponding to $P ( x ) = 0 . 0 5 , 0 . 5 , 0 . 9 5$ and $s = 5 0$ samples. The three distributions are centered at the correct values, $P ( x )$ , and the variance is much reduced compared to Figure 4.10.

as the sample size s increases.

$$
\lim _ {s \to \infty} \operatorname * {P r} (P _ {s} (x; s)) = \left\{ \begin{array}{l l} 1 & P _ {s} = P (x) \\ 0 & \text { otherwise } \end{array} \right. \quad - \infty <   x <   \infty
$$

The convergence is often not uniform in x. Achieving a given variance in $P _ { s } \left( x ; s \right)$ generally requires larger sample sizes for x values in the tails of the density $p ( x )$ compared to the sample sizes required to achieve this variance for x values in regions of high density. The nonuniform convergence is perhaps displayed more clearly in Figures 4.12 and 4.13. We have chosen the beta distribution for $P ( x )$ and show the spread in the probability of $P _ { s }$ for three x values, corresponding to $P ( x ) ~ = ~ \{ 0 . 1 , 0 . 5 , 0 . 9 \}$ . Given $s ~ = ~ 2 5$ samples in Figure 4.12, we see a rather broad probability distribution for the sampled distribution $P _ { s } ( x )$ . Turning up the number of samples to $s \ = \ 2 5 0$ gives the tighter probability distribution shown in Figure 4.13.

Finally, we present a classic sampling error distribution result due to Kolmogorov. The measure of sampling error is defined to be

$$D _ {s} = \sup _ {x} | P _ {s} (x; s) - P (x) |$$

and we have the following result on the distribution of $D _ { s }$ for large sample sizes.

Theorem 4.29 (Kolmogoroff (1933)). 6 Suppose that $P ( x )$ is continuous. Then for every fixed $z \geq 0$ as $s \to \infty$

$$\operatorname * {P r} \left(D _ {s} \leq z s ^ {- 1 / 2}\right)\rightarrow L (z) \tag {4.41}$$

in which $L ( z )$ is the cumulative distribution function given for $z > 0$ by

$$L (z) = \sqrt {2 \pi} z ^ {- 1} \sum_ {\nu = 1} ^ {\infty} e ^ {- (2 \nu - 1) ^ {2} \pi^ {2} / 8 z ^ {2}} \tag {4.42}$$

and $L ( z ) = 0 \ f o r z \leq 0$ .

One of the significant features of results such as this one is that the limiting distribution is independent of the details of the sampled distribution $P ( x )$ itself. Feller (1948) provides a proof of this theorem and discussion of this and other famous sampling error distribution results due to Smirnov (1939).

![](image/ae8faee60e89c34b23ce0abd726e0e9dc91e34deca8e684c94b96a3df46cc06b.jpg)

<details>
<summary>line</summary>
