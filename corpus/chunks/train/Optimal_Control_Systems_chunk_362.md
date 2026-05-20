$$
\begin{array}{l} \mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), J _ {\mathbf {x}} ^ {*}, t) = \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \frac {1}{2} J _ {\mathbf {x}} ^ {* \prime} \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) J _ {\mathbf {x}} ^ {*} \\ + J _ {\mathbf {x}} ^ {* \prime} \mathbf {A} (t) \mathbf {x} (t) - J _ {\mathbf {x}} ^ {* \prime} \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) J _ {\mathbf {x}} ^ {*} \\ = \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) - \frac {1}{2} J _ {\mathbf {x}} ^ {* \prime} \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) J _ {\mathbf {x}} ^ {*} \\ + J _ {\mathbf {x}} ^ {* \prime} \mathbf {A} (t) \mathbf {x} (t). \tag {6.5.7} \\ \end{array}
$$

The HJB equation is

$$J _ {t} ^ {*} + \mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), J _ {\mathbf {x}} ^ {*}, t) = 0. \tag {6.5.8}$$

With (6.5.7), the HJB equation (6.5.8) becomes

$$J _ {t} ^ {*} + \frac {1}{2} \mathbf {x} ^ {* \prime} (t) \mathbf {Q} (t) \mathbf {x} ^ {*} (t) - \frac {1}{2} J _ {\mathbf {x}} ^ {* \prime} \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) J _ {\mathbf {x}} ^ {*}+ J _ {\mathbf {x}} ^ {* \prime} \mathbf {A} (t) \mathbf {x} ^ {*} (t) = 0, \tag {6.5.9}$$

with boundary condition

$$J ^ {*} (\mathbf {x} ^ {*} (t _ {f}), t _ {f}) = \frac {1}{2} \mathbf {x} ^ {* \prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} ^ {*} (t _ {f}). \tag {6.5.10}$$

\- Step 4: Since the performance index $J$ is a quadratic function of the state, it seems reasonable to assume a solution as

$$J ^ {*} (\mathbf {x} (t), t) = \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} (t) \tag {6.5.11}$$

where, $\mathbf{P}(t)$ is a real, symmetric, positive-definite matrix to be determined (for convenience \* is omitted for $\mathbf{x}(t)$ ). With

$$\frac {\partial J ^ {*}}{\partial t} = J _ {t} = \frac {1}{2} \mathbf {x} (t) \dot {\mathbf {P}} (t) \mathbf {x} (t),\frac {\partial J ^ {*}}{\partial \mathbf {x}} = J _ {\mathbf {x}} = \mathbf {P} (t) \mathbf {x} (t) \tag {6.5.12}$$

and using the performance index (6.5.11) in the HJB equation (6.5.9), we get
