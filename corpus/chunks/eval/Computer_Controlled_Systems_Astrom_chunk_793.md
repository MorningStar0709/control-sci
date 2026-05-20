# Statistical Interpretation

To analyze the properties of the least-squares estimator, it is necessary to make some assumptions. Let the data be generated from the process

$$y = \Phi \theta_ {0} + \varepsilon \tag {13.8}$$

where $\theta_{0}$ is the vector of “true” parameters, and $\varepsilon$ is a vector of noise with zero-mean value. The following theorem is given without proof.

THEOREM 13.2 PROPERTIES OF LEAST-SQUARES ESTIMATE Consider the estimate (13.5) and assume that the data are generated from (13.8), where $\varepsilon$ is white noise with variance $\sigma^2$ . Then, if $n$ is the number of parameters of $\hat{\theta}$ and $\theta_0$ and $N$ is the number of data, the following conditions hold.

1. $\mathbf{E}\hat{\theta} = \theta_0$   
2. $\operatorname{var} \hat{\theta} = \sigma^2 (\Phi^T \Phi)^{-1}$   
3. $s^2 = 2J(\theta) / (N - n)$ is an unbiased estimate of $\sigma^2$

Theorem 13.2 implies that the parameters in (13.1) can be estimated without bias if $C(q) = q^n$ . If $C(q) \neq q^n$ , then the estimates will be biased. This is due to the correlation between the noise $C^*(q^{-1})e(k)$ and the data in $\varphi(k)$ .
