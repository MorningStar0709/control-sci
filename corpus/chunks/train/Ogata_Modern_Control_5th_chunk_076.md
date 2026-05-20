Define the outputs of the integrators as state variables, as shown in Figure 2–27(b). Then from Figure 2–27(b) we obtain

$$\frac {X _ {1} (s)}{X _ {2} (s) + a [ U (s) - X _ {1} (s) ]} = \frac {1}{s}\frac {X _ {2} (s)}{U (s) - X _ {1} (s)} = \frac {b}{s}Y (s) = X _ {1} (s)$$

which may be modified to

$$s X _ {1} (s) = X _ {2} (s) + a \big [ U (s) - X _ {1} (s) \big ]s X _ {2} (s) = - b X _ {1} (s) + b U (s)Y (s) = X _ {1} (s)$$

![](image/15394e846b42ca5edcd5b1b3e8e0fe9c46703a85e55ba484ecb2d407f4104a0f.jpg)  
Figure 2–27 (a) Control system; (b) modified block diagram.

Taking the inverse Laplace transforms of the preceding three equations, we obtain

$$\dot {x} _ {1} = - a x _ {1} + x _ {2} + a u\dot {x} _ {2} = - b x _ {1} + b uy = x _ {1}$$

Rewriting the state and output equations in the standard vector-matrix form, we obtain

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - a & 1 \\ - b & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} a \\ b \end{array} \right] u

y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

A–2–10. Obtain a state-space representation of the system shown in Figure 2–28(a).

Solution. In this problem, first expand $( s + z ) / ( s + p )$ into partial fractions.

$$\frac {s + z}{s + p} = 1 + \frac {z - p}{s + p}$$

Next, convert $K / { \big [ } s ( s + a ) { \big ] }$ into the product of $K / s$ and $1 / ( s + a )$ . Then redraw the block diagram, as shown in Figure 2–28(b). Defining a set of state variables, as shown in Figure 2–28(b), we obtain the following equations:

$$
\begin{array}{l} \dot {x} _ {1} = - a x _ {1} + x _ {2} \\ \dot {x} _ {2} = - K x _ {1} + K x _ {3} + K u \\ \dot {x} _ {3} = - (z - p) x _ {1} - p x _ {3} + (z - p) u \\ y = x _ {1} \\ \end{array}
$$

Figure 2–28 (a) Control system; (b) block diagram defining state variables for the system.   
![](image/6c503c766e2cc327e84581098f5c51dff385b4f93b3a0ea824a5858660569a48.jpg)

Rewriting gives

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - a & 1 & 0 \\ - K & 0 & K \\ - (z - p) & 0 & - p \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ K \\ z - p \end{array} \right] u

y = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$
