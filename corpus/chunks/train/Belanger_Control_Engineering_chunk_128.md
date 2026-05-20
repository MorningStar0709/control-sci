# Example 3.15 (Active Suspension)

Examine the controllability of the (linearized) suspension system in Example 2.2 (Chapter 2).

Solution We use the eigenvector method, for no special reason except to illustrate its use. The eigenvalues and eigenvectors of the $A$ matrix were calculated in Example 3.11; we need them for $A^T$ . The eigenvalues of $A^T$ are the same as those of $A$ , but the eigenvectors are not, and must be calculated. The eigenvalues and eigenvectors of $A^{T}$ are as follows:

$$
\begin{array}{l} - 6. 1 5 2 3 \pm j 2 4. 5 3 4 \quad \text { and } \quad \left[ \begin{array}{c} - 9. 3 3 2 \times 1 0 ^ {- 2} \\ 1 \\ - 1. 8 0 0 \times 1 0 ^ {- 2} \\ 9. 0 4 9 \times 1 0 ^ {- 3} \end{array} \right] \pm j \left[ \begin{array}{c} - 6. 0 6 3 \times 1 0 ^ {- 3} \\ 0 \\ 2. 4 2 5 \times 1 0 ^ {- 3} \\ - 3. 7 1 4 \times 1 0 ^ {- 2} \end{array} \right] \\ - 0. 8 4 7 7 \pm j 2. 9 4 2 8 \quad \text {and} \quad \left[ \begin{array}{c} 1 \\ - 1. 6 3 5 \times 1 0 ^ {- 1} \\ 1. 0 9 6 \times 1 0 ^ {- 1} \\ 4. 1 4 2 \times 1 0 ^ {- 3} \end{array} \right] \pm j \left[ \begin{array}{c} 0 \\ 6. 0 3 5 \times 1 0 ^ {- 1} \\ - 3. 1 3 8 \times 1 0 ^ {- 1} \\ - 3. 2 5 0 \times 1 0 ^ {- 3} \end{array} \right] \\ \end{array}
$$

The $B$ matrix is

$$
B = \left[ \begin{array}{c} 0 \\ 0 \\ . 0 0 3 3 4 \\ . 0 2 \end{array} \right].
$$

Clearly, neither vector is orthogonal to $B$ , and the system is controllable.
