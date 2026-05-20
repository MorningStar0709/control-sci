$$
\begin{array}{l} 1 + \left[ \mathbf {A} \mathbf {x} ^ {*} (t) \right] ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) + \mathbf {u} ^ {* \prime} (t) \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \\ \leq 1 + \left[ \mathbf {A} \mathbf {x} ^ {*} (t) \right] ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \tag {7.1.21} \\ \end{array}
$$

which can be simplified to

$$
\begin{array}{l} \mathbf {u} ^ {* \prime} (t) \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \leq \mathbf {u} ^ {\prime} (t) \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t), \\ \mathbf {u} ^ {* \prime} (t) \mathbf {q} ^ {*} (t) \leq \mathbf {u} ^ {\prime} (t) \mathbf {q} ^ {*} (t), \\ = \min _ {| \mathbf {u} (t) | \leq 1} \left\{\mathbf {u} ^ {\prime} (t) \mathbf {q} ^ {*} (t) \right\} \tag {7.1.22} \\ \end{array}
$$

where $\mathbf{q}^{*}(t) = \mathbf{B}'\boldsymbol{\lambda}^{*}(t)$ , and $\mathbf{q}^{*}(t)$ is not to be confused as the vector version of the weighting matrix Q used in quadratic performance measures.

\- Step 5: Optimal Control: We now derive the optimal sequence for $\mathbf{u}^{*}(t)$ . From the optimal condition (7.1.21)

1. if $\mathbf{q}^{*}(t)$ is positive, the optimal control $\mathbf{u}^{*}(t)$ must be the smallest admissible control value -1 so that

$$\min _ {| \mathbf {u} (t) | \leq 1} \left\{\mathbf {u} ^ {\prime} (t) \mathbf {q} ^ {*} (t) \right\} = - \mathbf {q} ^ {*} (t) = - \left| \mathbf {q} ^ {*} (t) \right|, \tag {7.1.23}$$

2. and on the other hand, if $\mathbf{q}^{*}(t)$ is negative, the optimal control $\mathbf{u}^{*}(t)$ must be the largest admissible value +1 so that

$$\min _ {| \mathbf {u} (t) | \leq 1} \left\{\mathbf {u} ^ {\prime} (t) \mathbf {q} ^ {*} (t) \right\} = + \mathbf {q} ^ {*} (t) = - | \mathbf {q} ^ {*} (t) |. \tag {7.1.24}$$

In other words, the previous two relations can be written in a compact form (for either $\mathbf{q}^{*}(t)$ is positive or negative) as

$$\min _ {| \mathbf {u} (t) | \leq 1} \left\{\mathbf {u} ^ {\prime} (t) \mathbf {q} ^ {*} (t) \right\} = - \left| \mathbf {q} ^ {*} (t) \right|. \tag {7.1.25}$$

Also, the combination of (7.1.23) and (7.1.24) means that

$$
\mathbf {u} ^ {*} (t) = \left\{ \begin{array}{l l} + 1 & \text { if   } \mathbf {q} ^ {*} (t) <   0, \\ - 1 & \text { if   } \mathbf {q} ^ {*} (t) > 0, \\ \text { indeterminate } & \text { if   } \mathbf {q} ^ {*} (t) = 0. \end{array} \right. \tag {7.1.26}
$$
