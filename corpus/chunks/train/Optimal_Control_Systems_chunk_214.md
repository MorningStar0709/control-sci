# 4.1.1 Linear Quadratic Tracking System: Summary

Given the linear, observable system (see Figure 4.1)

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t)\mathbf {y} (t) = \mathbf {C} (t) \mathbf {x} (t) \tag {4.1.29}$$

the desired output $\mathbf{z}(t)$ , the error $\mathbf{e}(t)=\mathbf{z}(t)-\mathbf{y}(t)$ , and the performance index

$$J = \frac {1}{2} \mathbf {e} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {e} (t _ {f}) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {e} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {e} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t \tag {4.1.30}$$

then the optimal control $\mathbf{u}^{*}(t)$ is given by

$$
\begin{array}{l} \mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) [ \mathbf {P} (t) \mathbf {x} ^ {*} (t) - \mathbf {g} (t) ] \\ = - \mathbf {K} (t) \mathbf {x} ^ {*} (t) + \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {g} (t) \tag {4.1.31} \\ \end{array}
$$

where, the $nxn$ symmetric, positive definite matrix $\mathbf{P}(t)$ is the solution of the nonlinear, matrix differential Riccati equation (DRE)

$$\dot {\mathbf {P}} (t) = - \mathbf {P} (t) \mathbf {A} (t) - \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) + \mathbf {P} (t) \mathbf {E} (t) \mathbf {P} (t) - \mathbf {V} (t) \tag {4.1.32}$$

with final condition

$$\mathbf {P} (t _ {f}) = \mathbf {C} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {C} (t _ {f}), \tag {4.1.33}$$

and the $n$ th order $\mathbf{g}(t)$ is the solution of the linear, nonhomogeneous vector differential equation

$$\dot {\mathbf {g}} (t) = - \left[ \mathbf {A} (t) - \mathbf {E} (t) \mathbf {P} (t) \right] ^ {\prime} \mathbf {g} (t) - \mathbf {W} (t) \mathbf {z} (t) \tag {4.1.34}$$

with final condition

$$\mathbf {g} (t _ {f}) = \mathbf {C} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {z} (t _ {f}) \tag {4.1.35}$$

where, $\mathbf{E}(t)$ , $\mathbf{V}(t)$ and $\mathbf{W}(t)$ are defined in (4.1.11), the optimal state (trajectory) is the solution of the linear state equation

$$\dot {\mathbf {x}} ^ {*} (t) = \left[ \mathbf {A} (t) - \mathbf {E} ^ {\prime} (t) \mathbf {P} (t) \right] \mathbf {x} ^ {*} (t) + \mathbf {E} (t) \mathbf {g} (t), \tag {4.1.36}$$

and the optimal cost $J^{*}$

$$J ^ {*} (t _ {0}) = \frac {1}{2} \mathbf {x} ^ {* ^ {\prime}} (t _ {0}) \mathbf {P} (t _ {0}) \mathbf {x} ^ {*} (t _ {0}) - \mathbf {x} ^ {*} (t _ {0}) \mathbf {g} (t _ {0}) + \mathbf {h} (t _ {0}). \tag {4.1.37}$$

The implementation of the tracking system is shown in Figure 4.1. The entire procedure is now summarized in Table 4.1.
