where the $i$ th row of $T^{-1}$ is orthogonal to all columns of $T$ except the $i$ th column, whose scalar product with the $i$ th row of $T^{-1}$ is unity. It turns out that the rows of $T^{-1}$ are left eigenvectors and generalized eigenvectors of $A$ . The order is the reverse of that of the right eigenvectors, in that the last generalized eigenvector in the chain comes first, down to the eigenvector. Thus, $\mathbf{w}_{11}^{2^T}, \mathbf{w}_{12}^{1^T}$ , and $\mathbf{w}_{21}^{1^T}$ are left eigenvectors of $A$ .

We now form the product $T^{-1}AT$ , starting with

$$A T =\left[ s _ {1} \mathbf {v} _ {1 1} ^ {0} \quad \mathbf {v} _ {1 1} ^ {0} + s _ {1} \mathbf {v} _ {1 1} ^ {1} \quad \mathbf {v} _ {1 1} ^ {1} + s _ {1} \mathbf {v} _ {1 1} ^ {2} \quad s _ {1} \mathbf {v} _ {1 2} ^ {0} \mathbf {v} _ {1 2} ^ {0} + s _ {1} \mathbf {v} _ {1 2} ^ {1} s _ {2} \mathbf {v} _ {2 1} ^ {0} \quad \mathbf {v} _ {2 1} ^ {0} + s _ {2} \mathbf {v} _ {2 1} ^ {1} \right]$$

where Equation 3.71 was used in the form

$$A \mathbf {v} _ {i} ^ {j + 1} = \mathbf {v} _ {i} ^ {j} + s _ {i} \mathbf {v} _ {i} ^ {j + 1}.$$

The product $T^{-1}AT$ is formed, generating the $i$ th column by multiplying each row of $T^{-1}$ by the $i$ th column of $AT$ . The result is

$$
T ^ {- 1} A T = \left[ \begin{array}{c c c c c c c} s _ {1} & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & s _ {1} & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & s _ {1} & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & s _ {1} & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & s _ {1} & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & s _ {2} & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & s _ {2} \end{array} \right]. \tag {3.74}
$$

This matrix is block diagonal. The blocks are called Jordan blocks, and there are as many of them as there are generalized eigenvector chains. The independent-eigenvector case generates $1 \times 1$ Jordan blocks, as a special case.

Equations for $T^{-1}B$ and $CT$ are easily written, as were Equations 3.63 and 3.64. The following state equations result:

$$
\dot {\mathbf {z}} _ {1} = \left[ \begin{array}{l l l} s _ {1} & 1 & 0 \\ 0 & s _ {1} & 1 \\ 0 & 0 & s _ {1} \end{array} \right] \dot {\mathbf {z}} _ {1} + \left[ \begin{array}{l} \mathbf {w} _ {1 1} ^ {0 ^ {T}} B \\ \mathbf {w} _ {1 1} ^ {1 ^ {T}} B \\ \mathbf {w} _ {1 1} ^ {2 ^ {T}} B \end{array} \right] \mathbf {u}

\dot {\mathbf {z}} _ {2} = \left[ \begin{array}{c c} s _ {1} & 1 \\ 0 & s _ {1} \end{array} \right] \mathbf {z} _ {2} + \left[ \begin{array}{c} \mathbf {w} _ {1 2} ^ {0 ^ {T}} B \\ \mathbf {w} _ {1 2} ^ {1 ^ {T}} B \end{array} \right] \mathbf {u}
