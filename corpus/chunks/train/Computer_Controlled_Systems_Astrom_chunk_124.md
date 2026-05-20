$$A (z) = z ^ {n a} + a _ {1} z ^ {n a - 1} + \dots + a _ {n a}$$

and

$$B (z) = b _ {0} z ^ {n b} + b _ {1} z ^ {n b - 1} + \dots + b _ {n b}$$

the difference equation can be written as

$$A (q) y (k) = B (q) u (k) \tag {2.22}$$

When necessary, the degree of a polynomial can be indicated by a subscript, for example, $A_{na}(q)$ . Equation (2.22) can be also expressed in terms of the backward-shift operator. Notice that (2.21) can be written as

$$y (k) + a _ {1} y (k - 1) + \dots + a _ {n a} y (k - n a) = b _ {0} u (k - d) + \dots + b _ {n b} u (k - d - n b)$$

where $d = na - nb$ is the pole excess of the system. The polynomial

$$A ^ {*} (z) = 1 + a _ {1} z + \dots + a _ {n a} z ^ {n a} = z ^ {n a} A (z ^ {- 1})$$

which is obtained from the polynomial A by reversing the order of the coefficients, is called the reciprocal polynomial. Introduction of the reciprocal polynomials allows the system in (2.22) to be written as

$$A ^ {*} (q ^ {- 1}) y (k) = B ^ {*} (q ^ {- 1}) u (k - d)$$

Some care must be exercised when operating with reciprocal polynomials because $A^{**}$ is not necessarily the same as $A$ . The polynomial $A(z) = z$ has the reciprocal $A^{*}(z) = z \cdot z^{-1} = 1$ . The reciprocal of $A^{*}$ is $A^{**}(z) = 1$ , which is different from $A$ . A polynomial $A(z)$ is called self-reciprocal if

$$A ^ {*} (z) = A (z)$$
