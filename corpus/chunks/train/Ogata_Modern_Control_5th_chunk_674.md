# EXAMPLE 9–9 The vectors

$$
\mathbf {x} _ {1} = \left[ \begin{array}{l} 1 \\ 2 \\ 3 \end{array} \right], \quad \mathbf {x} _ {2} = \left[ \begin{array}{l} 1 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {x} _ {3} = \left[ \begin{array}{l} 2 \\ 2 \\ 4 \end{array} \right]
$$

are linearly dependent since

$$\mathbf {x} _ {1} + \mathbf {x} _ {2} - \mathbf {x} _ {3} = \mathbf {0}$$

The vectors

$$
\mathbf {y} _ {1} = \left[ \begin{array}{l} 1 \\ 2 \\ 3 \end{array} \right], \quad \mathbf {y} _ {2} = \left[ \begin{array}{l} 1 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {y} _ {3} = \left[ \begin{array}{l} 2 \\ 2 \\ 2 \end{array} \right]
$$

are linearly independent since

$$c _ {1} \mathbf {y} _ {1} + c _ {2} \mathbf {y} _ {2} + c _ {3} \mathbf {y} _ {3} = \mathbf {0}$$

implies that

$$c _ {1} = c _ {2} = c _ {3} = 0$$

Note that if an $n \times n$ matrix is nonsingular (that is, the matrix is of rank n or the determinant is nonzero) then n column (or row) vectors are linearly independent. If the n\*n matrix is singular (that is, the rank of the matrix is less than n or the determinant is zero), then n column (or row) vectors are linearly dependent. To demonstrate this, notice that

$$
\begin{array}{l} \left[ \begin{array}{c c c} \mathbf {x} _ {1} & \mathbf {x} _ {2} & \mathbf {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 1 & 2 \\ 2 & 0 & 2 \\ 3 & 1 & 4 \end{array} \right] = \text { singular } \\ \left[ \mathbf {y} _ {1} \mid \mathbf {y} _ {2} \mid \mathbf {y} _ {3} \right] = \left[ \begin{array}{l l l} 1 & 1 & 2 \\ 2 & 0 & 2 \\ 3 & 1 & 2 \end{array} \right] = \text { nonsingular } \\ \end{array}
$$
