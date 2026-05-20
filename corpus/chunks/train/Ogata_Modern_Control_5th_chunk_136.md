The bellows acts like a spring, and the following equation holds true:

$$A p _ {c} = k _ {s} y \tag {4-18}$$

where A is the effective area of the bellows and $k _ { s }$ is the equivalent spring constant— that is, the stiffness due to the action of the corrugated side of the bellows.

Assuming that all variations in the variables are within a linear range, we can obtain a block diagram for this system from Equations (4–16), (4–17), and (4–18) as shown in Figure 4–8(e). From Figure 4–8(e), it can be clearly seen that the pneumatic controller shown in Figure 4–8(a) itself is a feedback system.The transfer function between $p _ { c }$ and e is given by

$$\frac {P _ {c} (s)}{E (s)} = \frac {\frac {b}{a + b} K}{1 + K \frac {a}{a + b} \frac {A}{k _ {s}}} = K _ {p} \tag {4-19}$$

A simplified block diagram is shown in Figure 4–8(f). Since $p _ { c }$ and e are proportional, the pneumatic controller shown in Figure 4–8(a) is a pneumatic proportional controller. As seen from Equation (4–19), the gain of the pneumatic proportional controller can be widely varied by adjusting the flapper connecting linkage. [The flapper connecting linkage is not shown in Figure $4 \mathrm { - } 8 ( \mathrm { a } ) . ]$ In most commercial proportional controllers an adjusting knob or other mechanism is provided for varying the gain by adjusting this linkage.

As noted earlier, the actuating error signal moved the flapper in one direction, and the feedback bellows moved the flapper in the opposite direction, but to a smaller degree.

![](image/b9aa25f9db3a7a88cdec204817c10ff275d4597898a8da4daf1cda98e69c5f66.jpg)

<details>
<summary>text_image</summary>

Pb
X
Ps
Pc
(a)
</details>

![](image/04cce1d1e0cbf458bae5d06735b875ecfc94134a294029fe2bd9b3dc66003c88.jpg)

<details>
<summary>line</summary>

| X | Pb |
| --- | --- |
| 0 | Ps |
| >0.5 | Pa |
</details>

![](image/591e72eb8925d84c4864740bc39904e33386d4b81d438cc47b6c208c3f1e45ea.jpg)

<details>
<summary>line</summary>

| X | Pc |
| --- | --- |
| 0 | Ps |
| >0.5 | Pa |
</details>

Figure 4–9   
(a) Pneumatic controller without a feedback mechanism; (b) curves $P _ { b }$ versus X and $P _ { c }$ versus $X .$

The effect of the feedback bellows is thus to reduce the sensitivity of the controller. The principle of feedback is commonly used to obtain wide proportional-band controllers.
