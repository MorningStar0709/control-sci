We develop the procedure for free-end-point regulator system under the following steps (see Table 2.1).

- Step 1: Hamiltonian   
- Step 2: Optimal Control   
- Step 3: State and Costate System   
- Step 4: Closed-Loop Optimal Control   
- Step 5: Boundary Conditions

Now, we address these steps in detail.

\- Step 1: Hamiltonian: Formulate the Hamiltonian as

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t)) = \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \\ + \boldsymbol {\lambda} ^ {\prime} (t) [ \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) ] \tag {4.3.6} \\ \end{array}
$$

\- Step 2: Optimal Control: Taking the partial of $\mathcal{H}$ w.r.t. $\mathbf{u}$ , we have

$$\frac {\partial \mathcal {H}}{\partial \mathbf {u}} = 0 \longrightarrow \mathbf {R} (t) \mathbf {u} (t) + \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} (t) = 0 \tag {4.3.7}$$

which gives optimal control $\mathbf{u}^{*}(t)$ as

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t). \tag {4.3.8}$$
