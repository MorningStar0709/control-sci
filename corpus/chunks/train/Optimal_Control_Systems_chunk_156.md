$$
\begin{array}{l} \frac {\partial}{\partial \mathbf {u}} \left\{\frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right\} = \mathbf {R} (t) \mathbf {u} (t) \quad \text { and } \\ \frac {\partial}{\partial \mathbf {u}} \left\{\boldsymbol {\lambda} ^ {\prime} (t) \mathbf {B} (t) \mathbf {u} (t) \right\} = \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} (t). \\ \end{array}
$$

Similar expressions are used throughout the rest of the book. Further details on such relations are found in Appendix A. We immediately notice from (3.2.5) the need for $\mathbf{R}(t)$ to be positive definite and not positive semidefinite so that the inverse $\mathbf{R}^{-1}(t)$ exists.

\- Step 3: State and Costate System: Obtain the state and costate equations according to (2.7.30) and (2.7.31) as

$$\dot {\mathbf {x}} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*} \longrightarrow \dot {\mathbf {x}} ^ {*} (t) = \mathbf {A} (t) \mathbf {x} ^ {*} (t) + \mathbf {B} (t) \mathbf {u} ^ {*} (t) \tag {3.2.6}\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} \longrightarrow \dot {\boldsymbol {\lambda}} ^ {*} (t) = - \mathbf {Q} (t) \mathbf {x} ^ {*} (t) - \mathbf {A} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t). \tag {3.2.7}$$

Substitute the control relation $(3.2.5)$ in the state equation $(3.2.6)$ to obtain the (state and costate) canonical system (also called Hamiltonian system) of equations

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} ^ {*} (t) \\ \dot {\boldsymbol {\lambda}} ^ {*} (t) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} (t) & - \mathbf {E} (t) \\ - \mathbf {Q} (t) & - \mathbf {A} ^ {\prime} (t) \end{array} \right] \left[ \begin{array}{c} \mathbf {x} ^ {*} (t) \\ \boldsymbol {\lambda} ^ {*} (t) \end{array} \right] \tag {3.2.8}
$$

where $\mathbf{E}(t) = \mathbf{B}(t)\mathbf{R}^{-1}(t)\mathbf{B}'(t)$ . The general boundary condition given by the relation (2.7.32) is reproduced here as

$$\left[ \mathcal {H} ^ {*} + \frac {\partial S}{\partial t} \right] _ {t _ {f}} \delta t _ {f} + \left[ \left(\frac {\partial S}{\partial \mathbf {x}}\right) _ {*} - \boldsymbol {\lambda} ^ {*} (t) \right] _ {t _ {f}} ^ {\prime} \delta \mathbf {x} _ {f} = 0 \tag {3.2.9}$$
