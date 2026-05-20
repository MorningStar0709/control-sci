# THEOREM 2.5 Continuous-time least-squares estimation

Assume that the matrix $R(t)$ given by Eq. (2.29) is invertible for all t. The estimate that minimizes Eq. (2.27) satisfies

$$\frac {d \hat {\theta}}{d t} = P (t) \varphi (t) e (t) \tag {2.30}e (t) = y (t) - \varphi^ {T} (t) \hat {\theta} (t) \tag {2.31}\frac {d P (t)}{d t} = \alpha P (t) - P (t) \varphi (t) \varphi^ {T} (t) P (t) \tag {2.32}$$

Proof: The theorem is proved by differentiating Eq. (2.28).

Remark 1. The matrix $R(t) = P(t)^{-1}$ satisfies

$$\frac {d R}{d t} = - \alpha R + \varphi \varphi^ {T}$$

Remark 2. There are also continuous-time versions of the simplified algorithms. The projection algorithm corresponding to Eqs. (2.25) and (2.26) is given by Eq. (2.30) with

$$P (t) = \left(\int_ {0} ^ {t} \varphi^ {T} (\tau) \varphi (\tau) d \tau\right) ^ {- 1}$$

where $P(t)$ is now a scalar.
