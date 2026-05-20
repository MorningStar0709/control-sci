# Example 4.5 (Level Control)

For the level-control problem of Example 2.8 (Chapter 2), $P(s) = (-2.0) / (s + .005)$ (see Eq. 3.25 in Chapter 3). Design a compensator $F(s)$ so that $T(s) = \omega_0^2 / (s^2 + \sqrt{2}\omega_0 s + \omega_0^2)$ ; i.e., $T$ is a second-order Butterworth response.

Solution We have

$$S (s) = 1 - T (s) = \frac {s ^ {2} + \sqrt {2} \omega_ {0} s}{s ^ {2} + \sqrt {2} \omega_ {0} s + \omega_ {0} ^ {2}}.$$

Using Equation 4.37,

$$F (s) = \frac {T}{P S} = \frac {\omega_ {0} ^ {2} (s + . 0 0 5)}{s (s + \sqrt {2} \omega_ {0}) (- 2)}.$$

In this example, $P$ has neither RHP poles nor zeros, so the choice of $T$ (or $S$ ) is unconstrained, save for the requirement that $F$ be proper.
