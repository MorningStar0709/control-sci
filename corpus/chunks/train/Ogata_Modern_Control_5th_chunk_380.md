![](image/d0506a67e2ba65284e2fe7be655123f21523e8ce7df75e1cd4f64e4d24aa2135.jpg)

<details>
<summary>other</summary>

| Angle (°) | Value |
| --- | --- |
| 45.573 | -2.039 |
| 25.913 | -1.085 |
| 166.026 | 1.085 |
</details>

Figure 6–83   
(a) PD control of an unstable plant; (b) root-locus diagram for the system.

$( \zeta = 0 . 7$ corresponds to a line having an angle of 45.573° with the negative real axis.) Hence, the desired closed-loop poles are at

$$s = - 0. 3 5 \pm j 0. 3 5 7$$

The open-loop poles and the desired closed-loop pole in the upper half-plane are located in the diagram shown in Figure 6–83(b). The angle deficiency at point $s = - 0 . 3 5 + j 0 . 3 5 7$ is

$$- 1 6 6. 0 2 6 ^ {\circ} - 2 5. 9 1 3 ^ {\circ} + 1 8 0 ^ {\circ} = - 1 1. 9 3 9 ^ {\circ}$$

This means that the zero at $s = - 1 / T _ { d }$ must contribute 11.939°, which, in turn, determines the location of the zero as follows:

$$s = - \frac {1}{T _ {d}} = - 2. 0 3 9$$

Hence, we have

$$K _ {p} (1 + T _ {d} s) = K _ {p} T _ {d} \left(\frac {1}{T _ {d}} + s\right) = K _ {p} T _ {d} (s + 2. 0 3 9) \tag {6-31}$$

The value of $T _ { d }$ is

$$T _ {d} = \frac {1}{2 . 0 3 9} = 0. 4 9 0 4$$

The value of gain $K _ { p }$ can be determined from the magnitude condition as follows:

$$\left| K _ {p} T _ {d} \frac {s + 2 . 0 3 9}{1 0 0 0 0 (s ^ {2} - 1 . 1 7 7 2)} \right| _ {s = - 0. 3 5 + j 0. 3 5 7} = 1$$

or

$$K _ {p} T _ {d} = 6 9 9 9. 5$$

Hence,

$$K _ {p} = \frac {6 9 9 9 . 5}{0 . 4 9 0 4} = 1 4, 2 7 3$$

By substituting the numerical values of $T _ { d }$ and $K _ { p }$ into Equation (6–31), we obtain

$$K _ {p} \left(1 + T _ {d} s\right) = 1 4, 2 7 3 (1 + 0. 4 9 0 4 s) = 6 9 9 9. 5 (s + 2. 0 3 9)$$

which gives the transfer function of the desired proportional-plus-derivative controller.

A–6–15. Consider the control system shown in Figure 6–84. Design a lag compensator $G _ { c } ( s )$ such that the static velocity error constant $K _ { v }$ is $5 0 \mathrm { s e c } ^ { - 1 }$ without appreciably changing the location of the original closed-loop poles, which are at $s = - 2 \pm j \sqrt { 6 }$ .

Solution. Assume that the transfer function of the lag compensator is

$$G _ {c} (s) = \hat {K} _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\beta T}} \quad (\beta > 1)$$

![](image/e30a481272c63118ec0e44e25e9ecd5e8b7094f9dae682499e39a5541340a56b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum
    Sum --> Gc["Gc(s)"]
    Gc --> |10/(s(s+4))| C["C(s)"]
    C --> |feedback| Sum
```
</details>

Figure 6–84 Control system.

Since $K _ { v }$ is specified as $5 0 \mathrm { s e c } ^ { - 1 }$ , we have
