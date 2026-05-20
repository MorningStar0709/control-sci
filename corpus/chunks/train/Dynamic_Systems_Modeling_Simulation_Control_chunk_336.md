where $\dot { z } = \dot { x } - \dot { x } _ { \mathrm { i n } } ( t )$ is the relative velocity across the shock absorber (in m/s), and $\nu = 0 . 2 \mathrm { m / s }$ . Obtain the dynamic response using Simulink for a sinusoidal input $x _ { \mathrm { i n } } ( t ) = 0 . 0 3$ sin 12t (in m). The system is initially at rest.

![](image/ee82e6ed0c10524fefd6fbbee1abf8d5d98bc287c79906e1322b44b54d9007c6.jpg)

<details>
<summary>text_image</summary>

½ vehicle mass
m
Suspension system
k
Shock absorber
x
Wheel/axle position
x_in(t)
</details>

Figure P6.14

6.15 Consider again the 1-DOF vehicle suspension problem in Problem 6.14 and Fig. P6.14, but now use a more realistic nonlinear model of the shock absorber:

$$F _ {d} = \frac {3 3 8 9 (\dot {z} - v _ {1})}{\sqrt {(\dot {z} - v _ {1}) ^ {2} + v _ {2} ^ {2}}} + 1 0 2 0. 8 4 \quad (\text { in N })$$

where $\dot { z } = \dot { x } - \dot { x } _ { \mathrm { i n } } ( t )$ is the relative velocity across the damper (m/s), $\nu _ { 1 } = 0 . 0 6 \mathrm { m } / \mathrm { s }$ , and $\nu _ { 2 } = 0 . 1 9 \mathrm { m } / \mathrm { s }$ . This shock absorber model exhibits a larger damping force during extension $( \dot { z } > 0 )$ ) as compared to compression $( \dot { z } < 0 )$ . Obtain the dynamic response using Simulink for a sinusoidal input $x _ { \mathrm { i n } } ( t ) = 0 . 0 3$ sin 12t (in m). The system is initially at rest. Compare your results to the simulation results from Problem 6.14.

6.16 Figure P6.16 shows the washout filter circuit described in Problem 3.28 in Chapter 3 with capacitor $C =$ 0.01 F and resistor $R = 2 \Omega$ . Use Simulink to obtain the dynamic response of the output voltage $e _ { O } ( t )$ )

if the input voltage is $e _ { \mathrm { i n } } ( t ) = 1 5 0 0 t ^ { 2 } \mathrm { V }$ for $0 \leq t \leq 0 . 0 4 \mathrm { s }$ until it reaches a maximum input voltage of 2.4 V. Therefore, $e _ { \mathrm { i n } } ( t ) = 2 . 4 \ : \mathrm { V }$ for $t > 0 . 0 4 \mathrm { s }$ . The circuit has zero stored energy at time $t = 0$ . Plot output and input voltages $e _ { O } ( t )$ and $e _ { \mathrm { i n } } ( t )$ on the same plot. On the basis of your simulation results explain why this circuit is called a washout filter. [Hint: use the Saturation block from the Discontinuities library to limit the input voltage so it never exceeds 2.4 V].

![](image/3a3a2a66a3409e4580de2abb0e1b15f157cce8b56ab800e64c6bdb9fc075238b.jpg)

<details>
<summary>text_image</summary>

C
+
e_in(t)
-
I
R
Output Voltage
e_O
</details>

Figure P6.16
