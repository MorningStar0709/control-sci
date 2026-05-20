$$
\begin{array}{l} \dot {\boldsymbol {\lambda}} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial \mathbf {x}} \\ = - \mathbf {C} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {C} (t) \mathbf {x} ^ {*} (t) - \mathbf {A} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) \\ + \mathbf {C} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {z} (t). \tag {4.1.10} \\ \end{array}
$$

For the sake of simplicity, let us define

$$\mathbf {E} (t) = \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t), \quad \mathbf {V} (t) = \mathbf {C} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {C} (t),\mathbf {W} (t) = \mathbf {C} ^ {\prime} (t) \mathbf {Q} (t). \tag {4.1.11}$$

Using the relation $(4.1.11)$ and combining the state $(4.1.8)$ and costate $(4.1.10)$ equations, we obtain the Hamiltonian canonical system as

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} ^ {*} (t) \\ \dot {\boldsymbol {\lambda}} ^ {*} (t) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} (t) & - \mathbf {E} (t) \\ - \mathbf {V} (t) & - \mathbf {A} ^ {\prime} (t) \end{array} \right] \left[ \begin{array}{c} \mathbf {x} ^ {*} (t) \\ \boldsymbol {\lambda} ^ {*} (t) \end{array} \right] + \left[ \begin{array}{c} \mathbf {0} \\ \mathbf {W} (t) \end{array} \right] \mathbf {z} (t). \tag {4.1.12}
$$

This canonical system of 2n differential equations is linear, time-varying, but nonhomogeneous with $\mathbf{W}(t)\mathbf{z}(t)$ as forcing function. The boundary conditions for this state and costate equations are given by the initial condition on the state as

$$\mathbf {x} (t = t _ {0}) = \mathbf {x} (t _ {0}) \tag {4.1.13}$$

and the final condition on the costate (for the final time $t_{f}$ specified and state $\mathbf{x}(t_{f})$ being free) given by (3.2.10), which along with (4.1.4) become

$$
\begin{array}{l} \boldsymbol {\lambda} (t _ {f}) = \frac {\partial}{\partial \mathbf {x} (t _ {f})} \left[ \frac {1}{2} \mathbf {e} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {e} (t _ {f}) \right] \\ = \frac {\partial}{\partial \mathbf {x} (t _ {f})} \left[ \frac {1}{2} [ \mathbf {z} (t _ {f}) - \mathbf {C} (t _ {f}) \mathbf {x} (t _ {f}) ] ^ {\prime} \mathbf {F} (t _ {f}) [ \mathbf {z} (t _ {f}) - \mathbf {C} (t _ {f}) \mathbf {x} (t _ {f}) ] \right] \\ = \mathbf {C} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {C} (t _ {f}) \mathbf {x} (t _ {f}) - \mathbf {C} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {z} (t _ {f}). \tag {4.1.14} \\ \end{array}
$$
