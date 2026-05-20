# Problems

7.1 For the system

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - 1 \end{array} \right] \mathbf {x} + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u

y = \left[ \begin{array}{l l} 1 & 1 \end{array} \right] x
$$

a. Calculate the transfer function y/u.   
b. Write the state equations, with $u_{ex}$ as the input, if $u = -[k_1 - k_2]\mathbf{x} + u_{ex}$ .   
c. Calculate the transfer function $y / u_{ex}$ and verify that the zero is as in part (a).

7.2 Repeat Problem 7.1 for the system

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 1 \\ - 1 \end{array} \right] u

y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \mathbf {x}.
$$

7.3 Verify that the system of Problem 7.1 is controllable, and that it remains controllable under the control law of part (b), for any $k_{1}$ and $k_{2}$ .

7.4 Repeat-Problem 7.3 for the system of Problem 7.2.

7.5 A system is given as

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 1 \end{array} \right] \mathbf {x} + \left[ \begin{array}{c} - 1 \\ 1 \end{array} \right] u.
$$

a. Show that this system is uncontrollable, and find the uncontrollable mode.   
b. Write the state equations, with $u_{ex}$ as input, if $u = -\left[k_1 - k_2\right]\mathbf{x} + u_{ex}$ .   
c. Show that the system of part (b) is uncontrollable for any $k_{1}$ and $k_{2}$ , and that the uncontrollable mode is the same as that of the original system.   
d. For $y = [c_1 \quad c_2] \mathbf{x}$ , calculate the transfer functions $y / u_{ex}$ and show that there is always a pole-zero cancellation for any $c_1, c_2, k_1$ , and $k_2$ .

7.6 For the system of Problem 7.1, place the closed-loop poles at $s = -1, -1$ by:

a. Using the transfer function of part (c) of Problem 7.1 and adjusting $k_{1}$ and $k_{2}$ to obtain the correct closed-loop characteristic polynomial.   
b. Applying Equation 7.18.

7.7 Repeat Problem 7.6 for the system of Problem 7.2.

7.8 For the system

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & - 1 & 1 \\ 0 & - 1 & 2 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] u
$$

a. Verify controllability.   
b. Calculate the state feedback law to place poles at -2 and $-1 \pm j$ .

M

7.9 The intent of this problem is to study the interplay between robustness and the closed-loop pole locations.

a. For the system of Example 7.2, calculate the state feedback gain to place poles at $-6 \pm j6$ and $-48$ .
