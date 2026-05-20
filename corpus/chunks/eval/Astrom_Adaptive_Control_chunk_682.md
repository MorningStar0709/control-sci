# Application to Recursive Estimation

The basic step in recursive estimation can be described as follows: Let $\theta$ be Gaussian $N(\theta^{0}, P)$ . Assume that a linear observation

$$\boldsymbol {y} = \boldsymbol {\varphi} ^ {T} \boldsymbol {\theta} + \boldsymbol {e}$$

is made, where $e$ is normal $N(0, \sigma^2)$ . The new estimate is then given as the conditional mean $E(\theta | y)$ . The joint covariance matrix of $y$ and $\theta$ is

$$
R = \left( \begin{array}{l l} \varphi^ {T} P \varphi & \varphi^ {T} P \\ P \varphi & P \end{array} \right) + \left( \begin{array}{l l} \sigma^ {2} & 0 \\ 0 & 0 \end{array} \right)
$$

The symmetric nonnegative matrix P has a decomposition $P = LDL^{T}$ , where L is a lower triangular matrix with unit diagonal and D is a nonnegative diagonal matrix. The matrix R can then be written as

$$
\begin{array}{l} R = \left( \begin{array}{l l} \varphi^ {T} L D L ^ {T} \varphi + \sigma^ {2} & \varphi^ {T} L D L ^ {T} \\ L D L ^ {T} \varphi & L D L ^ {T} \end{array} \right) \\ = \left( \begin{array}{c c} 1 & \varphi^ {T} L \\ 0 & L \end{array} \right) \left( \begin{array}{c c} \sigma^ {2} & 0 \\ 0 & D \end{array} \right) \left( \begin{array}{c c} 1 & 0 \\ L ^ {T} \varphi & L ^ {T} \end{array} \right) \tag {11.32} \\ \end{array}
$$

If this matrix can be transformed to

$$
R = \left( \begin{array}{l l} 1 & 0 \\ K & \tilde {L} \end{array} \right) \left( \begin{array}{l l} \tilde {\sigma} ^ {2} & 0 \\ 0 & \tilde {D} \end{array} \right) \left( \begin{array}{l l} 1 & K ^ {T} \\ 0 & \tilde {L} ^ {T} \end{array} \right) \tag {11.33}
$$

Theorem 11.1 can be used to obtain the recursive estimate as

$$\hat {\theta} = \theta^ {0} + K (y - \varphi^ {T} \theta)$$

with covariance

$$P = \tilde {L} \tilde {D} \tilde {L} ^ {T}$$

The algorithm can thus be described as follows.
