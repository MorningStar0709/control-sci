# 4.4 Observers

It is unrealistic to assume that all states of a system can be measured, particularly if disturbances are part of the state as in Eq. (4.20). It is therefore of interest to determine the states of a system from available measurements and a model. It is assumed that the system is described by the sampled model

$$
\begin{array}{r l} x (k + 1) & = \Phi x (k) + \Gamma u (k) \\ u (k) & = C x (k) \end{array} \tag {4.23}
y (k) = C x (k)
$$

The problem is thus to calculate or reconstruct the state $x(k)$ from input and output sequences $y(k)$ , $y(k-1)$ , $\ldots$ , $u(k)$ , $u(k-l)$ , $\ldots$ is considered next. In Sec. 3.4 it was shown that this is possible if the system is observable.
