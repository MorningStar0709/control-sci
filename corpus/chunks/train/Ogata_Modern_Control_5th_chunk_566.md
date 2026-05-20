# MATLAB Program 7–32

num1 = [40 24 3.2]; den1 = [1 9.02 24.18 16.48 0.32 0]; bode(num1,den1) title('Bode Diagram of Gc(s)G(s)')

Figure 7–153 Bode diagram of the open-loop transfer function Gc(s)G(s) of the compensated system.   
![](image/3c4073ae9fa7f1535ada14346d8ffd74222e20bf154ebf29759df45614cc46be.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Magnitude (dB) | Phase (deg) |
| --- | --- | --- |
| 1e-4 | 100 | -100 |
| 1e-3 | ~80 | ~-95 |
| 1e-2 | ~60 | ~-100 |
| 1e-1 | ~30 | ~-150 |
| 1e0 | ~10 | ~-100 |
| 1e1 | ~-30 | ~-200 |
| 1e2 | ~-90 | ~-250 |
</details>

Since the phase margin of the compensated system is 50°, the gain margin is 12 dB, and the static velocity error constant is 10 sec–1, all the requirements are met.

We shall next investigate the transient-response characteristics of the designed system.

Unit-Step Response: Noting that

$$G _ {c} (s) G (s) = \frac {4 0 (s + 0 . 4) (s + 0 . 2)}{(s + 4) (s + 0 . 0 2) s (s + 1) (s + 4)}$$

we have

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {G _ {c} (s) G (s)}{1 + G _ {c} (s) G (s)} \\ = \frac {4 0 (s + 0 . 4) (s + 0 . 2)}{(s + 4) (s + 0 . 0 2) s (s + 1) (s + 4) + 4 0 (s + 0 . 4) (s + 0 . 2)} \\ \end{array}
$$

To determine the denominator polynomial with MATLAB, we may proceed as follows: Define

$$
\begin{array}{l} a (s) = (s + 4) (s + 0. 0 2) = s ^ {2} + 4. 0 2 s + 0. 0 8 \\ b (s) = s (s + 1) (s + 4) = s ^ {3} + 5 s ^ {2} + 4 s \\ c (s) = 4 0 (s + 0. 4) (s + 0. 2) = 4 0 s ^ {2} + 2 4 s + 3. 2 \\ \end{array}
$$

Then we have

$$a = [ 1 4. 0 2 0. 0 8 ]b = [ 1 \quad 5 \quad 4 \quad 0 ]c = [ 4 0 \quad 2 4 \quad 3. 2 ]$$

Using the following MATLAB program, we obtain the denominator polynomial.

$$
\begin{array}{l} \hline a = [ 1 4. 0 2 0. 0 8 ]; \\ b = [ 1 5 4 0 ]; \\ c = [ 4 0 2 4 3. 2 ]; \\ p = [ \text {conv(a,b)} ] + [ 0 0 0 c ] \\ p = \\ \quad 1. 0 0 0 0 9. 0 2 0 0 2 4. 1 8 0 0 5 6. 4 8 0 0 2 4. 3 2 0 0 3. 2 0 0 0 \\ \hline \end{array}
$$

MATLAB Program 7–33 is used to obtain the unit-step response of the compensated system. The resulting unit-step response curve is shown in Figure 7–154. (Note that the gain-adjusted but uncompensated system is unstable.)

$$
\begin{array}{l} \text {MATLAB Program 7 - 33} \\ \hline \% * * * * U n i t - s t e p r e s o n s e * * * \\ \text {num = [40 24 3.2];} \\ \text {den = [1 9.02 24.18 56.48 24.32 3.2];} \\ \text {t = 0:0.2:40;} \\ \text {step(num,den,t)} \\ \text {grid} \\ \text {title('Unit-Step Response of Compensated System')} \end{array}
$$

![](image/89728b993dd94c117a3ce8f20c1ec5f91b9268a2f68adfc34e2fab8b3a0462ca.jpg)

<details>
<summary>line</summary>
