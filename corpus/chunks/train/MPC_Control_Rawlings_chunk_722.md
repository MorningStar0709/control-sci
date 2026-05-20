# Exercise 6.1: Three looks at solving the LQ problem

In the following exercise, you will write three codes to solve the LQR using Octave or MATLAB. The objective function is the LQR with mixed term

$$V = \frac {1}{2} \sum_ {k = 0} ^ {N - 1} (x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k) + 2 x (k) ^ {\prime} M u (k)) + (1 / 2) x (N) ^ {\prime} P _ {f} x (N)$$

First, implement the method described in Section 6.1.1 in which you eliminate the state and solve the problem for the decision variable

$$\mathbf {u} = \{u (0), u (1), \dots , u (N - 1) \}$$

Second, implement the method described in Section 6.1.1 in which you do not eliminate the state and solve the problem for

$$\mathbf {z} = \{u (0), x (1), u (1), x (2), \dots , u (N - 1), x (N) \}$$

Third, use backward dynamic programming (DP) and the Riccati iteration to compute the closed-form solution for u(k) and x(k).

(a) Let

$$
A = \left[ \begin{array}{c c} 4 / 3 & - 2 / 3 \\ 1 & 0 \end{array} \right] \qquad B = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] \qquad C = \left[ \begin{array}{c c} - 2 / 3 & 1 \end{array} \right] \qquad x (0) = \left[ \begin{array}{c} 1 \\ 1 \end{array} \right]
Q = C ^ {\prime} C + 0. 0 0 1 I \quad P _ {f} = \Pi \quad R = 0. 0 0 1 \quad M = 0
$$

in which the terminal penalty, Pf is set equal to Π, the steady-state cost to go. Compare the three solutions for N = 5. Plot x(k), u(k) versus time for the closed-loop system.

(b) Let N = 50 and repeat. Do any of the methods experience numerical problems generating an accurate solution? Plot the condition number of the matrix that is inverted in the first two methods versus N.

(c) Now consider the following unstable system

$$
A = \left[ \begin{array}{c c c} 2 7. 8 & - 8 2. 6 & 3 4. 6 \\ 2 5. 6 & - 7 6. 8 & 3 2. 4 \\ 4 0. 6 & - 1 2 2. 0 & 5 1. 9 \end{array} \right] \qquad B = \left[ \begin{array}{c c} 0. 5 2 7 & 0. 5 4 8 \\ 0. 6 1 3 & 0. 5 3 0 \\ 1. 0 6 & 0. 8 2 8 \end{array} \right] \qquad x (0) = \left[ \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right]
$$

Consider regulator tuning parameters and constraints

$$Q = I \qquad P _ {f} = \Pi \qquad R = I \qquad M = 0$$

Repeat parts 6.1a and 6.1b for this system. Do you lose accuracy in any of the solution methods? What happens to the condition number of H(N) and S(N) as N becomes large? Which methods are still accurate for this case? Can you explain what happened?
