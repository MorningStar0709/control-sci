# 12.1.1 Equations of motion

The circuit for a DC motor is shown in figure 12.1.

![](image/45cbae56dee24ec2f5a4328cc867a0499ef5fce7e159700d43052a851361c104.jpg)

<details>
<summary>text_image</summary>

+
V
-
R
Vemf = ω/Kv
</details>

Figure 12.1: DC motor circuit

V is the voltage applied to the motor, I is the current through the motor in Amps, R is the resistance across the motor in Ohms, ω is the angular velocity of the motor in radians per second, and $K _ { v }$ is the angular velocity constant in radians per second per Volt. This circuit reflects the following relation.

$$V = I R + \frac {\omega}{K _ {v}} \tag {12.1}$$

![](image/09a74c250be9ca082641e623f34590b005c79a67cc4841b5a5d0828bea3f7d4f.jpg)

<details>
<summary>line</summary>

| Speed (RPM) | Current (A) | Output power (W) |
| --- | --- | --- |
| 0 | 134 | 0 |
| 9365 | 347 | 0.7 |
| 18730 | 0 | 0.7 |
</details>

Figure 12.2: Example motor datasheet for 775pro

The mechanical relation for a DC motor is

$$\tau = K _ {t} I \tag {12.2}$$

where $\tau$ is the torque produced by the motor in Newton-meters and $K _ { t }$ is the torque constant in Newton-meters per Amp. Therefore

$$I = \frac {\tau}{K _ {t}}$$

Substitute this into equation (12.1).

$$V = \frac {\tau}{K _ {t}} R + \frac {\omega}{K _ {v}} \tag {12.3}$$
