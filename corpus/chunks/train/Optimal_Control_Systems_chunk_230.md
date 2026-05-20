3. General Boundary Conditions: $\mathbf{x}(t_{0}) \neq 0$ and $\mathbf{x}(t_{f}) \neq 0$ . Here, both the given boundary conditions are not zero, and we assume a transformation as

$$\mathbf {x} ^ {*} (t) = \mathbf {M} (t) \boldsymbol {\lambda} ^ {*} (t) + \mathbf {v} (t). \tag {4.3.21}$$

As before, we substitute the transformation (4.3.21) in the state and costate system (4.3.11) and eliminate $\mathbf{x}^{*}(t)$ to get

$$\dot {\mathbf {x}} ^ {*} (t) = \dot {\mathbf {M}} (t) \boldsymbol {\lambda} ^ {*} (t) + \mathbf {M} (t) \dot {\boldsymbol {\lambda}} ^ {*} (t) + \dot {\mathbf {v}} (t) \tag {4.3.22}$$

leading to

$$
\begin{array}{l} \mathbf {A} (t) \left[ \mathbf {M} (t) \boldsymbol {\lambda} ^ {*} (t) + \mathbf {v} (t) \right] - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) \\ = \mathbf {M} (t) \boldsymbol {\lambda} ^ {*} (t) + \mathbf {M} (t) [ - \mathbf {Q} (t) [ \mathbf {M} (t) \boldsymbol {\lambda} ^ {*} (t) + \mathbf {v} (t) ] \\ \left. - \mathbf {A} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) \right] + \dot {\mathbf {v}} (t) \tag {4.3.23} \\ \end{array}
$$

further leading to

$$
\begin{array}{l} \left[ \dot {\mathbf {M}} (t) - \mathbf {A} (t) \mathbf {M} (t) - \mathbf {M} (t) \mathbf {A} ^ {\prime} (t) - \mathbf {M} (t) \mathbf {Q} (t) \mathbf {M} (t) + \right. \\ \left. \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \right] \boldsymbol {\lambda} ^ {*} (t) + \\ [ \dot {\mathbf {v}} (t) - \mathbf {M} (t) \mathbf {Q} (t) \mathbf {v} (t) - \mathbf {A} (t) \mathbf {v} (t) ] = 0. \tag {4.3.24} \\ \end{array}
$$

This should be valid for any orbit ray value of $\boldsymbol{\lambda}^{*}(t)$ , which leads us to a set of equations

$$
\begin{array}{l} \mathbf {M} (t) = \mathbf {A} (t) \mathbf {M} (t) + \mathbf {M} (t) \mathbf {A} ^ {\prime} (t) + \mathbf {M} (t) \mathbf {Q} (t) \mathbf {M} (t) \\ - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) (4.3.25) \\ \dot {\mathbf {v}} (t) = \mathbf {M} (t) \mathbf {Q} (t) \mathbf {v} (t) + \mathbf {A} (t) \mathbf {v} (t). (4.3.26) \\ \end{array}
$$

At $t = t_0$ , (4.3.21) becomes

$$\mathbf {x} ^ {*} (t _ {0}) = \mathbf {M} (t _ {0}) \boldsymbol {\lambda} ^ {*} (t _ {0}) + \mathbf {v} (t _ {0}). \tag {4.3.27}$$

Since $\lambda^{*}(t_{0})$ is arbitrary, (4.3.27) gives us

$$\mathbf {M} (t _ {0}) = 0; \quad \mathbf {v} (t _ {0}) = \mathbf {x} (t _ {0}). \tag {4.3.28}$$

At $t = t_f$ , (4.3.21) becomes
