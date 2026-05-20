# B.2.1 Gain margin

Let there be a linear system x˙ = Ax + BNu where N is a diagonal matrix of random, unknown gains on the control inputs. The gain margin is the maximum value of N for which the system is stable.

For stability analysis, we’ll use the Lyapunov function $V ( \mathbf { x } ) = \mathbf { x } ^ { \mathsf { T } } \mathbf { P } \mathbf { x }$ where P is the unique stabilizing solution to the continuous algebraic Riccati equation (CARE) $\mathbf { A } ^ { \mathsf { T } } \mathbf { P } + \mathbf { P A } - \mathbf { P B R } ^ { - 1 } \mathbf { B } ^ { \mathsf { T } } \mathbf { P } + \mathbf { Q } = \mathbf { 0 }$ . We’ll assume R is diagonal for sufficient decoupling.

The system is stable if $\dot { V } ( \mathbf { x } ) < 0$ for all $\mathbf { x } \neq \mathbf { 0 }$ .

$$\dot {\mathbf {x}} ^ {\mathsf {T}} \mathbf {P} \mathbf {x} + \mathbf {x} ^ {\mathsf {T}} \mathbf {P} \dot {\mathbf {x}} < 0$$

Substitute in the system dynamics $\dot { \mathbf { x } } = \mathbf { A x } + \mathbf { B N u }$ and their transpose $\dot { \mathbf { x } } ^ { \mathsf { T } } = \mathbf { x } ^ { \mathsf { T } } \mathbf { A } ^ { \mathsf { T } } +$ $\mathbf { u } ^ { \mathsf { T } } \mathbf { N } ^ { \mathsf { T } } \mathbf { B } ^ { \mathsf { T } }$ .

$$
\begin{array}{l} \left(\mathbf {x} ^ {\top} \mathbf {A} ^ {\top} + \mathbf {u} ^ {\top} \mathbf {N B} ^ {\top}\right) \mathbf {P x} + \mathbf {x} ^ {\top} \mathbf {P} (\mathbf {A x} + \mathbf {B N u}) <   0 \\ \mathbf {x} ^ {\top} \mathbf {A} ^ {\top} \mathbf {P x} + \mathbf {u} ^ {\top} \mathbf {N B} ^ {\top} \mathbf {P x} + \mathbf {x} ^ {\top} \mathbf {P A x} + \mathbf {x} ^ {\top} \mathbf {P B N u} <   0 \\ \mathbf {x} ^ {\top} \left(\mathbf {A} ^ {\top} \mathbf {P} + \mathbf {P A}\right) \mathbf {x} + \mathbf {u} ^ {\top} \mathbf {N B} ^ {\top} \mathbf {P x} + \mathbf {x} ^ {\top} \mathbf {P B N u} <   0 \\ \end{array}
$$

Substitute in the continuous time LQR control law $\mathbf { u } = - \mathbf { R } ^ { - 1 } \mathbf { B } ^ { \top } \mathbf { P } \mathbf { x }$ and its transpose $\mathbf { u } ^ { \mathsf { T } } = - \mathbf { x } ^ { \mathsf { T } } \mathbf { P } \mathbf { B } \mathbf { R } ^ { - 1 }$ .
