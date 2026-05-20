# Example 12.11 LQG for first order system

Consider a system characterized by

$$
\begin{array}{l} \boldsymbol {A} (z) = z + a \quad a \neq 0 \\ \boldsymbol {B} (z) = \boldsymbol {b} \\ C (z) = z + c \\ \end{array}
$$

To find the control law that minimizes the criterion of (12.8), the spectral-factorization problem is first solved. Equation (12.45) can be written as

$$r (z + p _ {1}) (z ^ {- 1} + p _ {1}) = \rho (z + a) (z ^ {- 1} + a) + b ^ {2}$$

Equating coefficients of equal powers of z gives

$$r p _ {1} = \rho ar (1 + p _ {1} ^ {2}) = \rho (1 + a ^ {2}) + b ^ {2}$$

Elimination of $p_1$ gives

$$r ^ {2} - r \left(\rho (1 + a ^ {2}) + b ^ {2}\right) + \rho^ {2} a ^ {2} = 0 \tag {12.62}$$

This equation has the solution

$$r = \frac {1}{2} \left(\rho (1 + a ^ {2}) + b ^ {2} + \sqrt {\rho^ {2} (1 - a ^ {2}) ^ {2} + 2 \rho b ^ {2} (1 + a ^ {2}) + b ^ {4}}\right)$$

where the positive root is chosen to give $|p_1| < 1$ . Furthermore

$$p _ {1} = \frac {\rho a}{r}$$

Because A and B are relative prime and $A(0) \neq 0$ , the solution can be found from the Diophantine equation (12.47). With $\deg S = 1$ and $S(0) = 0$ , Eq. (12.47) becomes

$$(z + a) (z + r _ {1}) + b s _ {0} z = (z + p _ {1}) (z + c)$$

Putting $z = -a$ we get

$$s _ {0} = - \frac {(p _ {1} - a) (c - a)}{a b}$$

It follows from (12.62) that

$$\rho a p _ {1} ^ {2} - \rho p _ {1} (1 + a ^ {2}) - p _ {1} b ^ {2} + \rho a = 0$$

Hence

$$\rho \left(a p _ {1} ^ {2} - a ^ {2} p _ {1} - p _ {1} + a\right) = p _ {1} b ^ {2}$$

or

$$\rho \left(a p _ {1} (p _ {1} - a) - (p _ {1} - a)\right) = p _ {1} b ^ {2}$$

which gives

$$p _ {1} - a = - \frac {p _ {1} b ^ {2}}{\rho (1 - a p _ {1})}$$

We thus get

$$s _ {0} = \frac {p _ {1} b ^ {2} (c - a)}{\rho a b (1 - a p _ {1})} = \frac {b (c - a)}{r (1 - a p _ {1})}$$

Furthermore, equating the constant terms in (12.47) gives

$$r _ {1} = \frac {p _ {1} c}{a} = \frac {\rho c}{r}$$

The control law thus becomes

$$u (k) = - \frac {S (q)}{R (q)} y (k) = - \frac {b (c - a)}{r (1 - a p _ {1})} \frac {q}{q + p _ {1} c / a} y (k)$$

The calculations in Example 12.11 do not work when $\alpha = 0$ , because in this case the solution to the LQG-problem is not uniquely determined by the Diophantine equation (12.47) and it is necessary to use (12.49).
