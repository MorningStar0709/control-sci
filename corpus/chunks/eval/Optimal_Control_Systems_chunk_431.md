$$g _ {1} (\mathbf {x} (t)) = \left[ x _ {2} (t) + 3 \right] \geq 0,g _ {2} (\mathbf {x} (t)) = [ 3 - x _ {2} (t) ] \geq 0. \tag {7.6.20}$$

\- Step 1: First formulate the Hamiltonian as

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} (t), u (t), \boldsymbol {\lambda} (t), \lambda_ {3} (t)) \\ = \frac {1}{2} x _ {1} ^ {2} (t) + \frac {1}{2} u ^ {2} (t) + \lambda_ {1} (t) x _ {2} (t) - \lambda_ {2} (t) u (t) \\ + \lambda_ {3} (t) \left\{\left[ x _ {2} (t) + 3 \right] ^ {2} H \left(x _ {2} (t) + 3\right) \right. \\ \left. + \left[ 3 - x _ {2} (t) \right] ^ {2} H \left(3 - x _ {2} (t)\right) \right\}. \tag {7.6.21} \\ \end{array}
$$

\- Step 2: The necessary condition for the state (7.6.10) becomes

$$\dot {x} _ {1} ^ {*} (t) = x _ {2} ^ {*} (t),\dot {x} _ {2} ^ {*} (t) = u ^ {*} (t),\dot {x} _ {3} ^ {*} (t) = \left[ x _ {2} (t) + 3 \right] ^ {2} H \left(x _ {2} (t) + 3\right) + \left[ 3 - x _ {2} (t) \right] ^ {2} H \left(3 - x _ {2} (t)\right), \tag {7.6.22}$$

and for the costate (7.6.11)

$$\dot {\lambda} _ {1} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial x _ {1}} = - x _ {1} ^ {*} (t),\dot {\lambda} _ {2} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial x _ {2}} = - \lambda_ {1} ^ {*} (t) - 2 \lambda_ {3} ^ {*} (t) \left[ x _ {2} ^ {*} (t) + 3 \right] H \left(x _ {2} ^ {*} (t) + 3\right)+ 2 \lambda_ {3} ^ {*} (t) [ 3 - x _ {2} ^ {*} (t) ] H (3 - x _ {2} ^ {*} (t))\dot {\lambda} _ {3} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial x _ {3}} = 0 \longrightarrow \lambda_ {3} ^ {*} (t) = \text { constant }. \tag {7.6.23}$$

\- Step 3: Minimize $\mathcal{H}$ w.r.t. the control (7.6.13)

$$\mathcal {H} \left(\mathbf {x} ^ {*} (t), u ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \lambda_ {3} ^ {*} (t)\right) \leq \mathcal {H} \left(\mathbf {x} ^ {*} (t), u (t), \boldsymbol {\lambda} ^ {*} (t), \lambda_ {3} ^ {*} (t)\right). \tag {7.6.24}$$

Using (7.6.21) in the condition (7.6.24) and taking out the terms not containing the control $u(t)$ explicitly, we get

$$
\begin{array}{l} \frac {1}{2} u ^ {* ^ {2}} (t) + \lambda_ {2} ^ {*} (t) u ^ {*} (t) \leq \frac {1}{2} u ^ {2} (t) + \lambda_ {2} ^ {*} (t) u (t) \\ = \min _ {| u | \leq 1} \left\{\frac {1}{2} u ^ {2} (t) + \lambda_ {2} ^ {*} (t) u (t) \right\}. \tag {7.6.25} \\ \end{array}
$$
