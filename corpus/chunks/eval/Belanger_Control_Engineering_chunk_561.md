# Example 9.13 (dc Servo)

In Example 6.11, a lead-lag compensator was designed for the dc servo. Obtain the discrete-time Bode plot and phase margin for the backward-difference implementation and $T_{s} = 0.05$ s, 0.1 s, and 0.2 s. Assume D/A conversion through a zero-order hold.

Solution The continuous-time compensator is

$$F _ {c} (s) = \frac {2 . 2 8 (1 . 1 4 s + 1) (0 . 6 3 s + 1)}{(1 . 7 6 s + 1) (0 . 1 7 7 s + 1)}.$$

To convert to discrete time, we note that a factor of the form $Ts \pm 1$ transforms as

$$T s \pm 1 \rightarrow T \frac {(z - 1)}{z T _ {s}} \pm 1 = \frac {(T \pm T _ {s}) z - T}{z T _ {s}}.$$

The compensator is

$$F (z) = 2. 2 8 \frac {[ (1 . 1 4 + T _ {s}) z - 1 . 1 4 ] [ (0 . 6 3 + T _ {s}) z - 0 . 6 3 ]}{[ (1 . 7 6 + T _ {s}) z - 1 . 7 6 ] [ (0 . 1 7 7 + T _ {s}) z - 0 . 1 7 7 ]}.$$

For $T_{s} = 0.05$ , the pulse transfer function of the plant (MATLAB c2dm) is

$$P (z) = \frac {(1 . 3 9 6 e - 3) z ^ {2} + (4 . 2 2 3 e - 3) z + 7 . 6 6 8 3 - 4}{z ^ {3} - 2 . 2 2 4 z ^ {2} + 1 . 5 2 4 z - 0 . 3 0 0 4}.$$

Figure 9.16 shows the Bode plots for all three values of $T_{s}$ . They are plotted against $\omega T_{s}$ ( $T_{s} = 1$ in MATLAB dbode).

The phase margins (MATLAB margin) are $53.6^{\circ}$ , $47.2^{\circ}$ , and $35.2^{\circ}$ , respectively, for $T_{s} = 0.05$ , 0.1, and 0.2.

![](image/9fde2a96196479633642916e5a10991f2bf145b6bd11936e12d7b65657365443.jpg)

<details>
<summary>line</summary>

| ω·Ts | Magnitude (db) for Ts = .05 | Magnitude (db) for Ts = .1 | Magnitude (db) for Ts = .2 |
| --- | --- | --- | --- |
| 0.1 | ~5 | ~10 | ~15 |
| 1 | ~-20 | ~-10 | ~-5 |
| 10 | ~-55 | ~-40 | ~-30 |
</details>

![](image/007a66bca556aaf1e2703b7951590dc86cb3f1a328f8a9e2b1016b1db1fb2145.jpg)

<details>
<summary>line</summary>

| ω·Ts | Phase (deg) for Ts = .05 | Phase (deg) for Ts = .1 | Phase (deg) for Ts = .2 |
| --- | --- | --- | --- |
| 0.1 | -100 | -100 | -100 |
| 1 | -200 | -180 | -160 |
| 10 | -350 | -340 | -330 |
</details>

Figure 9.16 Bode plot phases for Example 9.13, for $T_{s} = 0.05$ , 0.1, and 0.2 s
