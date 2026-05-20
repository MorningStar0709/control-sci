$$(a _ {3} s ^ {3} + a _ {2} s ^ {2} + a _ {1} s + a _ {0}) Y (s) e ^ {s t} = \left(b _ {1} s + b _ {0}\right) U (s) e ^ {s t} \tag {5.98}$$

Finally, use Eq. (5.98) to form the ratio $Y ( s ) / U ( s )$

$$\frac {Y (s)}{U (s)} = \frac {b _ {1} s + b _ {0}}{a _ {3} s ^ {3} + a _ {2} s ^ {2} + a _ {1} s + a _ {0}} = G (s) \tag {5.99}$$

We define the transfer function G(s) as the ratio shown in Eq. (5.99). The formal mathematical definition of the transfer function of a linear, time-invariant I/O equation is the Laplace transform of the output $Y ( s )$ divided by the Laplace transform of the input $U ( s )$ with the assumption of zero initial conditions (we repeat this definition in Chapter 8). The formal definition of the transfer function is identical to the result demonstrated by this example.

As a second example, we can derive the “time-domain” transfer function by applying the differential D operator to the third-order I/O equation (5.96)

$$a _ {3} D ^ {3} y + a _ {2} D ^ {2} y + a _ {1} D y + a _ {0} y = b _ {1} D u + b _ {0} u \tag {5.100}$$

We can factor out y(t) and $u ( t )$ from both sides of Eq. (5.100) and form the ratio of output to input:

$$\frac {y (t)}{u (t)} = \frac {b _ {1} D + b _ {0}}{a _ {3} D ^ {3} + a _ {2} D ^ {2} + a _ {1} D + a _ {0}} \tag {5.101}$$

Equation (5.101) is identical to the transfer function G(s) in Eq. (5.99) if we simply replace the differential operator D with the complex variable s. Note that in Laplace transform theory, the differentiation theorem states that the Laplace transform of ẏ is equal to $s Y ( s ) - y ( 0 )$ , and the Laplace transform of ÿ is $s ^ { 2 } Y ( s ) -$ sy(0) − ẏ (0), and so on for higher-order derivatives. Because all initial conditions y(0), ẏ (0), and ÿ(0) are assumed to be zero for a transfer function, we can conclude that multiplying by the kth power of Laplace variable s in the Laplace domain is equivalent to the kth derivative in the time domain.
