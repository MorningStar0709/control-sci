# E.3.5 Steady-state error

To demonstrate the problem of steady-state error, we will use a DC motor controlled by a velocity PID controller. A DC motor has a transfer function from voltage (V ) to angular velocity ( ˙θ) of

$$G (s) = \frac {\dot {\Theta} (s)}{V (s)} = \frac {K}{(J s + b) (L s + R) + K ^ {2}} \tag {E.7}$$

First, we’ll try controlling it with a P controller defined as

$$K (s) = K _ {p}$$

When these are in unity feedback, the transfer function from the input voltage to the error is

$$\frac {E (s)}{V (s)} = \frac {1}{1 + K (s) G (s)}E (s) = \frac {1}{1 + K (s) G (s)} V (s)E (s) = \frac {1}{1 + \left(K _ {p}\right) \left(\frac {K}{(J s + b) (L s + R) + K ^ {2}}\right)} V (s)E (s) = \frac {1}{1 + \frac {K _ {p} K}{(J s + b) (L s + R) + K ^ {2}}} V (s)$$

The steady-state of a transfer function can be found via

$$\lim _ {s \to 0} s H (s) \tag {E.8}$$

since steady-state has an input frequency of zero.

$$e _ {s s} = \lim _ {s \to 0} s E (s)e _ {s s} = \lim _ {s \to 0} s \frac {1}{1 + \frac {K _ {p} K}{(J s + b) (L s + R) + K ^ {2}}} V (s)e _ {s s} = \lim _ {s \to 0} s \frac {1}{1 + \frac {K _ {p} K}{(J s + b) (L s + R) + K ^ {2}}} \frac {1}{s}e _ {s s} = \lim _ {s \to 0} \frac {1}{1 + \frac {K _ {p} K}{(J s + b) (L s + R) + K ^ {2}}}e _ {s s} = \frac {1}{1 + \frac {K _ {p} K}{(J (0) + b) (L (0) + R) + K ^ {2}}}e _ {s s} = \frac {1}{1 + \frac {K _ {p} K}{b R + K ^ {2}}} \tag {E.9}$$

Notice that the steady-state error is nonzero. To fix this, an integrator must be included in the controller.

$$K (s) = K _ {p} + \frac {K _ {i}}{s}$$

The same steady-state calculations are performed as before with the new controller.

$$\frac {E (s)}{V (s)} = \frac {1}{1 + K (s) G (s)}E (s) = \frac {1}{1 + K (s) G (s)} V (s)E (s) = \frac {1}{1 + \left(K _ {p} + \frac {K _ {i}}{s}\right) \left(\frac {K}{(J s + b) (L s + R) + K ^ {2}}\right)} \left(\frac {1}{s}\right)e _ {s s} = \lim _ {s \to 0} s \frac {1}{1 + \left(K _ {p} + \frac {K _ {i}}{s}\right) \left(\frac {K}{(J s + b) (L s + R) + K ^ {2}}\right)} \left(\frac {1}{s}\right)e _ {s s} = \lim _ {s \rightarrow 0} \frac {1}{1 + \left(K _ {p} + \frac {K _ {i}}{s}\right)\left(\frac {K}{(J s + b) (L s + R) + K ^ {2}}\right)}e _ {s s} = \lim _ {s \to 0} \frac {1}{1 + \left(K _ {p} + \frac {K _ {i}}{s}\right) \left(\frac {K}{(J s + b) (L s + R) + K ^ {2}}\right)} \frac {s}{s}e _ {s s} = \lim _ {s \to 0} \frac {s}{s + (K _ {p} s + K _ {i}) \left(\frac {K}{(J s + b) (L s + R) + K ^ {2}}\right)}e _ {s s} = \frac {0}{0 + (K _ {p} (0) + K _ {i}) \left(\frac {K}{(J (0) + b) (L (0) + R) + K ^ {2}}\right)}e _ {s s} = \frac {0}{K _ {i} \frac {K}{b R + K ^ {2}}}$$

The denominator is nonzero, so $e _ { s s } = 0$ . Therefore, an integrator is required to eliminate steady-state error in all cases for this model.

It should be noted that $e _ { s s }$ in equation (E.9) approaches zero for $K _ { p } = \infty$ . This is known as a bang-bang controller. In practice, an infinite switching frequency cannot be achieved, but it may be close enough for some performance specifications.
