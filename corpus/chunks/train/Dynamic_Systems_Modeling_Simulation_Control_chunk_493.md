# Example 9.6

Figure 9.19 shows an RC circuit that is driven by sinusoidal voltage source $e _ { \mathrm { i n } } ( t ) = 2 . 4$ sin ??t V. If the capacitance is $C = 0 . 0 0 3 \mathrm { F }$ and the resistance is $R = 4 \Omega$ , use the Bode diagram to determine the input frequency ?? where the amplitude of the steady-state output voltage $e _ { C } ( t )$ is 1.2 V (or, the output/input amplitude ratio is one-half).

CThe mathematical model of the RC circuit can be determined by applying Kirchhoff’s voltage law to the single loop and the resulting I/O equation is

$$R C \dot {e} _ {C} + e _ {C} = e _ {\mathrm{in}} (t)$$

Hence the transfer function relating output voltage $e _ { C }$ to input voltage $e _ { \mathrm { i n } } ( t )$ is

$$G (s) = \frac {E _ {C} (s)}{E _ {\mathrm{in}} (s)} = \frac {1}{R C s + 1}$$

Clearly, the DC gain is unity and the time constant is $\tau = R C = 0 . 0 1 2 \mathrm { s }$ . We know that the magnitude plot of the Bode diagram will remain near 0 dB for frequencies less than the corner frequency $\omega _ { c } = 1 / \tau = 8 3 . 3 3$ rad/s. At frequencies higher than $\omega _ { c }$ the magnitude plot will drop off at the rate of −20 dB/decade.

![](image/190660e3b8f2878f69986b73b87817c6ef34e890874c564ae427d08246eb57c3.jpg)

<details>
<summary>text_image</summary>

Input
voltage,
e_in(t) = 2.4 sin ωt V
+
-
R
I
C
Output
voltage, e_C
</details>

Figure 9.19 RC circuit for Example 9.6.

![](image/75816459d8882f4f38b8675390577edbfb8b628a69b67a7357d05308aabea6bd.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude, dB |
| --- | --- |
| 10^0 | 0 |
| 10^1 | -6 |
| 10^2 | -10 |
| 10^3 | -25 |
</details>

![](image/ef41cf6dfaa664ae0b9b7fc8729eeccc3aa37f32b106d823959932fe64b87344.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Phase, deg |
| --- | --- |
| 1 | 0 |
| 10 | -15 |
| 100 | -60 |
| 1000 | -90 |
</details>

Figure 9.20 Bode diagram for RC circuit (Example 9.6).
