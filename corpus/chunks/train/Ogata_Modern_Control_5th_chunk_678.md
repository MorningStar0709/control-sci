$$\mathbf {x} = \mathbf {P z} \tag {9-57}$$

Substituting Equation (9–57) into Equation (9–56), we obtain

$$\dot {\mathbf {z}} = \mathbf {P} ^ {- 1} \mathbf {A} \mathbf {P} \mathbf {z} + \mathbf {P} ^ {- 1} \mathbf {B} \mathbf {u} \tag {9-58}$$

By defining

$$\mathbf {P} ^ {- 1} \mathbf {B} = \mathbf {F} = \left(f _ {i j}\right)$$

we can rewrite Equation (9–58) as

$$
\begin{array}{l} \dot {z} _ {1} = \lambda_ {1} z _ {1} + f _ {1 1} u _ {1} + f _ {1 2} u _ {2} + \dots + f _ {1 r} u _ {r} \\ \dot {z} _ {2} = \lambda_ {2} z _ {2} + f _ {2 1} u _ {1} + f _ {2 2} u _ {2} + \dots + f _ {2 r} u _ {r} \\ \dot {z} _ {n} = \lambda_ {n} z _ {n} + f _ {n 1} u _ {1} + f _ {n 2} u _ {2} + \dots + f _ {n r} u _ {r} \\ \end{array}
$$

If the elements of any one row of the $n \times r$ matrix F are all zero, then the corresponding state variable cannot be controlled by any of the $u _ { i } .$ . Hence, the condition of complete state controllability is that if the eigenvectors of A are distinct, then the system is completely state controllable if and only if no row of $\mathbf { P } ^ { - 1 } \mathbf { B }$ has all zero elements. It is important to note that, to apply this condition for complete state controllability, we must put the matrix $\mathbf { P } ^ { - 1 } \mathbf { A } \mathbf { P }$ in Equation (9–58) in diagonal form.

If the A matrix in Equation (9–56) does not possess distinct eigenvectors, then diagonalization is impossible. In such a case, we may transform A into a Jordan canonical form. If, for example, A has eigenvalues $\lambda _ { 1 } , \lambda _ { 1 } , \lambda _ { 1 } , \lambda _ { 4 } , \lambda _ { 4 } , \lambda _ { 6 } , \ldots , \lambda _ { n }$ and has $n - 3$ distinct eigenvectors, then the Jordan canonical form of A is

$$
\mathbf {J} = \left[ \begin{array}{c c c c c c c c c} \lambda_ {1} & 1 & 0 & & & & & & 0 \\ 0 & \lambda_ {1} & 1 & & & & & & \\ 0 & 0 & \lambda_ {1} & & & & & & \\ \hline & & & \lambda_ {4} & 1 & & & & \\ & & & 0 & \lambda_ {4} & & & & \\ \hline & & & & & \lambda_ {6} & & \\ & & & & & & \cdot & \\ & & & & & & & \cdot \\ 0 & & & & & & & \cdot \\ \hline \end{array} \right]
$$

The square submatrices on the main diagonal are called Jordan blocks.

Suppose that we can find a transformation matrix S such that

$$\mathbf {S} ^ {- 1} \mathbf {A} \mathbf {S} = \mathbf {J}$$

If we define a new state vector z by

$$\mathbf {x} = \mathbf {S z} \tag {9-59}$$

then substitution of Equation (9–59) into Equation (9–56) yields
