# THEOREM 11.1 Conditional mean values and covariances

Let the vectors x and y be jointly Gaussian random variables with mean values

$$E \binom{y}{x} = \binom{m _ {y}}{m _ {x}} \tag {11.23}$$

and covariance

$$
\operatorname{cov} \binom {y} {x} = \left( \begin{array}{c c} R _ {y} & R _ {y x} \\ R _ {x y} & R _ {x} \end{array} \right) = R \tag {11.24}
$$

where $R_{xy} = R_{yx}^T$ . Further assume that $\dim x = n$ and $\dim y = p$ . The conditional mean value of $x$ , given $y$ , is Gaussian with mean

$$E (x | y) = m _ {x} + R _ {x y} R _ {y} ^ {- 1} (y - m _ {y}) \tag {11.25}$$

and covariance

$$\operatorname{cov} (x \mid y) = R _ {x \mid y} = R _ {x} - R _ {x \dot {y}} R _ {y} ^ {- 1} R _ {y x} \tag {11.26}$$

A nonnegative matrix R can be decomposed as

$$
R = \rho \left( \begin{array}{c c} I & 0 \\ K & L _ {x} \end{array} \right) \left( \begin{array}{c c} D _ {y} & 0 \\ 0 & D _ {x} \end{array} \right) \left( \begin{array}{c c} I & 0 \\ K & L _ {x} \end{array} \right) ^ {T} \tag {11.27}
$$

where $D_x$ and $D_y$ are diagonal matrices and $L_x$ is lower triangular. Then

$$R _ {x y} R _ {y} ^ {- 1} = K \tag {11.28}$$

and

$$R _ {x \mid y} = \rho L _ {x} D _ {x} L _ {x} ^ {T} \tag {11.29}$$

Proof: We first show that the vector z defined by

$$z = x - m _ {x} - R _ {x y} R _ {y} ^ {- 1} \left(y - m _ {y}\right) \tag {11.30}$$

has zero mean, is independent of y, and has the covariance

$$R _ {z} = R _ {x} - R _ {x y} R _ {y} ^ {- 1} R _ {y z} \tag {11.31}$$

The mean value is zero. Furthermore,

$$
\begin{array}{l} E z (y - m _ {y}) ^ {T} = E \left\{(x - m _ {x}) (y - m _ {y}) ^ {T} - R _ {x y} R _ {y} ^ {- 1} (y - m _ {y}) (y - m _ {y}) ^ {T} \right\} \\ = R _ {x y} - R _ {x y} R _ {y} ^ {- 1} R _ {y} = 0 \\ \end{array}
$$

The variables z and y are thus uncorrelated. Since they are Gaussian, they are also independent. It now follows that

$$
\binom {y \dots m _ {y}} {x - m _ {x}} = \left( \begin{array}{c c} I & 0 \\ R _ {x y} R _ {y} ^ {\dots 1} & I \end{array} \right) \binom {y - m _ {y}} {z}
$$

The joint density function of x and y is

$$
\begin{array}{l} f (x, y) = (2 \pi) ^ {- (n + p) / 2} (\det R) ^ {- 1 / 2} \\ \exp \left\{- \frac {1}{2} \left(z ^ {T} R _ {z} ^ {- 1} z + (y - m _ {y}) ^ {T} R _ {y} ^ {- 1} (y - m _ {y})\right) \right\} \\ \end{array}
$$

The density function of $y$ is

$$f (y) = (2 \pi) ^ {- p / 2} (\det R _ {y}) ^ {- 1 / 2} \exp \left\{- \frac {1}{2} (y - m _ {y}) ^ {T} R _ {y} ^ {1} (y - m _ {y}) \right\}$$

where p is the dimension of y. The conditional density is then

$$f (x | y) = \frac {f (x , y)}{f (y)} = (2 \pi) ^ {- n / 2} (\det R _ {y}) ^ {1 / 2} (\det R) ^ {- 1 / 2} \exp \left\{- \frac {1}{2} z ^ {T} R _ {z} ^ {- 1} z \right\}$$
