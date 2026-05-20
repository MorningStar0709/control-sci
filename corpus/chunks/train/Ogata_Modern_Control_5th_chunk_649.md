$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} (t) \\ \dot {x} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} 0 & - 2 \\ 1 & - 3 \end{array} \right] \left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] + \left[ \begin{array}{c} 3 \\ 1 \end{array} \right] u (t) \\ y (t) = \left[ \begin{array}{c c} 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] \\ \end{array}
$$

Diagonal Canonical Form:

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} (t) \\ \dot {x} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} - 1 & 0 \\ 0 & - 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] + \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] u (t) \\ y (t) = \left[ \begin{array}{c c} 2 & - 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] \\ \end{array}
$$

Eigenvalues of an n  n Matrix A. The eigenvalues of an n\*n matrix A are the roots of the characteristic equation

$$\left| \lambda \mathbf {I} - \mathbf {A} \right| = 0$$

The eigenvalues are also called the characteristic roots.

Consider, for example, the following matrix A:

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 & - 1 1 & - 6 \end{array} \right]
$$

The characteristic equation is

$$
\begin{array}{l} | \lambda \mathbf {I} - \mathbf {A} | = \left| \begin{array}{c c c} \lambda & - 1 & 0 \\ 0 & \lambda & - 1 \\ 6 & 1 1 & \lambda + 6 \end{array} \right| \\ = \lambda^ {3} + 6 \lambda^ {2} + 1 1 \lambda + 6 \\ = (\lambda + 1) (\lambda + 2) (\lambda + 3) = 0 \\ \end{array}
$$

The eigenvalues of A are the roots of the characteristic equation, or –1, –2, and –3.

Diagonalization of n  n Matrix. Note that if an n\*n matrix A with distinct eigenvalues is given by

$$
\mathbf {A} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {n} & - a _ {n - 1} & - a _ {n - 2} & \dots & - a _ {1} \end{array} \right] \tag {9-12}
$$

the transformation $\mathbf { x } = \mathbf { P } \mathbf { z } ,$ , where
