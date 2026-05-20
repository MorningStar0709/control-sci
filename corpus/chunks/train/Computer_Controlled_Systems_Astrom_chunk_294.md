# Solving the Diophantine Equation

To solve the Diophantine equation we simply have to keep track of the intermediate steps in Euclid's algorithm. This can be done conveniently as follows. At the same time we also obtain the minimum-degree solutions U and V to the equation

$$A U + B V = 0 \tag {5.13}$$

Equations (5.12) and (5.13) can be written as

$$
\left( \begin{array}{l l} X & Y \\ U & V \end{array} \right) \binom {A} {B} = \binom {G} {0} \tag {5.14}
$$

which implies that

$$
\left( \begin{array}{l l} X & Y \\ U & V \end{array} \right) \left( \begin{array}{l l l} A & 1 & 0 \\ B & 0 & 1 \end{array} \right) = \left( \begin{array}{l l l} G & X & Y \\ 0 & U & V \end{array} \right) \tag {5.15}
$$

To determine the matrices X, Y, U, and V we can thus start with the matrix

$$
\left( \begin{array}{c c c} A & 1 & 0 \\ B & 0 & 1 \end{array} \right) \tag {5.16}
$$

and perform elementary row operations until a matrix with a zero in the 2,1 position is obtained, that is,

$$
\left( \begin{array}{c c c} G & X & Y \\ 0 & U & V \end{array} \right) \tag {5.17}
$$

The polynomials X, Y, U, and V are then obtained directly from the elements of this matrix. This algorithm is called the extended Euclidean algorithm. It is now straightforward to solve the Diophantine equation (5.4). This can be done as follows.
