$$\deg S ^ {*} \leq \max (\deg A ^ {*} + \deg P - 1, \deg B + \deg C ^ {*}) - \deg P < n \tag {12.51}$$

Using the same argument we also find that

$$R ^ {*} (z) = \frac {z ^ {d} B ^ {*} (z) X (z) + \rho A (z) C ^ {*} (z)}{r P (z)}$$

is a polynomial of degree

$$\deg R ^ {*} \leq \max (d + \deg B ^ {*} + \deg P - 1, \deg A + \deg C ^ {*}) - \deg P \leq n \tag {12.52}$$

The solution $X(z)$ , $S^{*}(z)$ and $R^{*}(z)$ to (12.49) is continuous in the coefficients of polynomials $A(z)$ and $B(z)$ . If polynomial $P(z)$ has multiple zeros we can the perturb the coefficients of $A(z)$ and $B(z)$ to obtain a $P(z)$ with distinct zeros and obtain the results by a limiting procedure. The details of this argument are delicate.

Remark 1. Notice that if one solution, $X_0$ , $R_0^*$ , $S_0^*$ , to Eq. (12.49) has been obtained all other solutions are given by

$$X (z) = X _ {0} (z) + Q (z) r P (z)R ^ {*} (z) = R _ {0} ^ {*} (z) + Q (z) z ^ {d} B ^ {*} (z) \tag {12.53}S ^ {*} (z) = S _ {0} ^ {*} (z) - Q (z) A ^ {*} (z)$$

where $Q(z)$ is an arbitrary polynomial. This is easily verified by direct insertion into the equation.

Remark 2. The polynomials $R(z)$ and $S(z)$ are given by $R(z) = z^n R^*(z^{-1})$ and $S(z) = z^n S^*(z^{-1})$ . The conditions $A^*(0) = P^*(0) = C^*(0) = 1$ together with Eq. (12.53) imply that $R^*(0) = 1$ , hence $\deg R(z) = n$ and $\deg S(z) \leq n$ and $\deg S^*(z) < n$ .

Remark 3. Eliminating X by multiplying the first equation by $z^{d}B^{*}(z)$ and the second by $A^{*}(z)$ and subtracting gives

$$r P S ^ {*} z ^ {d} B ^ {*} + r P A ^ {*} R ^ {*} = R C ^ {*} z ^ {d} B ^ {*} + \rho A ^ {*} C ^ {*} = r P P ^ {*} C ^ {*}$$

where the second equality follows from (12.46). Dividing by $rP$ shows that the polynomials $R^{*}$ and $S^{*}$ satisfy the Diophantine equation (12.48).

Remark 4. In the following we will need another property of the solutions to Eq. (12.49). Adding the first equation multiplied by $\rho A$ and the second multiplied by $B$ gives:

$$\left(\rho A A ^ {*} + z ^ {d} B B ^ {*}\right) X + \rho r A P S ^ {*} - r P B R ^ {*} = 0$$

Using the spectral factorization condition (12.46) and dividing by $rP$ now gives:

$$P ^ {*} (z) X (z) = B (z) R ^ {*} (z) - \rho A (z) S ^ {*} (z) \tag {12.54}$$

After these preliminaries we will now solve the LQG-problem with polynomial calculations.
