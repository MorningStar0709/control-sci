# Example 6.5

Given the spool-valve system in Fig. 6.3 and Example 6.2, create and execute a simulation using a state-space model. The applied force $f ( t )$ is a step function with a magnitude of 12 N.

We begin the derivation of an SSR from the second-order I/O equation (6.8) by defining the two state variables: $x _ { 1 } = y$ (valve position) and $x _ { 2 } = \dot { y }$ (valve velocity). Therefore, two state-variable equations are

$$\dot {x} _ {1} = \dot {y} \tag {6.13}\dot {x} _ {2} = \ddot {y} = \frac {1}{0 . 0 4} (- 1 6 \dot {y} - 7 0 0 0 y + f (t)) \tag {6.14}$$

Substituting the state variables, $x _ { 1 } = y$ and $x _ { 2 } = \dot { y }$ , and input $u = f ( t )$ into Eqs. (6.13) and (6.14) yields

$$\dot {x} _ {1} = x _ {2} \tag {6.15}\dot {x} _ {2} = - 4 0 0 x _ {2} - 1 7 5, 0 0 0 x _ {1} + 2 5 u \tag {6.16}$$

which can be assembled into the matrix-vector state equation

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 1 7 5, 0 0 0 & - 4 0 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 2 5 \end{array} \right] u \tag {6.17}
$$

Recall that the $2 \times 2$ square matrix in Eq. (6.17) is the state matrix A, and the $2 \times 1$ column vector is the input matrix B. In order to complete the SSR, we write the matrix-vector output equation, where the output (valve position) is the first state variable, or $y = x _ { 1 }$

$$
y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + [ 0 ] u \tag {6.18}
$$

The $1 \times 2$ row vector in Eq. (6.18) is the output matrix C, and the D “matrix” is null (zero).

We construct our Simulink diagram by using the State-Space block from the Continuous library, the Clock and Step blocks from the Sources library, and the To Workspace blocks from the Sinks library. Double-clicking the State-Space block opens a dialog box, where we can enter the appropriate numerical values for the A, B, C, and D matrices as demonstrated below

$$
\begin{array}{l} A = \left[ \begin{array}{l l l} 0 & 1 & - 1 7 5 e 3 - 4 0 0 \end{array} \right] \\ B = \left[ \begin{array}{l l} 0 & ; 2 5 \end{array} \right] \\ C = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \\ D = 0 \\ \end{array}
$$
