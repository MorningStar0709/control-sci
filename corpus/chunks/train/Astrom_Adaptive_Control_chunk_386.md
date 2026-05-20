and unstable otherwise. These bounds are shown as dashed lines in Fig. 6.2. If the parameter $\hat{\theta}$ is kept constant, $y$ diverges monotonically at the lower bound and diverges in an oscillatory manner with period 2 at the upper bound. In reality, parameter $\hat{\theta}$ will of course change. The smaller the adaptation gain is, the smaller rate of change. With the numbers used in the simulation the bounds are 0.5 and 2.5. The behavior shown in Fig. 6.2 can thus be explained qualitatively. The solution approaches the curve (6.12) and then moves along this curve. The variable $y$ appears to grow exponentially for $\hat{\theta} < 0.5$ ; it decays exponentially for $0.5 < \hat{\theta} < 1.5$ and decays in an oscillatory manner for $1.5 < \hat{\theta} < 2.5$ . The variable grows in an oscillatory manner for $\hat{\theta} > 2.5$ .

We now turn our attention to the equation for the parameter estimate. Introducing

$$\tilde {\theta} = \hat {\theta} - \theta_ {0}$$

we find

$$\tilde {\theta} (t + 1) = \left(1 - \gamma \frac {y ^ {2} (t)}{\alpha + y ^ {2} (t)}\right) \tilde {\theta} (t) + \gamma \frac {a y (t)}{\alpha + y ^ {2} (t)} \tag {6.13}$$

This equation implies that the signals y and $\tilde{\theta}$ cannot be unbounded because Eq. (6.13) is always stable when $\gamma$ is sufficiently small. For large values of $y(t)$ the added term is small, and the solution will decay. It thus appears as though the equilibrium solution that is locally stable may also be globally stable in this case. A more precise discussion of this is given in Section 6.5.
