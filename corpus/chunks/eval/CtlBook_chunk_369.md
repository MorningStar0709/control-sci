# Example 11.2

We are designing a digital implementation of the following control system:

$$C (s) = \frac {2 0 (s + 0 . 5)}{(s + 5) ^ {2}}$$

This controller has a zero, but the two poles take over above 5 rad/sec and bring the gain down for higher frequencies. What sampling rate should we use?

Solution 2: The Boss informs us that we must dene bandwidth as the frequency at which the magnitude of the system transfer function is equal to -40dB. Let's plot a Bode Diagram of the controller (using radians per second for frequency):

![](image/d5c00f396a039d81b7343a16f644a9f371d9202c45b9f250ba723db619a1a31e.jpg)

We can see that the curve intersects −40dB at $\omega _ { b } = 5 0 0 0$ . Thus

$$f _ {s a m p} = 2 \times \omega_ {b} = 1 0, 0 0 0 r a d / s e c = 1 5 9 2 H z$$
