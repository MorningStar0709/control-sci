$$
\mathbf {P} = \left[ \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ \lambda_ {1} & \lambda_ {2} & \dots & \lambda_ {n} \\ \lambda_ {1} ^ {2} & \lambda_ {2} ^ {2} & \dots & \lambda_ {n} ^ {2} \\ \cdot & \cdot & & \cdot \\ \cdot & \cdot & & \cdot \\ \cdot & \cdot & & \cdot \\ \lambda_ {1} ^ {n - 1} & \lambda_ {2} ^ {n - 1} & \dots & \lambda_ {n} ^ {n - 1} \end{array} \right]
\lambda_ {1}, \lambda_ {2}, \dots , \lambda_ {n} = n \text { distinct eigenvalues of } \mathbf {A}
$$

will transform $\mathbf { P } ^ { - 1 } \mathbf { A } \mathbf { P }$ into the diagonal matrix, or

$$
\mathbf {P} ^ {- 1} \mathbf {A P} = \left[ \begin{array}{c c c c c c} \lambda_ {1} & & & & & 0 \\ & \lambda_ {2} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & \lambda_ {n} \end{array} \right]
$$

If the matrix A defined by Equation (9–12) involves multiple eigenvalues, then diagonalization is impossible. For example, if the $3 \times 3$ matrix A, where

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right]
$$

has the eigenvalues $\lambda _ { 1 } , \lambda _ { 1 } , \lambda _ { 3 }$ , then the transformation $\mathbf { x } = \mathbf { S } \mathbf { z } $ , where

$$
\mathbf {S} = \left[ \begin{array}{c c c} 1 & 0 & 1 \\ \lambda_ {1} & 1 & \lambda_ {3} \\ \lambda_ {1} ^ {2} & 2 \lambda_ {1} & \lambda_ {3} ^ {2} \end{array} \right]
$$

will yield

$$
\mathbf {S} ^ {- 1} \mathbf {A} \mathbf {S} = \left[ \begin{array}{c c c} \lambda_ {1} & 1 & 0 \\ 0 & \lambda_ {1} & 0 \\ 0 & 0 & \lambda_ {3} \end{array} \right]
$$

This is in the Jordan canonical form.

EXAMPLE 9–2 Consider the following state-space representation of a system.

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 & - 1 1 & - 6 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ 6 \end{array} \right] u \tag {9-13}

y = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] \tag {9-14}
$$

Equations (9–13) and (9–14) can be put in a standard form as

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {9-15}y = \mathbf {C x} \tag {9-16}$$

where
