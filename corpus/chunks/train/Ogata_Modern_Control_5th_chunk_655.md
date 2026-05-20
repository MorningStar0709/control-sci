<table><tr><td>MATLAB Program 9-1</td></tr><tr><td>num = [10 10];den = [1 6 5 10];[A,B,C,D] = tf2ss(num,den)</td></tr><tr><td>A =</td></tr><tr><td>-6 -5 -10</td></tr><tr><td>1 0 0</td></tr><tr><td>0 1 0</td></tr><tr><td>B =</td></tr><tr><td>1</td></tr><tr><td>0</td></tr><tr><td>0</td></tr><tr><td>C =</td></tr><tr><td>0 10 10</td></tr><tr><td>D =</td></tr><tr><td>0</td></tr></table>

Transformation from State Space to Transfer Function. To obtain the transfer function from state-space equations, use the following command:

$$[ \text { num }, \text { den } ] = \text { ss2tf } (A, B, C, D, i u)$$

iu must be specified for systems with more than one input. For example, if the system has three inputs (u1, u2, u3), then iu must be either 1, 2, or 3, where 1 implies u1, 2 implies u2, and 3 implies u3.

If the system has only one input, then either

$$[ \text { num }, \text { den } ] = \text { ss2tf(A,B,C,D) }$$

or

$$[ \text { num }, \text { den } ] = \text { ss2tf } (A, B, C, D, 1)$$

may be used. (See Example 9–3 and MATLAB Program 9–2.)

For the case where the system has multiple inputs and multiple outputs, see Example 9–4.

EXAMPLE 9–3 Obtain the transfer function of the system defined by the following state-space equations:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 5. 0 0 8 & - 2 5. 1 0 2 6 & - 5. 0 3 2 4 7 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 2 5. 0 4 \\ - 1 2 1. 0 0 5 \end{array} \right] u

y = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

MATLAB Program 9–2 will produce the transfer function for the given system. The transfer function obtained is given by

$$\frac {Y (s)}{U (s)} = \frac {2 5 . 0 4 s + 5 . 0 0 8}{s ^ {3} + 5 . 0 3 2 5 s ^ {2} + 2 5 . 1 0 2 6 s + 5 . 0 0 8}$$

MATLAB Program 9–2   
A = [0 1 0;0 0 1;-5.008 -25.1026 -5.03247];
B = [0;25.04; -121.005];
C = [1 0 0];
D = [0];
[num,den] = ss2tf(A,B,C,D)
num =
    0 -0.0000 25.0400 5.0080
den =
    1.0000 5.0325 25.1026 5.0080
% **** The same result can be obtained by entering the following command *****
[num,den] = ss2tf(A,B,C,D,1)
num =
    0 -0.0000 25.0400 5.0080
den =
    1.0000 5.0325 25.1026 5.0080

Consider a system with multiple inputs and multiple outputs.When the system has more than one output, the command
