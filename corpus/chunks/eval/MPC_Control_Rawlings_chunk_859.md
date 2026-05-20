# A.16 Multivariate Density Functions

In applications we normally do not have a single random variable but a collection of random variables. We group these variables together in a vector and let random variable $\xi$ now take on values in Rn. The probability density function is still a nonnegative scalar function

$$p _ {\xi} (x): \mathbb {R} ^ {n} \to \mathbb {R} ^ {+}$$

which is sometimes called the joint density function. As in the scalar case, the probability that the n-dimensional random variable $\xi$ takes on values between a and b is given by

$$\operatorname * {P r} (a \leq \xi \leq b) = \int_ {a _ {n}} ^ {b _ {n}} \dots \int_ {a _ {1}} ^ {b _ {1}} p _ {\xi} (x) d x _ {1} \dots d x _ {n}$$

Marginal density functions. We are often interested in only some subset of the random variables in a problem. Consider two vectors of random variables, $\xi \in \mathbb { R } ^ { n }$ and $\eta \in \mathbb { R } ^ { m }$ . We can consider the joint distribution of both of these random variables $p _ { \xi , \eta } ( x , y )$ or we may only be interested in the $\xi$ variables, in which case we can integrate out the m η variables to obtain the marginal density of $\xi$

$$p _ {\xi} (x) = \int_ {- \infty} ^ {\infty} \dots \int p _ {\xi , \eta} (x, y) d y _ {1} \dots d y _ {m}$$

Analogously to produce the marginal density of η we use

$$p _ {\eta} (y) = \int_ {- \infty} ^ {\infty} \dots \int p _ {\xi , \eta} (x, y) d x _ {1} \dots d x _ {n}$$

Multivariate normal density. We define the multivariate normal density of the random variable $\boldsymbol { \xi } \in \mathbb { R } ^ { n }$ as

$$p _ {\xi} (x) = \frac {1}{(2 \pi) ^ {n / 2} (\det P) ^ {1 / 2}} \exp \left[ - \frac {1}{2} (x - m) ^ {\prime} P ^ {- 1} (x - m) \right] \tag {A.22}$$

in which $m \in \mathbb { R } ^ { n }$ is the mean and $P \in \mathbb { R } ^ { n \times n }$ is the covariance matrix. The notation det P denotes determinant of P. As noted before, P is a real, symmetric matrix. The multivariate normal density is well-defined only for $P > 0$ . The singular, or degenerate, case $P \geq 0$ is discussed subsequently. Shorthand notation for the random variable $\xi$ having a normal distribution with mean m and covariance P is

![](image/1c505f13a6715366424e7e8094b1813d3a29a331412cb6fa1b75519b4af0de25.jpg)

<details>
<summary>line</summary>

| x1 | y |
| --- | --- |
| -2 | 0 |
| -1 | 0.25 |
| 0 | 0.5 |
| 1 | 0.5 |
| 2 | 0.25 |
| 1 | 0 |
| 0 | -0.25 |
| -1 | -0.5 |
| -2 | -0.75 |
| -1 | -1 |
| 0 | -1.25 |
| 1 | -1.5 |
| 2 | -1.75 |
| 1 | -2 |
| 0 | -2 |
| -1 | -2 |
| -2 | -2 |
</details>
