# 2.9 Problems

Similarly, show that, in general, for extremization of

$$J = \int_ {t _ {0}} ^ {t _ {f}} V (x (t), \dot {x} (t), \ddot {x} (t), \dots , x ^ {(r)} (t), t) d t$$

with fixed-end point conditions, the Euler-Lagrange equation becomes

$$\sum_ {i = 0} ^ {r} (- 1) ^ {i} \frac {d ^ {i}}{d t ^ {i}} \left(\frac {\partial V}{\partial x ^ {(i)}}\right) = 0.$$

Problem 2.5 A first order system is given by

$$\dot {x} (t) = a x (t) + b u (t)$$

and the performance index is

$$J = \frac {1}{2} \int_ {0} ^ {t _ {f}} (q x ^ {2} (t) + r u ^ {2} (t)) d t$$

where, $x(t_0) = x_0$ and $x(t_f)$ is free and $t_f$ being fixed. Show that the optimal state $x^*(t)$ is given by

$$x ^ {*} (t) = x _ {0} \frac {\sinh \beta \left(t _ {f} - t\right)}{\sinh \beta t _ {f}}, \quad \beta = \sqrt {a ^ {2} + b ^ {2} q / r}.$$

Problem 2.6 A mechanical system is described by

$$\ddot {x} (t) = u (t)$$

find the optimal control and the states by minimizing

$$J = \frac {1}{2} \int_ {0} ^ {5} u ^ {2} (t) d t$$

such that the boundary conditions are

$$x (t = 0) = 2; \quad x (t = 5) = 0; \quad \dot {x} (t = 0) = 2; \quad \dot {x} (t = 5) = 0.$$

Problem 2.7 For the first order system

$$\frac {d x}{d t} = - x (t) + u (t)$$

find the optimal control $u^{*}(t)$ to minimize

$$J = \int_ {0} ^ {t _ {f}} [ x ^ {2} (t) + u ^ {2} (t) ] d t$$

where, $t_f$ is unspecified, and $x(0) = 5$ and $x(t_f) = 0$ . Also find $t_f$ .

Problem 2.8 Find the optimal control $u^{*}(t)$ of the plant

$$\dot {x} _ {1} (t) = x _ {2} (t); \quad x _ {1} (0) = 3, \quad x _ {1} (2) = 0\dot {x} _ {2} (t) = - 2 x _ {1} (t) + 5 u (t); \quad x _ {2} (0) = 5, \quad x _ {2} (2) = 0$$

which minimizes the performance index

$$J = \frac {1}{2} \int_ {0} ^ {2} \left[ x _ {1} ^ {2} (t) + u ^ {2} (t) \right] d t.$$

Problem 2.9 A second order plant is described by

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = - 2 x _ {1} (t) - 3 x _ {2} (t) + 5 u (t)$$

and the cost function is

$$J = \int_ {0} ^ {\infty} [ x _ {1} ^ {2} (t) + u ^ {2} (t) ] d t.$$

Find the optimal control, when $x_{1}(0) = 3$ and $x_{2}(0) = 2$ .

Problem 2.10 For a second order system

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = - 2 x _ {1} (t) + 3 u (t)$$

with performance index

$$J = 0. 5 x _ {1} ^ {2} (\pi / 2) + \int_ {0} ^ {\pi / 2} 0. 5 u ^ {2} (t) d t$$

and boundary conditions $\mathbf{x}(0) = [0\quad 1]'$ and $\mathbf{x}(t_f)$ is free, find the optimal control.

Problem 2.11 Find the optimal control for the plant

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = - 2 x _ {1} (t) + 3 u (t)$$

with performance criterion

$$J = \frac {1}{2} F _ {1 1} \left[ x _ {1} \left(t _ {f}\right) - 4 \right] ^ {2} + \frac {1}{2} F _ {2 2} \left[ x _ {2} \left(t _ {f}\right) - 2 \right] ^ {2}+ \frac {1}{2} \int_ {0} ^ {t _ {f}} \left[ x _ {1} ^ {2} (t) + 2 x _ {2} ^ {2} (t) + 4 u ^ {2} (t) \right] d t$$

and initial conditions as $\mathbf{x}(0) = [1\quad 2]'$ . The additional conditions are given below.
