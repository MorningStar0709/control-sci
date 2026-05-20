# Projections, Leakage, and Dead Zones

Equilibrium analysis based on averaging shows that the equilibria depend on the unmodeled dynamics and the nature of the command signal in a complicated way. Some general conclusions can be extracted, however. If the command signal is not persistently exciting of an order that corresponds to the number of updated parameters, the equilibrium set will in general be a manifold rather than a point. For systems that are linear in the parameters, the equilibria will actually be an affine set, which means that the controller gains may be very large on some points of the set. Small amounts of measurement noise or other disturbances may then cause a loss of equilibrium and result in drift of the parameters.

Several ideas have been proposed to modify the adaptive algorithms to avoid the difficulty. One possibility is to modify the algorithm so that the parameters are projected into a given fixed set. However, this requires that appropriate prior knowledge be available. For example, in Example 6.11 it is sufficient to project into a set such that $0 \leq \hat{\theta}_{2} \leq 17$ . A convenient way to obtain a controller with a finite gain is to introduce a path parallel to the process with gain $\rho$ . Let $G_{r}$ be the transfer function of the controller. The arrangement with the parallel path is equivalent to use a controller with the transfer function

$$G _ {r} ^ {\prime} = \frac {G _ {r}}{1 + \rho G _ {r}}$$

This is clearly bounded by $1 / \rho$ when $G_{r}$ has high gain.

In Section 5.3 we showed that the normalization in the estimator (6.2) is important to improve the properties of the algorithms. The normalization comes automatically when least-squares methods are used. Another modification is to change the parameter updating in Eq. (6.2) to

$$\frac {d \hat {\theta}}{d t} = \gamma \frac {\varphi e}{\alpha + \varphi^ {T} \varphi} + \alpha_ {1} (\theta^ {0} - \hat {\theta}) \tag {6.84}$$

where $\theta^{0}$ is an a priori estimate of the parameters and $\alpha_{1}>0$ is an appropriate constant. The added term $\alpha_{1}(\theta^{0}-\hat{\theta})$ , sometimes called leakage, will make sure the estimates are driven toward $\theta^{0}$ when they are far from $\theta^{0}$ . However, the modification will change the equilibrium. A priori knowledge is also required to choose $\theta^{0}$ and $\alpha_{1}$ .
