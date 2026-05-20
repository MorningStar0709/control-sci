$$
\begin{array}{l} \dot {x} _ {3} = \ddot {y} - \beta_ {0} \ddot {u} - \beta_ {1} \ddot {u} - \beta_ {2} \dot {u} \\ = \left(- a _ {1} \ddot {y} - a _ {2} \dot {y} - a _ {3} y\right) + b _ {0} \dddot {u} + b _ {1} \ddot {u} + b _ {2} \dot {u} + b _ {3} u - \beta_ {0} \dddot {u} - \beta_ {1} \ddot {u} - \beta_ {2} \dot {u} \\ = - a _ {1} \left(\ddot {y} - \beta_ {0} \ddot {u} - \beta_ {1} \dot {u} - \beta_ {2} u\right) - a _ {1} \beta_ {0} \ddot {u} - a _ {1} \beta_ {1} \dot {u} - a _ {1} \beta_ {2} u \\ - a _ {2} \left(\dot {y} - \beta_ {0} \dot {u} - \beta_ {1} u\right) - a _ {2} \beta_ {0} \dot {u} - a _ {2} \beta_ {1} u - a _ {3} \left(y - \beta_ {0} u\right) - a _ {3} \beta_ {0} u \\ + b _ {0} \ddot {u} + b _ {1} \dot {u} + b _ {2} \dot {u} + b _ {3} u - \beta_ {0} \ddot {u} - \beta_ {1} \dot {u} - \beta_ {2} \dot {u} \\ = - a _ {1} x _ {3} - a _ {2} x _ {2} - a _ {3} x _ {1} + \left(b _ {0} - \beta_ {0}\right) \ddot {u} + \left(b _ {1} - \beta_ {1} - a _ {1} \beta_ {0}\right) \ddot {u} \\ + \left(b _ {2} - \beta_ {2} - a _ {1} \beta_ {1} - a _ {2} \beta_ {0}\right) \dot {u} + \left(b _ {3} - a _ {1} \beta_ {2} - a _ {2} \beta_ {1} - a _ {3} \beta_ {0}\right) u \\ = - a _ {1} x _ {3} - a _ {2} x _ {2} - a _ {3} x _ {1} + \left(b _ {3} - a _ {1} \beta_ {2} - a _ {2} \beta_ {1} - a _ {3} \beta_ {0}\right) u \\ = - a _ {1} x _ {3} - a _ {2} x _ {2} - a _ {3} x _ {1} + \beta_ {3} u \\ \end{array}
$$

Hence, we get

$$\dot {x} _ {3} = - a _ {3} x _ {1} - a _ {2} x _ {2} - a _ {1} x _ {3} + \beta_ {3} u \tag {2-63}$$

Combining Equations (2–61), (2–62), and (2–63) into a vector-matrix equation, we obtain Equation (2–59). Also, from the definition of state variable $x _ { 1 }$ , we get the output equation given by Equation (2–60).

A–2–7. Obtain a state-space equation and output equation for the system defined by

$$\frac {Y (s)}{U (s)} = \frac {2 s ^ {3} + s ^ {2} + s + 2}{s ^ {3} + 4 s ^ {2} + 5 s + 2}$$

Solution. From the given transfer function, the differential equation for the system is

$$\ddot {y} + 4 \dot {y} + 5 \dot {y} + 2 y = 2 \ddot {u} + \dot {u} + \dot {u} + 2 u$$

Comparing this equation with the standard equation given by Equation (2–33), rewritten

$$\ddot {y} + a _ {1} \dot {y} + a _ {2} \dot {y} + a _ {3} y = b _ {0} \ddot {u} + b _ {1} \ddot {u} + b _ {2} \dot {u} + b _ {3} u$$

we find

$$a _ {1} = 4, \quad a _ {2} = 5, \quad a _ {3} = 2b _ {0} = 2, \qquad b _ {1} = 1, \qquad b _ {2} = 1, \qquad b _ {3} = 2$$

Referring to Equation (2–35), we have
