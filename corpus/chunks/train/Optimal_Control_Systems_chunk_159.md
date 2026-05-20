$$- \mathbf {Q} (t) \mathbf {x} ^ {*} (t) - \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t) = \dot {\mathbf {P}} (t) \mathbf {x} ^ {*} (t) +\mathbf {P} (t) \left[ \mathbf {A} (t) \mathbf {x} ^ {*} (t) - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t) \right] \longrightarrow\left[ \dot {\mathbf {P}} (t) + \mathbf {P} (t) \mathbf {A} (t) + \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) + \mathbf {Q} (t) - \right.\left. \mathbf {P} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \right] \mathbf {x} ^ {*} (t) = 0 \tag {3.2.16}$$

Essentially, we eliminated the costate function $\lambda^{*}(t)$ from the control (3.2.5), the state (3.2.6) and the costate (3.2.7) equations by introducing the transformation (3.2.11).

\- Step 5: Matrix Differential Riccati Equation: Now the relation (3.2.16) should be satisfied for all $t \in [t_0, t_f]$ and for any choice of the initial state $\mathbf{x}^{*}(t_{0})$ . Also, $\mathbf{P}(t)$ is not dependent on the initial state. It follows that the equation (3.2.16) should hold good for any value of $\mathbf{x}^{*}(t)$ . This clearly means that the function $\mathbf{P}(t)$ should satisfy the matrix differential equation

$$\dot {\mathbf {P}} (t) + \mathbf {P} (t) \mathbf {A} (t) + \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) + \mathbf {Q} (t) -\mathbf {P} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) = 0. \tag {3.2.17}$$

This is the matrix differential equation of the Riccati type, and often called the matrix differential Riccati equation (DRE). Also, the transformation (3.2.11) is called the Riccati transformation, $\mathbf{P}(t)$ is called the Riccati coefficient matrix or simply Riccati matrix or Riccati coefficient, and (3.2.12) is the optimal control (feedback) law. The matrix DRE (3.2.17) can also be written in a compact form as

$$\dot {\mathbf {P}} (t) = - \mathbf {P} (t) \mathbf {A} (t) - \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) - \mathbf {Q} (t) + \mathbf {P} (t) \mathbf {E} (t) \mathbf {P} (t) \tag {3.2.18}$$

where $\mathbf{E}(t) = \mathbf{B}(t)\mathbf{R}^{-1}(t)\mathbf{B}'(t)$ .

Comparing the boundary condition(3.2.10) and the Riccati transformation (3.2.11), we have the final condition on $\mathbf{P}(t)$ as

$$\boldsymbol {\lambda} ^ {*} (t _ {f}) = \mathbf {P} (t _ {f}) \mathbf {x} ^ {*} (t _ {f}) = \mathbf {F} (t _ {f}) \mathbf {x} ^ {*} (t _ {f}) \longrightarrow\boxed {\mathbf {P} (t _ {f}) = \mathbf {F} (t _ {f}).} \tag {3.2.19}$$

Thus, the matrix DRE (3.2.17) or (3.2.18) is to be solved backward in time using the final condition (3.2.19) to obtain the solution $\mathbf{P}(t)$ for the entire interval $[t_{0}, t_{f}]$ .
