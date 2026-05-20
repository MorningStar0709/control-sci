# Example 8.12

Repeat Example 8.11 and obtain the current response I(t) of the series RL circuit with a step voltage input $e _ { \mathrm { i n } } ( t ) =$ 2.4U(t) V.

Because we have the same system dynamics as Example 8.11 we can use Eq. (8.45) to express the Laplace transform of the current

$$I (s) = G (s) E _ {\mathrm{in}} (s) = \frac {1}{0 . 0 2 s + 1 . 2} E _ {\mathrm{in}} (s)$$

The above equation is valid for any voltage input. For this problem the voltage input is a step function, $e _ { \mathrm { i n } } ( t ) =$ $2 . 4 U ( t ) \mathrm { V } ,$ , and consequently the Laplace transform of the input is ${ \cal E } _ { \mathrm { i n } } ( s ) = 2 . 4 / s$ . Hence, the Laplace transform of the current is

$$I (s) = \frac {2 . 4}{s (0 . 0 2 s + 1 . 2)}$$

Dividing all terms by 0.02 and expanding in partial fractions we obtain

$$I (s) = \frac {1 2 0}{s (s + 6 0)} = \frac {a _ {1}}{s} + \frac {a _ {2}}{s + 6 0} \tag {8.49}$$

The residues of Eq. (8.49) are $a _ { 1 } = 2$ and $a _ { 2 } = - 2$ . Taking the inverse Laplace transform of Eq. (8.49) we see that the current response I(t) consists of a constant and an exponential function

$$I (t) = 2 \left(1 - e ^ {- 6 0 t}\right) \mathrm{A} \tag {8.50}$$

Consequently, the current response shows an exponential rise from zero (at time t = 0) to a steady-state value of 2 A with a settling time of 0.0667 s. We could have obtained this result by direct analysis of the I/O equation (8.43) to see that at steady state the current reaches a constant value (hence $\overset { \cdot } { I } = 0 )$ , which can be computed from Ohm’s law: $e _ { \mathrm { i n } } ( t ) / R = ( 2 . 4 \ : \mathrm { V } ) / ( 1 . 2 \ : \Omega ) = 2 \ : \mathrm { A }$ . The settling time is four time constants, where $\tau = 0 . 0 1 6 7 \mathrm { ~ s ~ }$ .
