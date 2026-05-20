# DEFINITION 2.1 Persistent excitation

A signal $u$ is called persistently exciting (PE) of order $n$ if the limits (2.44) exist and if the matrix $C_n$ given by Eq. (2.43) is positive definite.

Remark 1. In the adaptive control literature an alternative definition of PE is often used. The signal u is said to be persistently exciting of order n if for all t there exists an integer m such that

$$\rho_ {1} I > \sum_ {k = t} ^ {t + m} \varphi (k) \varphi^ {T} (k) > \rho_ {2} I$$

where $\rho_{1},\rho_{2} > 0$ and the vector $\varphi (t)$ is given by

$$
\varphi (t) = \left( \begin{array}{l l l l} u (t - 1) & u (t - 2) & \dots & u (t - n) \end{array} \right)
$$

Notice that the matrix (2.43) can be written as

$$C _ {n} = \lim _ {t \rightarrow \infty} \frac {1}{t} \sum_ {k = 1} ^ {t} \varphi (k) \varphi^ {T} (k)$$

Remark 2. Notice that no mean value is included in the definition of the empirical covariance $c(k)$ in Eq. (2.44).

The following result can be established.
