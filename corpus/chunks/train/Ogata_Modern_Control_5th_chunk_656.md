$$[ \text { NUM,den } ] = \text { ss2tf(A,B,C,D,iu) }$$

produces transfer functions for all outputs to each input. (The numerator coefficients are returned to matrix NUM with as many rows as there are outputs.)

Consider the system defined by

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 5 & - 4 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] \\ \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] \\ \end{array}
$$

This system involves two inputs and two outputs. Four transfer functions are involved: $Y _ { 1 } ( s ) / U _ { 1 } ( s )$ , $Y _ { 2 } ( s ) \dot { / } U _ { 1 } ( s ) , Y _ { 1 } ( s ) / U _ { 2 } ( s )$ and, $Y _ { 2 } ( s ) / U _ { 2 } ( s )$ (When considering input. $u _ { 1 }$ , we assume that input $u _ { 2 }$ is zero and vice versa.) See the output of MATLAB Program 9–3.
