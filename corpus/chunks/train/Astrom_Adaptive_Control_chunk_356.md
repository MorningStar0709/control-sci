Notice that the state variables $\xi$ represents a chain of r integrators, where the integer r is the nonlinear equivalence of pole excess. The variables $\eta$ will not appear if r = n. This case corresponds to a system without zeros. This actually occurs in Example 5.15, where r = n = 2.

A design procedure, which is the nonlinear analog of pole placement, can be constructed if $\beta(\xi,\eta)\neq0$ . If this is the case, we can introduce the feedback law

$$u = \frac {1}{\beta (\xi , \eta)} \left(- a _ {r} \xi_ {1} - a _ {r - 1} \xi_ {2} - \dots - a _ {1} \xi_ {r} - \alpha (\xi , \eta) + b _ {0} v\right)$$

The closed-loop system then becomes

$$
\frac {d \xi}{d t} = \left( \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & \\ \vdots & & & & \\ - a _ {r} & - a _ {r - 1} & - a _ {r - 2} & \dots & - a _ {1} \end{array} \right) \xi + \left( \begin{array}{c} 0 \\ 0 \\ \vdots \\ b _ {0} \end{array} \right) v \tag {5.86}
\frac {d \eta}{d t} = \gamma (\xi , \eta)
$$

The relation between $v$ and $\xi_1$ is given by a linear dynamical system with the transfer function

$$\frac {\Xi_ {1} (s)}{V (s)} = G (s) = \frac {b _ {0}}{s ^ {r} + a _ {1} s ^ {r - 1} + \dots a _ {r}}$$

This differential equation has a triangular structure. The part corresponding to the state vector $\xi$ is a linear system that is decoupled from the variable $\eta$ . If $\xi = 0$ , the behavior of the system (5.86) is governed by

$$\frac {d \eta}{d t} = \gamma (0, \eta) \tag {5.87}$$

This equation represents the zero dynamics. It is necessary for this system to be stable if the proposed control design is going to work. For linear systems the zero dynamics are the dynamics associated with the zeros of the transfer function. Feedback linearization is the nonlinear analog of pole placement with cancellation of all process zeros.
