Multiply matrices in the left term together.

$$J = \sum_ {k = 0} ^ {\infty}
\left(\left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left(\left[ \begin{array}{c c} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\mathsf {T}} \mathbf {Q} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) & (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\mathsf {T}} \mathbf {Q} (\mathbf {C B}) \\ (\mathbf {C B}) ^ {\mathsf {T}} \mathbf {Q} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) & (\mathbf {C B}) ^ {\mathsf {T}} \mathbf {Q} (\mathbf {C B}) \end{array} \right] \right. \right.

\left. + \left[\begin{array}{c c}\mathbf {0}&\mathbf {0}\\\mathbf {0}&\mathbf {R}\end{array}\right]\right)\left[\begin{array}{c}\mathbf {x} _ {k}\\\mathbf {u} _ {k}\end{array}\right]\left. \right)
$$

Add the terms together.

$$J = \sum_ {k = 0} ^ {\infty}
\left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\top} \left[ \begin{array}{c c} \underbrace {(\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\top} \mathbf {Q} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C})} _ {\mathbf {Q}} & \underbrace {(\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\top} \mathbf {Q} (\mathbf {C B})} _ {\mathbf {N}} \\ \underbrace {(\mathbf {C B}) ^ {\top} \mathbf {Q} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C})} _ {\mathbf {N} ^ {\top}} & \underbrace {(\mathbf {C B}) ^ {\top} \mathbf {Q} (\mathbf {C B}) + \mathbf {R}} _ {\mathbf {R}} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] \tag {B.5}
$$

Thus, implicit model following can be defined as the following optimization problem.
