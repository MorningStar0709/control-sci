# A.2 Matrices

Differentiation of a Vector w.r.t. a Scalar

If a vector $\mathbf{x}$ of dimension $n$ is a function of scalar $t$ , then the derivative of $\mathbf{x}$ w.r.t. $t$ is

$$
\frac {d \mathbf {x}}{d t} = \left[ \begin{array}{l} \frac {d x _ {1}}{d t} \\ \frac {d x _ {2}}{d t} \\ \dots \\ \frac {d x _ {n}}{d t} \end{array} \right]. \tag {A.2.30}
$$

Differentiation of a Vector w.r.t. a Vector

The derivative of an $m$ th order vector function $\mathbf{f}$ w.r.t. an $n$ th vector $\mathbf{x}$ is written as

$$
\frac {d \mathbf {f} ^ {\prime}}{d \mathbf {x}} = \mathbf {G} = \frac {\partial \mathbf {f} ^ {\prime}}{\partial \mathbf {x}} = \left[ \begin{array}{l l l l} \frac {\partial f _ {1}}{\partial x _ {1}} & \frac {\partial f _ {2}}{\partial x _ {1}} & \dots & \frac {\partial f _ {m}}{\partial x _ {1}} \\ \frac {\partial f _ {1}}{\partial x _ {2}} & \frac {\partial f _ {2}}{\partial x _ {2}} & \dots & \frac {\partial f _ {m}}{\partial x _ {2}} \\ \dots & \dots & \dots & \dots \\ \frac {\partial f _ {1}}{\partial x _ {n}} & \frac {\partial f _ {2}}{\partial x _ {n}} & \dots & \frac {\partial f _ {m}}{\partial x _ {n}} \end{array} \right] \tag {A.2.31}
$$

where, $\mathbf{G}$ is a matrix of order $n\mathbf{x}m$ . Note that

$$\mathbf {G} ^ {\prime} = \left[ \frac {\partial \mathbf {f} ^ {\prime}}{\partial \mathbf {x}} \right] ^ {\prime} \quad \text { which is written as } \frac {\partial \mathbf {f}}{\partial \mathbf {x}}. \tag {A.2.32}$$

This is also called Jacobian matrix denoted as

$$
\begin{array}{l} \mathbf {J} _ {\mathbf {x}} (\mathbf {f} (\mathbf {x})) = \frac {d \mathbf {f}}{d \mathbf {x}} = \frac {\partial \mathbf {f}}{\partial \mathbf {x}} = \left[ \frac {\partial f _ {i}}{\partial x _ {j}} \right] \\ = \left[ \begin{array}{l l l l} \frac {\partial f _ {1}}{\partial x _ {1}} & \frac {\partial f _ {1}}{\partial x _ {2}} & \dots & \frac {\partial f _ {1}}{\partial x _ {n}} \\ \frac {\partial f _ {2}}{\partial x _ {1}} & \frac {\partial f _ {2}}{\partial x _ {2}} & \dots & \frac {\partial f _ {2}}{\partial x _ {2}} \\ \dots & \dots & \dots & \dots \\ \frac {\partial f _ {m}}{\partial x _ {1}} & \frac {\partial f _ {m}}{\partial x _ {2}} & \dots & \frac {\partial f _ {m}}{\partial x _ {n}} \end{array} \right]. \tag {A.2.33} \\ \end{array}
$$

Thus, the total differential of $\mathbf{f}$ is

$$d \mathbf {f} = \frac {\partial \mathbf {f}}{\partial \mathbf {x}} d \mathbf {x}. \tag {A.2.34}$$

Differentiation of a Scalar w.r.t. Several Vectors
