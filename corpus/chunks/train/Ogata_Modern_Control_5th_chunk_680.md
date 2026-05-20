\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & - 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c c} 4 & 2 \\ 0 & 0 \\ 3 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]

\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \\ \dot {x} _ {4} \\ \dot {x} _ {5} \end{array} \right] = \left[ \begin{array}{c c c c c} - 2 & 1 & 0 & & 0 \\ 0 & - 2 & 1 & & \\ 0 & 0 & - 2 & & \\ \hdashline & & & - 5 & 1 \\ 0 & & & 0 & - 5 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \\ x _ {5} \end{array} \right] + \left[ \begin{array}{c} 4 \\ 2 \\ 1 \\ 3 \\ 0 \end{array} \right] u
$$

Condition for Complete State Controllability in the s Plane. The condition for complete state controllability can be stated in terms of transfer functions or transfer matrices.

It can be proved that a necessary and sufficient condition for complete state controllability is that no cancellation occur in the transfer function or transfer matrix. If cancellation occurs, the system cannot be controlled in the direction of the canceled mode.

EXAMPLE 9–13 Consider the following transfer function:

$$\frac {X (s)}{U (s)} = \frac {s + 2 . 5}{(s + 2 . 5) (s - 1)}$$

Clearly, cancellation of the factor (s+2.5) occurs in the numerator and denominator of this transfer function. (Thus one degree of freedom is lost.) Because of this cancellation, this system is not completely state controllable.

The same conclusion can be obtained by writing this transfer function in the form of a state equation. A state-space representation is

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 2. 5 & - 1. 5 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] u
$$

Since

$$
\left[ \begin{array}{c c} \mathbf {B} & \mathbf {A B} \end{array} \right] = \left[ \begin{array}{c c} 1 & 1 \\ 1 & 1 \end{array} \right]
$$

the rank of the matrix is 1. Therefore, we arrive at the same conclusion: The system isC B  AB D not completely state controllable.
