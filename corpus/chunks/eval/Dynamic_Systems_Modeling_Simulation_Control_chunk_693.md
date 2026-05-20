# Linear EHA Model

Recall that our overall goal is to design an automatic feedback system for precise position control of the EHA. The full EHA model presented in the previous subsections is complex and highly nonlinear. Designing

![](image/4fde533f4be4b4f4dd33c815602f10d9e43ae923021ddeea36773b4e24a705db.jpg)

<details>
<summary>line</summary>

| Time, s | Piston position, x(t), cm |
| --- | --- |
| 0 | 30 |
| 0.5 | 30 |
| 1 | 41 |
| 2 | 41 |
</details>

Figure 11.37 Piston stroke for 10-V pulse input.

![](image/a90bcd7c69a0f6dd1dd29e10587b97d83f918248421809ed276140acd2c6815f.jpg)

<details>
<summary>line</summary>

| Time, s | Vol. flow Q₁ (m³/s) | Vol. flow Q₂ (m³/s) |
| --- | --- | --- |
| 0.0 | 0 | 0 |
| 0.5 | 1.7 | -1.3 |
| 1.0 | 0 | -1.3 |
| 2.0 | 0 | 0 |
</details>

Figure 11.38 Volumetric-flow rates for 10-V pulse input.

![](image/47146324d955c7b2d8931ca03ae18baead0c023706f53c637d1e4824f5953360.jpg)

<details>
<summary>line</summary>

| Time, s | Pressure difference, ΔP = P₁−P₂, Pa (×10⁶) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.8 |
| 1.0 | -0.9 |
| 1.5 | 0.0 |
| 2.0 | 0.0 |
</details>

Figure 11.39 Differential pressure across the piston for 10-V pulse input.

a feedback control system becomes systematic when we have a linear plant model because we can make use of linear analysis tools such as the root-locus and frequency-response methods presented in Chapter 10. Therefore, it is to our advantage to develop a linear EHA model purely for the sake of control system design. It should be noted that we intend to test any potential control scheme designs with the full nonlinear EHA system dynamics.

The following linearization steps are similar to the process presented by Ogata [8] for linearizing a hydraulic actuator. To begin the analysis, rewrite Eqs. (11.39) and (11.40) for the magnitudes of the volumetric flows with valve displacement $y > 0$

$\mathrm { I n \mathrm { - } f l o w \ t o \ c h a m b e r \ 1 : \ } \ Q _ { 1 } = C _ { d } A _ { \nu } \sqrt { \frac { 2 } { \rho } ( P _ { S } - P _ { 1 } ) }$ 2 (PS − P1) (11.43)

$\mathrm { O u t \mathrm { - } f l o w \ f r o m \ c h a m b e r \ 2 : } \ Q _ { 2 } = C _ { d } A _ { \nu } \sqrt { \frac { 2 } { \rho } ( P _ { 2 } - P _ { r } ) }$ 2 (P2 − Pr) (11.44)

If we assume steady, incompressible flow where $Q _ { 1 } = Q _ { 2 }$ , then we can equate the two pressure differences contained in the radicands in Eqs. (11.43) and (11.44)

$$P _ {S} - P _ {1} = P _ {2} - P _ {r} \tag {11.45}$$
