<details>
<summary>line</summary>

| Time(s) | Voltage (V) - Solid Line | Voltage (V) - Dashed Line | Voltage (V) - Dotted Line |
| --- | --- | --- | --- |
| 0.0 | -3.0 | -3.0 | -3.0 |
| 0.5 | -0.5 | -0.8 | -0.2 |
| 1.0 | 0.1 | 0.0 | 0.2 |
| 1.5 | 0.0 | 0.0 | 0.0 |
| 2.0 | 0.0 | 0.0 | 0.0 |
</details>

![](image/a33158dbbfe276e7940cb91f5b7a0d16ba119cc3303ca925bd2369aaf4a3ae08.jpg)

<details>
<summary>line</summary>

| Time(s) | Angle error (rad) - Solid Line | Angle error (rad) - Dashed Line | Angle error (rad) - Dotted Line |
| --- | --- | --- | --- |
| 0.0 | -1.0 | -1.0 | -1.0 |
| 0.5 | -0.4 | -0.6 | -0.3 |
| 1.0 | 0.0 | -0.2 | 0.0 |
| 1.5 | 0.0 | 0.0 | 0.0 |
| 2.0 | 0.0 | 0.0 | 0.0 |
</details>

Figure 7.8 Results of LQ design for the dc servo: input voltage and angle error for Q11 = 4 (dashed), 9 (solid), and 20 (dotted)

![](image/f7052e8fc84c434f71185e946a59d172912d71753741cf91ed05c84a86750942.jpg)

<details>
<summary>line</summary>

| Time(s) | Q22 = 0 | Q22 = 3 |
| --- | --- | --- |
| 0.0 | -1.0 | -1.0 |
| 0.5 | -0.4 | -0.6 |
| 1.0 | 0.0 | -0.2 |
| 1.5 | 0.0 | -0.1 |
| 2.0 | 0.0 | -0.05 |
</details>

![](image/1249e6177b2b4c3ccb0ae0dd5d1d14a42ec0cedb0fff3c6abd5320861ebbc052.jpg)

<details>
<summary>line</summary>

| Time(s) | Angular velocity (rad/s) for Q22 = 0 | Angular velocity (rad/s) for Q22 = 3 |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 1.5 | 1.1 |
| 1.0 | 0.4 | 0.4 |
| 1.5 | 0.0 | 0.2 |
| 2.0 | 0.0 | 0.1 |
</details>

Figure 7.9 Results of LQ design for the dc servo: effect of weighting the angular velocity

which makes the error response more damped. The optimal gain for $Q_{22} = 3$ is $\mathbf{k}^T = [3 \quad 1.7165 \quad 0.2838]$ ; clearly, the velocity gain is greater than in the preceding case.
