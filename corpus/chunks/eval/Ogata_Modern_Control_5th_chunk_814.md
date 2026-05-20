# MATLAB Program 10–19

% ---------- Design of quadratic optimal regulator system -

$$
A = [ 0 \quad 1; 0 \quad - 1 ];\mathrm{B} = [ 0; 1 ];
Q = \left[ \begin{array}{c c c c} 1 & 0; 0 & 1 \end{array} \right];
R = [ 1 ];K = \operatorname{lqr} (A, B, Q, R)K =
\begin{array}{c c} 1. 0 0 0 0 & 1. 0 0 0 0 \end{array}
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u
$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 3 5 & - 2 7 & - 9 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right]
$$

The performance index J is given by

$$J = \int_ {0} ^ {\infty} \left(\mathbf {x} ^ {\prime} \mathbf {Q x} + u ^ {\prime} R u\right) d t$$

where

$$
\mathbf {Q} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right], \quad R = [ 1 ]
$$

Obtain the positive-definite solution matrix P of the Riccati equation, the optimal feedback gain matrix K, and the eigenvalues of matrix A-BK.

MATLAB Program 10–20 will solve this problem.
