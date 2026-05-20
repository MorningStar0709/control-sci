We can then solve the linear algebra problem

$$
\left[ \begin{array}{c c} H & - D ^ {\prime} \\ - D & 0 \end{array} \right] \left[ \begin{array}{c} r _ {s} \\ \lambda_ {s} \end{array} \right] = - \left[ \begin{array}{c} h \\ d \end{array} \right]
$$

and identify the linear gains between the optimal $u _ { 1 s }$ and the setpoint $y _ { \mathrm { s p } }$ and player two’s input $u _ { 2 s }$

$$u _ {1 s} ^ {0} = K _ {1 s} y _ {\mathrm{sp}} + L _ {1 s} u _ {2 s} ^ {p}$$

Combining the optimal control laws for each player gives

$$
\left[ \begin{array}{c} u _ {1 s} ^ {0} \\ u _ {2 s} ^ {0} \end{array} \right] = \left[ \begin{array}{c} K _ {1 s} \\ K _ {2 s} \end{array} \right] y _ {\text {sp}} + \left[ \begin{array}{c c} 0 & L _ {1 s} \\ L _ {2 s} & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1 s} \\ u _ {2 s} \end{array} \right] ^ {p}
$$

Substituting the optimal control into the iteration gives

$$
\left[ \begin{array}{c} u _ {1 s} \\ u _ {2 s} \end{array} \right] ^ {p + 1} = \underbrace {\left[ \begin{array}{c} w _ {1} K _ {1 s} \\ w _ {2} K _ {2 s} \end{array} \right]} _ {\overline {{K}} _ {s}} y _ {\mathrm{sp}} + \underbrace {\left[ \begin{array}{c c} (1 - w _ {1}) I & w _ {1} L _ {1 s} \\ w _ {2} L _ {2 s} & (1 - w _ {2}) I \end{array} \right]} _ {L _ {s}} \left[ \begin{array}{c} u _ {1 s} \\ u _ {2 s} \end{array} \right] ^ {p}
$$

Finally writing this equation in the plantwide notation, we express the iteration as

$$u _ {s} ^ {p + 1} = \overline {{K}} _ {s} y _ {\mathrm{sp}} + L _ {s} u _ {s} ^ {p}$$

As we did with the cooperative regulation problem, we can analyze the optimization problem to show that this iteration is always stable and converges to the centralized target. Next we explore the use of these approaches in some illustrative examples.
