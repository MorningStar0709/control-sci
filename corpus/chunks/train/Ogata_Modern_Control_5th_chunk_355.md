<details>
<summary>line</summary>

| Point | σ | jω |
| --- | --- | --- |
| A | -2.5 | -2.5 |
| B | -8.5 | -8.5 |
| P | -3.0 | 55° |
</details>

Figure 6–58 Determination of the desired pole-zero location.

By simple calculations, we find that if we choose $T _ { 2 } = 5 ,$ , then

$$1 > \text { magnitude } > 0. 9 8, \quad - 1. 5 ^ {\circ} < \text { angle } < 0 ^ {\circ}$$

and if we choose $T _ { 2 } = 1 0 $ , then

$$1 > \text { magnitude } > 0. 9 9, \quad - 1 ^ {\circ} < \text { angle } < 0 ^ {\circ}$$

Since $T _ { 2 }$ is one of the time constants of the lag–lead compensator, it should not be too large. If $T _ { 2 } = 1 0$ can be acceptable from practical viewpoint, then we may choose $T _ { 2 } = 1 0 .$ . Then

$$\frac {1}{\beta T _ {2}} = \frac {1}{3 . 5 0 3 \times 1 0} = 0. 0 2 8 5$$

Thus, the lag–lead compensator becomes

$$G _ {c} (s) = (1 0) \left(\frac {s + 2 . 3 8}{s + 8 . 3 4}\right) \left(\frac {s + 0 . 1}{s + 0 . 0 2 8 5}\right)$$

The compensated system will have the open-loop transfer function

$$G _ {c} (s) G (s) = \frac {4 0 (s + 2 . 3 8) (s + 0 . 1)}{(s + 8 . 3 4) (s + 0 . 0 2 8 5) s (s + 0 . 5)}$$

No cancellation occurs in this case, and the compensated system is of fourth order. Because the angle contribution of the phase lag portion of the lag–lead network is quite small, the dominant closed-loop poles are located very near the desired location. In fact, the location of the dominant closed-loop poles can be found from the characteristic equation as follows: The characteristic equation of the compensated system is

$$(s + 8. 3 4) (s + 0. 0 2 8 5) s (s + 0. 5) + 4 0 (s + 2. 3 8) (s + 0. 1) = 0$$

which can be simplified to

$$
\begin{array}{l} s ^ {4} + 8. 8 6 8 5 s ^ {3} + 4 4. 4 2 1 9 s ^ {2} + 9 9. 3 1 8 8 s + 9. 5 2 \\ = (s + 2. 4 5 3 9 + j 4. 3 0 9 9) (s + 2. 4 5 3 9 - j 4. 3 0 9 9) (s + 0. 1 0 0 3) (s + 3. 8 6 0 4) = 0 \\ \end{array}
$$

The dominant closed-loop poles are located at

$$s = - 2. 4 5 3 9 \pm j 4. 3 0 9 9$$

The other closed-loop poles are located at

$$s = - 0. 1 0 0 3; \quad s = - 3. 8 6 0 4$$

Since the closed-loop pole at is very close to a zero ats = -0.1003 $s = - 0 . 1$ they almost cancel, each other. Thus, the effect of this closed-loop pole is very small. The remaining closed-loop pole does not quite cancel the zero at The effect of this zero is to cause a(s = -3.8604) s = -2.4. larger overshoot in the step response than a similar system without such a zero. The unit-step response curves of the compensated and uncompensated systems are shown in Figure 6–59(a).The unit-ramp response curves for both systems are depicted in Figure 6–59(b).
