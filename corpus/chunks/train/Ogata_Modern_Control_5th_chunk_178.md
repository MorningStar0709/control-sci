# PROBLEMS

B–4–1. Consider the conical water-tank system shown in Figure 4–42. The flow through the valve is turbulent and is related to the head H by

$$Q = 0. 0 0 5 \sqrt {H}$$

where Q is the flow rate measured in m3 sec and H is in meters.

Suppose that the head is 2 m at t=0. What will be the head at $t = 6 0 \mathrm { s e c ? }$

![](image/8f5e6c272c6f93f1da1dd6931d5f057f591411eb6735d5bb422210b4b0549744.jpg)

<details>
<summary>text_image</summary>

2m
3m
r
H
2m
</details>

Figure 4–42 Conical water-tank system.

B–4–2. Consider the liquid-level control system shown in Figure 4–43. The controller is of the proportional type. The set point of the controller is fixed.

Draw a block diagram of the system, assuming that changes in the variables are small. Obtain the transfer function between the level of the second tank and the disturbance input $q _ { d } .$ Obtain the steady-state error when the disturbance $q _ { d }$ is a unit-step function.

B–4–3. For the pneumatic system shown in Figure 4–44, assume that steady-state values of the air pressure and the displacement of the bellows are andP – $\bar { X }$ respectively., Assume also that the input pressure is changed from $\bar { P }$ to ${ \overline { { P } } } + p _ { i } ,$ where , $p _ { i }$ is a small change in the input pressure.This change will cause the displacement of the bellows to change a small amount x.Assuming that the capacitance of the bellows is C and the resistance of the valve is $R ,$ obtain the transfer function relating x and $p _ { i }$ .

![](image/e967f39c344d9b0aeeed2dc00bbd9f2ed009c9987d82b2b355c3e769d611a824.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Q̅ + qi"] --> B["Valve"]
    B --> C["C1"]
    C --> D["R1"]
    D --> E["Proportional controller"]
    E --> F["h2"]
    F --> G["H̅"]
    G --> H["C2"]
    H --> I["R2"]
    I --> J["Q̅ + q0"]
    E --> K["qd"]
    style A fill:#f9f,stroke:#333
    style J fill:#f9f,stroke:#333
```
</details>

Figure 4–43 Liquid-level control system.

![](image/dca4f33497e55701ae921c8da24cfdcc1907aa49d9b787b428dbacf2a8d1bed6.jpg)

<details>
<summary>text_image</summary>

P̄ + pᵢ
R
C
X̄ + x
k
A
P̄ + pₒ
</details>

Figure 4–44 Pneumatic system.

B–4–4. Figure 4–45 shows a pneumatic controller.The pneumatic relay has the characteristic that $p _ { c } = K p _ { b }$ , where $K > 0 ,$ . What kind of control action does this controller produce? Derive the transfer function $P _ { c } ( s ) / E ( s )$ .
