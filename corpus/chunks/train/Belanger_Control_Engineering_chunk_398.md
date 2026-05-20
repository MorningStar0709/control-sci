Since $P_{22}$ must be real, $P_{12}$ must be positive. Furthermore, $P_{22}$ must be positive in order that $P > 0$ . Thus,

$$P _ {1 2} = \rho^ {1 / 2} \quad \text { and } \quad P _ {2 2} = \sqrt {2} \rho^ {3 / 4}.$$

Finally,

$$P _ {1 1} = \frac {1}{\rho} P _ {1 2} P _ {2 2} = \sqrt {2} \rho^ {1 / 4}$$

so that

$$
P = \left[ \begin{array}{c c} \sqrt {2} \rho^ {1 / 4} & \rho^ {1 / 2} \\ \rho^ {1 / 2} & \sqrt {2} \rho^ {3 / 4} \end{array} \right].
$$

We verify the positivity of $P$ by ascertaining that all principal minors are positive. Here,

$$P _ {1 1} = \sqrt {2} \rho^ {1 / 4} > 0$$

and

$$\det P = \rho > 0.$$

From Equation 7.27, the optimum gain is

$$
\begin{array}{l} K = R ^ {- 1} B ^ {T} P \\ = (1 / \rho) [ 0 1 ] \left[ \begin{array}{c c} \sqrt {2} \rho^ {1 / 4} & \rho^ {1 / 2} \\ \rho^ {1 / 2} & \sqrt {2} \rho^ {3 / 4} \end{array} \right] \\ = [ \rho^ {- 1 / 2} \sqrt {2} \rho^ {- 1 / 4} ]. \\ \end{array}
$$

It is useful to examine the closed-loop eigenvalues. The closed-loop A matrix is

$$
\begin{array}{l} A - B K = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] - \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \left[ \begin{array}{l l} \rho^ {- 1 / 2} & \sqrt {2} \rho^ {- 1 / 4} \end{array} \right] \\ = \left[ \begin{array}{c c} 0 & 1 \\ - \rho^ {- 1 / 2} & - \sqrt {2} \rho^ {- 1 / 4} \end{array} \right]. \\ \end{array}
$$

This matrix is in companion form, so the characteristic polynomial is written by inspection. It is

$$s ^ {2} + \sqrt {2} \rho^ {- 1 / 4} s + \rho^ {- 1 / 2}.$$

This is of standard second-order form, i.e., of the form $s^2 + 2\zeta \omega_0 s + \omega_0^2$ . We see that $\omega_0 = \rho^{-1/4}$ and $\zeta = \sqrt{2}/2$ . The optimal control yields a damping factor $\zeta = 0.707$ , which, as we have seen, represents a good compromise between speed and overshoot. The bandwidth $\omega_0$ depends on $\rho$ . The larger $\rho$ , the smaller $\omega_0$ and, hence, the slower the response.
