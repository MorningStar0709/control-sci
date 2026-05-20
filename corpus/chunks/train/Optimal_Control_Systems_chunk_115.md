\- Step 7: Hamiltonian: We define the Hamiltonian $\mathcal{H}^*$ (also called the Pontryagin $\mathcal{H}$ function) at the optimal condition as

$$\boxed {\mathcal {H} ^ {*} = V (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), t) + \boldsymbol {\lambda} ^ {* ^ {\prime}} (t) \mathbf {f} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), t),} \tag {2.7.27}$$

where,

$$\mathcal {H} ^ {*} = \mathcal {H} ^ {*} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t).$$

Then from (2.7.12) the Lagrangian $\mathcal{L}^*$ in terms of the Hamiltonian $\mathcal{H}^*$ becomes

$$
\begin{array}{l} \mathcal {L} ^ {*} = \mathcal {L} ^ {*} (\mathbf {x} ^ {*} (t), \dot {\mathbf {x}} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t) \\ = \mathcal {H} ^ {*} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t) \\ + \left(\frac {\partial S}{\partial \mathbf {x}}\right) _ {*} ^ {\prime} \dot {\mathbf {x}} ^ {*} (t) + \left(\frac {\partial S}{\partial t}\right) _ {*} - \boldsymbol {\lambda} ^ {* ^ {\prime}} (t) \dot {\mathbf {x}} ^ {*} (t). \tag {2.7.28} \\ \end{array}
$$

Using (2.7.28) in (2.7.20), (2.7.19), and (2.7.22) and noting that the terminal cost function $S = S(\mathbf{x}(t), t)$ , we have the control, state and costate equations, respectively expressed in terms of the Hamiltonian. Thus, for the optimal control $\mathbf{u}^{*}(t)$ , the relation (2.7.20) becomes

$$\left(\frac {\partial \mathcal {L}}{\partial \mathbf {u}}\right) _ {*} = 0 \longrightarrow \boxed {\left(\frac {\partial \mathcal {H}}{\partial \mathbf {u}}\right) _ {*} = 0} \tag {2.7.29}$$

for the optimal state $\mathbf{x}^{*}(t)$ , the relation (2.7.19) becomes
