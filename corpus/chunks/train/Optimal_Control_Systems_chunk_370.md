# 7.1 Constrained Optimal Control

From Chapter 6 (Table 6.1) the Pontryagin Principle is now summarized below for linear, time-invariant system with a quadratic perfor-

mance index. Given the system as

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) \tag {7.1.1}$$

with the control constraint as

$$U ^ {-} \leq \mathbf {u} (t) \leq U ^ {+} \longrightarrow | \mathbf {u} (t) | \leq \mathbf {U} \tag {7.1.2}$$

the performance index as

$$
\begin{array}{l} J (\mathbf {x} (t _ {0}), \mathbf {u} (t), t _ {0}) = J \\ = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t \tag {7.1.3} \\ \end{array}
$$

and the boundary conditions as

$$\mathbf {x} (t _ {0}) = \mathbf {x} _ {0} \text { fixed }, \mathbf {x} (t _ {f}) = \mathbf {x} _ {f} \text { is free and } t _ {f} \text { is free }, \tag {7.1.4}$$

to find the optimal control, form the Pontryagin $\mathcal{H}$ function

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) = \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \\ + \boldsymbol {\lambda} ^ {\prime} (t) [ \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) ] \tag {7.1.5} \\ \end{array}
$$

minimize $\mathcal{H}$ w.r.t. $\mathbf{u}(t)(\leq \mathbf{U})$ as

$$\mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t) \leq \mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} (t), \boldsymbol {\lambda} ^ {*} (t), t), \tag {7.1.6}$$

and solve the set of 2n state and costate differential equations

$$\dot {\mathbf {x}} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*},\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} \tag {7.1.7}$$

with the boundary conditions $\mathbf{x}_0$ and

$$\left[ \mathcal {H} + \frac {\partial S}{\partial t} \right] _ {* _ {t _ {f}}} \delta t _ {f} + \left[ \left(\frac {\partial S}{\partial \mathbf {x}}\right) - \boldsymbol {\lambda} (t) \right] _ {* _ {t _ {f}}} ^ {\prime} \delta \mathbf {x} _ {f} = 0 \tag {7.1.8}$$

where,

$$S [ \mathbf {x} (t _ {f}), t _ {f}) ] = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}).$$
