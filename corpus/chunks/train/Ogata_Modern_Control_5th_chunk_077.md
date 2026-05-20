Notice that the output of the integrator and the outputs of the first-order delayed integrators $[ 1 / ( s + a )$ and $( z - p ) / ( s + p ) ]$ are chosen as state variables. It is important to remember that the output of the block $( s + z ) / ( s + p )$ in Figure 2–28(a) cannot be a state variable, because this block involves a derivative term, $s + z .$

A–2–11. Obtain the transfer function of the system defined by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & - 1 & 1 \\ 0 & 0 & - 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right] u

y = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

Solution. Referring to Equation (2–29), the transfer function $G ( s )$ is given by

$$G (s) = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + D$$

In this problem, matrices A, B, C, and D are

$$
\mathbf {A} = \left[ \begin{array}{r r r} - 1 & 1 & 0 \\ 0 & - 1 & 1 \\ 0 & 0 & - 2 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {C} = [ 1 \quad 0 \quad 0 ], \quad D = 0
$$

Hence

$$
G (s) = [ 1 \quad 0 \quad 0 ] \left[ \begin{array}{c c c} s + 1 & - 1 & 0 \\ 0 & s + 1 & - 1 \\ 0 & 0 & s + 2 \end{array} \right] ^ {- 1} \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right]

= \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c c c} \frac {1}{s + 1} & \frac {1}{(s + 1) ^ {2}} & \frac {1}{(s + 1) ^ {2} (s + 2)} \\ 0 & \frac {1}{s + 1} & \frac {1}{(s + 1) (s + 2)} \\ 0 & 0 & \frac {1}{s + 2} \end{array} \right] \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right]
= \frac {1}{(s + 1) ^ {2} (s + 2)} = \frac {1}{s ^ {3} + 4 s ^ {2} + 5 s + 2}
$$

A–2–12. Consider a system with multiple inputs and multiple outputs.When the system has more than one output, the MATLAB command

$$[ \mathsf {N U M}, \mathsf {d e n} ] = \mathsf {s s 2 t f} (\mathsf {A}, \mathsf {B}, \mathsf {C}, \mathsf {D}, \mathsf {i u})$$

produces transfer functions for all outputs to each input. (The numerator coefficients are returned to matrix NUM with as many rows as there are outputs.)

Consider the system defined by
