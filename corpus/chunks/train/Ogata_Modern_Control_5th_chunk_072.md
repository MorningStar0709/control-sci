# A–2–6. Show that for the differential equation system

$$\ddot {y} + a _ {1} \dot {y} + a _ {2} \dot {y} + a _ {3} y = b _ {0} \ddot {u} + b _ {1} \dot {u} + b _ {2} \dot {u} + b _ {3} u \tag {2-58}$$

state and output equations can be given, respectively, by

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{l} \beta_ {1} \\ \beta_ {2} \\ \beta_ {3} \end{array} \right] u \tag {2-59}
$$

and

$$
y = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \beta_ {0} u \tag {2-60}
$$

where state variables are defined by

$$x _ {1} = y - \beta_ {0} ux _ {2} = \dot {y} - \beta_ {0} \dot {u} - \beta_ {1} u = \dot {x} _ {1} - \beta_ {1} ux _ {3} = \ddot {y} - \beta_ {0} \dot {u} - \beta_ {1} \dot {u} - \beta_ {2} u = \dot {x} _ {2} - \beta_ {2} u$$

and

$$\beta_ {0} = b _ {0}\beta_ {1} = b _ {1} - a _ {1} \beta_ {0}\beta_ {2} = b _ {2} - a _ {1} \beta_ {1} - a _ {2} \beta_ {0}\beta_ {3} = b _ {3} - a _ {1} \beta_ {2} - a _ {2} \beta_ {1} - a _ {3} \beta_ {0}$$

Solution. From the definition of state variables $x _ { 2 }$ and $x _ { 3 } ,$ , we have

$$\dot {x} _ {1} = x _ {2} + \beta_ {1} u \tag {2-61}\dot {x} _ {2} = x _ {3} + \beta_ {2} u \tag {2-62}$$

To derive the equation for ${ \dot { x } } _ { 3 } .$ we first note from Equation (2–58) that,

$$\ddot {y} = - a _ {1} \dot {y} - a _ {2} \dot {y} - a _ {3} y + b _ {0} \ddot {u} + b _ {1} \dot {u} + b _ {2} \dot {u} + b _ {3} u$$

Since

$$x _ {3} = \ddot {y} - \beta_ {0} \ddot {u} - \beta_ {1} \dot {u} - \beta_ {2} u$$

we have
