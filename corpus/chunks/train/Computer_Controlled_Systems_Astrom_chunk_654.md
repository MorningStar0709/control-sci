# Problem Formulation

The design problem is specified by giving the process, the criterion, and the admissible control laws.

The process. It is assumed that the process to be controlled is described by the continuous-time model

$$d x = A x d t + B u d t + d v _ {c} \tag {11.1}$$

where A and B may be time-varying matrices. The process $v_{c}$ has mean value of zero and uncorrelated increments. The incremental covariance of $v_{c}$ is $R_{1c} dt$ (compare with Sec. 10.5). The model in (11.1) can be sampled as in Sec. 10.6. Some modifications must be made because the system is allowed to be time-varying. The input $u(t)$ is constant over the sampling period; for the noise-free case the solution of (11.1) can be written as

$$x (t) = \Phi (t, k h) x (k h) + \Gamma (t, k h) u (k h) \tag {11.2}$$

where $\Phi(t, kh)$ is the fundamental matrix of (11.2) satisfying

$$\frac {d}{d t} \Phi (t, k h) = A (t) \Phi (t, k h) \quad \Phi (k h, k h) = I$$

and

$$\Gamma (t, k h) = \int_ {k h} ^ {t} \Phi (t, s) B (s) d s$$

Omitting the time arguments of the matrices, the sampled model can be written as

$$x (k h + h) = \Phi x (k h) + \Gamma u (k h) + v (k h) \tag {11.3}y (k h) = C x (k h) + e (k h)$$

where v and e are discrete-time Gaussian white-noise processes with zero-mean value and

$$\mathbf {E} v (k h) v ^ {T} (k h) = R _ {1} = \int_ {0} ^ {h} e ^ {A \tau} R _ {1 c} e ^ {A ^ {\tau} \tau} d \tau\operatorname{E} v (k h) e ^ {T} (k h) = R _ {1 2}\mathbf {E} e (k h) e ^ {T} (k h) = R _ {2}$$

The expression for the covariance matrix $R_{1}$ was given in Sec. 10.6. Further, it is assumed that the initial state $x(0)$ is Gaussian distributed with

$$\operatorname{Ex} (0) = m _ {0} \quad \text { and } \quad \operatorname{cov} (x (0)) = R _ {0}$$

The matrices $R_{0}, R_{1}$ , and $R_{2}$ are positive semidefinite. The covariance matrices may be time-varying. It is assumed that the model (11.3) is reachable and observable.

As discussed in Chapter 4, it is possible to include other types of disturbances and effects from the environment by augmenting the state vector of the process.

The criterion. The design criteria we will use is a way of weighting the magnitude of the states and control signals. One way can be to look at the power of the state, that is,

$$J = \int_ {0} ^ {N h} | x (t) | ^ {2} d t = \int_ {0} ^ {N h} x (t) ^ {T} x (t) d t$$

The components of the state may have different dimensions and we can instead use a more general weighting

$$J = \int_ {0} ^ {N h} x (t) ^ {T} Q _ {1 c} x (t) d t$$
