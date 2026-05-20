# Exercise 2.5: Computing the maximal output admissible set

Write an Octave or MATLAB program to determine the maximal constraint admissible set for the system $x ^ { + } = F x , y = H x$ subject to the hard constraint $y \in Y$ in which $Y = \{ y \mid E y \leq e \}$ . Use algorithm 3.2 in Gilbert and Tan (1991).

To check your program, verify for the system

$$
F = \left[ \begin{array}{c c} 0. 9 & 1 \\ 0 & 0. 0 9 \end{array} \right] \quad H = \left[ \begin{array}{c c} 1 & 1 \end{array} \right]
$$

subject to the constraint $Y = \{ y \mid - 1 \leq y \leq 1 \}$ , and that the maximal output admissible set is given by

$$
O _ {\infty} = \{x \in \mathbb {R} ^ {2} \mid A x \leq b \} \quad A = \left[ \begin{array}{c c} 1 & 1 \\ - 1 & 1 \\ 0. 9 & 1. 0 1 \\ - 0. 9 & - 1. 0 1 \end{array} \right] \quad b = \left[ \begin{array}{c} 1 \\ 1 \\ 1 \\ 1 \end{array} \right]
$$

Show that $t ^ { * }$ , the smallest integer t such that $O _ { t } = O _ { \infty }$ satisfies $t ^ { * } = 1$ .

What happens to $t ^ { * }$ as $F _ { 2 2 }$ increases and approaches 1. What do you conclude for the case $F _ { 2 2 } \ge 1 2$
