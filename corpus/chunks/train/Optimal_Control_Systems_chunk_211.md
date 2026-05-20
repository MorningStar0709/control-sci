\- Step 4: Riccati and Vector Equations: The boundary condition (4.1.14) and the solution of the system (4.1.12) indicate that the state and costate are linearly related as

$$\boldsymbol {\lambda} ^ {*} (t) = \mathbf {P} (t) \mathbf {x} ^ {*} (t) - \mathbf {g} (t) \tag {4.1.15}$$

where, the nxn matrix $\mathbf{P}(t)$ and n vector $\mathbf{g}(t)$ are yet to be determined so as to satisfy the canonical system (4.1.12). This is done by substituting the linear (Riccati) transformation (4.1.15) in the Hamiltonian system (4.1.12) and eliminating the costate function $\boldsymbol{\lambda}^{*}(t)$ . Thus, we first differentiate (4.1.15) to get

$$\dot {\boldsymbol {\lambda}} ^ {*} (t) = \dot {\mathbf {P}} (t) \mathbf {x} ^ {*} (t) + \mathbf {P} (t) \dot {\mathbf {x}} ^ {*} (t) - \dot {\mathbf {g}} (t). \tag {4.1.16}$$

Now, substituting for $\dot{\mathbf{x}}^{*}(t)$ and $\dot{\boldsymbol{\lambda}}^{*}(t)$ from (4.1.12) and eliminating $\boldsymbol{\lambda}^{*}(t)$ with (4.1.15), we get

$$
\begin{array}{l} - \mathbf {V} (t) \mathbf {x} ^ {*} (t) - \mathbf {A} ^ {\prime} (t) [ \mathbf {P} (t) \mathbf {x} ^ {*} (t) - \mathbf {g} (t) ] + \mathbf {W} (t) \mathbf {z} (t) = \dot {\mathbf {P}} (t) \mathbf {x} ^ {*} (t) \\ + \mathbf {P} (t) [ \mathbf {A} (t) \mathbf {x} (t) - \mathbf {E} (t) \left\{\mathbf {P} (t) \mathbf {x} ^ {*} (t) - \mathbf {g} (t) \right\} ] - \dot {\mathbf {g}} (t). \tag {4.1.17} \\ \end{array}
$$

Rearranging the above, we get

$$\left[ \dot {\mathbf {P}} (t) + \mathbf {P} (t) \mathbf {A} (t) + \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) - \mathbf {P} (t) \mathbf {E} (t) \mathbf {P} (t) + \mathbf {V} (t) \right] \mathbf {x} ^ {*} (t) -\left[ \dot {\mathbf {g}} (t) + \mathbf {A} ^ {\prime} (t) \mathbf {g} (t) - \mathbf {P} (t) \mathbf {E} (t) \mathbf {g} (t) + \mathbf {W} (t) \mathbf {z} (t) \right] = 0. \tag {4.1.18}$$

Now, this relation (4.1.18) must satisfy for all $\mathbf{x}^{*}(t)$ , $\mathbf{z}(t)$ and $t$ , which leads us to the $nxn$ matrix $\mathbf{P}(t)$ to satisfy the matrix differential Riccati equation (DRE)

$$\boxed {\dot {\mathbf {P}} (t) = - \mathbf {P} (t) \mathbf {A} (t) - \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) + \mathbf {P} (t) \mathbf {E} (t) \mathbf {P} (t) - \mathbf {V} (t)} \tag {4.1.19}$$

and the $n$ vector $\mathbf{g}(t)$ to satisfy the vector differential equation
