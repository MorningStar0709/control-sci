$$
J = \sum_ {k = 0} ^ {\infty} \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\top} \left[ \begin{array}{c c} \underbrace {\mathbf {C} ^ {\top} \mathbf {Q C}} _ {\mathbf {Q}} & \underbrace {\mathbf {C} ^ {\top} \mathbf {Q D}} _ {\mathbf {N}} \\ \underbrace {\mathbf {D} ^ {\top} \mathbf {Q C}} _ {\mathbf {N} ^ {\top}} & \underbrace {\mathbf {D} ^ {\top} \mathbf {Q D} + \mathbf {R}} _ {\mathbf {R}} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] \tag {B.3}
$$

Thus, state feedback with an output cost can be defined as the following optimization problem.
