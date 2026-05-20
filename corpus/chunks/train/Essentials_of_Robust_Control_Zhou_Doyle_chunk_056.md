\left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ 0 & A _ {2 2} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} A _ {1 1} ^ {- 1} & - A _ {1 1} ^ {- 1} A _ {1 2} A _ {2 2} ^ {- 1} \\ 0 & A _ {2 2} ^ {- 1} \end{array} \right].
$$

The following identity is also very useful. Suppose $A _ { 1 1 }$ and $A _ { 2 2 }$ are both nonsingular matrices; then

$$(A _ {1 1} - A _ {1 2} A _ {2 2} ^ {- 1} A _ {2 1}) ^ {- 1} = A _ {1 1} ^ {- 1} + A _ {1 1} ^ {- 1} A _ {1 2} (A _ {2 2} - A _ {2 1} A _ {1 1} ^ {- 1} A _ {1 2}) ^ {- 1} A _ {2 1} A _ {1 1} ^ {- 1}.$$

As a consequence of the matrix decomposition formulas mentioned previously, we can calculate the determinant of a matrix by using its submatrices. Suppose $A _ { 1 1 }$ is nonsingular; then

$$\det A = \det A _ {1 1} \det (A _ {2 2} - A _ {2 1} A _ {1 1} ^ {- 1} A _ {1 2}).$$

On the other hand, if $A _ { 2 2 }$ is nonsingular, then

$$\det A = \det A _ {2 2} \det (A _ {1 1} - A _ {1 2} A _ {2 2} ^ {- 1} A _ {2 1}).$$

In particular, for any $B \in \mathbb { C } ^ { m \times n }$ and $C \in \mathbb { C } ^ { n \times m }$ , we have

$$
\det {\left[ \begin{array}{l l} I _ {m} & B \\ - C & I _ {n} \end{array} \right]} = \det (I _ {n} + C B) = \det (I _ {m} + B C)
$$

and for $x , y \in \mathbb { C } ^ { n }$

$$\det (I _ {n} + x y ^ {*}) = 1 + y ^ {*} x.$$

Related MATLAB Commands: inv, det
