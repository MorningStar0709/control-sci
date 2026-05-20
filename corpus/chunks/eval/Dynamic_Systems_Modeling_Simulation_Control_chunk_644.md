# Impulse Response

In Chapter 7 we investigated a linear system’s homogeneous or free response, which depends on the “natural dynamics” of the system, which in turn can be determined by evaluating the roots of the characteristic equation. For a system composed of a single transfer function, the free response depends on the poles of transfer function. Because the seat-suspension system has multiple states, the state-space method is likely the best format for the system dynamics. Hence, the natural dynamics of the seat-suspension system can be determined by evaluating the eigenvalues of the state matrix A. The reader should recall that the poles of a system’s transfer function and the eigenvalues of the system’s state matrix A are both equivalent to the roots of the characteristic equation.

Table 11.1 Parameters for the Seat-Suspension System

<table><tr><td>System Parameter</td><td>Value</td></tr><tr><td>Seat mass,  $m_{1}$ </td><td>20 kg</td></tr><tr><td>Driver mass,  $m_{2}$ </td><td>50 kg</td></tr><tr><td>Suspension stiffness,  $k_{1}$ </td><td>7410 N/m</td></tr><tr><td>Suspension friction coefficient,  $b_{1}$ </td><td>1430 N-s/m</td></tr><tr><td>Seat cushion stiffness,  $k_{2}$ </td><td>8230 N/m</td></tr><tr><td>Seat cushion friction coefficient,  $b_{2}$ </td><td>153 N-s/m</td></tr></table>

The state matrix of the seat-suspension system can be computed by using the numerical parameters in Table 11.1, and the result is

$$
\mathbf {A} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ - 7 8 2 & - 7 9. 1 5 & 4 1 1. 5 & 7. 6 5 \\ 0 & 0 & 0 & 1 \\ 1 6 4. 6 & 3. 0 6 & - 1 6 4. 6 & - 3. 0 6 \end{array} \right]
$$

The system eigenvalues are computed using the MATLAB command

$$> > \text { eig } (A)$$

The four eigenvalues (or characteristic roots) are

$$r _ {1} = - 6 7. 5 9 5 8 \quad r _ {2} = - 7. 2 6 7 5 \quad r _ {3} = - 3. 6 7 3 3 + j 1 0. 5 1 8 9 \quad r _ {4} = - 3. 6 7 3 3 - j 1 0. 5 1 8 9$$

Two roots are real and negative, and two roots are complex with negative real parts. Consequently, the free response will eventually decay to zero as the system reaches its steady-state value. The general form of the free response (for either output) is

$$y _ {H} (t) = c _ {1} e ^ {- 6 7. 5 9 5 8 t} + c _ {2} e ^ {- 7. 2 6 7 5 t} + c _ {3} e ^ {- 3. 6 7 3 3 t} \cos (1 0. 5 1 8 9 t + \phi) \tag {11.4}$$
