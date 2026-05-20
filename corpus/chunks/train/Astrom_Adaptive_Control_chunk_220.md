![](image/1cb44745722ef2998c917923805000520148f700f3d32b76723bbcc3d7da5fa8.jpg)

<details>
<summary>line</summary>

| Time | Self-tuning control | Minimum variance control |
| --- | --- | --- |
| 0 | 0 | 0 |
| 100 | ~150 | ~120 |
| 200 | ~250 | ~220 |
| 300 | ~350 | ~320 |
| 400 | ~450 | ~420 |
| 500 | ~550 | ~520 |
</details>

Figure 4.3 The accumulated loss when a self-tuning regulator and the optimal minimum-variance controller are used on the system in Example 4.4.

The reason for the poor convergence of the three estimated process parameters is that the controller converges rapidly to a minimum-variance controller. After that there is poor excitation of the process. The example shows that the self-tuning controller compares well with the optimal controller for the known system. From the control law it can be seen that there may be numerical problems when $\hat{b}(t)$ is small.
