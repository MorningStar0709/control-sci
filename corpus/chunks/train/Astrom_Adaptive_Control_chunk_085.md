# THEOREM 2.3 Recursive least-squares estimation (RLS)

Assume that the matrix $\Phi(t)$ has full rank, that is, $\Phi^T(t)\Phi(t)$ is nonsingular, for all $t \geq t_0$ . Given $\hat{\theta}(t_0)$ and $P(t_0) = (\Phi^T(t_0)\Phi(t_0))^{-1}$ , the least-squares estimate $\hat{\theta}(t)$ then satisfies the recursive equations

$$
\hat {\theta} (t) = \hat {\theta} (t - 1) + K (t) \left(y (t) - \varphi^ {T} (t) \hat {\theta} (t - 1)\right) \tag {2.15}K (t) = P (t) \varphi (t) = P (t - 1) \varphi (t) \left(I + \varphi^ {T} (t) P (t - 1) \varphi (t)\right) ^ {- 1} \tag {2.16}
\begin{array}{l} P (t) = P (t - 1) - P (t - 1) \varphi (t) \left(I + \varphi^ {T} (t) P (t - 1) \varphi (t)\right) ^ {- 1} \varphi^ {T} (t) P (t - 1) \\ = \left(I - K (t) \varphi^ {T} (t)\right) P (t - 1) \tag {2.17} \\ \end{array}
$$

□

Remark 1. Equation (2.15) has strong intuitive appeal. The estimate $\hat{\theta}(t)$ is obtained by adding a correction to the previous estimate $\hat{\theta}(t-1)$ . The correction is proportional to $y(t)-\varphi^{T}(t)\hat{\theta}(t-1)$ , where the last term can be interpreted as the value of $y$ at time $t$ predicted by the model of Eq. (2.1). The correction term is thus proportional to the difference between the measured value of $y(t)$ and the prediction of $y(t)$ based on the previous parameter estimate. The components of the vector $K(t)$ are weighting factors that tell how the correction and the previous estimate should be combined.

Remark 2. The least-squares estimate can be interpreted as a Kalman filter for the process

$$\theta (t + 1) = \theta (t) \tag {2.18}y (t) = \varphi^ {T} (t) \theta (t) + e (t)$$

Remark 3. The recursive equations can also be derived by starting with the loss function of Eq. (2.2). Using Eqs. (2.8) and (2.6) gives

$$
\begin{array}{l} 2 V (\theta , t) = 2 V (\theta , t - 1) + \varepsilon^ {2} (\theta , t) \\ = Y ^ {T} (t - 1) \left(I - \Phi (t - 1) \left(\Phi^ {T} (t - 1) \Phi (t - 1)\right) ^ {- 1} \Phi (t - 1)\right) Y (t - 1) \\ + \left(\theta - \hat {\theta} (t - 1)\right) ^ {T} \Phi^ {T} (t - 1) \Phi (t - 1) \left(\theta - \hat {\theta} (t - 1)\right) \\ + \left(y (t) - \varphi^ {T} (t) \theta\right) ^ {T} \left(y (t) - \varphi^ {T} (t) \theta\right) \tag {2.19} \\ \end{array}
$$

The first term on the right-hand side is independent of $\theta$ , and the remaining two terms are quadratic in $\theta$ . $V(\theta, t)$ can then easily be minimized with respect to $\theta$ .
