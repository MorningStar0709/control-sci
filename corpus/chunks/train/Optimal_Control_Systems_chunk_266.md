$$\mathcal {L} (\mathbf {x} ^ {*} (k), \mathbf {x} ^ {*} (k + 1), \mathbf {u} ^ {*} (k), \boldsymbol {\lambda} ^ {*} (k + 1)) =\mathcal {H} (\mathbf {x} ^ {*} (k), \mathbf {u} ^ {*} (k), \boldsymbol {\lambda} ^ {*} (k + 1))- \lambda^ {*} (k + 1) \mathbf {x} ^ {*} (k + 1). \tag {5.2.12}$$

Now, using the relation $(5.2.12)$ in the set of Euler-Lagrange equations $(5.2.6)$ to $(5.2.8)$ , we get the required conditions for extremum in terms of the Hamiltonian as

$$\boxed \boldsymbol {\lambda} ^ {*} (k) = \frac {\partial \mathcal {H} (\mathbf {x} ^ {*} (k) , \mathbf {u} ^ {*} (k) , \boldsymbol {\lambda} ^ {*} (k + 1))}{\partial \mathbf {x} ^ {*} (k)}, \tag {5.2.13}0 = \frac {\partial \mathcal {H} (\mathbf {x} ^ {*} (k) , \mathbf {u} ^ {*} (k) , \boldsymbol {\lambda} ^ {*} (k + 1))}{\partial \mathbf {u} ^ {*} (k)}, \tag {5.2.14}\boxed {\mathbf {x} ^ {*} (k) = \frac {\partial \mathcal {H} (\mathbf {x} ^ {*} (k - 1) , \mathbf {u} ^ {*} (k - 1) , \boldsymbol {\lambda} ^ {*} (k))}{\partial \boldsymbol {\lambda} ^ {*} (k)}.} \tag {5.2.15}$$

Note that the relation $(5.2.15)$ can also be written in a more appropriate way by considering the whole relation at the next stage as

$$\mathbf {x} ^ {*} (k + 1) = \frac {\partial \mathcal {H} (\mathbf {x} ^ {*} (k) , \mathbf {u} ^ {*} (k) , \boldsymbol {\lambda} ^ {*} (k + 1))}{\partial \boldsymbol {\lambda} ^ {*} (k + 1)}. \tag {5.2.16}$$

For the present system described by the plant (5.2.1) and the performance index (5.2.3) we have the relations (5.2.16), (5.2.13), and (5.2.14) for the state, costate, and control, transforming respectively, to

$$\mathbf {x} ^ {*} (k + 1) = \mathbf {A} (k) \mathbf {x} ^ {*} (k) + \mathbf {B} (k) \mathbf {u} ^ {*} (k) \tag {5.2.17}\boldsymbol {\lambda} ^ {*} (k) = \mathbf {Q} (k) \mathbf {x} ^ {*} (k) + \mathbf {A} ^ {\prime} (k) \boldsymbol {\lambda} ^ {*} (k + 1) \tag {5.2.18}\mathbf {0} = \mathbf {R} (k) \mathbf {u} ^ {*} (k) + \mathbf {B} ^ {\prime} (k) \boldsymbol {\lambda} ^ {*} (k + 1). \tag {5.2.19}$$

\- Step 5: Open-Loop Optimal Control: The optimal control is then given by (5.2.19) as

$$\boxed {\mathbf {u} ^ {*} (k) = - \mathbf {R} ^ {- 1} (k) \mathbf {B} ^ {\prime} (k) \boldsymbol {\lambda} ^ {*} (k + 1)} \tag {5.2.20}$$
