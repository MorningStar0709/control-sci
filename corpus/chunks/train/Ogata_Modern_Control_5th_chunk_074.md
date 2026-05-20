$$\beta_ {0} = b _ {0} = 2\beta_ {1} = b _ {1} - a _ {1} \beta_ {0} = 1 - 4 \times 2 = - 7\beta_ {2} = b _ {2} - a _ {1} \beta_ {1} - a _ {2} \beta_ {0} = 1 - 4 \times (- 7) - 5 \times 2 = 1 9\beta_ {3} = b _ {3} - a _ {1} \beta_ {2} - a _ {2} \beta_ {1} - a _ {3} \beta_ {0}= 2 - 4 \times 1 9 - 5 \times (- 7) - 2 \times 2 = - 4 3$$

Referring to Equation (2–34), we define

$$x _ {1} = y - \beta_ {0} u = y - 2 ux _ {2} = \dot {x} _ {1} - \beta_ {1} u = \dot {x} _ {1} + 7 ux _ {3} = \dot {x} _ {2} - \beta_ {2} u = \dot {x} _ {2} - 1 9 u$$

Then referring to Equation (2–36),

$$\dot {x} _ {1} = x _ {2} - 7 u\dot {x} _ {2} = x _ {3} + 1 9 u\dot {x} _ {3} = - a _ {3} x _ {1} - a _ {2} x _ {2} - a _ {1} x _ {3} + \beta_ {3} u= - 2 x _ {1} - 5 x _ {2} - 4 x _ {3} - 4 3 u$$

Hence, the state-space representation of the system is

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 2 & - 5 & - 4 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} - 7 \\ 1 9 \\ - 4 3 \end{array} \right] u

y = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + 2 u
$$

This is one possible state-space representation of the system. There are many (infinitely many) others. If we use MATLAB, it produces the following state-space representation:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - 4 & - 5 & - 2 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right] u

y = \left[ \begin{array}{l l l} - 7 & - 9 & - 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + 2 u
$$

See MATLAB Program 2-4. (Note that all state-space representations for the same system are equivalent.)

<table><tr><td>MATLAB Program 2-4</td></tr><tr><td>num = [2 1 1 2];den = [1 4 5 2];[A,B,C,D] = tf2ss(num,den)</td></tr><tr><td>A =</td></tr><tr><td>-4 -5 -2</td></tr><tr><td>1 0 0</td></tr><tr><td>0 1 0</td></tr><tr><td>B =</td></tr><tr><td>1</td></tr><tr><td>0</td></tr><tr><td>0</td></tr><tr><td>C =</td></tr><tr><td>-7 -9 -2</td></tr><tr><td>D =</td></tr><tr><td>2</td></tr></table>

A–2–8. Obtain a state-space model of the system shown in Figure 2–26.
