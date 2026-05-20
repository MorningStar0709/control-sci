# A.7 Matrix Basics

Source: Introduction to Matrices and Determinants," F. Max Stein, 1967.

Assume A is a square matrix.

Matrix Multiplication Conceptual Denition:

A matrix is a mapping of a vector from one space to another which preserves straight lines. The matrix thus represents a linear transformation.

Algebraic Denition:

If A is a 3x3 matrix and B is a 3x1 vector,

$$
A B = \left[ \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right] \times \left[ \begin{array}{l} b _ {1} \\ b _ {2} \\ b _ {3} \end{array} \right] = \left[ \begin{array}{l} a _ {1 1} b _ {1} + a _ {1 2} b _ {2} + a _ {1 3} b _ {3} \\ a _ {2 1} b _ {1} + a _ {2 2} b _ {3} + a _ {2 3} b _ {3} \\ a _ {3 1} b _ {1} + a _ {3 2} b _ {3} + a _ {3 3} b _ {3} \end{array} \right]
$$

The rule is to multiply row by column and add component wise. This can also be written:

$$A B _ {i} = \sum_ {j = 1} ^ {N} a _ {i j} b _ {j}$$

(Did you know that Albert Einstein invented the idea of dropping the $\displaystyle \sum$ and the subscripts to simplify the notation of matrix multiplication?)
