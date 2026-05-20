# Example 9.1

Figure 9.5 shows the series RL circuit from Example 7.6 and Example 8.11. Obtain the frequency response for the current I(t) for a sinusoidal voltage input, $e _ { \mathrm { i n } } ( t ) = 2$ sin 50t V. The system has zero energy at time t = 0, or $I ( 0 ) = 0$ , and the inductance and resistance values are $L = 0 . 0 2$ H and $R = 1 . 2 \Omega$ , respectively.

The mathematical model of the RL circuit is

$$L \dot {I} + R I = e _ {\text { in }} (t) \tag {9.19}$$

Hence the transfer function relating current (output) to the voltage source (input) is

$$G (s) = \frac {I (s)}{E _ {\mathrm{in}} (s)} = \frac {1}{L s + R} = \frac {1}{0 . 0 2 s + 1 . 2} \tag {9.20}$$

The reader should note that the system’s I/O equation (9.19) or transfer function (9.20) remains unchanged whether the input is an impulse (as in Example 7.6) or a sinusoid as in this example.

Because the input voltage is a sine function, Eq. (9.17) provides the frequency response for the current at steady state. Furthermore, the sinusoidal voltage input is $e _ { \mathrm { i n } } ( t ) = 2$ sin 50t V, which tells us that the input amplitude is 2 V and the input frequency is 50 rad/s. Using Eq. (9.17) with $U _ { 0 } = 2 \mathrm { V }$ and $\omega = 5 0$ rad/s yields

$$I _ {\mathrm{ss}} (t) = | G (j \omega) | 2 \sin (5 0 t + \phi) \tag {9.21}$$

![](image/4b54a055a3ba0e7fa2bd33d96db223d89f462307facbdc4515e295a5a75a0b20.jpg)

<details>
<summary>text_image</summary>

e_in(t) = 2 sin 50t V
+
-
R
I
L
</details>

Figure 9.5 Electrical system with sinusoidal input (Example 9.1).

Therefore, we only need to compute the magnitude and phase of the sinusoidal transfer function for the input frequency $\omega = 5 0$ rad/s. We begin by writing the sinusoidal transfer function by using Eq. (9.20) with $s = j \omega$

$$G (j \omega) = \frac {1}{0 . 0 2 j \omega + 1 . 2} \tag {9.22}$$

The magnitude of the complex function $G ( j \omega )$ is computed by dividing the magnitude of the numerator by the magnitude of the denominator, or

$$| G (j \omega) | = \frac {\sqrt {1 ^ {2} + 0 ^ {2}}}{\sqrt {1 . 2 ^ {2} + (0 . 0 2 \omega) ^ {2}}} \tag {9.23}$$

Note that the magnitudes of the numerator and denominator terms are computing using Eq. (9.13) and the respective real and imaginary parts. Substituting the input frequency $\omega = 5 0$ rad/s into Eq. (9.23) we find that the magnitude is $| G ( j \omega ) | = 0 . 6 4 0 2$ .

| |The phase angle of $G ( j \omega )$ is computed by subtracting the phase angle of the denominator from the phase angle of the numerator, or
