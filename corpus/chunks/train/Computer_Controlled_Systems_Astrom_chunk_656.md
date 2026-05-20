# Sampling the Loss Function

The loss function in (11.4) is expressed in continuous time. It is first transformed into a discrete-time loss function. Integrating (11.4) over intervals of lengths h gives

$$J = \operatorname{E} \left(\sum_ {k = 0} ^ {N - 1} J (k) + x ^ {T} (N h) Q _ {0 c} x (N h)\right)$$

where

$$J (k) = \int_ {k h} ^ {k h + h} \left(x ^ {T} (t) Q _ {1 c} x (t) + 2 x ^ {T} (t) Q _ {1 2 c} u (t) + u ^ {T} (t) Q _ {2 c} u (t)\right) d t \tag {11.5}$$

Using (11.2) in (11.5) and the fact that $u(t)$ is constant over the sampling period gives

$$J (k) = x ^ {T} (k h) Q _ {1} x (k h) + 2 x ^ {T} (k h) Q _ {1 2} u (k h) + u ^ {T} (k h) Q _ {2} u (k h)$$

where

$$Q _ {1} = \int_ {k h} ^ {k h + h} \Phi^ {T} (s, k h) Q _ {1 c} \Phi (s, k h) d s \tag {11.6}Q _ {1 2} = \int_ {k h} ^ {k h + h} \Phi^ {T} (s, k h) \left(Q _ {1 c} \Gamma (s, k h) + Q _ {1 2 c}\right) d s \tag {11.7}Q _ {2} = \int_ {k h} ^ {k h + h} \left(\Gamma^ {T} (s, k h) Q _ {1 c} \Gamma (s, k h) + 2 \Gamma^ {T} (s, k h) Q _ {1 2 c} + Q _ {2 c}\right) d s \tag {11.8}$$

Minimizing the loss function of (11.4) when $u(t)$ is constant over the sampling period is thus the same as minimizing the discrete-time loss function

$$
\begin{array}{l} J = \mathrm{E} \left(\sum_ {k = 0} ^ {N - 1} \left(x ^ {T} (k h) Q _ {1} x (k h) + 2 x ^ {T} (k h) Q _ {1 2} u (k h) \right. \right. \\ \left. + u ^ {T} (k h) Q _ {2} u (k h)\right) + x ^ {T} (N h) Q _ {0} x (N h) \Bigg) \tag {11.9} \\ = \mathrm{E} \left(\sum_ {k = 0} ^ {N - 1} \left( \begin{array}{l l} x ^ {T} (k h) & u ^ {T} (k h) \end{array} \right) Q \binom{x (k h)}{u (k h)} + x ^ {T} (N h) Q _ {0 c} x (N h)\right) \\ \end{array}
$$

where

$$
Q = \left( \begin{array}{c c} Q _ {1} & Q _ {1 2} \\ Q _ {1 2} ^ {T} & Q _ {2} \end{array} \right) \tag {11.10}
$$

The matrices $Q_{1}, Q_{12}$ , and $Q_{2}$ are given by (11.6) to (11.8), respectively, and $Q_{0} = Q_{0c}$ . In the following it is assumed that $Q_{1}$ and $Q_{0}$ are positive semidefinite and that $Q_{2}$ is positive definite. The condition on $Q_{2}$ will be relaxed in what follows. Notice that the sampled loss function (11.9) will have a cross-coupling term $Q_{12}$ even if $Q_{12c} = 0$ .

When the stochastic case is considered, one additional term depending on the noise is obtained in (11.9). However, this term is independent of the control signal and can thus be disregarded when performing the minimization.

The optimal-control problem has now been transformed into the discrete-time problem of minimizing the loss function (11.9) when the process is described by (11.3). To facilitate the writing in the sequel, it is assumed that the sampling period is used as time unit, that is, h = 1.
