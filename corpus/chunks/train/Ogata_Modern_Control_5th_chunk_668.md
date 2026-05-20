1. Form adj $\left( \lambda \mathbf { I } - \mathbf { A } \right)$ and write the elements of ad $\left( \lambda \mathbf { I } - \mathbf { A } \right)$ as factored polynomials in l.   
2. Determine $d ( \lambda )$ as the greatest common divisor of all the elements of $\operatorname { a d j } ( \lambda \mathbf { I } - \mathbf { A } )$ . Choose the coefficient of the highest-degree term in l of $d ( \lambda )$ to be 1. If there is no common divisor, $d ( \lambda ) = 1$ .   
3. The minimal polynomial $\phi ( \lambda )$ is then given as $| \lambda \mathbf { I } - \mathbf { A } |$ divided by $d ( \lambda )$ .

Matrix Exponential $e ^ { \mathbf { A } t } .$ In solving control engineering problems, it often becomes. necessary to compute $e ^ { \mathbf { A } t }$ If matrix A is given with all elements in numerical values,. MATLAB provides a simple way to compute $e ^ { \mathbf { A } T }$ , where T is a constant.

Aside from computational methods, several analytical methods are available for the computation of $e ^ { \mathbf { A } t }$ We shall present three methods here..

Computation of $e ^ { \mathbf { A } t } \colon$ Method 1. If matrix A can be transformed into a diagonal form, then $e ^ { \mathbf { A } t }$ can be given by

$$
e ^ {\mathbf {A} t} = \mathbf {P} e ^ {\mathbf {D} t} \mathbf {P} ^ {- 1} = \mathbf {P} \left[ \begin{array}{c c c c c c} e ^ {\lambda_ {1} t} & & & & & 0 \\ & e ^ {\lambda_ {2} t} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & e ^ {\lambda_ {n} t} \end{array} \right] \mathbf {P} ^ {- 1} \tag {9-46}
$$

where P is a diagonalizing matrix for A. [For the derivation of Equation (9–46), see Problem A–9–11.]

If matrix A can be transformed into a Jordan canonical form, then $e ^ { \mathbf { A } t }$ can be given by

$$e ^ {\mathbf {A} t} = \mathbf {S} e ^ {\mathbf {J} t} \mathbf {S} ^ {- 1}$$

where S is a transformation matrix that transforms matrix A into a Jordan canonical form J.

As an example, consider the following matrix A:

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & - 3 & 3 \end{array} \right]
$$

The characteristic equation is

$$\left| \lambda \mathbf {I} - \mathbf {A} \right| = \lambda^ {3} - 3 \lambda^ {2} + 3 \lambda - 1 = (\lambda - 1) ^ {3} = 0$$

Thus, matrix A has a multiple eigenvalue of order 3 at It can be shown that matrixl = 1. A has a multiple eigenvector of order 3. The transformation matrix that will transform matrix A into a Jordan canonical form can be given by

$$
\mathbf {S} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 2 & 1 \end{array} \right]
$$

The inverse of matrix S is
