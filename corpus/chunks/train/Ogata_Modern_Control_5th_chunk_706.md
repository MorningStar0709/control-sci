By identifying the coefficients $a _ { i }$ of the minimal polynomial (which is the same as the characteristic polynomial in this case), we have

$$a _ {1} = 3, \quad a _ {2} = - 7, \quad a _ {3} = - 1 7$$

The inverse of A can then be obtained from Equation (9–100) as follows:

$$
\begin{array}{l} \mathbf {A} ^ {- 1} = - \frac {1}{a _ {3}} \left(\mathbf {A} ^ {2} + a _ {1} \mathbf {A} + a _ {2} \mathbf {I}\right) = \frac {1}{1 7} \left(\mathbf {A} ^ {2} + 3 \mathbf {A} - 7 \mathbf {I}\right) \\ = \frac {1}{1 7} \left\{\left[ \begin{array}{c c c} 7 & 0 & - 4 \\ - 2 & 7 & 8 \\ - 2 & 2 & 9 \end{array} \right] + 3 \left[ \begin{array}{c c c} 1 & 2 & 0 \\ 3 & - 1 & - 2 \\ 1 & 0 & - 3 \end{array} \right] - 7 \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \right\} \\ = \frac {1}{1 7} \left[ \begin{array}{c c c} 3 & 6 & - 4 \\ 7 & - 3 & 2 \\ 1 & 2 & - 7 \end{array} \right] \\ = \left[ \begin{array}{c c c} \frac {3}{1 7} & \frac {6}{1 7} & - \frac {4}{1 7} \\ \frac {7}{1 7} & - \frac {3}{1 7} & \frac {2}{1 7} \\ \frac {1}{1 7} & \frac {2}{1 7} & - \frac {7}{1 7} \end{array} \right] \\ \end{array}
$$

A–9–11. Show that if matrix A can be diagonalized, then

$$e ^ {\mathbf {A} t} = \mathbf {P} e ^ {\mathbf {D} t} \mathbf {P} ^ {- 1}$$

where P is a diagonalizing transformation matrix that transforms A into a diagonal matrix, or $\mathbf { P } ^ { - 1 } \mathbf { A } \mathbf { P } = \mathbf { D } $ , where D is a diagonal matrix.

Show also that if matrix A can be transformed into a Jordan canonical form, then

$$e ^ {\mathbf {A} t} = \mathbf {S} e ^ {\mathbf {J} t} \mathbf {S} ^ {- 1}$$

where S is a transformation matrix that transforms A into a Jordan canonical form J, or $\mathbf { S } ^ { - 1 } \mathbf { A } \mathbf { S } = \mathbf { J }$ .

Solution. Consider the state equation

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x}$$

If a square matrix can be diagonalized, then a diagonalizing matrix (transformation matrix) exists and it can be obtained by a standard method. Let P be a diagonalizing matrix for A. Let us define

$$\mathbf {x} = \mathbf {P} \hat {\mathbf {x}}$$

Then

$$\dot {\hat {\mathbf {x}}} = \mathbf {P} ^ {- 1} \mathbf {A} \mathbf {P} \hat {\mathbf {x}} = \mathbf {D} \hat {\mathbf {x}}$$

where D is a diagonal matrix. The solution of this last equation is

$$\hat {\mathbf {x}} (t) = e ^ {\mathbf {D} t} \hat {\mathbf {x}} (0)$$

Hence,

$$\mathbf {x} (t) = \mathbf {P} \hat {\mathbf {x}} (t) = \mathbf {P} e ^ {\mathbf {D} t} \mathbf {P} ^ {- 1} \mathbf {x} (0)$$

Noting that x(t) can also be given by the equation
