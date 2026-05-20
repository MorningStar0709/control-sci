# 6.2.1 Centralized Control

Centralized control requires the solution of the systemwide control problem. It can be stated as

$$\min _ {\mathbf {u} _ {1}, \mathbf {u} _ {2}} V (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2})\text { s . t . } x _ {1} ^ {+} = A _ {1} x _ {1} + \bar {B} _ {1 1} u _ {1} + \bar {B} _ {1 2} u _ {2}x _ {2} ^ {+} = A _ {2} x _ {2} + \overline {{B}} _ {2 2} u _ {2} + \overline {{B}} _ {2 1} u _ {1}$$

in which

$$
A _ {1} = \left[ \begin{array}{c c} A _ {1 1} & 0 \\ 0 & A _ {1 2} \end{array} \right] \quad A _ {2} = \left[ \begin{array}{c c} A _ {2 2} & 0 \\ 0 & A _ {2 1} \end{array} \right]

\overline {{B}} _ {1 1} = \left[ \begin{array}{c} B _ {1 1} \\ 0 \end{array} \right] \quad \overline {{B}} _ {1 2} = \left[ \begin{array}{c} 0 \\ B _ {1 2} \end{array} \right] \quad \overline {{B}} _ {2 1} = \left[ \begin{array}{c} 0 \\ B _ {2 1} \end{array} \right] \quad \overline {{B}} _ {2 2} = \left[ \begin{array}{c} B _ {2 2} \\ 0 \end{array} \right]
$$

This optimal control problem is more complex than all of the distributed cases to follow because the decision variables include both $\mathbf { u } _ { 1 }$ and $\mathbf { u } _ { 2 }$ . Because the performance is optimal, centralized control is a natural benchmark against which to compare the distributed cases: cooperative, noncooperative, and decentralized MPC. The plantwide stage cost and terminal cost can be expressed as quadratic functions of the subsystem states and inputs

$$\ell (x, u) = (1 / 2) \left(x ^ {\prime} Q x + u ^ {\prime} R u\right)V _ {f} (x) = (1 / 2) x ^ {\prime} P _ {f} x$$

in which

$$
x = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] \qquad u = \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] \qquad Q = \left[ \begin{array}{c c} \rho_ {1} Q _ {1} & 0 \\ 0 & \rho_ {2} Q _ {2} \end{array} \right]

R = \left[ \begin{array}{c c} \rho_ {1} R _ {1} & 0 \\ 0 & \rho_ {2} R _ {2} \end{array} \right] \quad P _ {f} = \left[ \begin{array}{c c} \rho_ {1} P _ {1 f} & 0 \\ 0 & \rho_ {2} P _ {2 f} \end{array} \right] \tag {6.9}
$$

and we have the standard MPC problem considered in Chapters 1 and 2

$$\min _ {\mathbf {u}} V (x (0), \mathbf {u})\mathrm{s.t.} x ^ {+} = A x + B u \tag {6.10}$$

in which

$$
A = \left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right] \quad B = \left[ \begin{array}{c c} \overline {{{B}}} _ {1 1} & \overline {{{B}}} _ {1 2} \\ \overline {{{B}}} _ {2 1} & \overline {{{B}}} _ {2 2} \end{array} \right] \tag {6.11}
$$

Given the terminal penalty in (6.8), stability of the closed-loop centralized system is guaranteed for all choices of system models and tuning parameters subject to the usual stabilizability assumption on the system model.
