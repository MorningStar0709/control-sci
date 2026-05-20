# Cautious Control

We now consider the special case in which N = 1 in Eq. (7.8). According to Theorem 7.1 the conditional distribution of $y(t + 1)$ , given $Y_{t}$ , is Gaussian with mean $\varphi^T (t)\hat{x} (t + 1)$ and covariance $R_{2} + \varphi^{T}(t)P(t + 1)\varphi (t)$ . Then

$$
\begin{array}{l} E \left\{\left(y (t + 1) - u _ {c} (t + 1)\right) ^ {2} \mid \mathcal {Y} _ {t} \right\} \\ = \left(\varphi^ {T} (t) \hat {x} (t + 1) - u _ {c} (t + 1)\right) ^ {2} + \varphi^ {T} (t) P (t + 1) \varphi (t) + R _ {2} \\ = \left(\tilde {\varphi} ^ {T} (t) \hat {x} (t + 1) + \hat {b} _ {0} (t + 1) u (t) - u _ {c} (t + 1)\right) ^ {2} \\ + \tilde {\varphi} ^ {T} (t) P (t + 1) \tilde {\varphi} (t) + u ^ {2} (t) p _ {b _ {0}} (t + 1) \\ + 2 u (t) \tilde {\varphi} ^ {T} (t) P (t + 1) \ell + R _ {2} \tag {7.14} \\ \end{array}
$$

The first equality is obtained by using the standard formula that

$$E (\zeta^ {2}) = m ^ {2} + p$$

when $\zeta$ is a Gaussian variable with mean m and variance p. The column vector $\ell$ selects the first column of the matrix $P(t)$ , that is,

$$
\ell^ {T} = \left( \begin{array}{c c c c} 1 & 0 & \dots & 0 \end{array} \right)
$$

Further, $p_{b_{0}}$ is the covariance of the parameter estimate $\hat{b}_{0}$ . Equation (7.14) is quadratic in $u(t)$ . Minimization of Eq. (7.14) with respect to $u(t)$ gives the admissible one-step optimal controller

$$u (t) = \frac {\hat {b} _ {0} (t + 1) u _ {c} (t + 1) - \tilde {\varphi} ^ {T} (t) \left(\hat {b} _ {0} (t + 1) \hat {x} (t + 1) + P (t + 1) \ell\right)}{\hat {b} _ {0} ^ {2} (t + 1) + p _ {b _ {0}} (t + 1)} \tag {7.15}$$

The minimum value of the loss function is

$$
\begin{array}{l} \min _ {u (t)} E \left\{\left(y (t + 1) - u _ {c} (t + 1)\right) ^ {2} \mid \mathcal {Y} _ {t} \right\} \\ = \left(\tilde {\varphi} ^ {T} (t) \hat {x} (t + 1) - u _ {c} (t + 1)\right) ^ {2} + R _ {2} + \tilde {\varphi} ^ {T} (t) P (t + 1) \tilde {\varphi} (t) \tag {7.16} \\ - \frac {\left(\hat {b} _ {0} (t + 1) u _ {c} (t + 1) - \tilde {\varphi} ^ {T} (t) \left(\hat {b} _ {0} (t + 1) \hat {x} (t + 1) + P (t + 1) \ell\right)\right) ^ {2}}{\hat {b} _ {0} ^ {2} (t + 1) + p _ {b _ {0}} (t + 1)} \\ \end{array}
$$

The one-step-ahead controller, or cautious controller, of Eq. (7.15) differs from Eq. (7.13) because the uncertainties of the parameter estimates are also taken into account. The controller becomes cautious when the estimates are uncertain. Notice that the cautious controller of Eq. (7.15) reduces to the certainty equivalence controller of Eq. (7.13) when $P(t + 1) = 0$ .
