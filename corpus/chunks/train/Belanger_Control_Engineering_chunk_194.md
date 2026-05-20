# Example 4.1

For $P(s) = (2s + 1) / (s^2 + 3s + 2)$ , design an open-loop compensator $F(s)$ such that

$$H _ {d} (s) = \frac {\mathrm{I}}{s ^ {2} + 1 . 4 s + \mathrm{I}}.$$

This is a second-order Butterworth function.

Solution

$$F (s) P (s) = H _ {d} (s)$$

or

$$F (s) = \frac {H _ {d} (s)}{P (s)} = \frac {1}{s ^ {2} + 1 . 4 s + 1} \frac {s ^ {2} + 3 s + 2}{2 s + 1}F (s) = \frac {s ^ {2} + 3 s + 2}{(2 s + 1) (s ^ {2} + 1 . 4 s + 1)}.$$

Note that P is stable and minimum-phase, so $H_{d}(s)$ could have been any stable transfer function.
