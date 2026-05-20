# Proportional-integral controller

The PI controller transfer function is

$$G _ {C} (s) = \frac {K _ {P} s + K _ {I}}{s}$$

The forward transfer function with $K _ { P } = 0 . 0 4 \ : \mathrm { V / m }$ and $K _ { I } = 0 . 0 0 2 \ : \mathrm { V / m { - } s }$ is

$$G (s) = \frac {2 (K _ {P} s + K _ {I})}{s ^ {2} (s + 0 . 3)} = \frac {0 . 0 8 s + 0 . 0 0 4}{s ^ {2} (s + 0 . 3)}$$

![](image/08edacf6f58311eb92d0925c9d445094e1e49d218544f38ed1a4ad6e3a78af25.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference position, x_ref(t)"] --> B((+))
    B --> C["Position error, x_e(t)"]
    C --> D["G_C(s), Controller"]
    D --> E["Actuator voltage, e_in(t)"]
    E --> F["K_A"]
    F --> G["Actuator gain (N/V)"]
    G --> H["Force, f(t)"]
    H --> I["\frac{1}{s^2 + 0.3s}"]
    I --> J["Position, x(t)"]
    J --> K["-"]
    K --> B
```
</details>

Figure 10.27 Closed-loop position control of a mechanical system (Example 10.8).

![](image/e1918caa81b610100cb0607c4f5c5c45a64083eecc430cc81982c9daab553a72.jpg)

<details>
<summary>line</summary>

| Time, s | Reference position x_ref(t) and position x(t), m (x_ref(t)) | Reference position x_ref(t) and position x(t), m (x(t)) |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | ~0.05 | ~0.02 |
| 10 | ~0.1 | ~0.06 |
| 15 | ~0.15 | ~0.1 |
| 20 | ~0.2 | ~0.15 |
| 25 | ~0.25 | ~0.2 |
| 30 | ~0.3 | ~0.25 |
| 35 | ~0.35 | ~0.3 |
| 40 | ~0.4 | ~0.35 |
</details>

Figure 10.28 Closed-loop position response to ramp input with P-controller (Example 10.8).

Clearly, the forward transfer function G(s) is type 2 because the PI controller has one free integrator and the plant contains one free integrator. Table 10.3 tells us that for a ramp input and a type 2 system, the steady-state error is zero. The values of the $K _ { P }$ and $K _ { I }$ gains do not affect the steady-state error, but they do affect the settling time and damping of the transient response. Figure 10.29 shows that the closed-loop response x(t) using the PI controller eventually tracks the ramp input $x _ { \mathrm { r e f } } ( t )$ at steady state with zero offset error.

![](image/af591599c1a237232fd597ada01488d00c2cf0f239a224271c2b6c9e2ec8a8a0.jpg)

<details>
<summary>line</summary>

| Time, s | x_ref(t) = 0.01t | x(t) |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 10 | 0.1 | 0.05 |
| 20 | 0.2 | 0.15 |
| 30 | 0.3 | 0.25 |
| 40 | 0.4 | 0.35 |
| 50 | 0.5 | 0.45 |
</details>

Figure 10.29 Closed-loop position response to ramp input with PI controller (Example 10.8).
