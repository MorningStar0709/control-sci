$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 3 & - 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

where the initial conditions are

$$
\left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] = \left[ \begin{array}{c} 1 \\ - 1 \end{array} \right]
$$

B–9–9. Consider the following state equation and output equation:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - 6 & 1 & 0 \\ - 1 1 & 0 & 1 \\ - 6 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 2 \\ 6 \\ 2 \end{array} \right] u

y = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

Show that the state equation can be transformed into the following form by use of a proper transformation matrix:

$$
\left[ \begin{array}{l} \dot {z} _ {1} \\ \dot {z} _ {2} \\ \dot {z} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 0 & - 6 \\ 1 & 0 & - 1 1 \\ 0 & 1 & - 6 \end{array} \right] \left[ \begin{array}{l} z _ {1} \\ z _ {2} \\ z _ {3} \end{array} \right] + \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right] u
$$

Then obtain the output y in terms of $z _ { 1 } , z _ { 2 }$ , and $z _ { 3 }$

B–9–10. Obtain a state-space representation of the following system with MATLAB:

$$\frac {Y (s)}{U (s)} = \frac {1 0 . 4 s ^ {2} + 4 7 s + 1 6 0}{s ^ {3} + 1 4 s ^ {2} + 5 6 s + 1 6 0}$$

B–9–11. Obtain a transfer-function representation of the following system with MATLAB:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{r r r} 0 & 1 & 0 \\ - 1 & - 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right] u

y = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

B–9–12. Obtain a transfer-function representation of the following system with MATLAB:
