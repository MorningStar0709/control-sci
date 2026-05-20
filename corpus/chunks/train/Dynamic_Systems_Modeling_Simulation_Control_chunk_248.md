# Example 5.14

Equation (5.89) is the I/O equation of the series RLC circuit from Example 5.12 (Fig. 5.6), where current is the output variable y and source voltage is the input variable u. Derive the system transfer function G(s) that relates output to input and use the following numerical values for the electrical system parameters: resistance R = 2 Ω, inductance L = 0.25 H, and capacitance C = 0.4 F.

Using the prescribed values for the electrical parameters, the I/O equation is

$$\ddot {y} + 8 \dot {y} + 1 0 y = 4 \dot {u} \tag {5.102}$$

Applying the D operator, Eq. (5.102) becomes

$$D ^ {2} y + 8 D y + 1 0 y = 4 D u \tag {5.103}$$

which can be solved for the output-to-input ratio y(t)∕u(t)

$$\frac {y (t)}{u (t)} = \frac {4 D}{D ^ {2} + 8 D + 1 0} \tag {5.104}$$

Replacing the differential operator D with s yields the transfer function

$$G (s) = \frac {4 s}{s ^ {2} + 8 s + 1 0} \tag {5.105}$$

The reader should also be able to convert a transfer function into an I/O differential equation.
