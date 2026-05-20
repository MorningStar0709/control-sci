# Example 9.3

$$C = \frac {1 0}{s} \quad P = \frac {5 0}{s + 1 0} \quad H = 1 \quad x (t) = A u (t) \quad X (s) = \frac {A}{s}$$

This is the same as the rst example, but the controller, C(s), now adds a pole at the origin.

$$E (s) = \frac {A / s}{\left(1 + \frac {5 0 0}{s (s + 1 0)}\right)} = \frac {A \left(s ^ {2} + 1 0 s\right)}{s \left(s ^ {2} + 1 0 s + 5 0 0\right)}$$

Applying the FVT:

$$\lim _ {t \rightarrow \infty} e (t) = \lim _ {s \rightarrow 0} \frac {A \left(s ^ {2} + 1 0 s\right)}{s ^ {2} + 1 0 s + 5 0 0} = 0$$

The plant was the same, but by adding a pole at the origin to the controller, we have eliminated SSE for step input to zero. Since this is such a nice result it is worth a look at this new controller (Figure 9.2). This controller can be implemented by building an integrator. Two ways to implement an integrator are an analog op-amp circuit with a feedback capacitor, or alternatively, a software loop in a microcontroller which sums the dierence between input and output.
