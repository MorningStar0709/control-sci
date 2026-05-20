$$
H = \operatorname{diag} \left(\left[ \begin{array}{c c c c c c c} R & Q & R & Q & \dots & R & P _ {f} \end{array} \right]\right)
$$

The constraints are

$$D \mathbf {z} = d$$

in which

$$
D = - \left[ \begin{array}{c c c c c c c} B & - I & & & & & \\ & A & B & - I & & & \\ & & & \ddots & & & \\ & & & & A & B & - I \end{array} \right] \qquad d = \left[ \begin{array}{c} A \\ 0 \\ \vdots \\ 0 \end{array} \right] x (0)
$$

We now substitute these results into (1.58) and obtain the linear algebra problem

$$
\left[ \begin{array}{c c c c c c c c c c} R & & & & & & & B ^ {\prime} & & \\ & Q & & & & & & - I & A ^ {\prime} & \\ & & R & & & & & & B ^ {\prime} & \\ & & & Q & & & & & - I & \\ & & & & \ddots & & & & & \\ & & & & & R & & & & \\ & & & & & & P _ {f} & & & & B ^ {\prime} \\ B & - I & & & & & & & & - I \\ & A & B & - I & & \\ & & & & \ddots & \\ & & & & & B & - I \end{array} \right] \left[ \begin{array}{c} u (0) \\ x (1) \\ u (1) \\ x (2) \\ \vdots \\ u (N - 1) \\ x (N) \\ \lambda (1) \\ \lambda (2) \\ \vdots \\ \lambda (N) \end{array} \right] = \left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ 0 \\ \vdots \\ 0 \\ 0 \\ - A \\ 0 \\ \vdots \\ 0 \end{array} \right] x (0)
$$

<table><tr><td>Method</td><td>FLOPs</td></tr><tr><td>dynamic programming (DP)</td><td> $Nm^{3}$ </td></tr><tr><td>dense least squares</td><td> $N^{3}m^{3}$ </td></tr><tr><td>banded least squares</td><td> $N(2n + m)(3n + m)^{2}$ </td></tr></table>

Table 6.1: Computational cost of solving finite horizon LQR problem.

This equation is rather cumbersome, but if we reorder the unknown vector to put the Lagrange multiplier together with the state and input from the same time index, and reorder the equations, we obtain the following banded matrix problem

$$
\left[ \begin{array}{c c c c c c c c c c} R & B ^ {\prime} & & & & & & & & \\ B & & - I & & & & & & & \\ & - I & Q & & R & & & & & \\ & & & \ddots & \ddots & & & & & \\ & & & & & R & B ^ {\prime} & & & \\ & & & & A & B & & - I & & \\ & & & & & & - I & Q & & A ^ {\prime} \\ & & & & & & & & R & B ^ {\prime} \\ & & & & & & & A & B & \\ & & & & & & & & & - I \\ & & & & & & & & - I \end{array} \right] \left[ \begin{array}{c} u (0) \\ \lambda (1) \\ x (1) \\ u (1) \\ \vdots \\ u (N - 2) \\ \lambda (N - 1) \\ x (N - 1) \\ u (N - 1) \\ \lambda (N) \\ x (N) \end{array} \right] = \left[ \begin{array}{c} 0 \\ - A \\ 0 \\ 0 \\ \vdots \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{array} \right] x (0) \tag {6.4}
$$
