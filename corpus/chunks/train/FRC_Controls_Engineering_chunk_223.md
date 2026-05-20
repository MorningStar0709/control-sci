# 8.3 Lyapunov stability

Lyapunov stability is a fundamental concept in nonlinear control, so we’re going to give a brief overview of what it is so students can research it further.

Since the state evolution in nonlinear systems is defined by a function rather than a constant matrix, the system’s poles as determined by linearization move around. Nonlinear control uses Lyapunov stability to determine if nonlinear systems are stable. From a linear control theory point of view, Lyapunov stability says the system is stable if, for a given initial condition, all possible eigenvalues of A from that point on remain in the left-half plane. However, nonlinear control uses a different definition.

Lyapunov stability means that the system trajectory can be kept arbitrarily close to the origin by starting sufficiently close to it. Lyapunov’s direct method uses a function consisting of the energy in a system or derivatives of the system’s state to prove stability around an equilibrium point. This is done by showing that the function, and thus its inputs, decay to some ground state. More rigorously, the value function $V ( \mathbf { x } )$ must be positive definite and equal zero at the equilibrium point

$$V (\mathbf {x}) > 0V (\mathbf {0}) = 0$$

and its derivative $\dot { V } ( \mathbf { x } )$ must be negative definite.

$$\dot {V} (\mathbf {x}) = \frac {d V}{d t} = \frac {\partial V}{\partial \mathbf {x}} \frac {d \mathbf {x}}{d t} \leq 0$$

More than one Lyapunov function can prove stability, and if one function doesn’t prove it, another candidate should be tried. For this reason, we refer to these functions as Lyapunov candidate functions.
