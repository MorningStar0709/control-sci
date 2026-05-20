# A Heuristic Derivation

For sufficiently large t the step size $\gamma(t)$ in Eqs. (6.74) is small, and the correction in $\hat{\theta}(t)$ is small. As in Section 6.6, we can separate the states from the parameters and assume that the parameters are constant in evaluating the behavior of the closed-loop system. Both $R(t)$ and $\varphi(t)$ depend on the parameter estimates. Since $\hat{\theta}$ is assumed to change slowly, the behavior of the model can be approximated by

$$y (t) = \varphi^ {T} (t - d, \bar {\theta}) \bar {\theta}$$

where $\bar{\theta}$ is the averaged value of the estimates. Also, $\varphi$ depends on the estimated variables through the feedback. The updating equation for R can be approximated by

$$\bar {R} (t) = \bar {R} (t - 1) + \gamma (t) \left(G (\bar {\theta}) - \bar {R} (t - 1)\right) \tag {6.77}$$

where

$$G (\bar {\theta}) = E \left\{\varphi (t - d, \bar {\theta}) \varphi^ {T} (t - d, \bar {\theta}) \right\} \tag {6.78}$$

The expectation is taken with respect to the underlying stochastic process in Eq. (6.71) and evaluated for the fixed value of the parameters $\bar{\theta}$ . In the same way the parameter update is approximated by

$$\bar {\theta} (t) = \bar {\theta} (t - 1) + \gamma (t) \bar {R} (t) ^ {- 1} f (\bar {\theta}) \tag {6.79}$$

where

$$f (\bar {\theta}) = E \left\{\varphi (t - d, \bar {\theta}) \left(y (t) - \varphi^ {T} (t - d, \bar {\theta}) \bar {\theta}\right) \right\} \tag {6.80}$$

Equations (6.79) and (6.77) are the averaged difference equations describing the estimator. Now let $\Delta\tau$ be a small number, and let $t'$ be defined by

$$\Delta \tau = \sum_ {k = t} ^ {t ^ {\prime}} \gamma (k)$$

Then

$$\bar {\theta} \left(t ^ {\prime}\right) = \bar {\theta} (t) + \Delta \tau \bar {R} (t) ^ {1} f (\bar {\theta} (t))\bar {R} \left(t ^ {\prime}\right) = \bar {R} (t) + \Delta \tau \left(G (\hat {\theta} (t)) - \bar {R} (t)\right)$$

With a change of time scale such that $t = \tau$ and $t' = t + \Delta\tau$ , these equations can be seen as a difference approximation of the ordinary differential equations

$$\frac {d \theta}{d \tau} = \tilde {R} (\tau) ^ {- 1} f (\bar {\theta} (\tau)) \tag {6.81}\frac {d \bar {R}}{d \tau} = G (\tilde {\theta} (\tau)) - \bar {R} (\tau) \tag {6.82}$$

If stochastic approximation is used, Eq. (6.82) is replaced by

$$\frac {d \bar {r}}{d \tau} = g (\bar {\theta} (\tau)) - \bar {r} (\tau)$$

where
