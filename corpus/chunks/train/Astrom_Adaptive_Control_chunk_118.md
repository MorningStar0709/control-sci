# Identification in Closed Loop

In adaptive control, system identification is often performed under closed-loop conditions, which may give rise to certain difficulties. Consider, for example, the estimation of the coefficients of a transfer function model as in Eq. (2.34). The matrix $\Phi$ is then

$$
\Phi = \left( \begin{array}{c c c c c c} - y (n) & \dots & - y (\mathbf {1}) & u (n) & \dots & u (1) \\ - y (n + 1) & \dots & - y (2) & u (n + 1) & \dots & u (2) \\ \vdots & & & & & \vdots \\ - y (t - 1) & \dots & - y (t - n) & u (t - 1) & \dots & u (t - n) \end{array} \right) \tag {2.48}
$$

A linear feedback of sufficiently low order introduces linear dependencies among the columns of the matrix $\Phi$ . This means that the parameters cannot be determined uniquely. A simple example shows what may happen.
