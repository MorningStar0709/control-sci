# Example 8.6

Given the following I/O equation (mathematical model)

$$2 \ddot {y} + 1 0 \dot {y} + 1 2 y = u (t) \quad \text { with } y (0) = - 1, \dot {y} (0) = 0. 5$$

determine the dynamic response y(t) if the input is a step function u(t) = 4 for $t > 0 ,$ .

We begin by taking the Laplace transform of each term on the left-hand side of the I/O equation and incorporating the respective initial conditions using Eqs. (8.5) and (8.6)

$$
\begin{array}{l} \mathcal {L} \{2 \ddot {y} \} = 2 (s ^ {2} Y (s) - s y (0) - \dot {y} (0)) = 2 s ^ {2} Y (s) + 2 s - 1 \\ \mathscr {L} \{1 0 \dot {y} \} = 1 0 (s Y (s) - y (0)) = 1 0 s Y (s) + 1 0 \\ \mathcal {L} \{1 2 y \} = 1 2 Y (s) \\ \end{array}
$$

Next, take the Laplace transform of the step-function input (right-hand side)

$$\mathcal {L} \{u (t) \} = \mathcal {L} \{4 \} = \frac {4}{s}$$

Combining all transform results yields

$$2 s ^ {2} Y (s) + 2 s - 1 + 1 0 s Y (s) + 1 0 + 1 2 Y (s) = \frac {4}{s}$$

or,

$$(2 s ^ {2} + 1 0 s + 1 2) Y (s) = \frac {4}{s} - 2 s - 9 = \frac {4 - 2 s ^ {2} - 9 s}{s} \tag {8.12}$$

Solving Eq. (8.12) for the Laplace transform Y(s) we obtain

$$Y (s) = \frac {- 2 s ^ {2} - 9 s + 4}{2 s (s ^ {2} + 5 s + 6)} = \frac {- 2 s ^ {2} - 9 s + 4}{2 s (s + 2) (s + 3)} \tag {8.13}$$

This Laplace transform does not appear in Table 8.1. However, we can use a partial-fraction expansion to express $Y ( s )$ as the sum of three fractions involving the three poles at $s = 0 , - 2 ,$ , and –3

$$Y (s) = \frac {- 2 s ^ {2} - 9 s + 4}{2 s (s + 2) (s + 3)} = \frac {a _ {1}}{s} + \frac {a _ {2}}{s + 2} + \frac {a _ {3}}{s + 3} \tag {8.14}$$

The corresponding constants are $a _ { 1 } = 1 / 3 , a _ { 2 } = - 7 / 2$ , and $a _ { 3 } = 1 3 / 6$ . Note that the inverse Laplace transform of each of the partial-fraction terms in Eq. (8.14) is easily found in Table 8.1: the first term is the Laplace transform of a constant, while the next two terms are the Laplace transforms of exponential functions. Therefore, taking the inverse Laplace transform of $Y ( s )$ yields the dynamic response

$$y (t) = \frac {1}{3} - \frac {7}{2} e ^ {- 2 t} + \frac {1 3}{6} e ^ {- 3 t}$$

We can check this result by evaluating the initial conditions: $y ( 0 ) = ( 1 / 3 ) - ( 7 / 2 ) + ( 1 3 / 6 ) = - 1$ as required. The first time derivative is $\dot { y } ( t ) = 7 e ^ { - 2 t } - ( 1 3 / 2 ) e ^ { - 3 t }$ and, therefore, $\dot { y } ( 0 ) = 7 - ( 1 3 / 2 ) = 0 . 5$ as required.
