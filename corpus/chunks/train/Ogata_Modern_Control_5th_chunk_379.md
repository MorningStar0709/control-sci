Figures 6–82(a) and (b) show the unit-step response and unit-ramp response of the compensated system.The unit-step response curve is reasonable and the unit-ramp response looks acceptable. Notice that in the unit-ramp response the output leads the input by a small amount.This is because the system has a feedback transfer function $1 / ( 0 . 1 s + 1 )$ ). If the feedback signal versus t is plotted, together with the unit-ramp input, the former will not lead the input ramp at steady state. See Figure 6–82(c).

Figure 6–82 (a) unit-step response of the compensated system; (b) unit-ramp response of the compensated system; (c) a plot of feedback signal versus t in the unit-ramp response.   
![](image/157b182820c26b2461526b68cfc0ba38d5c8e86d01a6212bfa645b685e67dff7.jpg)

<details>
<summary>line</summary>

| t Sec | Output |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.3 |
| 2 | 1.0 |
| 3 | 0.95 |
| 4 | 1.0 |
| 5 | 1.0 |
| 6 | 1.0 |
| 7 | 1.0 |
| 8 | 1.0 |
| 9 | 1.0 |
| 10 | 1.0 |
</details>

![](image/a30e61b8989c1152ac2834e527150bb12e506ebc4cfc16d5de79dddd2a7dda28.jpg)

<details>
<summary>line</summary>

| t Sec | Unit-Ramp Input and Output |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
</details>

(b)

![](image/1d98179906822c65e2af81655ff93e024a0901573a952609ec2947bc241c0918.jpg)

<details>
<summary>line</summary>

| t Sec | Unit-Ramp Input and Feedback Signal |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
</details>

(c)

A–6–14. Consider a system with an unstable plant as shown in Figure 6–83(a). Using the root-locus approach, design a proportional-plus-derivative controller that is, determine the values ofA $K _ { p }$ and $T _ { d } )$ such that the damping ratio $\zeta$ of the closed-loop system is 0.7 and the undamped natural frequency $\omega _ { n }$ is 0.5 radsec.

Solution. Note that the open-loop transfer function involves two poles at s=1.085 and $s = - 1 . 0 8 5$ and one zero at $s = - 1 / T _ { d }$ which is unknown at this point.,

Since the desired closed-loop poles must have $\omega _ { n } = 0 . 5$ radsec and $\zeta = 0 . 7$ , they must be located at

$$s = 0. 5 / 1 8 0 ^ {\circ} \pm 4 5. 5 7 3 ^ {\circ}$$

![](image/781e8d8092f742b505f6b9e9c1d357d1c6ddd6526c76c59a6ed0c065cb0c4dbd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Kp(1 + Tds)"]
    B --> C["1/(10000 (s² - 1.1772))"]
    C --> D["Output"]
    D --> E["Feedback"]
    E --> A
```
</details>
