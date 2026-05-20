# Discretization

The controller described by (8.22) can be discretized using any of the standard methods such as Tustin's approximation or ramp equivalence. Because the PIDcontroller is so simple, there are some special methods that are used. The following is a popular approximation that is very easy to derive. The proportional part

$$P (t) = K \left(b u _ {c} (t) - y (t)\right)$$

requires no approximation because it is a purely static part. The integral term

$$I (t) = \frac {K}{T _ {i}} \int^ {t} e (s) d s$$

is approximated by a forward approximation, that is,

$$I (k h + h) = I (k h) + \frac {K h}{T _ {i}} e (k h) \tag {8.23}$$

The derivative part given by

$$\frac {T _ {d}}{N} \frac {d D}{d t} + D = - K T _ {d} \frac {d y}{d t}$$

is approximated by taking backward differences. This gives

$$D (k h) = \frac {T _ {d}}{T _ {d} + N h} D (k h - h) - \frac {K T _ {d} N}{T _ {d} + N h} \left(y (k h) - y (k h - h)\right)$$

This approximation has the advantage that it is always stable and that the sampled pole goes to zero when $T_{d}$ goes to zero. Tustin's approximation gives an approximation such that the pole instead goes to = -1 as $T_{d}$ goes to zero. The control signal is given as

$$u (k h) = P (k h) + I (k h) + D (k h) \tag {8.24}$$

This approximation has the pedagogical advantage that the proportional, integral, and derivative terms are obtained separately. The other approximations give similar results. They can all be represented as

$$R (q) u (k h) = T (q) u _ {c} (k h) - S (q) y (k h) \tag {8.25}$$

where the polynomials R, S, and T are of second order. The polynomial R has the form

$$R (q) = (q - 1) (q - a _ {d}) \tag {8.26}$$

The number $a_{d}$ and the coefficients of the polynomials S and T obtained for different approximation methods are given in Table 8.1.

Table 8.1 Coefficients in different approximations of the continuous-time PID-controller.
