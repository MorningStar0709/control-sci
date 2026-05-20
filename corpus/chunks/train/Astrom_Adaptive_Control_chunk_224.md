# THEOREM 4.1 Asymptotic properties 1

Let Algorithm 4.1 with $Q^{*}/P^{*}=1$ be used with a least-squares estimator. The parameter $r_{0}=b_{0}$ can be either fixed or estimated. Assume that the regression vectors are bounded, and assume that the parameter estimates converge. The closed-loop system obtained in the limit is then characterized by

$$\overline {{y (t + \tau) y (t)}} = 0 \quad \tau = d, d + 1, \dots , d + l \tag {4.25}\overline {{y (t + \tau) u (t)}} = 0 \quad \tau = d, d + 1, \dots , d + k$$

where the overbar indicates a time average. Also, k and l are the degrees of the polynomials $R^{*}$ and $S^{*}$ , respectively.

Proof: The model of Eq. (4.23) can be written as

$$y (t + d) = \varphi^ {T} (t) \theta + \varepsilon (t + d)$$

and the control law becomes

$$\varphi^ {T} (t) \hat {\theta} (t + d) = 0 \tag {4.26}$$

At an equilibrium the estimated parameters $\hat{\theta}$ are constant. Furthermore, they satisfy the normal equations (2.5), which in this case are written as

$$\frac {1}{t} \sum_ {k = 1} ^ {t} \varphi (k) y (k + d) = \frac {1}{t} \sum_ {k = 1} ^ {t} \varphi (k) \varphi^ {T} (k) \hat {\theta} (t + d)$$

By using the control law it follows from Eq. (4.26) that

$$\lim _ {t \rightarrow \infty} \frac {1}{t} \sum_ {k = 1} ^ {t} \varphi (k) y (k + d) = \lim _ {t \rightarrow \infty} \frac {1}{t} \sum_ {k = 1} ^ {t} \varphi (k) \varphi^ {T} (k) (\hat {\theta} (t + d) - \hat {\theta} (k + d))$$

If the estimate $\hat{\theta}(t)$ converges as $t \to \infty$ and the regression vector $\varphi(k)$ is bounded, the right-hand side goes to zero. Equation (4.25) now follows from $Q^{*}/P^{*} = 1$ and the definition of the regression vector in Algorithm 4.1.

Stronger statements can be made if more is assumed about the system to be controlled.
