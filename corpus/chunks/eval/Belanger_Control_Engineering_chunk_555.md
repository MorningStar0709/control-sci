# Solution

Figure 9.12 shows the Bode plots. In each case, there is a pole at z = 1, and the Nyquist contour is indented to the right so as to include that pole. Since P = 3, we want Z = 3 and N = 0 for stability.

For $T_{s} = 0.2$ , the pulse transfer function (MATLAB c2dm) is

$$P (z) = \frac {0 . 0 0 1 2 (z + 3 . 2 2 5) (z + 0 . 2 2 9 9)}{(z - 1) (z - 0 . 8 1 8 7) (z - 0 . 6 7 0 3)}.$$

The Bode plots are shown in Figure 9.12a. We note real-axis crossings at $\omega = 1.225$ rad/s (180°, -13.1 db) and $\omega = \pi / T_s = 15.708$ rad/s (360°, -69.78 db). The pole at $z = 1$ is indented. As the indentation is entered (from below the point $z = 1$ ), the phase is +90 (negative of the positive-frequency plot), so the crossing is to the far right. The diagram in Figure 9.12b shows the real-axis crossings.

For $N = 0$ , we require

$$0 < k < 1 3. 1 \mathrm{db}.$$

![](image/d6266ca21270075a68fe8e0b1319ae81fd54fa942ca478e736874530f2d30abc.jpg)

![](image/028ea74818710902c8d49188647d1d5a5bbb670f57ab8ccbbe9d7dfa54642bf8.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | deg |
| --- | --- |
| 0.01 | -100 |
| 0.1 | -100 |
| 1 | -200 |
| 10 | -300 |
| 100 | -400 |
</details>

Figure 9.12a Bode plots for the plant of Example 9.12, $T_{s} = 0.2s$

![](image/4f87223cf371981559eaad921cbc50d86811ca38c21adf8d4cb4883523d5b3aa.jpg)

<details>
<summary>text_image</summary>

N = 0
ω = 1.225
N = 2
-13.1 db
ω = 15.7
-69.8 db
N = 1
ω = 0
∞
</details>

Figure 9.12b Real axis crossings of the Nyquist plot, Example 9.12, $T_{s} = 0.2s$

![](image/358462284f825130bffb126b98617703981fba0659ce3199b606d095fc491708.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | db |
| --- | --- |
| 0.01 | 35 |
| 0.1 | 20 |
| 1 | 0 |
| 10 | -20 |
| 100 | -40 |
</details>

![](image/a646f646fedb427e0aefe4a0a47309755425fe8163346a08d826ad0c343f0c6c.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | deg |
| --- | --- |
| 0.01 | -100 |
| 0.1 | -100 |
| 1 | -200 |
| 10 | -350 |
</details>

Figure 9.12c Bode plots for the plant of Example 9.12, $T_{s} = 2s$

![](image/5b51183204c3b8291443755c8303f5517dce2ebb619ec5a93c6d7ba1b04f2ec5.jpg)

<details>
<summary>text_image</summary>

N = 0
ω = 0.688
N = 2
-5.85 db
ω = 15.7
-33.72 db
N = 1
ω = 0
∞
</details>

Figure 9.12d Real axis crossings of the Nyquist plot, Example 9.12, $T_{s} = 2s$

For $T_{s} = 2$ , the pulse transfer function is

$$P (z) = \frac {0 . 3 8 0 8 (z + 1 . 1 3 1 1) (z + 0 . 0 4 6 1)}{(z - 1) (z - 0 . 1 3 5 3) (z - 0 . 0 1 8 3)}.$$

Figure 9.12c shows the Bode plots. They are qualitatively similar to the ones for $T_{s}=0.2$ . Figure 9.12d is the diagram of real-axis crossings. For stability,

$$0 < k < 5. 8 5 \mathrm{db}.$$
