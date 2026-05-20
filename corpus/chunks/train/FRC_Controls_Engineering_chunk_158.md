# 6.10.1 Continuous state-space model

By equation (12.18)

$$\dot {\omega} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega + \frac {G K _ {t}}{R J} V$$

Factor out ω and V into column vectors.

$$\left[ \dot {\omega} \right] = \left[ - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \right] \left[ \omega \right] + \left[ \frac {G K _ {t}}{R J} \right] \left[ V \right]$$

![](image/654c2bbe2acd1b4503441302b2c9c964ccfe53b2d677cbb7e7be1e1cb5987144.jpg)

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

Figure 6.4: Flywheel system diagram

Theorem 6.10.1 — Flywheel state-space model.

$$\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}\mathbf {x} = \omega = \text { angular velocity } \quad \mathbf {y} = \omega = \text { angular velocity } \quad \mathbf {u} = V = \text { voltage }\mathbf {A} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \tag {6.13}\mathbf {B} = \frac {G K _ {t}}{R J} \tag {6.14}\mathbf {C} = 1 \tag {6.15}\mathbf {D} = 0 \tag {6.16}$$
