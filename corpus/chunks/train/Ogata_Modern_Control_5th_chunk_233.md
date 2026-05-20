# EXAMPLE 5–10

Consider the following system that is subjected to the initial condition. (No external forcing function is present.)

$$\ddot {y} + 8 \dot {y} + 1 7 \dot {y} + 1 0 y = 0y (0) = 2, \quad \dot {y} (0) = 1, \quad \ddot {y} (0) = 0. 5$$

Obtain the response $y ( t )$ to the given initial condition.

By defining the state variables as

$$x _ {1} = yx _ {2} = \dot {y}x _ {3} = \ddot {y}$$

we obtain the following state-space representation for the system:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 0 & - 1 7 & - 8 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right], \quad \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \\ x _ {3} (0) \end{array} \right] = \left[ \begin{array}{c} 2 \\ 1 \\ 0. 5 \end{array} \right]

y = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

A possible MATLAB program to obtain the response y(t) is given in MATLAB Program 5–17. The resulting response curve is shown in Figure 5–34.
