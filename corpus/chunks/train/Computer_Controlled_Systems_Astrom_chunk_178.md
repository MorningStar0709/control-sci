# Example 3.6 Lyapunov function

Consider the discrete-time system

$$
x (k + 1) = \left( \begin{array}{c c} {0. 4} & {0} \\ {- 0. 4} & {0. 6} \end{array} \right) x (k)
$$

Using

$$
Q = \left( \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right)
$$

gives the solution of the Lyapunov equation

$$
P = \left( \begin{array}{c c} 1. 1 9 & - 0. 2 5 \\ - 0. 2 5 & 2. 0 5 \end{array} \right)
$$

Figure 3.9 shows the level curves of $V(x) = x^T Px$ and trajectories for some starting values of $x$ . The trajectories are such that for each step, the state is reaching a value of $V$ with a lower value.
