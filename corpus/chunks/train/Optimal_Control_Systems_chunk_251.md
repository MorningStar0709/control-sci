# 4.6 Problems

1. Make reasonable assumptions wherever necessary.

2. Use MATLAB $^{©}$ wherever possible to solve the problems and plot all the optimal controls and states for all problems. Provide the relevant MATLAB $^{©}$ m files.

Problem 4.1 A second order plant

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t), \\ \dot {x} _ {2} (t) = - 2 x _ {1} (t) - 3 x _ {2} (t) + u (t) \\ \mathbf {y} (t) = \mathbf {x} (t) \\ \end{array}
$$

is to be controlled to minimize a performance index and to keep the state $x_{1}(t)$ close to a ramp function 2t. The final time $t_{f}$ is specified, the final state $\mathbf{x}(t_{f})$ is free and the admissible controls and states are unbounded. Formulate the performance index, obtain the feedback control law and plot all the time histories of Riccati coefficients, optimal states and control.

Problem 4.2 A second order plant

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t), \\ \dot {x} _ {2} (t) = - 2 x _ {1} (t) - 4 x _ {2} (t) + 0. 5 u (t) \\ \mathbf {y} (t) = \mathbf {x} (t) \\ \end{array}
$$

is to be controlled to minimize the performance index

$$J = \int_ {t _ {0}} ^ {t _ {f}} \left[ 4 x _ {1} ^ {2} (t) + 6 x _ {2} ^ {2} (t) + 0. 0 2 u ^ {2} (t) \right] d t.$$

The final time $t_{f}$ is specified, the final state $\mathbf{x}(t_{f})$ is fixed and the admissible controls and states are unbounded. Obtain the feedback control law and plot all the time histories of inverse Riccati coefficients, optimal states and control.
