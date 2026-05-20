# 2.3 Matrix Inversion Formulas

Let A be a square matrix partitioned as follows:

$$
A := \left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right],
$$

where $A _ { 1 1 }$ and $A _ { 2 2 }$ are also square matrices. Now suppose $A _ { 1 1 }$ is nonsingular; then A has the following decomposition:

$$
\left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ A _ {2 1} A _ {1 1} ^ {- 1} & I \end{array} \right] \left[ \begin{array}{c c} A _ {1 1} & 0 \\ 0 & \Delta \end{array} \right] \left[ \begin{array}{c c} I & A _ {1 1} ^ {- 1} A _ {1 2} \\ 0 & I \end{array} \right]
$$

with $\Delta : = A _ { 2 2 } - A _ { 2 1 } A _ { 1 1 } ^ { - 1 } A _ { 1 2 }$ , and A is nonsingular iff ∆ is nonsingular. Dually, if $A _ { 2 2 }$ is nonsingular, then

$$
\left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} I & A _ {1 2} A _ {2 2} ^ {- 1} \\ 0 & I \end{array} \right] \left[ \begin{array}{c c} \hat {\Delta} & 0 \\ 0 & A _ {2 2} \end{array} \right] \left[ \begin{array}{c c} I & 0 \\ A _ {2 2} ^ {- 1} A _ {2 1} & I \end{array} \right]
$$

with $\hat { \Delta } : = A _ { 1 1 } - A _ { 1 2 } A _ { 2 2 } ^ { - 1 } A _ { 2 1 }$ , and A is nonsingular iff $\hat { \Delta }$ is nonsingular. The matrix ∆ (∆) is called the ˆ Schur complement of $A _ { 1 1 } \ \left( A _ { 2 2 } \right)$ in A.

Moreover, if A is nonsingular, then

$$
\left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} A _ {1 1} ^ {- 1} + A _ {1 1} ^ {- 1} A _ {1 2} \Delta^ {- 1} A _ {2 1} A _ {1 1} ^ {- 1} & - A _ {1 1} ^ {- 1} A _ {1 2} \Delta^ {- 1} \\ - \Delta^ {- 1} A _ {2 1} A _ {1 1} ^ {- 1} & \Delta^ {- 1} \end{array} \right]
$$

and

$$
\left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \hat {\Delta} ^ {- 1} & - \hat {\Delta} ^ {- 1} A _ {1 2} A _ {2 2} ^ {- 1} \\ - A _ {2 2} ^ {- 1} A _ {2 1} \hat {\Delta} ^ {- 1} & A _ {2 2} ^ {- 1} + A _ {2 2} ^ {- 1} A _ {2 1} \hat {\Delta} ^ {- 1} A _ {1 2} A _ {2 2} ^ {- 1} \end{array} \right].
$$

The preceding matrix inversion formulas are particularly simple if A is block triangular:

$$
\left[ \begin{array}{c c} A _ {1 1} & 0 \\ A _ {2 1} & A _ {2 2} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} A _ {1 1} ^ {- 1} & 0 \\ - A _ {2 2} ^ {- 1} A _ {2 1} A _ {1 1} ^ {- 1} & A _ {2 2} ^ {- 1} \end{array} \right]
