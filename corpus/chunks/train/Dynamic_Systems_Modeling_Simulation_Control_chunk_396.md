# Example 7.10

Given the SISO I/O equation

$$2 \ddot {y} + 8 \dot {y} + 4 0 y = 3 u \tag {7.102}$$

determine (a) the characteristic roots, (b) the poles of the transfer function, and (c) the eigenvalues of the system matrix.

First, let us write the second-order characteristic equation for this ODE

$$2 r ^ {2} + 8 r + 4 0 = 0$$

or, dividing by 2

$$r ^ {2} + 4 r + 2 0 = 0 \tag {7.103}$$

MATLAB can be used to determine the roots

$$> > \text { roots } ([ 1 4 2 0 ]) \quad \text { or } \quad > > \text { roots } ([ 2 8 4 0 ])$$

which yields the two characteristic roots, $r _ { 1 , 2 } = - 2 \pm j 4$ . Because the roots are complex, the system is underdamped.

We can derive the transfer function by applying the D operator to the governing I/O equation (7.102), which yields

$$(2 D ^ {2} + 8 D + 4 0) y = 3 u (t)$$

Next, form the ratio of output to input, $y ( t ) / u ( t )$ , and replace D with the Laplace variable s to derive the transfer function G(s)

$$G (s) = \frac {3}{2 s ^ {2} + 8 s + 4 0} = \frac {1 . 5}{s ^ {2} + 4 s + 2 0}$$

The poles of the transfer function G(s) are determined by setting the denominator polynomial to zero

$$2 s ^ {2} + 8 s + 4 0 = 0 \quad \text { or } \quad s ^ {2} + 4 s + 2 0 = 0 \tag {7.104}$$

which is identical to the characteristic equation (7.103). Hence, the poles of G(s) are equivalent to the characteristic roots $r _ { 1 . 2 } = - 2 \pm j 4$ .

1,2 Finally, to find the eigenvalues we must obtain an SSR. We can select the two states as $x _ { 1 } = y$ and $x _ { 2 } = \dot { y }$ and consequently the two state-variable equations are

$$\dot {x} _ {1} = \dot {y} = x _ {2}\dot {x} _ {2} = \ddot {y} = \frac {1}{2} (3 u - 8 \dot {y} - 4 0 y) = 1. 5 u - 4 x _ {2} - 2 0 x _ {1}$$

which can be assembled in the matrix-vector format as the state equation

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 0 & - 4 \end{array} \right] \mathbf {x} + \left[ \begin{array}{c} 0 \\ 1. 5 \end{array} \right] u
$$

The eigenvalues are computed from the determinant $| \lambda \mathbf { I } - \mathbf { A } | = 0$

$$
| \lambda \mathbf {I} - \mathbf {A} | = \left| \begin{array}{c c} \lambda & - 1 \\ 2 0 & \lambda + 4 \end{array} \right| = \lambda^ {2} + 4 \lambda + 2 0 = 0 \tag {7.105}
$$

This polynomial equation is identical to Eqs. (7.103) and (7.104), and hence it is the characteristic equation. The eigenvalues are $\lambda _ { 1 , 2 } = - 2 \pm j 4$ , and are equivalent to the characteristic roots and the poles of $G ( s )$ .
