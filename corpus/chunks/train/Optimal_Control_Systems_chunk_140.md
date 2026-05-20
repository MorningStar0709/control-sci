# 2.8.4 Stage IV: Optimal Control System with Hamiltonian Formalism: Pontryagin Principle

Here, we just transform the previous Lagrangian formalism to Hamiltonian formalism by defining the Hamiltonian as [57]

$$\mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) = V (\mathbf {x} (t), \mathbf {u} (t), t) + \boldsymbol {\lambda} ^ {\prime} (t) \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \tag {2.8.25}$$

which in terms of the Lagrangian (2.8.20) becomes

$$\mathcal {L} (\mathbf {x} (t), \dot {\mathbf {x}} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) = \mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) - \boldsymbol {\lambda} ^ {\prime} (t) \dot {\mathbf {x}} (t). \tag {2.8.26}$$

Now using $(2.8.26)$ , the set of Euler-Lagrange equations $(2.8.21)$ to $(2.8.23)$ which are in terms of the Lagrangian, are rewritten in terms

of the Hamiltonian as

$$\left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} - \frac {d}{d t} (- \boldsymbol {\lambda} ^ {*}) = 0 \tag {2.8.27}\left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*} - \dot {\mathbf {x}} ^ {*} (t) - \frac {d}{d t} (0) = 0 \tag {2.8.28}\left(\frac {\partial \mathcal {H}}{\partial \mathbf {u}}\right) _ {*} - \frac {d}{d t} (0) = 0 \tag {2.8.29}$$

which in turn are rewritten as

$$\boxed {\dot {\mathbf {x}} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*}} \text {state equation,} \tag {2.8.30}\boxed {\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*}} \text { costate equation, and } \tag {2.8.31}\boxed {0 = + \left(\frac {\partial \mathcal {H}}{\partial \mathbf {u}}\right) _ {*} c o n t r o l e q u a t i o n.} \tag {2.8.32}$$

Similarly using $(2.8.26)$ , the boundary condition $(2.8.24)$ is rewritten in terms of the Hamiltonian as

$$\left. \left[ \mathcal {H} - \boldsymbol {\lambda} ^ {\prime} (t) \dot {\mathbf {x}} (t) - \dot {\mathbf {x}} ^ {\prime} (t) (- \boldsymbol {\lambda} (t)) \right] \right| _ {* _ {t _ {f}}} \delta t _ {f} + \left. \left[ - \boldsymbol {\lambda} ^ {\prime} (t) \right] \right| _ {* _ {t _ {f}}} \delta \mathbf {x} _ {f} = 0 (2. 8. 3 3)$$

which becomes

$$\boxed {\mathcal {H} | _ {* t _ {f}} \delta t _ {f} - \boldsymbol {\lambda} ^ {* \prime} (t _ {f}) \delta \mathbf {x} _ {f} = 0.} \tag {2.8.34}$$

The sufficient condition is

$$\boxed {\left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}}\right) _ {*} > 0} \quad \text { for minimum and } \tag {2.8.35}\boxed {\left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}}\right) _ {*} < 0} \quad \text { for maximum. } \tag {2.8.36}$$

The state, costate, and control equations (2.8.30) to (2.8.32) are solved along with the given initial condition (2.8.16) and the final condition (2.8.34) leading us to a two-point boundary value problem (TPBVP).
