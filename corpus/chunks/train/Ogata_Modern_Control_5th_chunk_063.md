MATLAB transforms the transfer function given by Equation (2–39) into the state-space representation given by Equations (2–40) and (2–41). For the example system considered here, MATLAB Program 2–2 will produce matrices A, B, C, and D.

<table><tr><td colspan="3">MATLAB Program 2-2</td></tr><tr><td colspan="3">num = [1 0];den = [1 14 56 160];[A,B,C,D] = tf2ss(num,den)</td></tr><tr><td>A =</td><td></td><td></td></tr><tr><td>-14</td><td>-56</td><td>-160</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>B =</td><td></td><td></td></tr><tr><td>1</td><td></td><td></td></tr><tr><td>0</td><td></td><td></td></tr><tr><td>0</td><td></td><td></td></tr><tr><td>C =</td><td></td><td></td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>D =</td><td></td><td></td></tr><tr><td>0</td><td></td><td></td></tr></table>

Transformation from State Space Representation to Transfer Function. To obtain the transfer function from state-space equations, use the following command:

$$[ \mathrm{num}, \mathrm{den} ] = \mathrm{ss2tf} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{iu})$$

iu must be specified for systems with more than one input. For example, if the system has three inputs (u1, u2, u3), then iu must be either 1, 2, or 3, where 1 implies u1, 2 implies u2, and 3 implies u3.

If the system has only one input, then either

$$[ \text { num }, \text { den } ] = \text { ss2tf(A,B,C,D) }$$

or

$$[ \text { num,den } ] = \text { ss2tf(A,B,C,D,1) }$$

may be used. For the case where the system has multiple inputs and multiple outputs, see Problem A–2–12.

EXAMPLE 2–4 Obtain the transfer function of the system defined by the following state-space equations:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 5 & - 2 5 & - 5 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 2 5 \\ - 1 2 0 \end{array} \right] u

y = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

MATLAB Program 2-3 will produce the transfer function for the given system.The transfer function obtained is given by

$$\frac {Y (s)}{U (s)} = \frac {2 5 s + 5}{s ^ {3} + 5 s ^ {2} + 2 5 s + 5}$$
