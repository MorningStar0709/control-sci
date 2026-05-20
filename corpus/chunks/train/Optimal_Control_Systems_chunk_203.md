# 3.7 Problems

1. Make reasonable assumptions wherever necessary.

2. Use MATLAB $^{©}$ wherever possible to solve the problems and plot all the optimal controls and states for all problems. Provide the relevant MATLAB $^{©}$ m files.

Problem 3.1 A first order system is given by

$$\dot {x} (t) = x (t) + u (t).$$

(a) Find the unconstrained optimal control law which minimizes the performance index

$$J = \int_ {0} ^ {t _ {f}} [ 2 x ^ {2} (t) + 0. 2 5 u ^ {2} (t) ] d t,$$

such that the final time $t_f$ is fixed and the final state $x(t_f)$ is free. (b) Find the optimal control law as $t_f \to \infty$ .

Problem 3.2 A system is described by

$$\ddot {x} (t) + x (t) = u (t)$$

with initial conditions $x(0) = 0$ and $\dot{x}(0) = 1$ and the performance index

$$J = \int_ {0} ^ {\infty} \left[ 2 x ^ {2} (t) + 0. 2 5 u ^ {2} (t) \right] d t.$$

Find the closed-loop optimal control in terms of $x$ and $\dot{x}$ and the optimal cost function.

Problem 3.3 A first order system is described by

$$\dot {x} (t) = a x (t) + b u (t)$$

with performance index

$$J = \frac {1}{2} \int_ {0} ^ {t _ {f}} [ q x ^ {2} (t) + r u ^ {2} (t) ] d t$$

and with a fixed initial state $x(0)$ and final state $x(t_f) = 0$ , where $t_f$ is fixed. Show that the solution of the Riccati equation is given by

$$p (t) = \frac {r}{b ^ {2}} \left[ a - \beta c o t h \{\beta (t - t _ {f}) \} \right]$$

and the solution of the optimal state $x^{*}(t)$ is given by

$$x ^ {*} (t) = x (0) \frac {\sinh \{\beta (t _ {f} - t) \}}{\sinh \beta}$$

where, $\beta = \sqrt{a^2 + b^2q / r}$ .

Problem 3.4 Find the optimal feedback control for the plant

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) \\ \dot {x} _ {2} (t) = - 2 x _ {1} (t) + 4 x _ {2} (t) + 5 u (t) \\ \end{array}
$$

with performance criterion

$$
\begin{array}{l} J = \frac {1}{2} f _ {1 1} \left[ x _ {1} \left(t _ {f}\right) - 4 \right] ^ {2} + \frac {1}{2} f _ {2 2} \left[ x _ {2} \left(t _ {f}\right) - 2 \right] ^ {2} + \\ \frac {1}{2} \int_ {0} ^ {t _ {f}} \left[ 5 x _ {1} ^ {2} (t) + 2 x _ {2} ^ {2} (t) + 4 u ^ {2} (t) \right] d t \\ \end{array}
$$

and initial conditions as $\mathbf{x}(0) = [1\quad 2]'$ and the final state $\mathbf{x}(t_f)$ is free, where $t_f$ is specified.

Problem 3.5 Find the closed-loop, unconstrained, optimal control for the system

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) \\ \dot {x} _ {2} (t) = - 2 x _ {1} (t) - 3 x _ {2} (t) + u (t) \\ \end{array}
$$

and the performance index

$$J = \int_ {0} ^ {\infty} [ x _ {1} ^ {2} (t) + x _ {2} ^ {2} (t) + u ^ {2} (t) ] d t.$$

Problem 3.6 Find the optimal feedback control law for the plant

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) + u (t) \\ \dot {x} _ {2} (t) = - x _ {1} (t) - x _ {2} (t) + u (t) \\ \end{array}
$$

and the cost function

$$J = \int_ {0} ^ {\infty} [ 2 x _ {1} ^ {2} (t) + 4 x _ {2} ^ {2} (t) + 0. 5 u ^ {2} (t) ] d t.$$
