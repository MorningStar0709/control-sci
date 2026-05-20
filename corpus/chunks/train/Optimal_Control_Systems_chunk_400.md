<table><tr><td>Possible values of  $\lambda_{2}^{*}(t)$ </td><td>Resulting values of  $u^{*}(t)$ </td><td>Minimum value of  $\{|u(t)| + u(t)\lambda_{2}^{*}(t)\}$ </td></tr><tr><td> $\lambda_{2}^{*}(t) >+1$ </td><td> $u^{*}(t) = -1$ </td><td> $1 - \lambda_{2}^{*}(t)$ </td></tr><tr><td> $\lambda_{2}^{*}(t) < -1$ </td><td> $u^{*}(t) = +1$ </td><td> $1 + \lambda_{2}^{*}(t)$ </td></tr><tr><td> $\lambda_{2}^{*}(t) = +1$ </td><td> $-1 \leq u^{*}(t) \leq 0$ </td><td>0</td></tr><tr><td> $\lambda_{2}^{*}(t) = -1$ </td><td> $0 \leq u^{*}(t) \leq +1$ </td><td>0</td></tr><tr><td> $-1 < \lambda_{2}^{*}(t) < 1$ </td><td> $u^{*}(t) = 0$ </td><td>0</td></tr><tr><td>Possible values of  $\lambda_{2}^{*}(t)$ </td><td>Resulting values of  $u^{*}(t)$ </td><td>Maximum value of  $\{|u(t)| + u(t)\lambda_{2}^{*}(t)\}$ </td></tr><tr><td> $\lambda_{2}^{*}(t) = 0$ </td><td> $u^{*}(t) = +1 \text{ or } -1$ </td><td> $+1$ </td></tr><tr><td> $\lambda_{2}^{*}(t) >0$ </td><td> $u^{*}(t) = +1$ </td><td> $1 + \lambda_{2}^{*}(t)$ </td></tr><tr><td> $\lambda_{2}^{*}(t) < 0$ </td><td> $u^{*}(t) = -1$ </td><td> $1 - \lambda_{2}^{*}(t)$ </td></tr></table>

These relations are also exhibited in Figure 7.17

The previous tabular relations are also written as

$$
\begin{array}{l} u ^ {*} (t) = \left\{ \begin{array}{c c} 0 \text {   if   } - 1 <   \lambda_ {2} ^ {*} (t) <   + 1 \\ + 1 \text {   if   } & \lambda_ {2} ^ {*} (t) <   - 1 \\ - 1 \text {   if   } & \lambda_ {2} ^ {*} (t) > + 1 \end{array} \right. \tag {7.3.11} \\ 0 \leq u ^ {*} (t) \leq + 1 \quad \text { if } \quad \lambda_ {2} ^ {*} (t) = - 1 \\ - 1 \leq u ^ {*} (t) \leq 0 \quad \text { if } \quad \lambda_ {2} ^ {*} (t) = + 1. \\ \end{array}
$$

The previous relation is further rewritten as

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 0 & \text { if } | \lambda_ {2} ^ {*} (t) | <   1 \\ - s g n \{\lambda_ {2} ^ {*} (t) \} & \text { if } | \lambda_ {2} ^ {*} (t) | > 1 \\ \text { undetermined } & \text { if } | \lambda_ {2} ^ {*} (t) | = 1 \end{array} \right. \tag {7.3.12}
$$

where, sgn is already defined in the previous section on time-optimal control systems. In order to write the relation $(7.3.12)$ in a more compact form, let us define a dead-zone function between input function $f_{i}$ and output function $f_{o}$ , denoted by $dez\{\}$ , as $f_{o} = dez\{f_{i}\}$ means that

![](image/bd46b8aeb10e25cbf2efc9e92a3ab3d1a72bb9f17e7c9266673a27ec06693680.jpg)

<details>
<summary>text_image</summary>
