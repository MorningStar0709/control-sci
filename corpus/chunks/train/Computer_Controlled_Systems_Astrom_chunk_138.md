# Example 2.15 Pole-zero cancellations

Consider the difference equation

$$y (k + 1) + a y (k) = u (k + 1) + a u (k) \tag {2.32}$$

If (2.32) is considered as a dynamical system its pulse-transfer function is obtained as

$$H (z) = \frac {z + a}{z + a} = 1$$

The last equality is obtained because z is a complex variable. We may be thus misled to believe that the system (2.32) is identical to

$$y (k) = u (k) \tag {2.33}$$

This is clearly not true because the difference equation (2.32) has the solution

$$y (k) = (- a) ^ {k} y (0) + u (k) \quad k \geq 1$$

which is identical to (2.33) only if the initial condition $y(0)$ is zero. It may be reasonable to neglect the initial conditions if $|a| < 1$ , but not reasonable if $|a| \geq 1$ . We thus have the situation that from a system-theoretic point of view, the expression

$$\frac {z + a}{z + \hat {a}}$$

can be considered equal to one if $|a| < 1$ but not otherwise. If equation (2.32) is solved using shift-operator calculus we obtain formally

$$(q + a) y (k) = (q + a) u (k)$$

Notice that we cannot divide by $q + a$ because $q$ is an operator.

The conclusion that we can draw from the simple example is that the algebras of z-transforms and shift operators are different. In z-transforms calculus we can divide with an arbitrary expression, but this is not allowed in shift-operator calculus. The system-theoretic interpretation is that we may throw away some modes in the system with z-transform calculus by cancellation factors. This may make sense if the canceled factors correspond to stable modes, but it may be strongly misleading if the canceled factors are unstable. Another manifestation of this effect will be given in the discussions of the notions of observability and controllability in Chapter 3.
