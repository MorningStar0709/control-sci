$$
J = \sum_ {k = 0} ^ {\infty} \left(\left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left[ \begin{array}{c} \mathbf {C} ^ {\mathsf {T}} \\ \mathbf {D} ^ {\mathsf {T}} \end{array} \right] \mathbf {Q} \left[ \begin{array}{c c} \mathbf {C} & \mathbf {D} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] + \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left[ \begin{array}{c c} \mathbf {0} & \mathbf {0} \\ \mathbf {0} & \mathbf {R} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]\right)

J = \sum_ {k = 0} ^ {\infty} \left(\left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left(\left[ \begin{array}{c} \mathbf {C} ^ {\mathsf {T}} \\ \mathbf {D} ^ {\mathsf {T}} \end{array} \right] \mathbf {Q} \left[ \begin{array}{c c} \mathbf {C} & \mathbf {D} \end{array} \right] + \left[ \begin{array}{c c} \mathbf {0} & \mathbf {0} \\ \mathbf {0} & \mathbf {R} \end{array} \right]\right) \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]\right)
$$

Multiply in $\mathbf { Q } .$

$$
J = \sum_ {k = 0} ^ {\infty} \left(\left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\top} \left(\left[ \begin{array}{c} \mathbf {C} ^ {\top} \mathbf {Q} \\ \mathbf {D} ^ {\top} \mathbf {Q} \end{array} \right] \left[ \begin{array}{c c} \mathbf {C} & \mathbf {D} \end{array} \right] + \left[ \begin{array}{c c} \mathbf {0} & \mathbf {0} \\ \mathbf {0} & \mathbf {R} \end{array} \right]\right) \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]\right)
$$

Multiply matrices in the left term together.

$$
J = \sum_ {k = 0} ^ {\infty} \left(\left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left(\left[ \begin{array}{c c} \mathbf {C} ^ {\mathsf {T}} \mathbf {Q C} & \mathbf {C} ^ {\mathsf {T}} \mathbf {Q D} \\ \mathbf {D} ^ {\mathsf {T}} \mathbf {Q C} & \mathbf {D} ^ {\mathsf {T}} \mathbf {Q D} \end{array} \right] + \left[ \begin{array}{c c} \mathbf {0} & \mathbf {0} \\ \mathbf {0} & \mathbf {R} \end{array} \right]\right) \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]\right)
$$

Add the terms together.
