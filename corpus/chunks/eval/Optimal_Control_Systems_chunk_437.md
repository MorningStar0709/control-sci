# 7.7 Problems

1. Make reasonable assumptions wherever necessary.

2. Use MATLAB $^{©}$ wherever possible to solve the problems and plot all the optimal controls and states for all problems. Provide the relevant MATLAB $^{©}$ m files.

Problem 7.1 Derive the expressions for minimum time given by (7.2.28) for a double integral system.

Problem 7.2 A second order system, described by

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = - 2 x _ {2} (t) + x _ {1} (t) + u (t)$$

where, the initial and final states are specified, is to minimize the performance index

$$J = \frac {1}{2} \int_ {0} ^ {1} \left[ 2 x _ {1} ^ {2} (t) + x _ {2} ^ {2} (t) + u ^ {2} (t) \right] d t.$$

Find the optimal control $u^{*}(t)$ for

(a) $u(t)$ unconstrained, and

(b) $u(t)$ constrained as $|u(t)| \leq 1$ .

Problem 7.3 Find the optimal control law for transferring the second order linear system

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = u (t)$$

where, (a) the control $u(t)$ is unconstrained and (b) the control $|u(t)| \leq 1$ , from any arbitrary initial state to the final state [2, 2] in minimum time.

Problem 7.4 For the second order, linear system

$$\dot {x} _ {1} (t) = - x _ {1} (t) - u (t)\dot {x} _ {2} (t) = - 3 x _ {2} (t) - 2 u (t)$$

to be transferred from any arbitrary initial state to origin in minimum time, find the optimal control law if the control $u(t)$ is (a) unconstrained and (b) constrained as $|u(t)| \leq 1$ .

Problem 7.5 Given a second order linear system

$$
\begin{array}{l} \dot {x} _ {1} (t) = - x _ {1} (t) - u (t) \\ \dot {x} _ {2} (t) = - 3 x _ {2} (t) - 2 u (t), \quad | u (t) | \leq 1 \\ \end{array}
$$

find the expression for minimum time to transfer the above system from any initial state to the origin.

Problem 7.6 For a first order system

$$\dot {x} (t) = u (t), \quad | u (t) | \leq 1$$

find the optimal control law to minimize the performance index

$$J = \int_ {0} ^ {t _ {f}} | u (t) | d t \quad t _ {f} \text { is free }$$

so that the system is driven from $x(0) = x_0$ to origin.

Problem 7.7 Formulate and solve Problem 7.4 as fuel-optimal control problem.

Problem 7.8 A second order system

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) \\ \dot {x} _ {2} (t) = - a x _ {2} (t) + u (t), \quad a > 0 \\ \end{array}
$$

with control constraint as $|u(t)| \leq 1$ , discuss the optimal control strategy to transfer the system to origin and at the same time minimize the performance index

$$J = \int_ {0} ^ {t _ {f}} [ \beta + | u (t) | ] d t$$

where, the final time $t_f$ is free and $\beta > 0$ .
