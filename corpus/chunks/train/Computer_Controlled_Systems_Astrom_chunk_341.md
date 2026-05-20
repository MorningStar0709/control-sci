# Controller Design

The Diophantine equation (5.4) is

$$(z ^ {2} - 2 \beta z + 1) R (z) + (1 - \beta) (z + 1) S (z) = A _ {o} (z) A _ {c} (z) = P (z)$$

where

$$
\begin{array}{l} R (z) = (z + r) (z - 1) \\ S (z) = s _ {0} z ^ {2} + s _ {1} z + s _ {2} \\ P (z) = A _ {0} (z) A _ {c} (z) = z ^ {4} + p _ {1} z ^ {3} + p _ {2} z ^ {2} + p _ {3} z + p _ {4} \\ \end{array}
$$

The controller parameters are given by

$$
\begin{array}{l} r = 1 - \frac {P (- 1)}{4 (1 + \beta)} \\ s _ {0} = \frac {p _ {1} - r + 1 + 2 \beta}{1 - \beta} \\ s _ {1} = \frac {p _ {2} - p _ {1} - 2 \beta + 2 (1 + \beta) (r - 1)}{1 - \beta} \\ s _ {2} = \frac {p _ {4} + r}{1 - \beta} \\ \end{array}
$$

The polynomial $T$ is given by

$$T (z) = \frac {A _ {c} (1) A _ {o} (z)}{B (1)}$$

![](image/020ab24824478cea159cdfb372889667bf06b4023bd72e2d51fce23bfb9cebc5.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | 1 | 1 |
| 10 | 1 | 1 |
| 15 | 0.5 | 1 |
| 20 | 0.5 | 1 |
| 25 | 0.5 | 1 |
| 30 | 0.5 | 1 |
| 35 | 0.5 | 1 |
| 40 | 0.5 | 1 |
</details>

![](image/984bd5d107f13bd356ee6143b560007d000f7071df0ff6e2ae1b66b1b53ee0e6.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | 1 | 1 |
| 10 | 1 | 1 |
| 15 | 1 | 1 |
| 20 | 1 | 1 |
| 25 | 1 | 1 |
| 30 | 1 | 1 |
| 35 | 1 | 1 |
| 40 | 1 | 1 |
</details>

Figure 5.18 Simulation of the nominal design for the harmonic oscillator when $\omega = 1.5$ , $\omega_{\mathrm{obs}} = 3$ , $\zeta = \zeta_{\mathrm{obs}} = 0.7$ , and $h = 0.2$ . (a) Without an integrator. (b) With an integrator in the controller.

![](image/0f5118b859d2254116b31ecaf76445bfabf68e686da39b5e5d5e6fef897209b8.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | 1 | 1 |
| 10 | 1 | 1 |
| 15 | 1 | 1 |
| 20 | 1 | 1 |
| 25 | 1 | 1 |
| 30 | 1 | 1 |
| 35 | 1 | 1 |
| 40 | 1 | 1 |
</details>

![](image/65cebe4f3477e1569ce820b70c0a7a5bcf270589d5e255a75331caacdba2c3e5.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | 1 | 1 |
| 10 | 1 | 1 |
| 15 | 1 | 1 |
| 20 | 1 | 1 |
| 25 | 1 | 1 |
| 30 | 1 | 1 |
| 35 | 1 | 1 |
| 40 | 1 | 1 |
</details>

Figure 5.19 Response of the pole-placement design for the harmonic oscillator for different observer dynamics. (a) $\omega_{obs} = 4$ . (b) $\omega_{obs} = 8$ .
