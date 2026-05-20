# Example 2.17 Second-order system

Consider the continuous-time transfer function

$$\frac {2}{(s + 1) (s + 2)}$$

Using Table 2.1 gives the zero of the pulse-transfer function

$$z = - \frac {(1 - e ^ {- 2 h}) e ^ {- h} - 2 (1 - e ^ {- h}) e ^ {- 2 h}}{2 (1 - e ^ {- h}) - (1 - e ^ {- 2 h})}$$

When $h$ is small

$$z \approx - 1 + 3 h$$

Table 2.4 Numerator polynomials, $Z_{d}$ , when sampling $\mathbf{s}^{-d}$ . 

<table><tr><td>d</td><td> $Z_{d}$ </td></tr><tr><td>1</td><td>1</td></tr><tr><td>2</td><td> $z + 1$ </td></tr><tr><td>3</td><td> $z^{2} + 4z + 1$ </td></tr><tr><td>4</td><td> $z^{3} + 11z^{2} + 11z + 1$ </td></tr><tr><td>5</td><td> $z^{4} + 26z^{3} + 66z^{2} + 26z + 1$ </td></tr></table>

and when h approaches zero, the zero moves to -1. The zero moves toward the origin when h is increased. The zero for small values of h also can be obtained from Table 2.4. The pole excess of the continuous-time system is d = 2. The discrete-time system will have a zero at z = -1 when h goes to zero.
