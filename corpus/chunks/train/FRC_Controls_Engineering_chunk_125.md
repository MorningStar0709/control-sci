# 5.12.1 Jacobian

The Jacobian is the first-order partial derivative of a vector-valued function with respect to one of its vector arguments. The columns of the Jacobian of f are filled with partial derivatives of f’s rows with respect to each of the argument’s elements. For example, the Jacobian of f with respect to x is

$$
\frac {\partial \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} = \left[ \begin{array}{l l l} \frac {\partial \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial x _ {1}} & \dots & \frac {\partial \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial x _ {m}} \end{array} \right] = \left[ \begin{array}{l l l} \frac {\partial f _ {1}}{\partial x _ {1}} & \dots & \frac {\partial f _ {1}}{\partial x _ {m}} \\ \vdots & \ddots & \vdots \\ \frac {\partial f _ {m}}{\partial x _ {1}} & \dots & \frac {\partial f _ {m}}{\partial x _ {m}} \end{array} \right]
$$

$\frac { \partial f _ { 1 } } { \partial x _ { 1 } }$ is the partial derivative of the first row of f with respect to the first row of x, and so on for all rows of f and x. This has $m ^ { 2 }$ permutations and thus produces a square matrix.

The Jacobian of f with respect to u is

$$
\frac {\partial \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial \mathbf {u}} = \left[ \begin{array}{c c c} \frac {\partial \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial u _ {1}} & \ldots & \frac {\partial \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial u _ {n}} \end{array} \right] = \left[ \begin{array}{c c c} \frac {\partial f _ {1}}{\partial u _ {1}} & \dots & \frac {\partial f _ {1}}{\partial u _ {n}} \\ \vdots & \ddots & \vdots \\ \frac {\partial f _ {m}}{\partial u _ {1}} & \ldots & \frac {\partial f _ {m}}{\partial u _ {n}} \end{array} \right]
$$

∂f1∂u is the partial derivative of the first row of f with respect to the first row of u, and so $\frac { \partial f _ { 1 } } { \partial u _ { 1 } }$ 1 on for all rows of f and u. This has $m \times n$ permutations and can produce a nonsquare matrix if $m \neq n$ .
