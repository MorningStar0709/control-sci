# THEOREM 2.4 Recursive least squares with exponential forgetting

Assume that the matrix $\Phi(t)$ has full rank for $t \geq t_0$ . The parameter $\theta$ , which minimizes Eq. (2.20), is given recursively by

$$
\begin{array}{l} \hat {\theta} (t) = \hat {\theta} (t - 1) + K (t) \left(y (t) - \varphi^ {T} (t) \hat {\theta} (t - 1)\right) \\ K (t) = P (t) \varphi (t) = P (t - 1) \varphi (t) (\lambda I + \varphi^ {T} (t) P (t - 1) \varphi (t)) ^ {- 1} \tag {2.21} \\ \end{array}
P (t) = \left(I - K (t) \varphi^ {T} (t)\right) P (t - 1) / \lambda
$$

□

A disadvantage of exponential forgetting is that data is discounted even if $P(t)\varphi(t)=0$ . This condition implies that $y(t)$ does not contain any new information about the parameter $\theta$ . In this case it follows from Eqs. (2.21) that the matrix P increases exponentially with rate $\lambda$ . Several ways to avoid this are discussed in detail in Chapter 11.

An alternative method of dealing with time-varying parameters is to assume a time-varying mathematical model. Time-varying parameters can be obtained by replacing the first equation of Eqs. (2.18) with the model

$$\theta (t + 1) = \Phi_ {v} \theta (t) + v (t)$$

where $\Phi_{v}$ is a known matrix and $v(t)$ is discrete-time white noise. The filtering interpretation of the least-squares problem given in Remark 2 of Theorem 2.3 can now easily be generalized. The least-squares estimator will then be the Kalman filter. The case $\Phi_{v}=I$ corresponds to a model in which the parameters are drifting Wiener processes.
