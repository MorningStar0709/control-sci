$$
\frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} = \left[ \begin{array}{l l l l l} 0 & 0 & - \frac {v _ {l} + v _ {r}}{2} \sin \theta & \frac {1}{2} \cos \theta & \frac {1}{2} \cos \theta \\ 0 & 0 & \frac {v _ {l} + v _ {r}}{2} \cos \theta & \frac {1}{2} \sin \theta & \frac {1}{2} \sin \theta \\ 0 & 0 & 0 & - \frac {1}{2 r _ {b}} & \frac {1}{2 r _ {b}} \\ 0 & 0 & 0 & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \\ 0 & 0 & 0 & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \end{array} \right]

\frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {u}} = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ 0 & 0 \\ \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \end{array} \right]
$$

Therefore,

Theorem 8.7.3 — Linear time-varying differential drive state-space model.

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}
\mathbf {x} = \left[ \begin{array}{c} x \\ y \\ \theta \\ v _ {l} \\ v _ {r} \end{array} \right] = \left[ \begin{array}{c} \text {x position} \\ \text {y position} \\ \text {heading} \\ \text {left velocity} \\ \text {right velocity} \end{array} \right] \quad \mathbf {u} = \left[ \begin{array}{c} V _ {l} \\ V _ {r} \end{array} \right] = \left[ \begin{array}{c} \text {left voltage} \\ \text {right voltage} \end{array} \right]

\mathbf {A} = \left[ \begin{array}{c c c c c} 0 & 0 & - v s & \frac {1}{2} c & \frac {1}{2} c \\ 0 & 0 & v c & \frac {1}{2} s & \frac {1}{2} s \\ 0 & 0 & 0 & - \frac {1}{2 r _ {b}} & \frac {1}{2 r _ {b}} \\ 0 & 0 & 0 & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \\ 0 & 0 & 0 & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \end{array} \right] \tag {8.13}

\mathbf {B} = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ 0 & 0 \\ \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \end{array} \right] \tag {8.14}
$$
