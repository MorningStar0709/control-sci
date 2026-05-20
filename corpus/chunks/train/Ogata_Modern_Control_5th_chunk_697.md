$$s X _ {1} (s) = - p _ {1} X _ {1} (s) + X _ {2} (s)s X _ {2} (s) = - p _ {1} X _ {2} (s) + X _ {3} (s)s X _ {3} (s) = - p _ {1} X _ {3} (s) + U (s)s X _ {4} (s) = - p _ {4} X _ {4} (s) + U (s)s X _ {n} (s) = - p _ {n} X _ {n} (s) + U (s)$$

The inverse Laplace transforms of the preceding n equations give

$$\dot {x} _ {1} = - p _ {1} x _ {1} + x _ {2}\dot {x} _ {2} = - p _ {1} x _ {2} + x _ {3}\dot {x} _ {3} = - p _ {1} x _ {3} + u\dot {x} _ {4} = - p _ {4} x _ {4} + u\dot {x} _ {n} = - p _ {n} x _ {n} + u$$

The output equation, Equation (9–92), can be rewritten as

$$Y (s) = b _ {0} U (s) + c _ {1} X _ {1} (s) + c _ {2} X _ {2} (s) + c _ {3} X _ {3} (s) + c _ {4} X _ {4} (s) + \dots + c _ {n} X _ {n} (s)$$

The inverse Laplace transform of this output equation is

$$y = c _ {1} x _ {1} + c _ {2} x _ {2} + c _ {3} x _ {3} + c _ {4} x _ {4} + \dots + c _ {n} x _ {n} + b _ {0} u$$

Thus, the state-space representation of the system for the case when the denominator polynomial involves a triple root $- { p } _ { 1 }$ can be given as follows:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \\ \dot {x} _ {4} \\ \cdot \\ \cdot \\ \cdot \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c c c} - p _ {1} & 1 & 0 & 0 & \dots & 0 \\ 0 & - p _ {1} & 1 & \cdot & & \cdot \\ 0 & 0 & - p _ {1} & 0 & \dots & 0 \\ \hline 0 & \dots & 0 & - p _ {4} & & \\ \cdot & & \cdot & & \cdot & \\ \cdot & & \cdot & & \cdot & \\ \cdot & & \cdot & & & \cdot \\ 0 & \dots & 0 & 0 & & - p _ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 1 \\ 1 \\ \cdot \\ \cdot \\ \cdot \\ 1 \end{array} \right] u \tag {9-93}

y = \left[ \begin{array}{l l l l} c _ {1} & c _ {2} & \dots & c _ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + b _ {0} u \tag {9-94}
$$

The state-space representation in the form given by Equations (9–93) and (9–94) is said to be in the Jordan canonical form. Figure 9–4 shows a block diagram representation of the system given by Equations (9–93) and (9–94).

A–9–5. Consider the transfer-function system

$$\frac {Y (s)}{U (s)} = \frac {2 5 . 0 4 s + 5 . 0 0 8}{s ^ {3} + 5 . 0 3 2 4 7 s ^ {2} + 2 5 . 1 0 2 6 s + 5 . 0 0 8}$$

Obtain a state-space representation of this system with MATLAB.

Figure 9–4 Block diagram representation of the system defined by Equations (9–93) and (9–94) (Jordan canonical form).   
![](image/e532dd27eae6886096fa4628bbcd1c34ea28b23409ad6605de411469fb055762.jpg)

<details>
<summary>flowchart</summary>
