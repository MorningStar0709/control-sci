# 5.12.2 Hessian

The Hessian is the second-order partial derivative of a vector-valued function with respect to one of its vector arguments. For example, the Hessian of f with respect to x is

$$
\frac {\partial^ {2} \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x} ^ {2}} = \left[ \begin{array}{c c c} \frac {\partial^ {2} \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial x _ {1} ^ {2}} & \ldots & \frac {\partial^ {2} \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial x _ {m} ^ {2}} \end{array} \right] = \left[ \begin{array}{c c c} \frac {\partial^ {2} f _ {1}}{\partial x _ {1} ^ {2}} & \ldots & \frac {\partial^ {2} f _ {1}}{\partial x _ {m} ^ {2}} \\ \vdots & \ddots & \vdots \\ \frac {\partial^ {2} f _ {m}}{\partial x _ {1} ^ {2}} & \ldots & \frac {\partial^ {2} f _ {m}}{\partial x _ {m} ^ {2}} \end{array} \right]
$$

and the Hessian of f with respect to u is

$$
\frac {\partial^ {2} \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial \mathbf {u} ^ {2}} = \left[ \begin{array}{c c c} \frac {\partial^ {2} \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial u _ {1} ^ {2}} & \ldots & \frac {\partial^ {2} \mathbf {f} (\mathbf {x} , \mathbf {u})}{\partial u _ {n} ^ {2}} \end{array} \right] = \left[ \begin{array}{c c c} \frac {\partial^ {2} f _ {1}}{\partial u _ {1} ^ {2}} & \ldots & \frac {\partial^ {2} f _ {1}}{\partial u _ {n} ^ {2}} \\ \vdots & \ddots & \vdots \\ \frac {\partial^ {2} f _ {m}}{\partial u _ {1} ^ {2}} & \ldots & \frac {\partial^ {2} f _ {m}}{\partial u _ {n} ^ {2}} \end{array} \right]
$$
