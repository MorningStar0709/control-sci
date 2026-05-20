# EXAMPLE 2.18 Prior information in sampled models

Consider the system in Example 2.17. Sampling the system with sampling period h gives the pulse transfer operator

$$H (q) = \frac {b _ {1} q + b _ {2}}{q ^ {2} + a _ {1} q + a _ {2}}$$

where

$$
\begin{array}{l} b _ {1} = \theta_ {3} \frac {\theta_ {1} \left(1 - e ^ {- h / \theta_ {1}}\right) - \theta_ {2} \left(1 - e ^ {- h / \theta_ {2}}\right)}{\theta_ {1} - \theta_ {2}} \\ b _ {2} = \theta_ {3} \frac {\theta_ {2} \left(1 - e ^ {- h / \theta_ {2}}\right) e ^ {- h / \theta_ {1}} - \theta_ {1} \left(1 - e ^ {- h / \theta_ {1}}\right) e ^ {- h / \theta_ {2}}}{\theta_ {1} - \theta_ {2}} \\ a _ {1} = - \left(e ^ {- h / \theta_ {1}} + e ^ {- h / \theta_ {2}}\right) \\ a _ {2} = e ^ {- (1 / \theta_ {1} + 1 / \theta_ {2}) h} \\ \end{array}
$$

The pulse transfer function is nonlinear in $\theta_{1}$ , $\theta_{2}$ , and $\theta_{3}$ . Further, both parameters appear in all the coefficients of the discrete-time pulse transfer function. This implies that a change in the unknown time constant $\theta_{2}$ will influence all the coefficients in the sampled data model. There is, however, some structure in the parameter dependence. The denominator polynomial can be written as

$$
\begin{array}{l} q ^ {2} + a _ {1} q + a _ {2} = \left(q - e ^ {- h / \theta_ {1}}\right) \left(q - e ^ {- h / \theta_ {2}}\right) \\ = \left(q - \alpha_ {1}\right) \left(q - \alpha_ {2}\right) \\ \end{array}
$$

When $\theta_{1}$ is known, one factor of $A(q)$ is thus known. By reparameterization the sampled model can be written as

$$H (q) = \frac {b _ {1} q + b _ {2}}{(q - \alpha_ {1}) (q - \alpha_ {2})}$$

The prior information can be used to reduce the estimated parameters from 4 to 3. Further simplifications can be made when the sampling interval is small in comparison with $\theta_{1}$ and $\theta_{2}$ . A series approximation of $b_{1}$ and $b_{2}$ in h gives

$$b _ {1} \approx \frac {\theta_ {3}}{2 \theta_ {1} \theta_ {2}} h ^ {2} - \frac {\theta_ {3} (\theta_ {1} + \theta_ {2})}{6 \theta_ {1} ^ {2} \theta_ {2} ^ {2}} h ^ {3}b _ {2} \approx \frac {\theta_ {3}}{2 \theta_ {1} \theta_ {2}} h ^ {2} - \frac {\theta_ {3} (\theta_ {1} + \theta_ {2})}{\theta_ {1} ^ {2} \theta_ {2} ^ {2}} h ^ {3}$$

For short sampling periods we have

$$b _ {1} \approx b _ {2} \approx \frac {\theta_ {3}}{2 \theta_ {1} \theta_ {2}} h ^ {2}$$

The model can now be described by

$$H (q) = \frac {k (q + 1)}{(q - \alpha_ {1}) (q - \alpha_ {2})}$$
