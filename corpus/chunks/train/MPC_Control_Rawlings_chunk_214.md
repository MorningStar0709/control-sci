# 2.3 Dynamic Programming Solution

We examine next the DP solution of the optimal control problem $\mathbb { P } _ { N } ( x )$ , not because it provides a practical procedure but because of the insight it provides. DP can rarely be used for constrained and/or nonlinear control problems unless the state dimension n is small. MPC is best regarded as a practical means of implementing the DP solution; for a given state x it provides $V _ { N } ^ { 0 } ( x )$ and $\kappa _ { N } ( { \boldsymbol { x } } )$ , the value, respectively, of the value function and control law at a point x. DP, on the other hand, yields the value function $V _ { N } ^ { 0 } ( \cdot )$ and the implicit MPC control law $\kappa _ { N } ( \cdot )$ .

The optimal control problem $\mathbb { P } _ { N } ( x )$ is defined, as before, by (2.8) with the cost function $V _ { N } ( \cdot )$ defined by (2.4) and the constraints by (2.5). DP yields an optimal policy $\pmb { \mu } ^ { 0 } = \{ \mu _ { 0 } ^ { 0 } ( \cdot ) , \mu _ { 1 } ^ { 0 } ( \cdot ) , \ldots , \mu _ { N - 1 } ^ { 0 } ( \cdot ) \}$ , i.e., a sequence of control laws $\mu _ { i } : X _ { i } \to \mathbb { U } , i = 0 , 1 , \dots , N - 1$ . The domain $x _ { i }$ of each control law will be defined later. The optimal controlled system is time varying and satisfies

$$x ^ {+} = f (x, \mu_ {i} ^ {0} (x)), i = 0, 1, \ldots , N - 1$$

in contrast with the system using MPC, which is time invariant and satisfies

$$x ^ {+} = f (x, \kappa_ {N} (x)), i = 0, 1, \ldots , N - 1$$

where $\begin{array} { r } { \kappa _ { N } ( \cdot ) = \mu _ { 0 } ^ { 0 } ( \cdot ) } \end{array}$ . The optimal control law at time i is $\mu _ { i } ^ { 0 } ( \cdot )$ whereas receding horizon control (RHC) uses the time-invariant control law $\kappa _ { N } ( \cdot )$ obtained by assuming that at each time t, the terminal time or horizon is $t + N$ so that the horizon t + N recedes as t increases. One consequence is that the time-invariant control law $\kappa _ { N } ( \cdot )$ is not optimal for the problem of controlling $x ^ { + } = f ( x , u )$ over the fixed interval [0, T ] in such a way as to minimize $V _ { N }$ and satisfy the constraints.
