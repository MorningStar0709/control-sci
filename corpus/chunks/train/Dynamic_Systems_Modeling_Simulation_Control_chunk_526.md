9.20 Figure P9.20 shows a 1-DOF mechanical system. Displacement z is measured from the static equilibrium position. The system parameters are $m = 0 . 3 \mathrm { k g } , k _ { 1 } = 8 0 \mathrm { N } / \mathrm { m } , k _ { 2 } = 6 0 \mathrm { N } / \mathrm { m }$ , and $b = 1 . 5 \mathrm { N - s / m }$ .

![](image/89aa8131d1a7843a902f58f4f254dbfdaa5c8a197e7cd0066de08d7d58b37ba0.jpg)

<details>
<summary>text_image</summary>

Fixed
k₁
fₐ(t)
m
k₂
b
z
Fixed base
</details>

Figure P9.20

a. Use MATLAB to create the Bode diagrams using the transfer function $G ( s ) = Z ( s ) / F _ { a } ( s )$ ) and an appropriate SSR.   
b. Use MATLAB to estimate the bandwidth and resonant frequency.

9.21 Figure P9.21 shows a block diagram for a simple second-order system that is driven by the sinusoidal input function u(t) = 3 sin 10t.

![](image/178c2b146ae2894a97e8203992fd21e6e8bdf6155b4d3784d830590f2da6a0e9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u(t) = 3sin10t"] --> B["1/(2s² + 32)"]
    B --> C["y(t)"]
```
</details>

G(s)   
Figure P9.21

a. Compute the magnitude and phase of the sinusoidal transfer function G( j??) for the input frequency $\omega = 1 0 \mathrm { r a d / s }$ .   
b. Use MATLAB or Simulink to obtain the response to the sinusoidal input u(t). Plot y(t).   
c. Explain why the system response y(t) obtained in part (b) does not match the frequency response solution presented by Eq. (9.17).

9.22 Figure P9.22 shows the magnitude Bode plot for two LTI systems. The transfer function for one of the LTI systems is

$$G (s) = \frac {5 7 6}{1 6 s ^ {2} + 3 8 . 4 s + 5 7 6}$$

Match transfer function G(s) with the appropriate magnitude plot in Fig. P9.22. Explain your answer.

![](image/44bc3f3f521521943df9857d364d2287bf4e371c7a84fff5d4aa2286b3f1b325.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | System 1 | System 2 |
| --- | --- | --- |
| 0.1 | 0 | 0 |
| 1 | 0 | 0 |
| 10 | -10 | 5 |
| 100 | -50 | -25 |
</details>

Figure P9.22

9.23 A simple model of an electromechanical actuator is

$$0. 0 6 \ddot {z} + 5. 5 \dot {z} + 3 1 0 0 z = 4. 6 I0. 0 1 \dot {I} + 4 I = e _ {\mathrm{in}} (t) - 2. 3 \dot {z}$$

where z is the position of the mechanical mass–spring–damper subsystem (in meters) and I is the current in the solenoid armature circuit. The single input to the system is source voltage $e _ { \mathrm { i n } } ( t )$ .

a. Use MATLAB to obtain the frequency response of the mechanical actuator (position z) if the source voltage is $e _ { \mathrm { i n } } ( t ) = 8$ sin 150t V.   
b. Use MATLAB to compute the bandwidth of the electromechanical actuator.
