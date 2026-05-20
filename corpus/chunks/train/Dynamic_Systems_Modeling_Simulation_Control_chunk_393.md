# 7.6 STATE-SPACE REPRESENTATION AND EIGENVALUES

In Section 7.2 we presented an overview of the solution of linear ODEs with constant coefficients. Our solution process began with an assumed form for the homogenous solution, namely $y _ { H } ( t ) = c e ^ { r t }$ , which we applied to a homogeneous I/O equation. As a result, we obtained the characteristic equation (an nth-order polynomial in r), which leads to the characteristic roots. It is the characteristic roots that tell us the nature of the homogeneous response; that is, whether or not the response is stable or unstable, or the transient response is underdamped or overdamped. Recall that the poles of the system transfer function G(s) are the values of s that cause its denominator to equal zero, and that the poles of $G ( s )$ are identical to the characteristic roots. This fact should not be surprising as the system transfer function is derived from the governing I/O equation, and hence the denominator of G(s) is the same nth-order polynomial that is the characteristic equation. The reader may wish to review Example 7.3 to see the connection between the characteristic equation and its roots and the poles of the system transfer function.

In this section, we present another approach for determining the characteristic equation that is based on the state-space representation (SSR). To begin, consider the linear homogeneous state equation

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} \tag {7.92}$$

where x is the $n \times 1$ state vector, and A is the $n \times n$ state matrix composed of constant coefficients. Following our previous method of solving linear differential equations, let us assume an exponential solution form for each state variable:

$$x _ {1} (t) = c _ {1} e ^ {\lambda t}x _ {2} (t) = c _ {2} e ^ {\lambda t}x _ {n} (t) = c _ {n} e ^ {\lambda t} \tag {7.93}$$

where the constants $c _ { i }$ are generally different for each state-variable solution, but the exponential function $e ^ { \lambda t }$ is the same for each state solution. Equation (7.93) can be written in a compact vector format

$$\mathbf {x} (t) = \mathbf {c} e ^ {\lambda t} \tag {7.94}$$

where c is an $n \times 1$ column vector containing the constants $c _ { 1 } , c _ { 2 } , \ldots , c _ { n }$ . The time derivative of the assumed solution form, Eq. (7.94), is

$$\dot {\mathbf {x}} (t) = \lambda \mathbf {c} e ^ {\lambda t} \tag {7.95}$$
