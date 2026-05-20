# 5.5 Discrete-Time Linear Quadratic Tracking System

and the control equation as

$$\frac {\partial \mathcal {H}}{\partial \mathbf {u} ^ {*} (k)} = 0 \longrightarrow 0 = \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (k + 1) + \mathbf {R u} ^ {*} (k). \tag {5.5.8}$$

The final condition (5.2.37) becomes

$$\boldsymbol {\lambda} (k _ {f}) = \mathbf {C} ^ {\prime} \mathbf {F} \mathbf {C} \mathbf {x} (k _ {f}) - \mathbf {C} ^ {\prime} \mathbf {F} \mathbf {z} (k _ {f}). \tag {5.5.9}$$

\- Step 3: Open-Loop Optimal Control: The relation (5.5.8) yields the open-loop optimal control as

$$\mathbf {u} ^ {*} (k) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (k + 1) \tag {5.5.10}$$

and using this in the state (5.5.6) and costate (5.5.7) system (also called Hamiltonian system), we have the Hamiltonian (canonical) system as

$$
\left[ \begin{array}{c} \mathbf {x} ^ {*} (k + 1) \\ \boldsymbol {\lambda} ^ {*} (k) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & - \mathbf {E} \\ \mathbf {V} & \mathbf {A} ^ {\prime} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} ^ {*} (k) \\ \boldsymbol {\lambda} ^ {*} (k + 1) \end{array} \right] + \left[ \begin{array}{c} \mathbf {0} \\ - \mathbf {W} \end{array} \right] \mathbf {z} (k). \tag {5.5.11}
$$

Thus, we see that the Hamiltonian system is similar to that obtained for state regulator system in the previous section, except for the nonhomogeneous nature due to the forcing term $\mathbf{z}(k)$ .

\- Step 4: Riccati and Vector Equations: Now to obtain closed-loop configuration for the optimal control (5.5.10), we may assume from the nature of the boundary condition (5.5.9) a transformation

$$\boxed {\boldsymbol {\lambda} ^ {*} (k) = \mathbf {P} (k) \mathbf {x} ^ {*} (k) - \mathbf {g} (k)} \tag {5.5.12}$$

where, the matrix $\mathbf{P}(k)$ and the vector $\mathbf{g}(k)$ are yet to be determined. In order to do so we essentially eliminate the costate $\boldsymbol{\lambda}^{*}(k)$ from the canonical system (5.5.11) using the transformation (5.5.12). Thus,

$$\mathbf {x} ^ {*} (k + 1) = \mathbf {A x} ^ {*} (k) - \mathbf {E P} (k + 1) \mathbf {x} ^ {*} (k + 1) + \mathbf {E g} (k + 1) \tag {5.5.13}$$

which is solved for $\mathbf{x}^{*}(k + 1)$ to yield

$$\mathbf {x} ^ {*} (k + 1) = [ \mathbf {I} + \mathbf {E P} (k + 1) ] ^ {- 1} \left[ \mathbf {A x} ^ {*} (k) + \mathbf {E g} (k + 1) \right]. \tag {5.5.14}$$
