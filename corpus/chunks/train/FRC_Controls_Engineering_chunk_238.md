$$
\begin{array}{l} \left[ \begin{array}{c} \dot {v _ {l}} \\ v _ {r} \end{array} \right] = \left[ \begin{array}{c c} \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \end{array} \right] \left[ \begin{array}{c} v _ {l} \\ v _ {r} \end{array} \right] \\ + \left[ \begin{array}{c c} \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \end{array} \right] \left[ \begin{array}{c} V _ {l} \\ V _ {r} \end{array} \right] \\ \end{array}
$$

Theorem 8.7.1 — Differential drive velocity state-space model.

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}
\mathbf {x} = \left[ \begin{array}{c} v _ {l} \\ v _ {r} \end{array} \right] = \left[ \begin{array}{c} \text { left   velocity } \\ \text { right   velocity } \end{array} \right] \quad \mathbf {u} = \left[ \begin{array}{c} V _ {l} \\ V _ {r} \end{array} \right] = \left[ \begin{array}{c} \text { left   voltage } \\ \text { right   voltage } \end{array} \right]

\mathbf {A} = \left[ \begin{array}{l l} \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \end{array} \right] \tag {8.8}

\mathbf {B} = \left[ \begin{array}{l l} \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \end{array} \right] \tag {8.9}
$$

$\begin{array} { r } { \mathrm { w h e r e } \ C _ { 1 } = - \frac { G _ { l } ^ { 2 } K _ { t } } { K _ { v } R r ^ { 2 } } , C _ { 2 } = \frac { G _ { l } K _ { t } } { R r } , C _ { 3 } = - \frac { G _ { r } ^ { 2 } K _ { t } } { K _ { v } R r ^ { 2 } } , \mathrm { a n d } \ C _ { 4 } = \frac { G _ { r } K _ { t } } { R r } . } \end{array}$
