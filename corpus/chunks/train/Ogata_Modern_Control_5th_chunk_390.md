![](image/81894b1ab0e75f3a9dbae592691f90c3960cc1d1c25b799e3cea883e938b9a6b.jpg)

<details>
<summary>line</summary>

| σ | jω |
| --- | --- |
| -10 | -0.5 |
| -2 | 0.5 |
</details>

Figure 6–95   
Pole and zero of $\hat { G } _ { c } ( s )$ .

The entire compensator $G _ { c } ( s )$ for the system becomes

$$G _ {c} (s) = \hat {G} _ {c} (s) \frac {s + 4}{2 s + 0 . 1} = K _ {c} \frac {(s + 2) ^ {2}}{(s + 9 . 9 1 5 8) ^ {2}} \frac {s + 4}{2 s + 0 . 1}$$

The value of $K _ { c }$ can be determined from the magnitude condition. Since the open-loop transfer function is

$$G _ {c} (s) G (s) = K _ {c} \frac {(s + 2) ^ {2} (s + 4)}{(s + 9 . 9 1 5 8) ^ {2} s (s ^ {2} + 0 . 1 s + 4)}$$

the magnitude condition becomes

$$\left| K _ {c} \frac {(s + 2) ^ {2} (s + 4)}{(s + 9 . 9 1 5 8) ^ {2} s (s ^ {2} + 0 . 1 s + 4)} \right| _ {s = - 2 + j 2 \sqrt {3}} = 1$$

Hence,

$$
\begin{array}{l} K _ {c} = \left| \frac {(s + 9 . 9 1 5 8) ^ {2} s (s ^ {2} + 0 . 1 s + 4)}{(s + 2) ^ {2} (s + 4)} \right| _ {s = - 2 + j 2 \sqrt {3}} \\ = 8 8. 0 2 2 7 \\ \end{array}
$$

Thus the compensator $G _ { c } ( s )$ becomes

$$G _ {c} (s) = 8 8. 0 2 2 7 \frac {(s + 2) ^ {2} (s + 4)}{(s + 9 . 9 1 5 8) ^ {2} (2 s + 0 . 1)}$$

The open-loop transfer function is given by

$$G _ {c} (s) G (s) = \frac {8 8 . 0 2 2 7 (s + 2) ^ {2} (s + 4)}{(s + 9 . 9 1 5 8) ^ {2} s \left(s ^ {2} + 0 . 1 s + 4\right)}$$

A root-locus plot for the compensated system is shown in Figure 6–96. The closed-loop poles for the compensated system are indicated in the plot. The closed-loop poles, the roots of the characteristic equation

$$(s + 9. 9 1 5 8) ^ {2} s \left(s ^ {2} + 0. 1 s + 4\right) + 8 8. 0 2 2 7 (s + 2) ^ {2} (s + 4) = 0$$

Root-Locus Plot of Compensated System   
![](image/0bbc8d99f00f19e8cdab6b41496de37ec35ceaeccb8b5bd64cbab95eca28f2c3.jpg)

<details>
<summary>scatter</summary>
