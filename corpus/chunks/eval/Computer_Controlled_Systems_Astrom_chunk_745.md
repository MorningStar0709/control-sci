THEOREM 12.4 LINEAR QUADRATIC GAUSSIAN CONTROL Consider the system in (12.5) with $\deg A(z) = \deg C(z) = n$ . Assume that all the zeros of polynomial $C(z)$ are inside the unit disc, that there are no factors common to all three of the polynomials $A(z), B(z)$ , and $C(z)$ , and that a possible common factor of $A(z)$ and $B(z)$ has all its zeros inside the unit disc. Let the monic polynomial $P(z)$ , which has all its zeros inside the unit disc, he the solution to (12.45) with $\deg P(z) = n$ . The admissible control law with no delay that minimizes the criterion of (12.8) is given by

$$u (k) = - \frac {S ^ {*} (q ^ {- 1})}{R ^ {*} (q ^ {- 1})} y (k) = - \frac {S (q)}{R (q)} y (k) \tag {12.55}$$

where polynomials $R^{*}(z)$ and $S^{*}(z)$ are the unique solution to Equation (12.49) with $\deg X(z) < n$ . With the control law of (12.55), the output becomes

$$y (k) = \frac {R (q)}{P (q)} e (k) \tag {12.56}$$

and the control signal is

$$u (k) = - \frac {S (q)}{P (q)} e (k) \tag {12.57}$$

The minimal value of the loss function is

$$\min \mathrm{E} (y ^ {2} + \rho u ^ {2}) = \frac {\sigma^ {2}}{2 \pi i} \oint \frac {R (z) R (z ^ {- 1}) + \rho S (z) S (z ^ {- 1})}{P (z) P (z ^ {- 1})} \frac {d z}{z} \tag {12.58}$$

Proof. Introduce

$$u = v - \frac {S}{R} y \tag {12.59}$$

where v may be regarded as a transformed control variable, which has to be determined. Equations (12.5), (12.47), and (12.59) give

$$y = \frac {B R v + C R e}{A R + B S} = \frac {B R v + C R e}{P C} = \frac {B R}{P C} v + \frac {R}{P} e \tag {12.60}$$

It then follows from (12.60) that

$$u = v - \frac {S B v + S C e}{P C} = \frac {P C - B S}{P C} v - \frac {S}{P} e = \frac {A R}{P C} v - \frac {S}{P} e \tag {12.61}$$

The loss function of (12.8) can be written as

$$
\begin{array}{l} J = \mathrm{E} \left(y ^ {2} + \rho u ^ {2}\right) = \mathrm{E} \left(\frac {B R}{P C} v + \frac {R}{P} e\right) ^ {2} + \rho \mathrm{E} \left(\frac {A R}{P C} v - \frac {S}{P} e\right) ^ {2} \\ = J _ {1} + 2 J _ {2} + J _ {3} \\ \end{array}
$$

where

$$J _ {1} = \mathrm{E} \left(\left(\frac {B R}{P C} v\right) ^ {2} + \rho \left(\frac {A R}{P C} v\right) ^ {2}\right)J _ {2} = \mathrm{E} \left(\left(\frac {B R}{P C} v\right) \left(\frac {R}{P} e\right) - \rho \left(\frac {A R}{P C} v\right) \left(\frac {S}{P} e\right)\right)J _ {3} = \mathrm{E} \left(\left(\frac {R}{P} e\right) ^ {2} + \rho \left(\frac {S}{P} e\right) ^ {2}\right)$$

It follows from Remark 2 of Theorem 10.2 and (12.45) that
