# Example 13.2 Least-squares estimate of first-order systems

Determine the least-squares estimate of the parameters $a$ and $b$ in the model

$$y (k) = - a y (k - 1) + b u (k - 1)$$

in such a way that the criterion

$$J (a, b) = \frac {1}{2} \sum_ {i = 2} ^ {N} \varepsilon (k) ^ {2}$$

is minimal, where

$$
\begin{array}{l} \varepsilon (k) = y (k) - \hat {y} (k) = y (k) + a y (k - 1) - b u (k - 1) \\ = y (k) - \varphi^ {T} (k) \theta \\ \end{array}
$$

A comparison with the general case gives

$$
y = \left( \begin{array}{c} y (2) \\ y (3) \\ \vdots \\ y (N) \end{array} \right) \qquad \Phi = \left( \begin{array}{c c} - y (1) & u (1) \\ - y (2) & u (2) \\ \vdots & \vdots \\ - y (N - 1) & u (N - 1) \end{array} \right) \qquad \varepsilon = \left( \begin{array}{c} \varepsilon (2) \\ \varepsilon (3) \\ \vdots \\ \varepsilon (N) \end{array} \right)
$$

and

$$
\theta = \left( \begin{array}{c c} a & b \end{array} \right) ^ {T}
$$

Hence

$$
\Phi^ {T} \Phi = \left( \begin{array}{c c} \sum_ {k = 1} ^ {N - 1} y (k) ^ {2} & - \sum_ {k = 1} ^ {N - 1} y (k) u (k) \\ - \sum_ {k = 1} ^ {N - 1} y (k) u (k) & \sum_ {k = 1} ^ {N - 1} u (k) ^ {2} \end{array} \right)

\Phi^ {T} y = \left( \begin{array}{c} - \sum_ {k = 1} ^ {N - 1} y (k + 1) y (k) \\ \sum_ {k = 1} ^ {N - 1} y (k + 1) u (k) \end{array} \right)
$$

Provided the matrix $\Phi^{T}\Phi$ is nonsingular, the least-squares estimate of the parameters a and b is now easily obtained. The matrix $\Phi^{T}\Phi$ will be nonsingular if conditions (sufficient richness or persistent excitation) are imposed on the input signal.
