# Inverse of a Matrix

If we have a relation

$$\mathbf {P} \mathbf {A} = \mathbf {I}, \quad \text { where } \mathbf {I} \text { is an identity matrix }, \tag {A.2.18}$$

then P is called the inverse of the matrix A denoted as $A^{-1}$ . The inverse of a matrix can be calculated in several ways. Thus,

$$\mathbf {A} ^ {- 1} = \frac {\operatorname{adj} \mathbf {A}}{| \mathbf {A} |}. \tag {A.2.19}$$

It can be easily seen that

$$\left(\mathbf {A} ^ {- 1}\right) ^ {\prime} = \left(\mathbf {A} ^ {\prime}\right) ^ {- 1}(\mathbf {A} \mathbf {B}) ^ {- 1} = \mathbf {B} ^ {- 1} \mathbf {A} ^ {- 1}. \tag {A.2.20}$$

Further, the inverse of sum of matrices is given as

$$[ \mathbf {A} + \mathbf {B C D} ] ^ {- 1} = \mathbf {A} ^ {- 1} - \mathbf {A} ^ {- 1} \mathbf {B} [ \mathbf {D A} ^ {- 1} \mathbf {B} + \mathbf {C} ^ {- 1} ] ^ {- 1} \mathbf {D A} ^ {- 1} \tag {A.2.21}$$

where, A and C are nonsingular matrices, the matrix $[A + BCD]$ can be formed and is nonsingular and the matrix $[DA^{-1}B + C^{-1}]$ is nonsingular. As a special case

$$\left[ \mathbf {I} - \mathbf {F} [ s \mathbf {I} - A ] ^ {- 1} \mathbf {B} \right] ^ {- 1} = \mathbf {I} + \mathbf {F} [ s \mathbf {I} - \mathbf {A} - \mathbf {B F} ] ^ {- 1} \mathbf {B}. \tag {A.2.22}$$

If a matrix $\mathbf{A}$ consists of submatrices as

$$
\mathbf {A} = \left[ \begin{array}{l l} \mathbf {A} _ {1 1} & \mathbf {A} _ {1 2} \\ \mathbf {A} _ {2 1} & \mathbf {A} _ {2 2} \end{array} \right] \tag {A.2.23}
$$

then

$$
| \mathbf {A} | = | \mathbf {A} _ {1 1} |. | \mathbf {A} _ {2 2} - \mathbf {A} _ {2 1} \mathbf {A} _ {1 1} ^ {- 1} \mathbf {A} _ {1 2} |= \left| \mathbf {A} _ {2 2} \right|. \left| \mathbf {A} _ {1 1} - \mathbf {A} _ {1 2} \mathbf {A} _ {2 2} ^ {- 1} \mathbf {A} _ {2 1} \right|
\mathbf {A} ^ {- 1} = \left[ \begin{array}{c c} \mathbf {E} _ {1} ^ {- 1} & - \mathbf {E} _ {1} ^ {- 1} \mathbf {A} _ {1 2} \mathbf {A} _ {2 2} ^ {- 1} \\ - \mathbf {A} _ {2 2} ^ {- 1} \mathbf {A} _ {2 1} \mathbf {E} _ {1} ^ {- 1} & \mathbf {E} _ {2} ^ {- 1} \end{array} \right] \tag {A.2.24}
$$

where, the inverses of $\mathbf{A}_{11}$ and $\mathbf{A}_{22}$ exist and

$$\mathbf {E} _ {1} = \left[ \mathbf {A} _ {1 1} - \mathbf {A} _ {1 2} \mathbf {A} _ {2 2} ^ {- 1} \mathbf {A} _ {2 1} \right], \quad \mathbf {E} _ {2} = \left[ \mathbf {A} _ {2 2} - \mathbf {A} _ {2 1} \mathbf {A} _ {1 1} ^ {- 1} \mathbf {A} _ {1 2} \right] \tag {A.2.25}$$
