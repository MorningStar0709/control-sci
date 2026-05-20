# Exercise 5.16 (Nonlinear system)

Given the optimal control problem for a scalar nonlinear system:

$$u ^ {*} := \underset {u: [ 0, 1 ] \rightarrow \mathbb {R}} {\operatorname{argmin}} J (u) := \int_ {0} ^ {1} [ x (t) u (t) ] ^ {2} d t \tag {358}$$

subject to (359)

$$\dot {x} (t) = x (t) u (t), \quad t \in [ 0, 1 ] \tag {360}x (0) = 1 \tag {361}$$

Obtain the optimal feedback solution by solving the associated HJB equation.

Hint: First show that the HJB partial differential equation admits a solution that is quadratic in x.
