# Example 2.11 Role of initial conditions

Consider the difference equation

$$y (k + 1) - a y (k) = u (k)$$

where $|a| < 1$ . In operator notation the equation can be written as

$$(q - a) y (k) = u (k) \tag {2.23}$$

If $y(k_0) = y_0$ it follows from (2.17) that the solution can be written as

$$
\begin{array}{l} y (k) = a ^ {k - k _ {0}} y _ {0} + \sum_ {j = k _ {0}} ^ {k - 1} a ^ {k - j - 1} u (j) \\ = a ^ {k - k _ {0}} y _ {0} + \sum_ {i = 1} ^ {k - k _ {0}} a ^ {i - 1} u (k - i) \\ \end{array}
$$

A formal solution of the operator equation (2.23) can be obtained as follows:

$$y (k) = \frac {1}{q - a} u (k) = \frac {q ^ {- 1}}{1 - a q ^ {- 1}} u (k)$$

Because $q^{-1}$ has unit norm, the right-hand side can be expressed as a convergent series.

$$
\begin{array}{l} y (k) = q ^ {- 1} \left(1 + a q ^ {- 1} + a ^ {2} q ^ {- 2} + \dots\right) u (k) \\ = \sum_ {i = 1} ^ {\infty} a ^ {i - 1} u (k - i) \tag {2.25} \\ \end{array}
$$

It is clear that solutions in (2.24) and (2.25) are the same only if it is assumed that $y_0 = 0$ or that $k - k_0 \to \infty$ .

It is possible to develop an operator algebra that allows division by an arbitrary polynomial in $q$ if it is assumed that there is some $k_0$ such that all sequences are zero for $k \leq k_0$ . This algebra then allows the normal manipulations of multiplication and division of equations by polynomials in the shift operator as well as addition and subtraction of equations. However, the assumption does imply that all initial conditions for the difference equation are zero, which is the convention used in this book. (Compare with Example 2.11.)

If no assumptions on the input sequences are made, it is possible to develop a slightly different shift-operator algebra that allows division only by polynomials with zeros inside the unit disc. This corresponds to the fact that effects of initial conditions on stable modes will eventually vanish. This algebra is slightly more complicated because it does not allow normal division.
