$$
\begin{array}{l} V _ {N - 2} = \min _ {u (N - 2), u (N - 1)} \left(\sum_ {i = N - 2} ^ {N - 1} \left(x ^ {T} (i) Q _ {1} x (i) + u ^ {T} (i) Q _ {2} u (i) \right. \right. \\ \left. + 2 x ^ {T} (i) Q _ {1 2} u (i)\right) + x ^ {T} (N) Q _ {0} x (N) \Bigg) \\ = \min _ {u (N - 2)} \left(x ^ {T} (N - 2) Q _ {1} x (N - 2) + u ^ {T} (N - 2) Q _ {2} u (N - 2) \right. \\ \left. + 2 x ^ {T} (N - 2) Q _ {1 2} u (N - 2) + V _ {N - 1}\right) \\ \end{array}
$$

This is the same as (11.20), but with the time arguments shifted one step. The procedure can now be repeated, and $V_{0} = x^{T}(0)S(0)x(0)$ , which is the minimum of J, is obtained by iterating backward in time. This proves (11.17) to (11.19).

It also follows that (11.17) can be written as

$$
S (k) = \left(\Phi - \Gamma L (k)\right) ^ {T} S (k + 1) \left(\Phi - \Gamma L (k)\right) + \left( \begin{array}{c c} I & - L (k) ^ {T} \end{array} \right) Q \binom {I} {- L (k)} \tag {11.21}
$$

This implies that $S(k)$ is positive semidefinite if $S(N) = Q_0$ is positive semidefinite.

Remark 1. Notice that it is not assumed that $Q_{2}$ be positive definite, only that $Q_{2} + \Gamma^{T}S(k)\Gamma$ is positive definite.

Remark 2. The calculations needed to determine the LQ-controller can be made by hand only for very simple examples. In practice it is necessary to have access to interactive programs, which can compute the control law and simulate the systems.
