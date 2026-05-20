# 4.6 Problems

Problem 4.3 For a linear, time-varying system (3.2.48) given as

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t),\mathbf {y} (t) = \mathbf {C} (t) \mathbf {x} (t)$$

with a general cost functional (3.2.49) as

$$
\begin{array}{l} J = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {u} ^ {\prime} (t) \right] \left[ \begin{array}{c c} \mathbf {Q} (t) & \mathbf {S} (t) \\ \mathbf {S} ^ {\prime} (t) & \mathbf {R} (t) \end{array} \right] \left[ \begin{array}{c} \mathbf {x} (t) \\ \mathbf {u} (t) \end{array} \right] d t, \\ \end{array}
$$

where, the various vectors and matrices are defined in Chapter 3, formulate a tracking problem and obtain the results similar to those obtained in Chapter 4.

Problem 4.4 Using the frequency-domain results, determine the optimal feedback coefficients and the closed-loop optimal control for the multi-input, multi-output system

$$
\dot {\mathbf {x}} (t) = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \mathbf {x} (t) + \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \mathbf {u} (t)
$$

and the cost function

$$J = \int_ {0} ^ {\infty} [ 4 x _ {1} ^ {2} (t) + 4 x _ {2} ^ {2} (t) + 0. 5 u _ {1} ^ {2} (t) + u _ {2} ^ {2} (t) ] d t.$$

Problem 4.5 For the D.C. motor speed control system described in Problem 1.1, find the closed-loop optimal control to track the speed at a particular value.

Problem 4.6 For the liquid-level control system described in Problem 1.2, find the closed-loop optimal control to track the liquid level along a ramp function 0.25t.

Problem 4.7 For the mechanical control system described in Problem 1.4, find the closed-loop optimal control to track the system along (i) a constant value and (ii) a ramp function.

Problem 4.8 For the chemical control system described in Problem 1.6, find the closed-loop optimal control to track the system along (i) a constant value and (ii) a ramp function.
