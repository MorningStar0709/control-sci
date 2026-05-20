# 8.7.2 Heading state-space model

We can control heading by augmenting the state with that. The change in heading is defined as

$$\dot {\theta} = \frac {v _ {r} - v _ {l}}{2 r _ {b}} = \frac {v _ {r}}{2 r _ {b}} - \frac {v _ {l}}{2 r _ {b}}$$

This gives the following linear model.

![](image/e3e5a39b91b6f83837ff0dc610294df71f764181d24b502c9cab4c48535cb429.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference Left velocity (m/s) | State Left velocity (m/s) | Reference Right velocity (m/s) | State Right velocity (m/s) | Input Left voltage (V) | Input Right voltage (V) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 2 | 2 | 10 | 10 | 10 | 10 |
| 14 | 2 | 2 | 10 | 10 | 10 | 10 |
| 15 | 0 | 0 | - | - | - | - |
| 16 | - | - | - | - | - | - |
</details>

Figure 8.3: Drivetrain response

Theorem 8.7.2 — Differential drive heading state-space model.

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}
\mathbf {x} = \left[ \begin{array}{c} \theta \\ v _ {l} \\ v _ {r} \end{array} \right] = \left[ \begin{array}{c} \text { heading } \\ \text { left   velocity } \\ \text { right   velocity } \end{array} \right] \quad \mathbf {u} = \left[ \begin{array}{c} V _ {l} \\ V _ {r} \end{array} \right] = \left[ \begin{array}{c} \text { left   voltage } \\ \text { right   voltage } \end{array} \right]

\mathbf {A} = \left[ \begin{array}{c c c} 0 & - \frac {1}{2 r _ {b}} & \frac {1}{2 r _ {b}} \\ 0 & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \\ 0 & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \end{array} \right] \tag {8.10}

\mathbf {B} = \left[ \begin{array}{c c} 0 & 0 \\ \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \end{array} \right] \tag {8.11}
$$

where $\begin{array} { r } { C _ { 1 } \ = \ - \frac { G _ { l } ^ { 2 } K _ { t } } { K _ { v } R r ^ { 2 } } , C _ { 2 } \ = \ \frac { G _ { l } K _ { t } } { R r } , C _ { 3 } \ = \ - \frac { G _ { r } ^ { 2 } K _ { t } } { K _ { v } R r ^ { 2 } } } \end{array}$ GlKt , C = − G2rKtK Rr2 , and C4 = GrKtRr . The $\begin{array} { r } { C _ { 4 } ~ = ~ \frac { G _ { r } K _ { t } } { R r } } \end{array}$ constants $C _ { 1 }$ vthrough $C _ { 4 }$ vare from the derivation in section 12.6.

The velocity states are required to make the heading controllable.
