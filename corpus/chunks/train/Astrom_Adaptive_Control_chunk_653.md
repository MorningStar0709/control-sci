# Euclid's Algorithm

This algorithm finds the greatest common divisor G of two polynomials A and B. If one of the polynomials, say B, is zero, then G is equal to A. If this is not the case, the algorithm is as follows. Put $A_{0} = A$ and $B_{0} = B$ and iterate the equations

$$A _ {n + 1} = B _ {n} \tag {11.7}B _ {n + 1} = A _ {n} \bmod B _ {n}$$

until $B_{n+1} = 0$ . The greatest common divisor is then $G = B_{n}$ . When A and B are polynomials, A mod B means the remainder when A is divided by B. This is in full agreement with the case when A and B are numbers. Backtracking, we find that G can be expressed as

$$A X + B Y = G \tag {11.8}$$

where the polynomials X and Y can be found by keeping track of $A_{n}$ div $B_{n}$ in Euclid's algorithm. This establishes the link between Euclid's algorithm and the Diophantine equation. The extended Euclidean algorithm gives a convenient way to determine X and Y as well as the minimum-degree solutions U and V to

$$A U + B V = 0 \tag {11.9}$$

Equations (11.8) and (11.9) can be written as

$$
F \binom {A} {B} = \left( \begin{array}{l l} X & Y \\ U & V \end{array} \right) \binom {A} {B} = \binom {G} {0} \tag {11.10}
$$

The matrix $F$ can thus be viewed as the matrix, which performs row operations on $\left( \begin{array}{cc} A & B \end{array} \right)^T$ to give $\left( \begin{array}{cc} G & 0 \end{array} \right)^T$ . A convenient way to find $F$ is to observe that

$$
{\left( \begin{array}{l l} {X} & {Y} \\ {U} & {V} \end{array} \right)} {\left( \begin{array}{l l l} {A} & {1} & {0} \\ {B} & {0} & {1} \end{array} \right)} = {\left( \begin{array}{l l l} {G} & {X} & {Y} \\ {0} & {U} & {V} \end{array} \right)}
$$

The extended Euclidean algorithm can be expressed as follows: Start with the matrix

$$
M = \left( \begin{array}{c c c} A & 1 & 0 \\ B & 0 & 1 \end{array} \right)
$$

If we assume that $\deg A \geq \deg B$ , then calculate Q = A div B, multiply the second row of M by Q, and subtract from the first row. Then apply the same procedure to the second row and repeat until the following matrix is obtained:

$$
\left( \begin{array}{c c c} G & X & Y \\ 0 & U & V \end{array} \right)
$$

A nice feature of this algorithm is that possible common factors in A and B are determined automatically. The essential difficulty in implementing the algorithm is to find a good way to test for a polynomial being zero.
