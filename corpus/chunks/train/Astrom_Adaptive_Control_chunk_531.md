# EXAMPLE 7.6 Time-varying parameters

The system in Examples 7.2 and 7.3 will now be controlled by a suboptimal dual controller that minimizes Eq. (7.19), with $f(P(t + 2))$ given by Eq. (7.20). (See Wittenmark and Elevitch (1985).) Figure 7.7 shows the same experiment using the same noise sequences as in Fig. 7.4. With the suboptimal dual controller there is no tendency toward turn-off. The simulation in Fig. 7.7 shows that the suboptimal dual controller is much better than the cautious controller. Comparisons using Monte Carlo simulations have also been done with the numerically computed optimal dual controller. The result is that the suboptimal dual controller is as good as the numerically computed optimal controller. A summary of some simulations is shown in Fig. 7.8, which shows mean values and standard deviations of the loss when the standard deviation of the parameter noise $R_{1}$ is changed. It is assumed that

$$\varphi_ {b} = \sqrt {1 - R _ {1}}$$

![](image/25d69e3e4c9386fab2d30b3deda17c15171f0a249de5c021d9945522a3dc0941.jpg)

<details>
<summary>line</summary>

| Time | y |
| --- | --- |
| 0 | ~0 |
| 100 | ~-5 |
| 200 | ~-5 |
| 300 | ~-5 |
| 400 | ~-5 |
</details>

![](image/1024456e5cafb8028c03d32e0c8ffbcc9d73eeca09827bc8300b499eef64fc74.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | -1.5 |
| 100 | -1.8 |
| 200 | -1.2 |
| 300 | -1.6 |
| 400 | -1.4 |
</details>

![](image/df1d44e69e6e8365b96fe44e84b76b4e06386a632bd49e3c5c0af53e9d1893bb.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 100 | 10 |
</details>

![](image/44fb73650fdd9919a45c959258bf852d5d9ac0a422d3ed97cf7c33de82f4c735.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | ~-1 |
| 100 | ~-2 |
| 200 | ~-1 |
| 300 | ~-1 |
| 400 | ~-1 |
</details>

![](image/aeddaa64450c744ad8dd3326a4da0cd8db1b493592f485b17f499e059484b439.jpg)

<details>
<summary>line</summary>

| Time | p_b |
| --- | --- |
| 0 | ~0 |
| 100 | ~0 |
| 200 | ~0 |
| 300 | ~0 |
| 400 | ~0 |
</details>

![](image/35e8fa040dca8d62a7c073585c69382555290b3aa7d5d8b499da9ca11c864f5b.jpg)

<details>
<summary>line</summary>

| Time | Σy² |
| --- | --- |
| 0 | 0 |
| 100 | ~300 |
| 200 | ~700 |
| 300 | ~1000 |
| 400 | ~1200 |
</details>

Figure 7.7 Simulation of the integrator with time-varying gain using a suboptimal dual controller. Compare Fig. 7.4.
