# 2.2 Model Predictive Control

As discussed briefly in Chapter 1, most nonlinear system descriptions derived from physical arguments are continuous time descriptions in the form of nonlinear differential equations

$$\frac {d x}{d t} = f (x, u)$$

For this class of systems, the control law with arguably the best closedloop properties is the solution to the following infinite horizon, constrained optimal control problem. The cost is defined to be

$$V _ {\infty} (x, u (\cdot)) = \int_ {0} ^ {\infty} \ell (x (t), u (t)) d t$$

in which $x ( t )$ and $u ( t )$ satisfy $\dot { x } = f ( x , u )$ . The optimal control problem $\mathbb { P } ( x )$ is defined by

$$\min _ {u (\cdot)} V _ {\infty} (x, u (\cdot))$$

subject to:

$$\dot {x} = f (x, u) \quad x (0) = x _ {0}u (t) \in \mathbb {U} \quad x (t) \in \mathbb {X} \quad \text { for all } t \in (0, \infty)$$

If $\ell ( \cdot )$ is positive definite, the goal of the regulator is to steer the state of the system to the origin.

We denote the solution to this problem (when it exists) and the optimal value function by

$$V _ {\infty} ^ {0} (x) \qquad u _ {\infty} ^ {0} (\cdot ; x)$$

The closed-loop system under this optimal control law evolves as

$$\frac {d x (t)}{d t} = f (x (t), u _ {\infty} ^ {0} (t; x))$$

We can demonstrate that the origin is an asymptotically stable solution for the closed-loop system as follows. If $f ( \cdot )$ and $\ell ( \cdot )$ satisfy certain differentiability and growth assumptions and there are no state constraints, then a solution to $\mathbb { P } ( x )$ exists for all $x ; V _ { \infty } ^ { 0 } ( \cdot )$ is differentiable and satisfies

$$\dot {V} _ {\infty} ^ {0} (x) = - \ell (x, u _ {\infty} ^ {0} (0; x))$$

Using this and upper and lower bounds on $V _ { \infty } ^ { 0 } ( \cdot )$ enables global asymptotic stability of the origin to be established.

Although the control law $u _ { \infty } ^ { 0 } ( 0 ; \cdot )$ provides excellent closed-loop properties, there are several impediments to its use. A feedback, rather than an open-loop, control is usually necessary because of uncertainty. Solution of the optimal control problem $\mathbb { P } ( x )$ yields the optimal control $u _ { \infty } ^ { 0 } ( 0 ; x )$ for the state x but does not provide a control law. Dynamic programming may, in principle, be employed, but is generally impractical if the state dimension and the horizon are not small.
