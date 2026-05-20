# THEOREM 2.2 Statistical properties of least-squares estimation

Consider the estimate in Eq. (2.6) and assume that data is generated from Eq. (2.12), where $\{e(i), i = 1, 2, \ldots\}$ is a sequence of independent random variables with zero mean and variance $\sigma^{2}$ . Let E denote mathematical expectation and cov the covariance of a random variable.

If $\Phi^T\Phi$ is nonsingular, then

(i) $E\hat{\theta} (t) = \theta^0$   
(ii) $\operatorname{cov} \hat{\theta}(t) = \sigma^2 (\Phi^T \Phi)^{-1}$   
(iii) $\hat{\sigma}^2 (t) = 2V(\hat{\theta},t) / (t - n)$ is an unbiased estimate of $\sigma^2$

where n is the number of parameters in $\theta^{0}$ and $\hat{\theta}$ and t is the number of data points.

The theorem states that the estimates are unbiased, that is, $E\hat{\theta}(t) = \theta^{0}$ . Further, it is desirable that an estimate converges to the true parameter value as the number of observations increases toward infinity. This property is called consistency. There are several notions of consistency corresponding to different convergence concepts for random variables. Mean square convergence is one possibility, which can be investigated simply by analyzing the variance of the estimate. The result (ii) can be used to determine how the variance of the estimate decreases with the number of observations. This is illustrated by an example.
