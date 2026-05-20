- For $\omega = 0$ : at $-20$ db, downward (increasing phase)   
- For $\omega = 1.81$ rad/s: at $-29.45$ db, upward (decreasing phase)   
- For $\omega = \infty$ : at the origin, downward (the Nyquist lower approaches the origin from $-270^{\circ}$ , in the top half plane)

![](image/a42a4a232ecd9d3833ca619822d82047e7992413441d2035fdf2e8928071b9b6.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Phase (deg) |
| --- | --- |
| 0.1 | -180 |
| 1.0 | -175 |
| 1.81 | -190 |
| 10 | -240 |
| 100 | -270 |
</details>

![](image/0c56908be0fdc209b311c8ccd101d2848f992c9eebe8b173a1d3882c0f8fe1da.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (dB) |
| --- | --- |
| 10⁻¹ | -29.45 |
| 10⁰ | -30 |
| 1.81 | -30 |
| 10¹ | -60 |
| 10² | -120 |
</details>

Figure 5.24 Bode plots

![](image/a1b6e26f6878df235fa647a9c9032ccb4cd87deee9ed6cb27b6916ab33657bcd.jpg)

<details>
<summary>text_image</summary>

N = 0 (-20db) N = -1 (-29.45db) N = 1 ω = ∞ N = 0
ω = 0 ↑ ω = 1.81
</details>

Figure 5.25 Real-axis crossings of the Nyquist plot

Figure 5.25 shows the real-axis crossings of the Nyquist plot, with the values of N corresponding to each interval. The stability interval, N = -1, is achieved for k > 0 and

$$- 2 9. 4 5 \mathrm{db} < \frac {1}{| k |} < - 2 0 \mathrm{db}$$

or

$$2 0 \mathrm{db} < k < 2 9. 4 5 \mathrm{db}.$$

Example 5.16 Use Bode plots to study the stability of

$$L (s) = \frac {k (s ^ {2} + 4)}{(s + 1) ^ {2} (s ^ {2} + 9) (s + 2)}.$$

Solution Figure 5.26 shows the Bode plots (MATLAB bode). Since $P = 0$ , we need $N = 0$ for stability. The real-axis crossings are as follows:

- For $\omega = 0$ : on the positive real axis (phase $= 0^{\circ}$ ) at a distance of $-13.2$ db from the origin, downward   
- For $\omega = 2$ : corresponding to the $j$ -axis zero, at the origin, upward (because the phase at $\omega = 2_{-}$ is $-171^{\circ}$ , corresponding to the lower half plane)   
- For $\omega = 2.22$ : on the positive real axis (phase $= -360^{\circ}$ ) at a distance of $-37.7$ db from the origin, downward   
- For $\omega = 3$ : corresponding to the $j$ -axis pole, far from the origin on the negative real axis, upward (because the circular arc begins at a point with a phase between $-360^{\circ}$ and $-400^{\circ}$ , in the lower half plane)   
- for $\omega = \infty$ ; at the origin, downward (because the approach is at $-630^{\circ}$ , equivalent to $-270^{\circ}$ )
