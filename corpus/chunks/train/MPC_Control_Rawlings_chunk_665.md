$$
\begin{array}{l} \ell_ {1} \left(x _ {1}, u _ {1}\right) = (1 / 2) \left(y _ {1} ^ {\prime} \overline {{{Q}}} _ {1} y _ {1} + u _ {1} ^ {\prime} R _ {1} u _ {1}\right) \\ \ell_ {1} (x _ {1}, u _ {1}) = (1 / 2) (x _ {1} ^ {\prime} Q _ {1} x _ {1} + u _ {1} ^ {\prime} R _ {1} u _ {1}) \\ \end{array}
$$

in which

$$
Q _ {1} = C _ {1} ^ {\prime} \overline {{{{Q}}}} _ {1} C _ {1} \quad C _ {1} = \left[ \begin{array}{c c} C _ {1 1} & C _ {1 2} \end{array} \right]
$$

Motivated by the warm start to be described later, for stable systems, we choose the terminal penalty to be the infinite horizon cost to go under zero control

$$V _ {1 f} (x _ {1} (N)) = (1 / 2) x _ {1} ^ {\prime} (N) P _ {1 f} x _ {1} (N)$$

We choose $P _ { 1 f }$ as the solution to the following Lyapunov equation assuming $A _ { 1 }$ is stable

$$A _ {1} ^ {\prime} P _ {1 f} A _ {1} - P _ {1 f} = - Q _ {1} \tag {6.8}$$

We proceed analogously to define player two’s local objective function and penalties

$$V _ {2} \left(x _ {2} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}\right) = \sum_ {k = 0} ^ {N - 1} \ell_ {2} \left(x _ {2} (k), u _ {2} (k)\right) + V _ {2 f} \left(x _ {2} (N)\right)$$

In centralized control and the cooperative game, the two players share a common objective, which can be considered to be the overall plant objective

$$V (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}) = \rho_ {1} V _ {1} (x _ {1} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}) + \rho_ {2} V _ {2} (x _ {2} (0), \mathbf {u} _ {2}, \mathbf {u} _ {1})$$

in which the parameters $\rho _ { 1 } , \rho _ { 2 }$ are used to specify the relative weights of the two subsystems in the overall plant objective. Their values are restricted so $\rho _ { 1 } , \rho _ { 2 } > 0 , \rho _ { 1 } + \rho _ { 2 } = 1$ so that both local objectives must have some nonzero effect on the overall plant objective.
