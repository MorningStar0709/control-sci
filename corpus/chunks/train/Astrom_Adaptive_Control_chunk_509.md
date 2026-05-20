# Systems with Known Parameters

If the parameters of the system of Eq. (7.1) are known, it is easy to determine the optimal feedback. The vector $\tilde{\varphi}^{T}$ defined by Eq. (7.11) is used to show the dependence of $u(t)$ :

$$
\begin{array}{l} y (t + 1) = \varphi^ {T} (t) x (t + 1) + e (t + 1) \\ = b _ {0} (t + 1) u (t) + \tilde {\varphi} ^ {T} (t) x (t + 1) + e (t + 1) \\ \end{array}
$$

The optimal feedback when $b_0(t + 1)$ and $x(t + 1)$ are known is then given by

$$u (t) = \frac {u _ {\mathrm{c}} (t + 1) - \tilde {\varphi} ^ {T} (t) x (t + 1)}{b _ {0} (t + 1)} \tag {7.12}$$

Notice that $\tilde{\varphi}(t)$ is a function of the admissible data. This controller gives

$$y (t + 1) = u _ {c} (t + 1) + e (t + 1)$$

and it minimizes Eq. (7.8), since $e(t + 1)$ is independent of $\mathcal{Y}_t$ and $u(t)$ . The minimal loss is given by

$$\min J _ {N} = R _ {2}$$

Notice that it is necessary to assume that $b_{0}(t+1) \neq 0$ and that the system is minimum-phase at every instant of time. The control signal may otherwise be unbounded.
