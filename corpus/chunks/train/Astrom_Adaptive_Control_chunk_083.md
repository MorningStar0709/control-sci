# Recursive Computations

In adaptive controllers the observations are obtained sequentially in real time. It is then desirable to make the computations recursively to save computation time. Computation of the least-squares estimate can be arranged in such a way that the results obtained at time t - 1 can be used to get the estimates at time t. The solution in Eq. (2.6) to the least-squares problem will be rewritten in a recursive form. Let $\hat{\theta}(t - 1)$ denote the least-squares estimate based on t - 1 measurements. Assume that the matrix $\Phi^{T}\Phi$ is nonsingular for all t. It follows from the definition of $P(t)$ in Eq. (2.3) that

$$
\begin{array}{l} P ^ {- 1} (t) = \Phi^ {T} (t) \Phi (t) = \sum_ {i = 1} ^ {t} \varphi (i) \varphi^ {T} (i) \\ = \sum_ {i = 1} ^ {t - 1} \varphi (i) \varphi^ {T} (i) + \varphi (t) \varphi^ {T} (t) \\ = P ^ {- 1} (t - 1) + \varphi (t) \varphi^ {T} (t) \tag {2.14} \\ \end{array}
$$

The least-squares estimate $\hat{\theta}(t)$ is given by Eq. (2.9):

$$\hat {\theta} (t) = P (t) \left(\sum_ {i = 1} ^ {t} \varphi (i) y (i)\right) = P (t) \left(\sum_ {i = 1} ^ {t - 1} \varphi (i) y (i) + \varphi (t) y (t)\right)$$

It follows from Eqs. (2.9) and (2.14) that

$$\sum_ {i = 1} ^ {t - 1} \varphi (i) y (i) = P ^ {- 1} (t - 1) \hat {\theta} (t - 1) = P ^ {- 1} (t) \hat {\theta} (t - 1) - \varphi (t) \varphi^ {T} (t) \hat {\theta} (t - 1)$$

The estimate at time t can now be written as

$$
\begin{array}{l} \hat {\theta} (t) = \hat {\theta} (t - 1) - P (t) \varphi (t) \varphi^ {T} (t) \hat {\theta} (t - 1) + P (t) \varphi (t) y (t) \\ = \hat {\theta} (t - 1) + P (t) \varphi (t) \left(y (t) - \varphi^ {T} (t) \hat {\theta} (t - 1)\right) \\ = \hat {\theta} (t - 1) + K (t) \varepsilon (t) \\ \end{array}
$$

where

$$
\begin{array}{l} K (t) = P (t) \varphi (t) \\ \varepsilon (t) = y (t) - \varphi^ {T} (t) \hat {\theta} (t - 1) \\ \end{array}
$$

The residual $\varepsilon(t)$ can be interpreted as the error in predicting the signal $y(t)$ one step ahead based on the estimate $\hat{\theta}(t-1)$ .

To proceed, it is necessary to derive a recursive equation for $P(t)$ rather than for $P(t)^{-1}$ as in Eq. (2.14). The following lemma is useful.
