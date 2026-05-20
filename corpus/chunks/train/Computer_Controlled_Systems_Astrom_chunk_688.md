# Properties of the Closed-Loop System

The closed-loop system with LQG-control is described by

$$
\begin{array}{l} x (k + 1) = \Phi x (k) + \Gamma u (k) + v (k) \\ y (k) = C x (k) + e (k) \\ u (k) = - (L - M C) \hat {x} (k \mid k - 1) - M y (k) \\ \hat {x} (k + 1 \mid k) = \Phi \hat {x} (k \mid k - 1) + \Gamma u (k) + K (y (k) - C \hat {x} (k \mid k - 1)) \\ \end{array}
$$

By introducing $x$ and $\tilde{x} = x - \hat{x}$ , the equations can be written as

$$
\begin{array}{l} \binom {x (k + 1)} {\tilde {x} (k + 1)} = \left( \begin{array}{c c} \Phi - \Gamma L & \Gamma (L - M C) \\ 0 & \Phi - K C \end{array} \right) \binom {x (k)} {\tilde {x} (k)} \\ + \binom{I}{I} v (k) + \binom{- \Gamma M}{- K} e (k) \\ \end{array}
$$

The dynamics of the closed-loop system are determined by $\Phi-\Gamma L$ and $\Phi-KC$ , that is, the dynamics of the corresponding deterministic LQ-control problem and the dynamics of the optimal filter (compare with Sec. 4.5). Notice that the closed-loop systems have the same poles independently even if the current measurement is used or not to determine u.
