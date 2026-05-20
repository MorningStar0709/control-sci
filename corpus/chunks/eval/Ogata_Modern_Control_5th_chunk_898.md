$$
\begin{array}{l} \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {0} & \mathbf {D} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \mathbf {A} ^ {- 1} & - \mathbf {A} ^ {- 1} \mathbf {B D} ^ {- 1} \\ \mathbf {0} & \mathbf {D} ^ {- 1} \end{array} \right] \\ \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ \mathbf {C} & \mathbf {D} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \mathbf {A} ^ {- 1} & \mathbf {0} \\ - \mathbf {D} ^ {- 1} \mathbf {C A} ^ {- 1} & \mathbf {D} ^ {- 1} \end{array} \right] \\ \end{array}
$$

$\mathrm { I f } \left| \mathbf { A } \right| \neq 0 , \mathbf { S } = \mathbf { D } - \mathbf { C A } ^ { - 1 } \mathbf { B } , \left| \mathbf { S } \right| \neq 0 , \mathrm { t h e n }$

$$
\left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \mathbf {A} ^ {- 1} + \mathbf {A} ^ {- 1} \mathbf {B S} ^ {- 1} \mathbf {C A} ^ {- 1} & - \mathbf {A} ^ {- 1} \mathbf {B S} ^ {- 1} \\ - \mathbf {S} ^ {- 1} \mathbf {C A} ^ {- 1} & \mathbf {S} ^ {- 1} \end{array} \right]
$$

${ \mathrm { I f } } \left| \mathbf { D } \right| \neq 0 , \mathbf { T } = \mathbf { A } - \mathbf { B } \mathbf { D } ^ { - 1 } \mathbf { C } , { \mathrm { a n d } } \left| \mathbf { T } \right| \neq 0 , { \mathrm { t h e n } }$

$$
\left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \mathbf {T} ^ {- 1} & - \mathbf {T} ^ {- 1} \mathbf {B D} ^ {- 1} \\ - \mathbf {D} ^ {- 1} \mathbf {C T} ^ {- 1} & \mathbf {D} ^ {- 1} + \mathbf {D} ^ {- 1} \mathbf {C T} ^ {- 1} \mathbf {B D} ^ {- 1} \end{array} \right]
$$

Finally, we present the MATLAB approach to obtain the inverse of a square matrix. If all elements of the matrix are given as numerical values, this approach is best.

MATLAB Approach to Obtain the Inverse of a Square Matrix. The inverse of a square matrix A can be obtained with the command

$$\operatorname{inv} (A)$$

For example, if matrix A is given by

$$
\mathbf {A} = \left[ \begin{array}{c c c} 1 & 1 & 2 \\ 3 & 4 & 0 \\ 1 & 2 & 5 \end{array} \right]
$$

then the inverse of matrix A is obtained as follows:

$$
\begin{array}{c c c c} \hline A = [ 1 1 2; 3 4 0; 1 2 5 ]; \\ \text {inv(A)} \\ \text {ans =} \\ \hline 2. 2 2 2 2 & - 0. 1 1 1 1 & - 0. 8 8 8 9 \\ - 1. 6 6 6 7 & 0. 3 3 3 3 & 0. 6 6 6 7 \\ 0. 2 2 2 2 & - 0. 1 1 1 1 & 0. 1 1 1 1 \\ \hline \end{array}
$$

That is

$$
\mathbf {A} ^ {- 1} = \left[ \begin{array}{c c c} 2. 2 2 2 2 & - 0. 1 1 1 1 & - 0. 8 8 8 9 \\ - 1. 6 6 6 7 & 0. 3 3 3 3 & 0. 6 6 6 7 \\ 0. 2 2 2 2 & - 0. 1 1 1 1 & 0. 1 1 1 1 \end{array} \right]
$$
