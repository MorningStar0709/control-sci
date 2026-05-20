# 12.2.1 Equations of motion

We want to derive an equation for the carriage acceleration a (derivative of v) given an input voltage V , which we can integrate to get carriage velocity and position.

First, we’ll find a torque to substitute into the equation for a DC motor. Based on figure 12.3

$$\tau_ {m} G = \tau_ {p} \tag {12.7}$$

where G is the gear ratio between the motor and the pulley and $\tau _ { p }$ is the torque produced by the pulley.

$$r F _ {m} = \tau_ {p} \tag {12.8}$$

where r is the radius of the pulley. Substitute equation (12.7) into $\tau _ { m }$ in the DC motor equation (12.3).

$$V = \frac {\frac {\tau_ {p}}{G}}{K _ {t}} R + \frac {\omega_ {m}}{K _ {v}}V = \frac {\tau_ {p}}{G K _ {t}} R + \frac {\omega_ {m}}{K _ {v}}$$

Substitute in equation (12.8) for $\tau _ { p }$

$$V = \frac {r F _ {m}}{G K _ {t}} R + \frac {\omega_ {m}}{K _ {v}} \tag {12.9}$$

The angular velocity of the motor armature $\omega _ { m }$ is

$$\omega_ {m} = G \omega_ {p} \tag {12.10}$$

where $\omega _ { p }$ is the angular velocity of the pulley. The velocity of the mass (the elevator carriage) is

$$v = r \omega_ {p}\omega_ {p} = \frac {v}{r} \tag {12.11}$$

Substitute equation (12.11) into equation (12.10).

$$\omega_ {m} = G \frac {v}{r} \tag {12.12}$$

Substitute equation (12.12) into equation (12.9) for $\omega _ { m }$

$$
\begin{array}{l} V = \frac {r F _ {m}}{G K _ {t}} R + \frac {G \frac {v}{r}}{K _ {v}} \\ V = \frac {R r F _ {m}}{G K _ {t}} + \frac {G}{r K _ {v}} v \\ \end{array}
$$

Solve for $F _ { m }$

$$
\begin{array}{l} \frac {R r F _ {m}}{G K _ {t}} = V - \frac {G}{r K _ {v}} v \\ F _ {m} = \left(V - \frac {G}{r K _ {v}} v\right) \frac {G K _ {t}}{R r} \\ F _ {m} = \frac {G K _ {t}}{R r} V - \frac {G ^ {2} K _ {t}}{R r ^ {2} K _ {v}} v \tag {12.13} \\ \end{array}
$$

We need to find the acceleration of the elevator carriage. Note that

$$\sum F = m a \tag {12.14}$$

where $\textstyle \sum F$ is the sum of forces applied to the elevator carriage, m is the mass of the elevator carriage in kilograms, and a is the acceleration of the elevator carriage.

$$
\begin{array}{l} m a = F _ {m} \\ m a = \left(\frac {G K _ {t}}{R r} V - \frac {G ^ {2} K _ {t}}{R r ^ {2} K _ {v}} v\right) \\ a = \frac {G K _ {t}}{R r m} V - \frac {G ^ {2} K _ {t}}{R r ^ {2} m K _ {v}} v \\ a = - \frac {G ^ {2} K _ {t}}{R r ^ {2} m K _ {v}} v + \frac {G K _ {t}}{R r m} V \tag {12.15} \\ \end{array}
$$

![](image/31e3688fbe7ef585732f879a6441a30ead51c24bd6bb676381d2ec6cc9728673.jpg)

Gravity is not part of the modeled dynamics because it complicates the statespace model and the controller will behave well enough without it.

This model will be converted to state-space notation in section 6.9.

![](image/0d3cdbf980028921c964c620f565afebec4126303a2737dd3f110bccefbc1507.jpg)

<details>
<summary>text_image</summary>

R
I
V
Vemf
ωm
G
ωf
J
circuit
mechanics
</details>

Figure 12.4: Flywheel system diagram
