# Example 7.5

Calculate the optimal state feedback gain for the plant

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u \quad \text { and } \quad J = \int_ {0} ^ {\infty} [ x _ {1} ^ {2} (t) + \rho u ^ {2} (t) ] d t, \qquad \rho > 0.
$$

Solution With

$$\mathbf {x} ^ {T} Q \mathbf {x} = q _ {1 1} x _ {1} ^ {2} + 2 q _ {1 2} x _ {1} x _ {2} + q _ {2 2} x _ {2} ^ {2}$$

the first term in the integrand, $x_{1}^{2}$ , implies that $q_{11} = 1$ , $q_{12} = q_{22} = 0$ ; i.e.,

$$
Q = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \end{array} \right]
$$

with

$$
A = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], \qquad \mathbf {b} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right], \qquad R = \rho .
$$

It can be verified that $(A, Q^{1/2})$ is observable. We write the matrix Riccati equation, Equation 7.28:

$$
\begin{array}{l} \left[ \begin{array}{c c} 0 & 0 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c c} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right] + \left[ \begin{array}{c c} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right] \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right] \\ - \left[ \begin{array}{c c} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \rho^ {- 1} \left[ \begin{array}{c c} 0 & 1 \end{array} \right] \left[ \begin{array}{c c} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \end{array} \right] = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] \\ \end{array}
$$

or

$$
\left[ \begin{array}{c c} 0 & 0 \\ P _ {1 1} & P _ {1 2} \end{array} \right] + \left[ \begin{array}{c c} 0 & P _ {1 1} \\ 0 & P _ {1 2} \end{array} \right] \frac {1}{\rho} \left[ \begin{array}{c} P _ {1 2} \\ P _ {2 2} \end{array} \right] \left[ \begin{array}{c c} P _ {1 2} & P _ {2 2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \end{array} \right] = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right].
$$

Equating element by element, we have the following. For the 11 element,

$$- \frac {1}{\rho} P _ {1 2} ^ {2} + 1 = 0.$$

For the 12 (or 21) element,

$$P _ {1 1} - \frac {1}{\rho} P _ {1 2} P _ {2 2} = 0.$$

For the 22 element,

$$2 P _ {1 2} - \frac {1}{\rho} P _ {2 2} ^ {2} = 0.$$

From the "11" equation,

$$P _ {1 2} = \pm \rho^ {1 / 2}.$$

The "22" equation yields

$$P _ {2 2} = \pm [ 2 \rho P _ {1 2} ] ^ {1 / 2}.$$
