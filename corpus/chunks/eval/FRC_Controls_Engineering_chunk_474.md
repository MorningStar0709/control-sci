# B.1 Derivation

Let there be a discrete time linear system defined as

$$\mathbf {x} _ {k + 1} = \mathbf {A} \mathbf {x} _ {k} + \mathbf {B} \mathbf {u} _ {k} \tag {B.1}$$

with the cost functional

$$
J = \sum_ {k = 0} ^ {\infty} \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left[ \begin{array}{c c} \mathbf {Q} & \mathbf {N} \\ \mathbf {N} ^ {\mathsf {T}} & \mathbf {R} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]
$$

where J represents a trade-off between state excursion and control effort with the weighting factors Q, R, and N. Q is the weight matrix for error, R is the weight matrix for control effort, and N is a cross weight matrix between error and control effort. N is commonly utilized when penalizing the output in addition to the state and input.

$$
J = \sum_ {k = 0} ^ {\infty} \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left[ \begin{array}{c} \mathbf {Q x} _ {k} + \mathbf {N u} _ {k} \\ \mathbf {N} ^ {\mathsf {T}} \mathbf {x} _ {k} + \mathbf {R u} _ {k} \end{array} \right]
