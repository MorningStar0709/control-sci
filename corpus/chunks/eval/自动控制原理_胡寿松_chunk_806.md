$$J _ {a} = \varphi [ \boldsymbol {x} (N) ] + \boldsymbol {\gamma} ^ {\mathrm{T}} \boldsymbol {\psi} [ \boldsymbol {x} (N) ] + \sum_ {k = 0} ^ {N - 1} [ H (k) - \boldsymbol {\lambda} ^ {\mathrm{T}} (k + 1) \boldsymbol {x} (k + 1) ]$$

因为“离散分部积分”

$$
\begin{array}{l} \sum_ {k = 0} ^ {N - 1} \boldsymbol {\lambda} ^ {T} (k + 1) \boldsymbol {x} (k + 1) = \sum_ {m = 1} ^ {N} \boldsymbol {\lambda} ^ {T} (m) \boldsymbol {x} (m) \\ = \sum_ {m = 0} ^ {N - 1} \boldsymbol {\lambda} ^ {T} (m) \boldsymbol {x} (m) - \boldsymbol {\lambda} ^ {T} (0) \boldsymbol {x} (0) + \boldsymbol {\lambda} ^ {T} (N) \boldsymbol {x} (N) \\ = \sum_ {k = 0} ^ {N - 1} \boldsymbol {\lambda} ^ {T} (k) \boldsymbol {x} (k) - \boldsymbol {\lambda} ^ {T} (0) \boldsymbol {x} (0) + \boldsymbol {\lambda} ^ {T} (N) \boldsymbol {x} (N) \\ \end{array}
$$

所以，离散广义泛函可写为

$$
\begin{array}{l} J _ {a} = \varphi [ x (N) ] + \lambda^ {T} \psi [ x (N) ] + \sum_ {k = 0} ^ {N - 1} [ H (k) - \lambda^ {T} (k) x (k) ] \\ + \boldsymbol {\lambda} ^ {T} (0) \boldsymbol {x} (0) - \boldsymbol {\lambda} ^ {T} (N) \boldsymbol {x} (N) \\ \end{array}
$$

对上式取一次变分,考虑到 $\delta x(0)=0$ ,可得

$$
\begin{array}{l} \delta J _ {a} = \left[ \frac {\partial \varphi}{\partial x (N)} + \frac {\partial \boldsymbol {\psi} ^ {T}}{\partial x (N)} \boldsymbol {\gamma} - \boldsymbol {\lambda} (N) \right] ^ {T} \delta x (N) \\ + \sum_ {k = 0} ^ {N - 1} \left\{\left[ \frac {\partial H (k)}{\partial x (k)} - \lambda (k) \right] ^ {T} \delta x (k) + \left[ \frac {\partial H (k)}{\partial u (k)} \right] ^ {T} \delta u (k) \right\} \\ \end{array}
$$

令 $\delta J_{a} = 0$ ，考虑到变分 $\delta x(k)$ 和 $\delta x(N)$ 是任意的，可得

$$\boldsymbol {\lambda} (k) = \frac {\partial H (k)}{\partial \boldsymbol {x} (k)}, \quad \boldsymbol {\lambda} (N) = \frac {\partial \varphi}{\partial \boldsymbol {x} (N)} + \frac {\partial \boldsymbol {\psi} ^ {T}}{\partial \boldsymbol {x} (N)} \boldsymbol {\gamma}$$

对于

$$\sum_ {k = 0} ^ {N - 1} \left[ \frac {\partial H (k)}{\partial \boldsymbol {u} (k)} \right] ^ {T} \delta \boldsymbol {u} (k) = 0$$

当 $u(k)$ 不受约束时， $\delta u(k)$ 是任意的，故必有

$$\frac {\partial H (k)}{\partial \boldsymbol {u} (k)} = \boldsymbol {0}$$

当 $u(k)\in \Omega$ 时，不加证明得

$$H ^ {*} (k) = \min _ {u (k) \in \Omega} H (k)$$
