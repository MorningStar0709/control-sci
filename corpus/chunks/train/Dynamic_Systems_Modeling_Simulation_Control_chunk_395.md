Equation (7.101) is the system’s characteristic equation, which in this case is a third-order polynomial in the parameter ??. The n values of ?? for which the characteristic equation (7.101) is zero are called the eigenvalues of the system matrix A. They are used in the homogeneous state solution $\mathbf { x } ( t ) = \mathbf { c } e ^ { \lambda t }$ just as we used the characteristic roots $r _ { i }$ in the homogeneous response $y _ { H } ( t ) = c e ^ { r t }$ shown in Eq. (7.7). Hence, the eigenvalues tell us the nature of the free or transient response of a dynamic system.

Knowledge of the characteristic roots allows one to understand the natural response of linear dynamic systems, and the characteristic roots are easily determined from the system’s mathematical model, which may be represented as an I/O equation, transfer function, or SSR. This important result can be summarized as follows:

1. If the system is represented as an SISO I/O equation, then the n characteristic roots $r _ { i }$ can be obtained by solving the nth-order characteristic equation, which is readily determined from the coefficients in the I/O equation.   
2. If the system is represented as a transfer function G(s), then the n poles are the values of s that make the nth-order denominator polynomial of G(s) equal zero. The poles of G(s) are equivalent to the characteristic roots $r _ { i } .$ .   
3. If a state-space approach is used, then the n eigenvalues can be obtained from the determinant $| \lambda \mathbf { I } - \mathbf { A } | = 0$ . The eigenvalues $\lambda _ { i }$ are equivalent to the characteristic roots $r _ { i }$ and the poles of the system transfer function.

We can use MATLAB to compute the eigenvalues of the system matrix A by using the command

$$> > \text { eig } (A)$$

The following example demonstrates the equivalence between the characteristic roots, the poles of the transfer function, and the eigenvalues of the system matrix A.
