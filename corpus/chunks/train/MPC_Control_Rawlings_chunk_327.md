# Exercise 2.19: MPC and multivariable, constrained systems

Consider a two-input, two-output process with the following transfer function

$$
G (s) = \left[ \begin{array}{c c} \frac {2}{1 0 s + 1} & \frac {2}{s + 1} \\ \frac {1}{s + 1} & - \frac {4}{s + 1} \end{array} \right]
$$

(a) Consider a unit setpoint change in the first output. Choose a reasonable sample time, ∆. Simulate the behavior of an offset-free discrete time MPC controller with $Q = I , S = I$ and large N.

(b) Add the constraint $- 1 \leq u ( k ) \leq 1$ and simulate the response.

(c) Add the constraint $- 0 . 1 \leq \Delta u / \Delta \leq 0 . 1$ and simulate the response.

(d) Add significant noise to both output measurements (make the standard deviation in each output about 0.1). Retune the MPC controller to obtain good performance. Describe which controller parameters you changed and why.
