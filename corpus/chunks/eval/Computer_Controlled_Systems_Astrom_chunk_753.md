# Uncontrollable and Unstable Modes

Models with the property that polynomials $A(z)$ and $B(z)$ have a common factor that is not a factor of $C(z)$ are important in practice. They appear when there are modes that are excited by disturbances and uncontrollable from the input. Compare Sec. 12.2. Because the modes are not controllable, they are not influenced by feedback.

Theorem 12.4 covers the case of stable common factors, but it does not work for unstable common factors. Unstable common factors are important in practice because they give one way of obtaining regulators with integral action.

To see what happens when there are unstable common factors, let $A_{2}$ denote the greatest common divisor of A and B and let $A_{2}^{-}$ denote the factor of $A_{2}$ with zeros outside the unit disc or on the unit circle. Let the feedback be

$$u (k) = - \frac {S (q)}{R (q)} y (k)$$

where $R(z)$ and $S(z)$ are relatively prime. It follows from (12.5) that

$$y (k) = \frac {R (q) C (q)}{A (q) R (q) + B (q) S (q)} e (k) \tag {12.63}u (k) = - \frac {S (q) C (q)}{A (q) R (q) + B (q) S (q)} e (k) \tag {12.64}$$

The unstable factor $A_{2}^{-}(z)$ divides the denominators of the right-hand sides of (12.63) and (12.64). Both $y$ and $u$ will be unhounded unless $R(z)$ or $S(z)$ are chosen in special ways. The signal $y$ will be bounded if $R(z)$ is divisible by $A_{2}^{-}(z)$ , and $u$ will be bounded if $A_{2}^{-}(z)$ divides $S(z)$ . Because $R(z)$ and $S(z)$ are relatively prime, it is not possible to make both $y$ and $u$ bounded. This is natural because infinitely large control actions are necessary to compensate for infinitely large disturbances.

To describe a problem of this type as a meaningful optimization problem, the criterion of (12.8) must be modified. One possibility is to introduce the variable

$$w (k) = q ^ {- m} A _ {2} ^ {-} (q) u (k) \tag {12.65}$$

where $m = \deg A_{2}^{-}(z)$ , and to introduce the criterion

$$J _ {l q} ^ {\prime} = \mathrm{E} \left(y ^ {2} (k) + \rho w ^ {2} (k)\right) \tag {12.66}$$
