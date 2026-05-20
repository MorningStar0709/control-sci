# Recursive Least Squares

Parameter convergence for recursive least squares is first discussed for the simple model (6.21), which is linear in the parameters and for which are no disturbances. Let the parameter vector have n elements. The parameters can be calculated exactly from n data points, provided that the vectors $\varphi(1),\ldots,\varphi(n)$ are linearly independent. The least-squares estimate is given by

$$
\begin{array}{l} \hat {\theta} (n) = \left(\sum_ {k = 1} ^ {n} \varphi (k) \varphi^ {T} (k)\right) ^ {- 1} \sum_ {k = 1} ^ {n} \varphi (k) y (k) \\ = \left(\sum_ {k = 1} ^ {n} \varphi (k) \varphi^ {T} (k)\right) ^ {1} \sum_ {k = 1} ^ {n} \varphi (k) \varphi^ {T} (t) \theta^ {0} = \theta^ {0} \tag {6.27} \\ \end{array}
$$

The correct state is obtained in n steps. If the estimate is instead calculated by recursive least squares, the following estimate is obtained:

$$\hat {\theta} (t) = \left(P ^ {- 1} (0) + \sum_ {k = 1} ^ {t} \varphi (k) \varphi^ {T} (k)\right) ^ {- 1} \left(\sum_ {k = 1} ^ {t} \varphi (k) y (k) + P ^ {- 1} (0) \hat {\theta} (0)\right) \tag {6.28}$$

where $\hat{\theta}(0)$ is the initial estimate and $P(0)$ is the initial covariance of the estimator. By making $P(0)$ positive definite but arbitrarily large, the result from the recursive estimation can be made arbitrarily close to the true value.

From this analysis we obtain the following result.
