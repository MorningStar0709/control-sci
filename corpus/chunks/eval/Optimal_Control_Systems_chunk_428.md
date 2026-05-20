Now we use the Hamiltonian approach to minimize the PI (7.6.2) subject to the system equation (7.6.1) and the state inequality constraint (7.6.3). Let us define the Hamiltonian as

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), \lambda_ {n + 1} (t), t) \\ = V (\mathbf {x} (t), \mathbf {u} (t), t) + \lambda^ {\prime} (t) \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \\ + \lambda_ {n + 1} (t) \left\{\left[ g _ {1} (\mathbf {x} (t), t ] ^ {2} H \left(g _ {1}\right) + \left[ g _ {2} (\mathbf {x} (t), t) \right] ^ {2} H \left(g _ {2}\right) + \dots \right. \right. \\ \left. + \left[ g _ {p} (\mathbf {x} (t), t) \right] ^ {2} H \left(g _ {m}\right) \right\}, \\ = V (\mathbf {x} (t), \mathbf {u} (t), t) + \lambda^ {\prime} (t) \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \\ + \lambda_ {n + 1} (t) f _ {n + 1} (\mathbf {x} (t), t). \tag {7.6.9} \\ \end{array}
$$

Thus, the previous Hamiltonian is formed with $n+1$ costates and $n+1$ states. Note that the Hamiltonian (7.6.9) does not explicitly contain the new state variable $x_{n+1}(t)$ . Now, we apply the necessary optimality conditions for the state as

$$\dot {\mathbf {x}} ^ {*} (t) = \frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}} = \mathbf {f} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), t),\dot {x} _ {n + 1} ^ {*} (t) = \frac {\partial \mathcal {H}}{\partial \lambda_ {n + 1}} = f _ {n + 1} (\mathbf {x} ^ {*} (t), t), \tag {7.6.10}$$

for the costate as

$$\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial \mathbf {x}},\dot {\lambda} _ {n + 1} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial x _ {n + 1}} = 0 \tag {7.6.11}$$

and for the control as

$$\mathcal {H} \left(\mathbf {x} ^ {*} (t), \mathbf {u} (t), \boldsymbol {\lambda} ^ {*} (t), \lambda_ {n + 1} ^ {*} (t), t\right) \leq \mathcal {H} \left(\mathbf {x} ^ {*} (t), \mathbf {u} (t), \boldsymbol {\lambda} ^ {*} (t), \lambda_ {n + 1} ^ {*} (t), t\right). \tag {7.6.12}$$

or

$$\frac {\min _ {| \mathbf {u} (t) | \leq \mathbf {U}} \left\{\mathcal {H} \left(\mathbf {x} ^ {*} (t) , \mathbf {u} (t) , \boldsymbol {\lambda} ^ {*} (t) , \lambda_ {n + 1} ^ {*} (t) , t\right) \right\} = \mathcal {H} \left(\mathbf {x} ^ {*} (t) , \mathbf {u} (t) , \boldsymbol {\lambda} ^ {*} (t) , \lambda_ {n + 1} ^ {*} (t) , t\right).}{(7 . 6 . 1 3)}$$

Note that in the above, $\lambda_{n+1}^{*}(t) = 0$ because the Hamiltonian (7.6.9) does not contain $x_{n+1}(t)$ explicitly (see Table 7.1).

Let us now illustrate the previous method by an example.
