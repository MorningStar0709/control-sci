# 9.6.1 The Jury Criterion

The Routh criterion is used to ascertain the number of LHP roots of a polynomial. Its counterpart in discrete time is the Jury criterion [3]. We begin with the polynomial

$$p (z) = a _ {n} z ^ {n} + a _ {n - 1} z ^ {n - 1} + \dots + a _ {0}$$

and form the two rows

$$a _ {n} \quad a _ {n - 1} \dots a _ {1} a _ {0}a _ {0} \quad a _ {1} \dots a _ {n - 1} a _ {n}$$

by writing the coefficients of $p(z)$ in forward and reverse orders, respectively.

The third row is obtained by multiplying the second row by $\alpha_{n} = a_{0} / a_{n}$ and subtracting from the first row. The fourth row is the third in reverse order:

$$
\begin{array}{c c c c c} a _ {n} & a _ {n - 1} & \ldots & a _ {1} & a _ {0} \\ a _ {0} & a _ {1} & \ldots & a _ {n - 1} & a _ {n} \\ a _ {n} - \frac {a _ {0} ^ {2}}{a _ {n}} & a _ {n - 1} - \frac {a _ {0} a _ {1}}{a _ {n}} & \ldots & a _ {1} - \frac {a _ {n - 1} a _ {0}}{a _ {n}} & 0 \\ a _ {1} - \frac {a _ {n - 1} a _ {0}}{a _ {n}} & & \ldots & a _ {n} - \frac {a _ {0} ^ {2}}{a _ {n}} \end{array}
$$

Note that the last element of the third row, equal to zero, is removed from its row before the fourth row is written. The next row is formed from rows 3 and 4 in the same manner as row 3 was formed from rows 1 and 2; row 6 is row 5 in reverse order with the final zero-element removed. The procedure is repeated until there are $2n + 1$ rows, with the last having only one element.

We can always make $a_{n} > 0$ with no loss of generality. That being the case, $p(z)$ has all roots inside the unit circle if, and only if, the leading coefficients of all odd-numbered rows are positive. If these coefficients are all nonzero, the number of negative coefficients is equal to the number of roots outside the unit circle.

Example 9.9 A plant with a pulse transfer function $P(z) = \frac{z}{(z - .5)^2}$ is controlled by a 1-DOF system with a pure-gain controller $k$ . Calculate the range of values of $k$ for which the closed-loop system is stable.

Solution The closed-loop characteristic polynomial is $z^2 + (k - 1)z + 0.25$ . The Jury array is

$$
\begin{array}{c c c} 1 & k - 1 & 0. 2 5 \\ 0. 2 5 & k - 1 & 1 \\ 0. 9 3 7 5 & 0. 7 5 (k - 1) \\ 0. 7 5 (k - 1) & 0. 9 3 7 5 \\ 0. 9 3 7 5 - 0. 6 (k - 1) ^ {2} \end{array}
$$

For stability, we require

$$1 > 0, \quad 0. 9 3 7 5 > 0, \quad 0. 9 3 7 5 - 0. 6 (k - 1) ^ {2} > 0$$

or

$$(k - 1) ^ {2} > 1. 5 6 2 5| k - 1 | > 1. 2 5- 0. 2 5 < k < 2. 2 5.$$
