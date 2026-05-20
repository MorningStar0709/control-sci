Remark 1. Equation (13.10) has a strong intuitive appeal. The estimate $\hat{\theta}(N+1)$ is obtained by adding a correction to the previous estimate $\hat{\theta}(N)$ . The correction is proportional to $y_{N+1}-\varphi^{T}(N+1)\hat{\theta}(N)$ , where the last term can be interpreted as the value of $y$ at time $N+1$ predicted by the model (13.2). The correction term is thus proportional to the difference between the measured value of $y_{N+1}$ and the prediction of $y_{N+1}$ based on the previous estimates of the parameters. The components of the vector $K(N)$ are weighting factors that tell how the correction and the previous estimate should be combined. Notice that the $i$ th component of $K(N)$ is proportional to $\varphi_{i}^{T}(N+1)$ .

Remark 2. The least-squares estimate can be interpreted as a Kalman filter for the process

$$
\begin{array}{l} \theta (k + 1) = \theta (k) \\ y (k) = \varphi^ {T} (k) \theta (k) + e (k) \\ \end{array}
$$

See Section 11.3.

Notice that the matrix $P(N)$ is defined only when the matrix $\Phi^{T}(N)\Phi(N)$ is nonsingular. Because

$$\Phi^ {T} (N) \Phi (N) = \sum_ {k = 1} ^ {N} \varphi (k) \varphi^ {T} (k)$$

it follows that $\Phi^T\Phi$ is always singular if $N$ is sufficiently small. In order to obtain an initial condition for $P$ , it is necessary to choose an $N = N_0$ such that $\Phi^T(N_0)\Phi(N_0)$ is nonsingular and determine

$$
\begin{array}{l} P (N _ {0}) = \left(\Phi^ {T} (N _ {0}) \Phi (N _ {0})\right) ^ {- 1} \\ \hat {\boldsymbol {\theta}} = P \left(N _ {0}\right) \boldsymbol {\Phi} ^ {T} \left(N _ {0}\right) y \left(N _ {0}\right) \\ \end{array}
$$

The recursive equations can then be used from $N \geq N_{0}$ . It is, however, often convenient to use the recursive equations in all steps. If the recursive equations are begun with the initial condition

$$P (0) = P _ {0}$$

where $P_0$ is positive definite, then

$$P (N) = \left(P _ {0} ^ {- 1} + \Phi^ {T} (N) \Phi (N)\right) ^ {- 1}$$

This can be made arbitrarily close to $\left(\Phi^{T}(N)\Phi(N)\right)^{-1}$ by choosing $P_{0}$ sufficiently large.

. Using the statistical interpretation of the least-squares method shows that this way of starting the recursion corresponds to the situation when the parameters have a prior covariance proportional to $P_{0}$ .
