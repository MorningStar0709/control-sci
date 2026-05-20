# Simplified Algorithms

The recursive least-squares algorithm given by Theorem 2.3 has two sets of state variables, $\hat{\theta}$ and $P$ , which must be updated at each step. For large $n$ the updating of the matrix $P$ dominates the computing effort. There are several simplified algorithms that avoid updating the $P$ matrix at the cost of slower convergence. Kaczmarz's projection algorithm is one simple solution. To describe this algorithm, consider the unknown parameter as an element of $R^n$ . One measurement

$$y (t) = \varphi^ {T} (t) \theta \tag {2.22}$$

determines the projection of the parameter vector $\theta$ on the vector $\varphi(t)$ . From this it is immediately clear that $n$ measurements, where $\varphi(1),\ldots,\varphi(n)$ span

$R^{n}$ , are required to determine the parameter vector $\theta$ uniquely. Assume that an estimate $\hat{\theta}(t-1)$ is available and that a new measurement such as Eq. (2.22) is obtained. Since the measurement $y(t)$ contains information only in the direction $\varphi(t)$ in parameter space, it is natural to choose as the new estimate the value $\hat{\theta}(t)$ that minimizes $\|\hat{\theta}(t)-\hat{\theta}(t-1)\|$ subject to the constraint $y(t)=\varphi^{T}(t)\hat{\theta}(t)$ . Introducing a Lagrangian multiplier $\bar{\alpha}$ to handle the constraint, we thus have to minimize the function

$$V = \frac {1}{2} \left(\hat {\theta} (t) - \hat {\theta} (t - 1)\right) ^ {T} \left(\hat {\theta} (t) - \hat {\theta} (t - 1)\right) + \bar {\alpha} \left(y (t) - \varphi^ {T} (t) \hat {\theta} (t)\right)$$

Taking derivatives with respect to $\hat{\theta}(t)$ and $\tilde{\alpha}$ , we get

$$\hat {\theta} (t) - \hat {\theta} (t - 1) - \bar {\alpha} \varphi (t) = 0y (t) - \varphi^ {T} (t) \hat {\theta} (t) = 0$$

Solving these equations gives

$$\hat {\theta} (t) = \hat {\theta} (t - 1) + \frac {\varphi (t)}{\varphi^ {T} (t) \varphi (t)} \left(y (t) - \varphi^ {T} (t) \hat {\theta} (t - 1)\right) \tag {2.23}$$

The updating formula is called Kaczmarz's algorithm. It is useful to be able to change the step length of the parameter adjustment by introducing a factor $\gamma$ . This gives

$$\hat {\theta} (t) - \hat {\theta} (t - 1) + \frac {\gamma \varphi (t)}{\varphi^ {T} (t) \varphi (t)} \left(y (t) - \varphi^ {T} (t) \hat {\theta} (t - 1)\right)$$
