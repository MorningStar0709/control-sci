$$P (t + 1) = \tilde {P} (t) + \beta (t) \varphi_ {0} \varphi_ {0} ^ {T}$$

where

$$\tilde {P} (t) = \frac {1}{\lambda^ {t}} \left(P _ {0} - \frac {P _ {0} \varphi_ {0} \varphi_ {0} ^ {T} P _ {0}}{\lambda^ {t} \alpha (t) + \varphi_ {0} ^ {T} P _ {0} \varphi_ {0}}\right) - \beta (t) \varphi_ {0} \varphi_ {0} ^ {T}$$

and

$$\beta (t) = \alpha (t) \frac {\varphi_ {0} ^ {T} P _ {0} \varphi_ {0}}{(\varphi_ {0} ^ {T} \varphi_ {0}) ^ {2} (\lambda^ {t} \alpha (t) + \varphi_ {0} ^ {T} P _ {0} \varphi_ {0})}$$

The matrix $\tilde{P}(t)$ is of rank $n - 1$ with $\tilde{P}(t)\varphi_0 = 0$ . Since $|\lambda| < 1$ we have as $t \to \infty$

$$a (t) \rightarrow 1 - \lambdab (t) \rightarrow \frac {1 - \lambda}{\left(\varphi_ {0} ^ {T} \varphi_ {0}\right) ^ {2}}$$

In the decomposition of $P(t + 1)$ we thus find that the matrix $\tilde{P}$ goes to infinity as $\lambda^{-t}$ and that $\beta(t)\varphi_0\varphi_0^T$ goes to a constant $(1 - \lambda)\varphi_0\varphi_0^T / (\varphi_0^T\varphi)^2$ .

Intuitively, the result of the calculation can be interpreted as follows: When the regression vector is constant, we obtain information only about the component of the parameter that is parallel to the regression vector. This component can be estimated reliably with exponential forgetting. The “projection” of the

P-matrix in this direction converges to $1 - \lambda$ , and the “orthogonal” part of the P-matrix goes to infinity as $\lambda^{-t}$ . Estimator windup is thus obtained by exponential forgetting combined with poor excitation. There are several ways to avoid estimator windup. We now discuss some of these techniques.
