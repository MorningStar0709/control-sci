# Conditional Updating

One possibility to avoid windup in the estimator is to update the estimate and the covariance only when there is excitation. The algorithms obtained are called algorithms with conditional updating or dead zones. A correct detection of excitation should be based on calculation of covariances or spectra as discussed in Section 2.4. Simpler conditions are often used in practice. Common tests are based on the magnitudes of the variations in process inputs and outputs or other signals such as $\varepsilon$ and $\varphi^{T}P\varphi$ . Notice that the quantity $\varphi^{T}P\varphi$ is dimension free.

If the regression vector is constant, it follows from Eq. (11.20) that

$$\varphi_ {0} ^ {T} P (t) \varphi_ {0} = a (t) \frac {\varphi_ {0} ^ {T} P _ {0} \varphi_ {0}}{\lambda^ {t} a (t) + \varphi_ {0} ^ {T} P _ {0} \varphi_ {0}}$$

As $t \to \infty$ , it follows that $a(t) \to 1 - \lambda$ . If $\varphi^T P \varphi$ is used as a test quantity, it is thus natural to normalize it by $1 - \lambda$ . The effect of conditional updating is illustrated by an example.
