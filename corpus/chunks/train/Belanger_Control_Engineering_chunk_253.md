# Example 5.7 (Pendulum on a Cart)

Obtain the Root Locus for the cart-and-pendulum system of Example 2.9 (Chapter 2), with x as the output and pure-gain control. Can the system be stabilized with that pure-gain control system?

Solution The transfer function is given by Equation 3.27 (Chapter 3). It is

$$\frac {x}{F} = \frac {(s + 3 . 1 3 0 5) (s - 3 . 1 3 0 5)}{s ^ {2} (s + 4 . 4 2 7 2) (s - 4 . 4 2 7 2)}.$$

The Root Locus is displayed in Figure 5.6. Since there is always one unstable pole and a pair of poles on the j-axis for any positive k, the system cannot be stabilized by pure-gain feedback with k > 0. (The reader may verify that k < 0 also fails to stabilize.)
