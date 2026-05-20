$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 5 & - 4 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]

\left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]
$$

This system involves two inputs and two outputs. Four transfer functions are involved: $Y _ { 1 } ( s ) / U _ { 1 } ( s )$ , $Y _ { 2 } ( s ) / U _ { 1 } ( s ) , Y _ { 1 } ( s ) / U _ { 2 } ( s )$ and, $Y _ { 2 } ( s ) / U _ { 2 } ( s )$ (When considering input. $u _ { 1 } .$ , we assume that input $u _ { 2 }$ is zero and vice versa.)

Solution. MATLAB Program 2-5 produces four transfer functions.

This is the MATLAB representation of the following four transfer functions:

$$\frac {Y _ {1} (s)}{U _ {1} (s)} = \frac {s + 4}{s ^ {2} + 4 s + 2 5}, \quad \frac {Y _ {2} (s)}{U _ {1} (s)} = \frac {- 2 5}{s ^ {2} + 4 s + 2 5}\frac {Y _ {1} (s)}{U _ {2} (s)} = \frac {s + 5}{s ^ {2} + 4 s + 2 5}, \quad \frac {Y _ {2} (s)}{U _ {2} (s)} = \frac {s - 2 5}{s ^ {2} + 4 s + 2 5}$$

<table><tr><td colspan="4">MATLAB Program 2-5</td></tr><tr><td colspan="4">A = [0 1;-25 -4];</td></tr><tr><td colspan="4">B = [1 1;0 1];</td></tr><tr><td colspan="4">C = [1 0;0 1];</td></tr><tr><td colspan="4">D = [0 0;0 0];</td></tr><tr><td colspan="4">[NUM,den] = ss2tf(A,B,C,D,1)</td></tr><tr><td colspan="4">NUM =</td></tr><tr><td></td><td>0</td><td>1</td><td>4</td></tr><tr><td></td><td>0</td><td>0</td><td>-25</td></tr><tr><td colspan="4">den =</td></tr><tr><td></td><td>1</td><td>4</td><td>25</td></tr><tr><td colspan="4">[NUM,den] = ss2tf(A,B,C,D,2)</td></tr><tr><td colspan="4">NUM =</td></tr><tr><td></td><td>0</td><td>1.0000</td><td>5.0000</td></tr><tr><td></td><td>0</td><td>1.0000</td><td>-25.0000</td></tr><tr><td colspan="4">den =</td></tr><tr><td></td><td>1</td><td>4</td><td>25</td></tr></table>
