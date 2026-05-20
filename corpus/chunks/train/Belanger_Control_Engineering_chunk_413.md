| Time(s) | Velocity (m/s) - Solid Line | Velocity (m/s) - Dashed Line |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | ~2.5 | ~2.0 |
| 10 | ~5 | ~4.5 |
| 15 | ~7.5 | ~7.0 |
| 20 | ~10 | ~9.5 |
| 25 | ~12.5 | ~11.5 |
| 30 | ~14 | ~13 |
</details>

![](image/f79ae26c4902447105ecb385275ebf3fc462ae81b29c211faaede9a1783bffc6.jpg)

<details>
<summary>line</summary>

| Time(s) | Spring, coupler 1 | Spring, coupler 2 | Damper, coupler 1 |
| --- | --- | --- | --- |
| 0 | 10000 | 10000 | 0 |
| 5 | ~8000 | ~6000 | ~0 |
| 10 | ~7000 | ~5500 | ~0 |
| 15 | ~6500 | ~5000 | ~0 |
| 20 | ~6000 | ~4500 | ~0 |
| 25 | ~5500 | ~4000 | ~0 |
| 30 | ~5000 | ~3500 | ~0 |
</details>

Figure 7.18 LQ control of train motion, Trial 1: Traction force, desired and actual (dotted) velocities, coupler forces

To lower $F_{1}(t)$ , we increase the value of $R$ , nominally $(1/120)^{2}$ , by a factor that, after a few trials, turns out to be 35. The new gain is

$$
\begin{array}{l} K = [ 0. 4 5 5 9 \quad 0. 3 3 3 1 \quad 0. 2 1 7 0 \quad 0. 1 0 6 9 \quad 1 1. 5 4 \\ - 0. 2 6 2 2 \quad - 0. 3 3 7 1 \quad - 0. 3 8 6 5 \quad - 0. 4 1 1 0 \quad 5. 3 7 3 ] \\ \end{array}
$$

Figure 7.19 shows the responses. The coupler forces are even lower than before, and the traction does just meet the specification. Unfortunately, the velocity error is greater than 2 m/s in magnitude.

It is unlikely that the velocity specification can be met in this case. We need to either (i) relax the velocity error limit or (ii) follow a slower trajectory—for example, $25(1 - e^{-t/\tau})$ , $\tau > 40s$ .
