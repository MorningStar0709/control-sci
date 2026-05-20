# 8.3.1 Lyapunov stability for linear systems

We’re going to find stability criteria for the linear system $\dot { \mathbf { x } } = \mathbf { A } \mathbf { x }$ using Lyapunov theory. Let’s use the following Lyapunov candidate function.

$$V (\mathbf {x}) = \mathbf {x} ^ {\top} \mathbf {P x} \text { where } \mathbf {P} = \mathbf {P} ^ {\top} > 0$$

This function is positive definite by definition. Its derivative is

$$
\begin{array}{l} \dot {V} (\mathbf {x}) = \dot {\mathbf {x}} ^ {\top} \mathbf {P} \mathbf {x} + \mathbf {x} ^ {\top} \dot {\mathbf {P}} \mathbf {x} + \mathbf {x} ^ {\top} \mathbf {P} \dot {\mathbf {x}} \\ \dot {V} (\mathbf {x}) = \dot {\mathbf {x}} ^ {\mathsf {T}} \mathbf {P} \mathbf {x} + \mathbf {x} ^ {\mathsf {T}} \mathbf {0 x} + \mathbf {x} ^ {\mathsf {T}} \mathbf {P} \dot {\mathbf {x}} \\ \dot {V} (\mathbf {x}) = \dot {\mathbf {x}} ^ {\mathsf {T}} \mathbf {P} \mathbf {x} + \mathbf {x} ^ {\mathsf {T}} \mathbf {P} \dot {\mathbf {x}} \\ \dot {V} (\mathbf {x}) = \left(\mathbf {A x}\right) ^ {\top} \mathbf {P x} + \mathbf {x} ^ {\top} \mathbf {P} (\mathbf {A x}) \\ \dot {V} (\mathbf {x}) = \mathbf {x} ^ {\top} \mathbf {A} ^ {\top} \mathbf {P x} + \mathbf {x} ^ {\top} \mathbf {P A x} \\ \dot {V} (\mathbf {x}) = \mathbf {x} ^ {\mathsf {T}} (\mathbf {A} ^ {\mathsf {T}} \mathbf {P} + \mathbf {P A}) \mathbf {x} \\ \end{array}
$$

For this function to be negative definite, $\mathbf { A } ^ { \mathsf { T } } \mathbf { P } + \mathbf { P } \mathbf { A }$ must be negative definite. Since P is positive definite, the only way to satisfy that condition is if A is negative definite (i.e., A is stable).
