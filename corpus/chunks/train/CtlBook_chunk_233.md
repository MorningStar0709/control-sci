# Example 8.1

Let's review the small SS system from Section 4.3.

$$
\dot {X} = \left[ \begin{array}{c} \dot {x} \\ \ddot {x} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ \frac {- (K _ {1} + K _ {2})}{M} & \frac {- B}{M} \end{array} \right] \left[ \begin{array}{c} x \\ \dot {x} \end{array} \right] + \left[ \begin{array}{c c} 0 & \frac {1}{M} \end{array} \right] \left[ \begin{array}{c} 0 \\ f (t) \end{array} \right]
$$

Problem: Input the above state space system into python.control by deriving A, B, C, D using the ctl.ss(A,B,C,D) method and compute step response. Also make a phase plot. Assume the following values for input and system parameters:

$$K 1 = 1 0. 0, K 2 = 2 0. 0, B = 1 0. 0, M = 1 0 0. 0, f (t) = 5 u (t)$$

The states of our system are inside some kind of opaque box such that the output we can actually measure is y = 2x + 0.7 ˙x. Design the matrices C and D.
