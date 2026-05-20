$$
\mathbf {f} = \mathbf {f} (\mathbf {y}, \mathbf {x}, t), \quad \mathbf {y} = \mathbf {y} (\mathbf {x}, t), \quad \mathbf {x} = \mathbf {x} (t)
\begin{array}{l} \frac {d \mathbf {f}}{d \mathbf {x}} = \left[ \frac {\partial \mathbf {f} ^ {\prime}}{\partial \mathbf {y}} \right] ^ {\prime} \left[ \frac {\partial \mathbf {y} ^ {\prime}}{\partial \mathbf {x}} \right] ^ {\prime} + \frac {\partial \mathbf {f}}{\partial \mathbf {x}} \\ = \left[ \frac {\partial \mathbf {f}}{\partial \mathbf {y}} \right] \left[ \frac {\partial \mathbf {y}}{\partial \mathbf {x}} \right] + \frac {\partial \mathbf {f}}{\partial \mathbf {x}} \\ \end{array}
\frac {d \mathbf {f}}{d t} = \left[ \frac {\partial \mathbf {f} ^ {\prime}}{\partial \mathbf {y}} \right] ^ {\prime} \left[ \left\{\frac {\partial \mathbf {y} ^ {\prime}}{\partial \mathbf {x}} \right\} ^ {\prime} \frac {d \mathbf {x}}{d t} + \frac {\partial \mathbf {y}}{\partial t} \right] + \left[ \frac {\partial \mathbf {f} ^ {\prime}}{\partial \mathbf {x}} \right] ^ {\prime} \frac {d \mathbf {x}}{d t} + \frac {\partial \mathbf {f}}{\partial t}= \left[ \frac {\partial \mathbf {f}}{\partial \mathbf {y}} \right] \left[ \left\{\frac {\partial \mathbf {y}}{\partial \mathbf {x}} \right\} \frac {d \mathbf {x}}{d t} + \frac {\partial \mathbf {y}}{\partial t} \right] + \left[ \frac {\partial \mathbf {f}}{\partial \mathbf {x}} \right] \frac {d \mathbf {x}}{d t} + \frac {\partial \mathbf {f}}{\partial t}. \tag {A.2.37}
$$

Differentiation of a Matrix w.r.t. a Scalar

If each element of a matrix is a function of a scalar variable t, then the matrix $\mathbf{A}(t)$ is said to be a function of t. Then the derivative of the matrix $\mathbf{A}(t)$ is defined as

$$
\frac {d \mathbf {A} (t)}{d t} = \left[ \begin{array}{c c c c} \frac {d a _ {1 1}}{d t} & \frac {d a _ {1 2}}{d t} & \dots & \frac {d a _ {1 m}}{d t} \\ \frac {d a _ {2 1}}{d t} & \frac {d a _ {2 2}}{d t} & \dots & \frac {d a _ {2 m}}{d t} \\ \dots & \dots & \dots & \dots \\ \frac {d a _ {n 1}}{d t} & \frac {d a _ {n 2}}{d t} & \dots & \frac {d a _ {n m}}{d t} \end{array} \right]. \tag {A.2.38}
$$

It follows (from chain rule) that

$$\frac {d}{d t} [ \mathbf {A} (t) \mathbf {B} (t) ] = \frac {d \mathbf {A} (t)}{d t} \mathbf {B} (t) + \mathbf {A} (t) \frac {d \mathbf {B} (t)}{d t}. \tag {A.2.39}$$

It is obvious that

$$\frac {d}{d t} \left[ e ^ {\mathbf {A} t} \right] = \mathbf {A} e ^ {\mathbf {A} t} = e ^ {\mathbf {A} t} \mathbf {A}\frac {d}{d t} \left[ \mathbf {A} ^ {- 1} (t) \right] = - \mathbf {A} ^ {- 1} (t) \frac {d \mathbf {A} (t)}{d t} \mathbf {A} ^ {- 1} (t). \tag {A.2.40}$$
