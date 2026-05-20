# A.2 Matrices

Differentiation of a Scalar w.r.t. a Matrix Suppose a scalar $f$ is a function of a matrix $\mathbf{A}$ , then

$$
\frac {d f}{d \mathbf {A}} = \left[ \begin{array}{c c c c} \frac {d f}{d a _ {1 1}} & \frac {d f}{d a _ {1 2}} & \dots & \frac {d f}{d a _ {1 m}} \\ \frac {d f}{d a _ {2 1}} & \frac {d f}{d a _ {2 2}} & \dots & \frac {d f}{d a _ {2 m}} \\ \dots & \dots & \dots & \dots \\ \frac {d f}{d a _ {n 1}} & \frac {d f}{d a _ {n 2}} & \dots & \frac {d f}{d a _ {n m}} \end{array} \right] \tag {A.2.41}
$$

The integration process for matrices and vectors is similarly defined for all the previous cases. For example,

$$\int \mathbf {A} d t = \left[ \int a _ {i j} d t \right]. \tag {A.2.42}$$

Taylor Series Expansion

It is well known that the Taylor series expansion of a function $f$ w.r.t. $\mathbf{x}$ about $\mathbf{x}_0$ is

$$
\begin{array}{l} f (\mathbf {x}) = f \left(\mathbf {x} _ {0}\right) + \left. \left[ \frac {\partial f}{\partial \mathbf {x}} \right] ^ {\prime} \right| _ {\mathbf {x} _ {0}} \left(\mathbf {x} - \mathbf {x} _ {0}\right) + \frac {1}{2 !} \left(\mathbf {x} - \mathbf {x} _ {0}\right) ^ {\prime} \left. \frac {\partial^ {2} f}{\partial \mathbf {x} ^ {2}} \right| _ {\mathbf {x} _ {0}} \left(\mathbf {x} - \mathbf {x} _ {0}\right) \\ + \mathcal {O} (3) \tag {A.2.43} \\ \end{array}
$$

where, $\mathcal{O}(3)$ indicates terms of order 3 and higher.
