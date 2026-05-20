$$\frac {d \mathbf {x} (t)}{d t} = A \mathbf {x} (t) + B \mathbf {u} (t). \tag {4.120}$$

The model of the target maneuver and the system states $y _ { d } , y _ { d } , a _ { T }$ can be written in the usual state-space notation

$$
\left[ \begin{array}{l} \dot {y} _ {d} \\ \ddot {y} _ {d} \\ \dot {a} _ {T} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & - 2 v \end{array} \right] \left[ \begin{array}{l} y _ {d} \\ \dot {y} _ {d} \\ a _ {T} \end{array} \right] + \left[ \begin{array}{c} 0 \\ - 1 \\ 0 \end{array} \right] u _ {c} + \left[ \begin{array}{c} 0 \\ 0 \\ 2 v w \end{array} \right], \tag {4.153}
$$

where $w$ is a white process noise, and $u _ { c }$ is the corrective missile acceleration. Equation (4.145) corresponds to (4.121) of Section 4.8.3 with

$$
S = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right], Q = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right], R = \gamma ,
$$

while in (4.120) of Section 4.8.3,

$$
B = \left[ \begin{array}{c} 0 \\ - 1 \\ 0 \end{array} \right], u _ {c} = \frac {d ^ {2} y _ {M}}{d t ^ {2}}.
$$

From the foregoing equations, the solution for the three control gains is given by [31]

$$C _ {1} = 3 (t _ {i} - t) / [ 3 \gamma + (t _ {i} - t) ^ {3} ], \tag {4.154a}C _ {2} = (t _ {i} - t) C _ {1}, \tag {4.154b}C _ {3} = (3 \left(t _ {i} - t\right) / 4 v ^ {2}) \left\{\left[ \exp (- 2 v \left(t _ {i} - t\right)) + 2 v \left(t _ {i} - t\right) - 1 \right] / \left(3 \gamma + \left(t _ {i} - t\right) ^ {3}\right) \right\}. \tag {4.154c}$$

The missile corrective acceleration normal to the LOS is

$$\frac {d ^ {2} Y _ {d}}{d t ^ {2}} = u _ {c} = C _ {1} y _ {d} + C _ {2} \dot {y} _ {d} + C _ {3} a _ {T}. \tag {4.155}$$

Inserting the C-values, making use of

$$\frac {d \lambda}{d t} = 1 / v _ {c} t _ {g o} ^ {2},$$

we have

$$\frac {d ^ {2} y _ {M}}{d t ^ {2}} = N ^ {\prime} v _ {c} \left(\frac {d \lambda}{d t}\right) + N ^ {\prime} \left\{\left[ \exp \left(- 2 v t _ {g o}\right) + 2 v t _ {g o} - 1 \right] / 4 v ^ {2} t _ {g o} ^ {2} \right\} a _ {T}, \tag {4.156}$$

where $t _ { g o } = t _ { i } - t$ and the effective navigation ratio $N ^ { \prime }$ is

$$N ^ {\prime} = 3 t _ {g o} ^ {3} / (3 \gamma + t _ {g o} ^ {3}). \tag {4.157}$$
