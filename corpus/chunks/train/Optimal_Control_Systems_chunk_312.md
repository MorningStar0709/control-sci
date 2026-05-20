# 5.7 Problems

1. Make reasonable assumptions wherever necessary.

2. Use MATLAB $^{©}$ wherever possible to solve the problems and plot all the optimal controls and states for all problems. Provide the relevant MATLAB $^{©}$ m files.

Problem 5.1 Show that the coefficient matrix $\mathbf{P}(k)$ in the matrix difference Riccati equation (5.3.11)

$$\mathbf {P} (k) = \mathbf {A} ^ {\prime} (k) \mathbf {P} (k + 1) [ \mathbf {I} + \mathbf {E} (k) \mathbf {P} (k + 1) ] ^ {- 1} \mathbf {A} (k) + \mathbf {Q} (k)$$

is positive definite.

Problem 5.2 A second order discrete-time system is given by

$$x _ {1} (k + 1) = 2 x _ {1} (k) + 0. 2 x _ {2} (k), \quad x _ {1} (0) = 2x _ {2} (k + 1) = 2 x _ {2} (k) + 0. 2 u (k), \quad x _ {2} (0) = 0.$$

The performance index to be minimized is

$$J = \frac {1}{2 0} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left[ x _ {1} (k) ^ {2} + u (k) ^ {2} \right]$$

where, $k_0 = 0$ , and $k_f = 10$ . In order to drive the above system to the final states $x_1(10) = x_2(10) = 0$ ,

(a) find the open-loop optimal control, and

(b) find the closed-loop optimal control.

Problem 5.3 Find the open-loop optimal control sequence $u(0)$ , $u(1)$ , $u(2)$ for the second order discrete-time system

$$
\mathbf {x} (k + 1) = {\left[ \begin{array}{l l} 0 & 1 \\ - 1 & 1 \end{array} \right]} \mathbf {x} (k) + {\left[ \begin{array}{l} 0 \\ 1 \end{array} \right]} u (k), \quad \mathbf {x} (0) = {\left[ \begin{array}{l} 1 \\ 2 \end{array} \right]}
$$

and the performance index

$$J = \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left[ x _ {1} ^ {2} (k) + u ^ {2} (k) \right]$$

where, $k_{f} = 5$ , $x_{1}(5)$ is unspecified, and $x_{2}(5) = 0$ .

Problem 5.4 Derive the relation for the optimal cost function given by (5.3.28) as

$$J ^ {*} = \frac {1}{2} \mathbf {x} ^ {* \prime} (k _ {0}) \mathbf {P} (k _ {0}) \mathbf {x} (k _ {0}).$$

Problem 5.5 Given the plant as

$$\mathbf {x} (k + 1) = \mathbf {A} (k) \mathbf {x} (k) + \mathbf {B} (k) \mathbf {u} (k)$$

the performance index as

$$
\begin{array}{l} J (k _ {0}) = \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f}) \mathbf {F} (k _ {f}) \mathbf {x} (k _ {f}) \\ + \frac {1}{2} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left[ \mathbf {x} ^ {\prime} (k) \mathbf {Q} (k) \mathbf {x} (k) + \mathbf {u} ^ {\prime} (k) \mathbf {R} (k) \mathbf {u} (k) \right] \\ \end{array}
$$
