The designed compensator has the following transfer function:

$$G _ {c} (s) = \frac {4 0}{s} \hat {G} _ {c} (s) = \frac {4 0 (0 . 1 5 2 6 s + 1)}{s}$$

![](image/ebabfe86acc0fd3e57bb20c414c8ab66bbdae210309e4ef258efdb6dd8056df4.jpg)  
Figure 8–54

Bode diagram of

$$G (s) = 4 0 (s + 0. 1)(0. 1 5 2 6 s + 1) /[ s (s ^ {2} + 1) ].$$

The open-loop transfer function of the designed system is

$$
\begin{array}{l} \text { Open - loop   transfer   function } = \frac {4 0 (0 . 1 5 2 6 s + 1)}{s} \frac {s + 0 . 1}{s ^ {2} + 1} \\ = \frac {6 . 1 0 4 s ^ {2} + 4 0 . 6 1 0 4 s + 4}{s (s ^ {2} + 1)}. \\ \end{array}
$$

We shall next check the unit-step response and the unit-ramp response of the designed system.

The closed-loop transfer function is

$$\frac {C (s)}{R (s)} = \frac {6 . 1 0 4 s ^ {2} + 4 0 . 6 1 0 4 s + 4}{s ^ {3} + 6 . 1 0 4 s ^ {2} + 4 1 . 6 1 0 4 s + 4}$$

The closed-loop poles are located at

$$s = - 3. 0 0 3 2 + j 5. 6 5 7 3s = - 3. 0 0 3 2 - j 5. 6 5 7 3s = - 0. 0 9 7 5$$

MATLAB Program 8–12 will produce the unit-step response curve of the designed system.The resulting unit-step response curve is shown in Figure 8–55. Notice that the closed-loop pole at s = −0.0975 and the plant zero at s = −0.1 produce a long tail of small amplitude.

MATLAB Program 8–12   
```matlab
% ***** Unit-Step Response *****
num = [6.104 40.6104 4];
den = [1 6.104 41.6104 4];
t = 0:0.01:10;
step(num,den,t)
grid 
```

![](image/66dfcf47b21ae76d42583ab95a682881137a3951bd0d39b755ebf0054216d83e.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0 | 0.0 |
| 0.5 | 1.3 |
| 1.0 | 0.9 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
| 4.5 | 1.0 |
| 5.0 | 1.0 |
| 5.5 | 1.0 |
| 6.0 | 1.0 |
| 6.5 | 1.0 |
| 7.0 | 1.0 |
| 7.5 | 1.0 |
| 8.0 | 1.0 |
| 8.5 | 1.0 |
| 9.0 | 1.0 |
| 9.5 | 1.0 |
| 10.0 | 1.0 |
</details>

Figure 8–55

Unit-step response of

$$C (s) / R (s) = (6. 1 0 4 s ^ {2} +4 0. 6 1 0 4 s + 4) / (s ^ {3} +6. 1 0 4 s ^ {2} + 4 1. 6 1 0 4 s + 4).$$

Figure 8–56 Unit-ramp response of C(s)/R(s)= (6.104s2 +40.6104s+ 4) $/ ( s ^ { 3 } + 6 . 1 0 4 s ^ { 2 } +$ 41.6104s+4).   
![](image/cccce400f1a48c924061aafa3a6634391df1e0d2b11652f9b6dbfd64f5951364.jpg)

<details>
<summary>line</summary>

| t (sec) | Input Ramp Function | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 2 | 2 | 2 |
| 4 | 4 | 4 |
| 6 | 6 | 6 |
| 8 | 8 | 8 |
| 10 | 10 | 10 |
| 12 | 12 | 12 |
| 14 | 14 | 14 |
| 16 | 16 | 16 |
| 18 | 18 | 18 |
| 20 | 20 | 20 |
</details>

MATLAB Program 8–13 produces the unit-ramp response curve of the designed system. The resulting response curve is shown in Figure 8–56.
