# Mathematical Model

The complete mathematical model of the electromagnetic system consists of the electrical (coil) and mechanical (ball) subsystems. We will assume that the electrical system shown in Fig. 11.49 is a linear RL circuit comprised of coil resistance R, constant inductance L, and source voltage $e _ { \mathrm { i n } } ( t )$ . Applying Kirchhoff’s voltage law around the loop yields

$$- e _ {R} - e _ {L} + e _ {\text { in }} (t) = 0 \tag {11.64}$$

where the voltage drops across the resistor and inductor are $e _ { R } = R I$ and $e _ { L } = L \dot { I }$ , respectively. Substituting the voltage drops across the passive elements in Eq. (11.64) we obtain

$$L \dot {I} + R I = e _ {\text { in }} (t) \tag {11.65}$$

Equation (11.65) is the mathematical model of the electrical coil and it matches the solenoid coil modeling equation (11.9) for the case with constant inductance L.

Figure 11.50 shows a free-body diagram of the mechanical subsystem, which consists of the ball mass m. The only forces acting on the ball are the electromagnetic force $F _ { \mathrm { e m } }$ and gravity. Applying Newton’s second law with a positive sign convention upward yields

$$+ \uparrow \sum F = F _ {\mathrm{em}} - m g = m \ddot {z} \tag {11.66}$$

The electromagnetic force is

$$F _ {\mathrm{em}} = \frac {K _ {F} I ^ {2}}{(d - z) ^ {2}} \tag {11.67}$$

where $K _ { F }$ is a force constant that depends on the number of coil wraps, material properties of the electromagnetic core, and electromagnet geometry. It is again noted that $d - z$ is the air gap (distance between the ball and the electromagnet) and hence the electromagnetic force exhibits an inverse-square relationship with the air gap. Clearly, the force is a nonlinear function of current I and position z. Substituting Eq. (11.67) into Eq. (11.66) and rearranging yields the mechanical subsystem model

$$m \ddot {z} = \frac {K _ {F} I ^ {2}}{(d - z) ^ {2}} - m g \tag {11.68}$$

![](image/0335c7eec1945d43582d6c61a3524b0ef27519026d427bec3869675eb81dd10c.jpg)

<details>
<summary>text_image</summary>

Fem
Ball, m
mg
+z
</details>

Figure 11.50 Free-body diagram of the mechanical ball.

Table 11.6 Parameters for the Magnetic Levitation System
