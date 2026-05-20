$$- \left(\frac {\partial J ^ {*}}{\partial t}\right) = \min _ {u (t) \in \mathcal {U}} \left[ L (\mathbf {x} (\mathbf {u}, t), \mathbf {u}, t) + \left(\frac {\partial J ^ {*}}{\partial \mathbf {x}}\right) ^ {T} f (\mathbf {x}, \mathbf {u}, t) \right] \tag {4.122}$$

because it provides a necessary condition for optimality (note that we will use the asterisk to denote optimality). The Bellman equation assumes a system of the form

$$\frac {d \mathbf {x}}{d t} = f (\mathbf {x}, \mathbf {u}, t) \tag {4.123}$$

starting from an initial state $\mathbf { x } ( t _ { 0 } ) = t _ { 0 }$ . Then, one wishes to find an input ${ \bf \delta u } ( t )$ , defined over $[ t _ { 0 } , T ]$ , that minimizes a performance index of the form

$$J = \int_ {t _ {0}} ^ {T} L (\mathbf {x}, \mathbf {u}, t) d t, \tag {4.124}$$

where the function $L ( \mathbf { x } , \mathbf { u } , t )$ is assumed to be continuous with respect to t. Thus, the Bellman equation for (4.121) is

$$- \frac {\partial J ^ {*}}{\partial t} = \left[ \frac {1}{2} \mathbf {x} ^ {T} (t) \mathbf {Q} (t) \mathbf {x} (t) + \frac {1}{2} \mathbf {u} ^ {* T} (t) \mathbf {R} (t) \mathbf {u} ^ {*} (t) + \left(\frac {\partial J ^ {*}}{\partial \mathbf {x}}\right) ^ {T} (\mathbf {A} (t) \mathbf {x} + \mathbf {B} (t) \mathbf {u} ^ {*}) \right]. \tag {4.125}$$

The boundary condition is

$$\lim _ {t \to T} J ^ {*} (\mathbf {x}, t) = \frac {1}{2} \mathbf {x} ^ {T} (T) \mathbf {S} \mathbf {x} (T). \tag {4.126}$$

The minimization procedure results in

$$\left. \frac {\partial L}{\partial \mathbf {u}} \right| _ {\mathbf {u} = \mathbf {u} ^ {*}} + \frac {\partial}{\partial \mathbf {u}} \left[ \left(\frac {\partial J ^ {*}}{\partial \mathbf {x}}\right) ^ {T} (\mathbf {A} (t) \mathbf {x} + \mathbf {B} (t) \mathbf {u}) \right] \bigg | _ {\mathbf {u} = \mathbf {u} ^ {*}} = 0, \tag {4.127}$$

where L is the integrand in (4.121). This yields

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {T} (t) (\partial J ^ {*} / \partial \mathbf {x}). \tag {4.128}$$

If we wish to have a linear feedback control, $J ^ { * }$ should be of the quadratic form

$$J ^ {*} (\mathbf {x}, t) = \frac {1}{2} \mathbf {x} ^ {T} \mathbf {P} (t) \mathbf {x} \tag {4.129}$$

with $\mathbf { P } ( t )$ an $n \times n$ symmetric matrix. Now, substituting (4.128) and (4.129) into the Bellman equation (i.e., (4.122)), we obtain a matrix Riccati equation [25]
