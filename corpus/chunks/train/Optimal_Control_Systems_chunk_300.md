\- Step 1: Hamiltonian: We first formulate the Hamiltonian as

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} (k), \mathbf {u} (k), \boldsymbol {\lambda} (k + 1)) = \frac {1}{2} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left\{\left[ \mathbf {C x} (k) - \mathbf {z} (k) \right] ^ {\prime} \mathbf {Q} [ \mathbf {C x} (k) - \mathbf {z} (k) ] \right. \\ \left. + \mathbf {u} ^ {\prime} (k) \mathbf {R u} (k) \right\} + \boldsymbol {\lambda} ^ {\prime} (k + 1) [ \mathbf {A x} (k) + \mathbf {B u} (k) ] \tag {5.5.4} \\ \end{array}
$$

and follow the identical approach of the state regulator system described in the previous section. For the sake of simplicity, let us define

$$\mathbf {E} = \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime}, \quad \mathbf {V} = \mathbf {C} ^ {\prime} \mathbf {Q} \mathbf {C} \text { and } \mathbf {W} = \mathbf {C} ^ {\prime} \mathbf {Q}. \tag {5.5.5}$$

\- Step 2: State and Costate System: Using (5.2.15), (5.2.13) and (5.2.14) for the state, costate, and control, respectively, we obtain the state equation as

$$\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda} ^ {*} (k + 1)} = \mathbf {x} ^ {*} (k + 1) \longrightarrow \mathbf {x} ^ {*} (k + 1) = \mathbf {A x} ^ {*} (k) + \mathbf {B u} ^ {*} (k), \tag {5.5.6}$$

the costate equation as

$$\frac {\partial \mathcal {H}}{\partial \mathbf {x} ^ {*} (k)} = \boldsymbol {\lambda} ^ {*} (k) \longrightarrow \boldsymbol {\lambda} ^ {*} (k) = \mathbf {A} ^ {\prime} \boldsymbol {\lambda} ^ {*} (k + 1) + \mathbf {V} \mathbf {x} ^ {*} (k) - \mathbf {W} \mathbf {z} (k), \tag {5.5.7}$$
