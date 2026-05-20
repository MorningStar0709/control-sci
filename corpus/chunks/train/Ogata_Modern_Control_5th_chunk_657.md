# MATLAB Program 9–3

$$
\begin{array}{l} A = [ 0 \quad 1; - 2 5 \quad - 4 ]; \\ B = [ 1 \quad 1; 0 \quad 1 ]; \\ C = [ 1 \quad 0; 0 \quad 1 ]; \\ D = [ 0 0; 0 0 ]; \\ [ \text { NUM }, \text { den } ] = \text { ss2tf } (A, B, C, D, 1) \\ \mathsf {N U M} = \\ \begin{array}{c c c} 0 & 1 & 4 \\ 0 & 0 & - 2 5 \end{array} \\ \mathrm{den} = \\ \begin{array}{c c c} 1 & 4 & 2 5 \end{array} \\ [ \text { NUM }, \text { den } ] = \text { ss2tf } (A, B, C, D, 2) \\ \mathsf {N U M} = \\ \begin{array}{c c c} 0 & 1. 0 0 0 0 & 5. 0 0 0 0 \\ 0 & 1. 0 0 0 0 & - 2 5. 0 0 0 0 \end{array} \\ \mathrm{den} = \\ \begin{array}{c c c} 1 & 4 & 2 5 \end{array} \\ \end{array}
$$

This is the MATLAB representation of the following four transfer functions:

$$
\begin{array}{l} \frac {Y _ {1} (s)}{U _ {1} (s)} = \frac {s + 4}{s ^ {2} + 4 s + 2 5}, \quad \frac {Y _ {2} (s)}{U _ {1} (s)} = \frac {- 2 5}{s ^ {2} + 4 s + 2 5} \\ \frac {Y _ {1} (s)}{U _ {2} (s)} = \frac {s + 5}{s ^ {2} + 4 s + 2 5}, \quad \frac {Y _ {2} (s)}{U _ {2} (s)} = \frac {s - 2 5}{s ^ {2} + 4 s + 2 5} \\ \end{array}
$$

In this section, we shall obtain the general solution of the linear time-invariant state equation.We shall first consider the homogeneous case and then the nonhomogeneous case.

Solution of Homogeneous State Equations. Before we solve vector-matrix differential equations, let us review the solution of the scalar differential equation

$$\dot {x} = a x \tag {9-25}$$

In solving this equation, we may assume a solution x(t) of the form

$$x (t) = b _ {0} + b _ {1} t + b _ {2} t ^ {2} + \dots + b _ {k} t ^ {k} + \dots \tag {9-26}$$

By substituting this assumed solution into Equation (9–25), we obtain

$$
\begin{array}{l} b _ {1} + 2 b _ {2} t + 3 b _ {3} t ^ {2} + \dots + k b _ {k} t ^ {k - 1} + \dots \\ = a \left(b _ {0} + b _ {1} t + b _ {2} t ^ {2} + \dots + b _ {k} t ^ {k} + \dots\right) \tag {9-27} \\ \end{array}
$$

If the assumed solution is to be the true solution, Equation (9–27) must hold for any t. Hence, equating the coefficients of the equal powers of t, we obtain

$$
\begin{array}{l} b _ {1} = a b _ {0} \\ b _ {2} = \frac {1}{2} a b _ {1} = \frac {1}{2} a ^ {2} b _ {0} \\ b _ {3} = \frac {1}{3} a b _ {2} = \frac {1}{3 \times 2} a ^ {3} b _ {0} \\ b _ {k} = \frac {1}{k !} a ^ {k} b _ {0} \\ \end{array}
$$

The value of $b _ { 0 }$ is determined by substituting t=0 into Equation (9–26), or

$$x (0) = b _ {0}$$

Hence, the solution x(t) can be written as

$$
\begin{array}{l} x (t) = \left(1 + a t + \frac {1}{2 !} a ^ {2} t ^ {2} + \dots + \frac {1}{k !} a ^ {k} t ^ {k} + \dots\right) x (0) \\ = e ^ {a t} x (0) \\ \end{array}
$$

We shall now solve the vector-matrix differential equation
