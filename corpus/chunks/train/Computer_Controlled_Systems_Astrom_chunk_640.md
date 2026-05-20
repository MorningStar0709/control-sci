# State-Space Models

State models for continuous-time processes can be obtained by a formal generalization of $(10.7)$ to

$$\frac {d x}{d t} = A x + \dot {v}$$

where $\dot{v}$ is a vector whose elements are white-noise stochastic processes. Because $\dot{v}$ has infinite variance, it is customary to write the equation in terms of differentials as

$$d x = A x d t + d v \tag {10.26}$$

where v is the integral of $\dot{v}$ . The signal v is thus assumed to have zero mean, uncorrelated increments, and the variance

$$\operatorname{cov} (v (t), v (t)) = R _ {1} t \tag {10.27}$$

It is also assumed that dv is uncorrelated with x. A precise meaning can be given to (10.26) without any reference to white noise. This form is therefore common in mathematically oriented texts. The form is also useful as a reminder that dv has a magnitude proportional to $\sqrt{dt}$ .

Equation (10.26) is called a stochastic differential equation. To specify it fully, it is also necessary to give the initial probability distribution of x at the starting time. The following continuous-time analog of Theorem 10.2 is then obtained.

THEOREM 10.5 FILTERING OF CONTINUOUS-TIME PROCESSES Consider a stochastic process defined by the linear stochastic differential equation (10.26) where the process v has zero mean and incremental covariance $R_{1}dt$ . Let the initial state have mean $m_{0}$ and covariance $R_{0}$ . The mean-value function of the process x is then given by

$$\frac {d m (t)}{d t} = A m (t) \qquad m (0) = m _ {0} \tag {10.28}$$

and the covariance function is given by

$$\operatorname{cov} \Big (x (s), x (t) \Big) = e ^ {A (s - t)} P (t) \qquad s \geq t \tag {10.29}$$

where $P(t) = \operatorname{cov}(x(t), x(t))$ is given by

$$\frac {d P (t)}{d t} = A P (t) + P (t) A ^ {T} + R _ {1} \quad P (0) = R _ {0} \tag {10.30}$$

Proof. The formula (10.28) for the mean value is obtained simply by taking the mean value of (10.26). Notice that dv has zero mean.

To obtain the differential equation in (10.30), notice that

$$d (x x ^ {T}) = (x + d x) (x + d x) ^ {T} - x x ^ {T} = x d x ^ {T} + d x x ^ {T} + d x d x ^ {T}$$

Equation (10.26) then gives

$$d (x x ^ {T}) = x (A x d t + d v) ^ {T} + (A x d t + d v) x ^ {T} + (A x d t + d v) (A x d t + d v) ^ {T}$$

Taking mean values gives

$$d \left(\mathbf {E} x x ^ {T}\right) = \left(\mathbf {E} x x ^ {T}\right) \mathbf {A} ^ {T} d t + A \left(\mathbf {E} x x ^ {T}\right) d t + \mathbf {E} d v d v ^ {T} + A \left(\mathbf {E} x x ^ {T}\right) \mathbf {A} ^ {T} (d t) ^ {2}$$

because $dv$ is uncorrelated with $x$ . Furthermore, it follows from (10.27) that

$$\mathbf {E} d v d v ^ {T} = R _ {1} d t$$

Hence

$$d P = P A ^ {T} d t + A P d t + R _ {1} d t + A P A ^ {T} (d t) ^ {2}$$

Dividing by dt and taking the limit as dt goes to zero gives the differential equation in (10.30). To obtain Eq. (10.29), let $s \geq t$ and integrate (10.26). Hence

$$x (s) = e ^ {A (s - t)} x (t) + \int_ {t} ^ {s} e ^ {A (s - s ^ {\prime})} d v (s ^ {\prime})$$

Multiplying by $x^T(t)$ from the right and taking mathematical expectation give (10.29). Notice that $dv(s')$ is uncorrelated with $x(t)$ if $s' \geq t$ .
