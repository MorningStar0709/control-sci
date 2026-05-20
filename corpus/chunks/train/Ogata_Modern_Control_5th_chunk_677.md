$$
\left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]
$$

be of rank n, or contain n linearly independent column vectors. The matrix

$$
\left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]
$$

is commonly called the controllability matrix.

EXAMPLE 9–10 Consider the system given by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 1 \\ 0 & - 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] u
$$

Since

$$
\left[ \begin{array}{c c} \mathbf {B} & \mathbf {A B} \end{array} \right] = \left[ \begin{array}{c c} 1 & 1 \\ 0 & 0 \end{array} \right] = \text { singular }
$$

the system is not completely state controllable.

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 1 \\ 2 & - 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] [ u ]
$$

For this case,

$$
\left[ \begin{array}{c c} \mathbf {B} & \mathbf {A B} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 1 & - 1 \end{array} \right] = \text { nonsingular }
$$

The system is therefore completely state controllable.

Alternative Form of the Condition for Complete State Controllability. Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} \tag {9-56}$$

where x = state vector (n-vector)

$$\mathbf {u} = \text { control vector } (r \text {-vector})\mathbf {A} = n \times n \text { matrix }\mathbf {B} = n \times r \text { matrix }$$

If the eigenvectors of A are distinct, then it is possible to find a transformation matrix P such that

$$
\mathbf {P} ^ {- 1} \mathbf {A P} = \mathbf {D} = \left[ \begin{array}{c c c c c c} \lambda_ {1} & & & & & 0 \\ & \lambda_ {2} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & \lambda_ {n} \end{array} \right]
$$

Note that if the eigenvalues of A are distinct, then the eigenvectors of A are distinct; however, the converse is not true. For example, an n\*n real symmetric matrix having multiple eigenvalues has n distinct eigenvectors. Note also that each column of the P matrix is an eigenvector of A associated with $\lambda _ { i } ( i = 1 , 2 , \ldots , n )$ .

Let us define
