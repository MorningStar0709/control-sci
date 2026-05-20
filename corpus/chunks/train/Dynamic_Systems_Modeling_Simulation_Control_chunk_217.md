A final note is in order to explain matrix-vector multiplication. All right-hand side terms in the state and output equations involve a matrix multiplied by a column vector, and both left-hand side terms are column vectors. When multiplying a matrix and a column vector, the number of columns of the matrix must equal the number of rows of the column vector. For example, consider a case with four states (n = 4) and two inputs (r = 2). The dimensions of the matrices and vectors of the state equation for this case are

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \\ \dot {x} _ {4} \end{array} \right] = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} & a _ {1 4} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} & a _ {3 4} \\ a _ {4 1} & a _ {4 2} & a _ {4 3} & a _ {4 4} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] + \left[ \begin{array}{c c} b _ {1 1} & b _ {1 2} \\ b _ {2 1} & b _ {2 2} \\ b _ {3 1} & b _ {3 2} \\ b _ {4 1} & b _ {4 2} \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]
4 \times 1 = [ 4 \times 4 ] [ 4 \times 1 ] + [ 4 \times 2 ] [ 2 \times 1 ]
$$

Here, we see that the state matrix A must have four columns in order to multiply with the 4 × 1 state vector x, and the input matrix B must have two columns in order to multiply with the 2 × 1 input vector u. Because the left-hand side is the first derivative of 4 × 1 state vector x, both matrices A and B must have four rows.

The reader should verify that any single state-variable equation can be written by simply using the coefficients from the appropriate rows in matrices A and B. For example, the third state-variable equation is

$$\dot {x} _ {3} = a _ {3 1} x _ {1} + a _ {3 2} x _ {2} + a _ {3 3} x _ {3} + a _ {3 4} x _ {4} + b _ {3 1} u _ {1} + b _ {3 2} u _ {2}$$

which uses the coefficients from the third rows of matrices A and B. Similar arguments apply to the matrixvector multiplication for the output equation.

An SSR does not change the system dynamics; it is simply a compact matrix-vector format for representing the mathematical model (the ODEs) and the desired output variables. As previously stated, this compact format is well-suited for representing complex systems with multiple inputs and multiple outputs in a computer simulation environment such as MATLAB and Simulink. It should be stressed that an SSR can be obtained only if the mathematical modeling equations are linear. The following examples illustrate how to develop a complete SSR.
