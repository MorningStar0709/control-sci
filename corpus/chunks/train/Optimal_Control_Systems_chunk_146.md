# 2.9 Problems

1. Make reasonable assumptions wherever necessary.

2. Use MATLAB $^{©}$ wherever possible to solve the problems and plot all the optimal controls and states for all problems. Provide the relevant MATLAB $^{©}$ m files.

Problem 2.1 Find the extremal of the following functional

$$J = \int_ {0} ^ {2} [ 2 x ^ {2} (t) + \dot {x} ^ {2} (t) ] d t$$

with the initial condition as $x(0) = 0$ and the final condition as $x(2) = 5$ .

Problem 2.2 Find the extremal of the functional

$$J = \int_ {- 2} ^ {0} \left[ 1 2 t x (t) + \dot {x} ^ {2} (t) \right] d t$$

to satisfy the boundary conditions $x(-2) = 3$ , and $x(0) = 0$ .

Problem 2.3 Find the extremal for the following functional

$$J = \int_ {1} ^ {2} \frac {\dot {x} ^ {2} (t)}{2 t ^ {3}} d t$$

with $x(1) = 1$ and $x(2) = 10$ .

Problem 2.4 Consider the extremization of a functional which is dependent on derivatives higher than the first derivative $\dot{x}(t)$ such as

$$J (x (t), t) = \int_ {t _ {0}} ^ {t _ {f}} V (x (t), \dot {x} (t), \ddot {x} (t), t) d t.$$

with fixed-end point conditions. Show that the corresponding Euler-Lagrange equation is given by

$$\frac {\partial V}{\partial x} - \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {x}}\right) + \frac {d ^ {2}}{d t ^ {2}} \left(\frac {\partial V}{\partial \ddot {x}}\right) = 0.$$
