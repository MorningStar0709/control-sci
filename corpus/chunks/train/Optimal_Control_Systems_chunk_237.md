# 4.4.1 Regulator System with Prescribed Degree of Stability: Summary

For a controllable, linear, time-invariant plant

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t), \tag {4.4.11}$$

and the infinite interval cost functional

$$J = \frac {1}{2} \int_ {t _ {0}} ^ {\infty} e ^ {2 \alpha t} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R u} (t) \right] d t, \tag {4.4.12}$$

the optimal control is given by

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {x} ^ {*} (t) = - \bar {\mathbf {K}} \mathbf {x} ^ {*} (t) \tag {4.4.13}$$

where, $\bar{\mathbf{K}} = \mathbf{R}^{-1}\mathbf{B}'\bar{\mathbf{P}}$ and $\bar{\mathbf{P}}$ , the $nxn$ constant, positive definite, symmetric matrix, is the solution of the nonlinear, matrix algebraic Riccati equation (ARE)

$$\bar {\mathbf {P}} (\mathbf {A} + \alpha \mathbf {I}) + \left(\mathbf {A} ^ {\prime} + \alpha \mathbf {I}\right) \bar {\mathbf {P}} - \bar {\mathbf {P}} \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} + \mathbf {Q} = 0, \tag {4.4.14}$$

the optimal trajectory is the solution of

$$\dot {\mathbf {x}} ^ {*} (t) = \left(\mathbf {A} - \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}}\right) \mathbf {x} ^ {*} (t), \tag {4.4.15}$$

and the optimal cost is given by

$$J ^ {*} = \frac {1}{2} e ^ {2 \alpha t _ {0}} \mathbf {x} ^ {* \prime} (t _ {0}) \bar {\mathbf {P}} \mathbf {x} ^ {*} (t _ {0}). \tag {4.4.16}$$

The entire procedure is now summarized in Table 4.2. Consider a first-order system example to illustrate the previous method.
