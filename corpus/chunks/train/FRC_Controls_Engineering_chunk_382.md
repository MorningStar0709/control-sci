# 12.4.1 Equations of motion

We want to derive an equation for the arm angular acceleration $\dot { \omega } _ { a r m }$ given an input voltage V , which we can integrate to get arm angular velocity and angle.

We will start with the equation derived earlier for a DC motor, equation (12.3).

$$V = \frac {\tau_ {m}}{K _ {t}} R + \frac {\omega_ {m}}{K _ {v}}$$

Solve for the angular acceleration. First, we’ll rearrange the terms because from inspection, V is the model input, $\omega _ { m }$ is the state, and $\tau _ { m }$ contains the angular acceleration.

$$V = \frac {R}{K _ {t}} \tau_ {m} + \frac {1}{K _ {v}} \omega_ {m}$$

![](image/dd69edde70fab919fec9853837f611b83a42379f5c2990d1f09bf2b97359ebd8.jpg)

<details>
<summary>text_image</summary>

R
I
V
Vemf
ωm
G
m
ωarm
l
circuit
mechanics
</details>

Figure 12.5: Single-jointed arm system diagram

Solve for τm. $\tau _ { m }$

$$V = \frac {R}{K _ {t}} \tau_ {m} + \frac {1}{K _ {v}} \omega_ {m}\frac {R}{K _ {t}} \tau_ {m} = V - \frac {1}{K _ {v}} \omega_ {m}\tau_ {m} = \frac {K _ {t}}{R} V - \frac {K _ {t}}{K _ {v} R} \omega_ {m} \tag {12.20}$$

Since $\tau _ { m } G = \tau _ { a r m }$ and $\omega _ { m } = G \omega _ { a r m }$ ,

$$\left(\frac {\tau_ {a r m}}{G}\right) = \frac {K _ {t}}{R} V - \frac {K _ {t}}{K _ {v} R} (G \omega_ {a r m})\frac {\tau_ {a r m}}{G} = \frac {K _ {t}}{R} V - \frac {G K _ {t}}{K _ {v} R} \omega_ {a r m}\tau_ {a r m} = \frac {G K _ {t}}{R} V - \frac {G ^ {2} K _ {t}}{K _ {v} R} \omega_ {a r m} \tag {12.21}$$

The torque applied to the arm is defined as

$$\tau_ {a r m} = J \dot {\omega} _ {a r m} \tag {12.22}$$

where J is the moment of inertia of the arm and $\dot { \omega } _ { a r m }$ is the angular acceleration. Substitute equation (12.22) into equation (12.21).

$$(J \dot {\omega} _ {a r m}) = \frac {G K _ {t}}{R} V - \frac {G ^ {2} K _ {t}}{K _ {v} R} \omega_ {a r m}\dot {\omega} _ {a r m} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega_ {a r m} + \frac {G K _ {t}}{R J} V$$

We’ll relabel $\omega _ { a r m }$ as ω for convenience.

$$\dot {\omega} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega + \frac {G K _ {t}}{R J} V \tag {12.23}$$

This model will be converted to state-space notation in section 6.11.
