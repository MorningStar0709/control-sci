$$
\begin{array}{l} \dot {\mathbf {z}} = \mathbf {S} ^ {- 1} \mathbf {A} \mathbf {S} \mathbf {z} + \mathbf {S} ^ {- 1} \mathbf {B} \mathbf {u} \\ = \mathbf {J} \mathbf {z} + \mathbf {S} ^ {- 1} \mathbf {B} \mathbf {u} \tag {9-60} \\ \end{array}
$$

The condition for complete state controllability of the system of Equation (9–56) may then be stated as follows: The system is completely state controllable if and only if (1)

no two Jordan blocks in J of Equation (9–60) are associated with the same eigenvalues, (2) the elements of any row of $\bar { \mathbf { S } } ^ { - 1 } \mathbf { B }$ that correspond to the last row of each Jordan block are not all zero, and (3) the elements of each row of $\mathbf { S } ^ { - 1 } \mathbf { B }$ that correspond to distinct eigenvalues are not all zero.

EXAMPLE 9–12 The following systems are completely state controllable:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & 0 \\ 0 & - 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 2 \\ 5 \end{array} \right] u

\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & - 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 4 \\ 3 \end{array} \right] u

\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \\ \dot {x} _ {4} \\ \dot {x} _ {5} \end{array} \right] = \left[ \begin{array}{c c c c c c} - 2 & 1 & 0 & & & 0 \\ 0 & - 2 & 1 & & & \\ 0 & 0 & - 2 & & & \\ \hdashline & & & - 5 & 1 \\ 0 & & & 0 & - 5 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \\ x _ {5} \end{array} \right] + \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \\ 3 & 0 \\ 0 & 0 \\ 2 & 1 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]
$$

The following systems are not completely state controllable:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & 0 \\ 0 & - 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 2 \\ 0 \end{array} \right] u
