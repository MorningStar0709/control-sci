# Example 4.3 An unreachable system

The system

$$
x (k + 1) = \left( \begin{array}{c c} 0. 5 & 1 \\ 0 & 0. 3 \end{array} \right) x (k) + \binom {1} {0} u (k)
$$

is not reachable because

$$
\det W _ {c} = \det \left( \begin{array}{c c} 1 & 0. 5 \\ 0 & 0 \end{array} \right) = 0
$$

The control law $u = -l_{1}x_{1} - l_{2}x_{2}$ gives a closed-loop system with the characteristic equation

$$(z - 0. 5 + l _ {1}) (z - 0. 3) = 0$$

The open-loop pole in 0.5 can be changed to an arbitrary value by changing the parameter $l_{1}$ . The second pole 0.3, which corresponds to the nonreachable state, cannot be changed.
