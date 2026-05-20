which is the desired minimum-variance control law. The result can be summarized as follows.

THEOREM 12.2 MINIMUM-VARIANCE CONTROL—STABLE INVERSE Consider a process described by (12.5), where $e(k)$ is a sequence of independent random variables with zero mean values and standard deviations $\sigma$ . Let the polynomials $B$ and $C$ have all their zeros inside the unit disc. The minimum-variance control law is then given by (12.27), where the polynomials $F^{*}$ and $G^{*}$ are given by (12.20) with $m = d$ . This control law gives the output

$$y (k) = F ^ {*} \left(q ^ {- 1}\right) e (k) = e (k) + f _ {1} e (k - 1) + \dots + f _ {d - 1} e (k - d + 1)$$

in steady state.

Remark 1. The theorem still holds when $e(i)$ and $e(j)$ are uncorrelated for $i \neq j$ if a linear control law is postulated.

Remark 2. The result is closely related to the solution of the prediction problem (Theorem 12.1). Identity (12.17) or (12.20) was used in both cases. The last two terms in (12.25) can be interpreted as the d-step prediction of the output. The minimum-variance strategy is thus obtained by predicting the output d steps ahead and choosing a control that makes the prediction equal to the desired output. The stochastic-control problem can thus be separated into two problems, one stochastic-prediction problem and one deterministic-control problem. Theorem 12.2 can therefore be interpreted as a separation theorem.

Remark 3. The error under minimum-variance control is a moving average of order d - 1. Thus the covariance function of the regulation error will vanish for arguments larger than d - 1. This fact can be used for diagnosis to determine if a minimum-variance strategy is used.

Remark 4. All process zeros are canceled when the control law of (12.27) is used. The consequences of this are discussed later.

It is very easy to calculate the minimum-variance control law for a given model (12.5), as illustrated by the following example.
