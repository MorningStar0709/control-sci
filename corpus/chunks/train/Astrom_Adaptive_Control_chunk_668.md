# Estimator Windup

Exponential forgetting works well only if the process is properly excited all the time. There are problems with exponential forgetting when the excitation is poor. To understand this, we first consider the extreme case in which there is no excitation at all, that is, $\varphi = 0$ . The equations for the estimate then become

$$\theta (t + 1) = \theta (t)P (t + 1) = \frac {1}{\lambda} P (t)$$

The equation for the estimate $\theta$ is thus unstable with all eigenvalues equal to 1, and the equation for the P-matrix is unstable with all eigenvalues equal to $1/\lambda$ . In this case the estimate will thus remain constant, and the P-matrix will grow exponentially if $\lambda < 1$ . Since the estimator gain is $P\varphi$ , the gain of the estimator will also grow exponentially. This means that the estimates may change very drastically whenever $\varphi$ becomes different from zero. The phenomenon is called estimator windup in analogy with integrator windup.

A similar situation occurs if the regression vector is different from zero but restricted to a subspace. We illustrate this by an example.
