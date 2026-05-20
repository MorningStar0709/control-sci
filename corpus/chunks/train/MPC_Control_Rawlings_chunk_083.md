# 1.4.1 Linear Systems and Normal Distributions

This section summarizes the probability and random variable results required for deriving a linear optimal estimator such as the Kalman filter. We assume that the reader is familiar with the concepts of a random variable, probability density and distribution, the multivariate normal distribution, mean and variance, statistical independence, and conditional probability. Readers unfamiliar with these terms should study the material in Appendix A before reading this and the next sections.

In the following discussion let x, y, and z be vectors of random variables. We use the notation

$$x \sim N (m, P)p _ {x} (x) = n (x, m, P)$$

to denote random variable x is normally distributed with mean m and covariance (or simply variance) P, in which

$$n (x, m, P) = \frac {1}{(2 \pi) ^ {n / 2} (\det P) ^ {1 / 2}} \exp \left[ - \frac {1}{2} (x - m) ^ {\prime} P ^ {- 1} (x - m) \right] \tag {1.20}$$

and det P denotes the determinant of matrix P. Note that if $x \in \mathbb { R } ^ { n }$ , then $m \in \mathbb { R } ^ { n }$ and $P \in \mathbb { R } ^ { n \times n }$ is a positive definite matrix. We require three main results. The simplest version can be stated as follows.

Joint independent normals. If x and y are normally distributed and (statistically) independent5

$$x \sim N (m _ {x}, P _ {x}) \quad y \sim N (m _ {y}, P _ {y})$$

then their joint density is given by

$$
p _ {x, y} (x, y) = n \left(x, m _ {x}, P _ {x}\right) n \left(y, m _ {y}, P _ {y}\right)
\left[ \begin{array}{l} x \\ y \end{array} \right] \sim N \left(\left[ \begin{array}{l} m _ {x} \\ m _ {y} \end{array} \right], \left[ \begin{array}{c c} P _ {x} & 0 \\ 0 & P _ {y} \end{array} \right]\right) \tag {1.21}
$$

Note that, depending on convenience, we use both $( x , y )$ and the vector $\left[ \begin{array} { l } { x } \\ { y } \end{array} \right]$ to denote the pair of random variables.

Linear transformation of a normal. If x is normally distributed with mean m and variance P, and y is a linear transformation of x, $y = A x$ , then y is distributed with mean Am and variance $A P A ^ { \prime }$

$$x \sim N (m, P) \quad y = A x \quad y \sim N (A m, A P A ^ {\prime}) \tag {1.22}$$

Conditional of a joint normal. If x and y are jointly normally distributed as

$$
\left[ \begin{array}{c} x \\ y \end{array} \right] \sim N \left(\left[ \begin{array}{c} m _ {x} \\ m _ {y} \end{array} \right] \left[ \begin{array}{c c} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right]\right)
$$
