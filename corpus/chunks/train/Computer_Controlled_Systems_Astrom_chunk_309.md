# Example 5.6 Motor with no cancellation of process zero

Consider the same motor as in Example 5.5, but assume that the desired closed-loop transfer function is

$$H _ {m} (z) = \frac {1 + p _ {1} + p _ {2}}{1 - b} \frac {z - b}{z ^ {2} + p _ {1} z + p _ {2}} \tag {5.37}$$

Notice that the process zero on the negative real axis is now also a zero of the desired closed-loop transfer function. This means that the zero does not have to be canceled by the regulator. Factor B as

$$\boldsymbol {B} ^ {+} = 1B ^ {-} = K (z - b)$$

Hence,

$$\bar {B} _ {m} = \frac {1 + p _ {1} + p _ {2}}{K (1 - b)}$$

The degree of the observer polynomial is

$$\deg A _ {o} \geq 2 \deg A - \deg A _ {m} - \deg B ^ {+} - 1 = 1$$

Therefore, the observer polynomial should be of at least first degree. A deadbeat observer is chosen:

$$A _ {0} (z) = z$$

The minimal degrees of the polynomials R and S are then given by

$$\deg R = \deg A _ {m} + \deg A _ {o} - \deg A = 1\deg S = \deg A - 1 = 1$$

The Diophantine equation can then be written as

$$(z - 1) (z - a) \left(z + r _ {1}\right) + K (z - b) \left(s _ {0} z + s _ {1}\right) = z ^ {3} + p _ {1} z ^ {2} + p _ {2} z \tag {5.38}$$

To determine $r_1$ , put $z = b$ in (5.38). Hence,

$$(b - 1) (b - a) (b + r _ {1}) = b ^ {3} + p _ {1} b ^ {2} + p _ {2} b$$

which gives

$$r _ {1} = - b + \frac {b (b ^ {2} + p _ {1} b + p _ {2})}{(b - 1) (b - a)}$$

Now put $z = 1$ and $z = a$ in (5.38). This gives

$$K (1 - b) \left(s _ {0} + s _ {1}\right) = 1 + p _ {1} + p _ {2}K (a - b) \left(s _ {0} a + s _ {1}\right) = a ^ {3} + p _ {1} a ^ {2} + p _ {2} a$$

from which $s_{0}$ and $s_{1}$ can be determined. Further

$$T (z) = A _ {o} \bar {B} _ {m} = z \frac {1 + p _ {1} + p _ {2}}{K (1 - b)} = t _ {0} z$$

The control law is then

$$u (k) = t _ {0} u _ {c} (k) - s _ {0} y (k) - s _ {1} y (k - 1) - r _ {1} u (k - 1)$$

Notice that this feedback law is of the same form as (5.36). However, the coefficients are different. A simulation of the step response of the system is shown in Fig. 5.5. A comparison with Fig. 5.4 shows that the control signal is much smoother; there is no ringing. The response start is also a little slower, because $A_{o}$ is of higher degree than in Example 5.5.
