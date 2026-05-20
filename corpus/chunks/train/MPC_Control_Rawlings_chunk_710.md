$$
\begin{array}{l} \left[ \begin{array}{c c c c} I - A _ {1} & & - \overline {{B}} _ {1 1} & - \overline {{B}} _ {1 2} \\ & I - A _ {2} & - \overline {{B}} _ {2 1} & - \overline {{B}} _ {2 2} \end{array} \right] \left[ \begin{array}{c} x _ {1 s} \\ x _ {2 s} \\ u _ {1 s} \\ u _ {2 s} \end{array} \right] = \left[ \begin{array}{c} B _ {d 1} \hat {d} _ {1} (k) \\ B _ {d 2} \hat {d} _ {2} (k) \end{array} \right] \\ E _ {1} u _ {1 s} \leq e _ {1} \tag {6.28} \\ \end{array}
$$

The equality constraints for the two players appear coupled when written in this form. Coupled constraints admit the potential for the optimization to become stuck on the boundary of the feasible region, and not achieve the centralized target solution after iteration to convergence. But Exercise 6.30 discusses how to show that the equality constraints are, in fact, uncoupled. Also, the distributed target problem as expressed here may not have a unique solution when there are more manipulated variables than controlled variables. In such cases, a regularization term using the input setpoint can be added to the objective function. The controlled variable penalty can be converted to a linear penalty with a large penalty weight to ensure exact satisfaction of the controlled variable setpoint.

If the input inequality constraints are coupled, however, then the distributed target problem may indeed become stuck on the boundary of the feasible region and not eliminate offset in the controlled variables. If the input inequality constraints are coupled, we recommend using the centralized approach to computing the steady-state target. As discussed above, the centralized target problem eliminates offset in the controlled variables as long as it remains feasible given the disturbance estimates.

Zero offset. Finally we establish the zero offset property. As described in Chapter 1, the regulator is posed in deviation variables

$$\tilde {x} (k) = \hat {x} (k) - x _ {s} (k) \quad \tilde {u} (k) = u (k) - u _ {s} (k) \quad \tilde {\mathbf {u}} = \mathbf {u} - u _ {s} (k)$$

in which the notation ${ \bf u } - u _ { s } ( k )$ means to subtract $u _ { s } ( k )$ from each element of the u sequence. Player one then solves
