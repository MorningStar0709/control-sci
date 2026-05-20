Notice that the matrix $P(t)$ is defined only when the matrix $\Phi^T (t)\Phi (t)$ is nonsingular. Since

$$\Phi^ {T} (t) \Phi (t) = \sum_ {i = 1} ^ {t} \varphi (i) \varphi^ {T} (i)$$

it follows that $\Phi^{T}\Phi$ is always singular if t < n. To obtain an initial condition for P, it is thus necessary to choose $t = t_{0}$ such that $\Phi^{T}(t_{0})\Phi(t_{0})$ is nonsingular. The initial conditions are then

$$P \left(t _ {0}\right) = \left(\Phi^ {T} \left(t _ {0}\right) \Phi \left(t _ {0}\right)\right) ^ {- 1}\hat {\theta} \left(t _ {0}\right) = P \left(t _ {0}\right) \Phi^ {T} \left(t _ {0}\right) Y \left(t _ {0}\right)$$

The recursive equations can then be used for $t > t_{0}$ . It is, however, often convenient to use the recursive equations in all steps. If the recursive equations are started with the initial condition

$$P (0) = P _ {0}$$

where $P_0$ is positive definite, then

$$P (t) = \left(P _ {0} ^ {- 1} + \Phi^ {T} (t) \Phi (t)\right) ^ {- 1}$$

Notice that $P(t)$ can be made arbitrarily close to $\left(\Phi^T (t)\Phi (t)\right)^{-1}$ by choosing $P_0$ sufficiently large.

By using the Kalman filter interpretation of the least-squares method, it may be seen that this way of starting the recursion corresponds to the situation in which the parameters have an initial distribution with mean $\theta_{0}$ and covariance $P_{0}$ .
