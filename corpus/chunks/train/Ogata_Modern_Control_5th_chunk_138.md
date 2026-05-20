The operation of the force-balance type controller shown in Figure 4–10 may be summarized as follows: 20-psig air from an air supply flows through an orifice, causing a reduced pressure in the bottom chamber. Air in this chamber escapes to the atmosphere through the nozzle. The flow through the nozzle depends on the gap and the pressure drop across it. An increase in the reference input pressure $P _ { r }$ while the out-, put pressure $P _ { o }$ remains the same, causes the valve stem to move down, decreasing the gap between the nozzle and the flapper diaphragm.This causes the control pressure $P _ { c }$ to increase. Let

$$p _ {e} = P _ {r} - P _ {o} \tag {4-20}$$

If $p _ { e } = 0$ , there is an equilibrium state with the nozzle–flapper distance equal to $\bar { X }$ and the control pressure equal to $\hat { P } _ { c }$ At this equilibrium state,. $P _ { 1 } = \overline { { P } } _ { c } k$ (where $k < 1 )$ and

$$\bar {X} = \alpha \left(\bar {P} _ {c} A _ {1} - \bar {P} _ {c} k A _ {1}\right) \tag {4-21}$$

where a is a constant.

Let us assume that $p _ { e } \neq 0$ and define small variations in the nozzle–flapper distance and control pressure as x and $p _ { c }$ , respectively. Then we obtain the following equation:

$$\bar {X} + x = \alpha \left[ \left(\bar {P} _ {c} + p _ {c}\right) A _ {1} - \left(\bar {P} _ {c} + p _ {c}\right) k A _ {1} - p _ {e} \left(A _ {2} - A _ {1}\right) \right] \tag {4-22}$$

From Equations (4–21) and (4–22), we obtain

$$x = \alpha \left[ p _ {c} (1 - k) A _ {1} - p _ {e} \left(A _ {2} - A _ {1}\right) \right] \tag {4-23}$$

At this point, we must examine the quantity x. In the design of pneumatic controllers, the nozzle–flapper distance is made quite small. In view of the fact that x/a is very much smaller than $p _ { c } ( 1 - k ) A _ { 1 }$ or $p _ { e } ( A _ { 2 } - A _ { 1 } )$ —that is, for $p _ { e } \neq 0$

$$
\begin{array}{l} \frac {x}{\alpha} \ll p _ {c} (1 - k) A _ {1} \\ \frac {x}{\alpha} \ll p _ {e} (A _ {2} - A _ {1}) \\ \end{array}
$$

we may neglect the term x in our analysis. Equation (4–23) can then be rewritten to reflect this assumption as follows:

$$p _ {c} (1 - k) A _ {1} = p _ {e} \left(A _ {2} - A _ {1}\right)$$

and the transfer function between $p _ { c }$ and $p _ { e }$ becomes

$$\frac {P _ {c} (s)}{P _ {e} (s)} = \frac {A _ {2} - A _ {1}}{A _ {1}} \frac {1}{1 - k} = K _ {p}$$
