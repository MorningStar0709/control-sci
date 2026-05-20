# Mean Value of a Quadratic Form

In the following, expressions of the form

$$\mathbf {E} \boldsymbol {x} ^ {T} \boldsymbol {S} \boldsymbol {x}$$

will be evaluated, where $x$ is a Gaussian random variable with mean $m$ and covariance matrix $R$ . We have

$$\mathbf {E} x ^ {T} S x = \mathbf {E} (x - m) ^ {T} S (x - m) + \mathbf {E} m ^ {T} S x + \mathbf {E} x ^ {T} S m - \mathbf {E} m ^ {T} S m= \mathbf {E} (x - m) ^ {T} S (x - m) + m ^ {T} S m$$

Further,

$$
\begin{array}{l} \mathbf {E} (x - m) ^ {T} S (x - m) = \mathbf {E} \operatorname{tr} (x - m) ^ {T} S (x - m) = \mathbf {E} \operatorname{tr} S (x - m) (x - m) ^ {T} \\ = \operatorname{tr} \operatorname{SE} (x - m) (x - m) ^ {T} = \operatorname{tr} S R \\ \end{array}
$$

Thus

$$\mathbf {E} x ^ {T} S x = m ^ {T} S m + \operatorname{tr} S R \tag {11.28}$$
