# Solution

Figure 4.4 (top) shows a typical EKF performance for these conditions. Note that the EKF cannot reconstruct the state for this system and that the estimates converge to incorrect steady states displaying negative concentrations of A and B. For some realizations of the noise sequences, the EKF may converge to the correct steady state. Even for these cases, however, negative concentration estimates still occur during the transient, which correspond to physically impossible states. Figure 4.4 (bottom) presents typical results for the clipped EKF, in which negative values of the filtered estimates are set to zero. Note that although the estimates converge to the system states, this estimator gives pressure

![](image/93377559257d59b4bc6429f6c8ab16af872ac5943874326c9a328f7a12287355.jpg)

<details>
<summary>line</summary>

| t | A | B | C | A_C | B_C | C_C |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.5 | 0.0 | 0.0 | 1.5 |
| 5 | 0.1 | -0.1 | 0.6 | 0.3 | -0.1 | 1.4 |
| 10 | 0.1 | -0.1 | 0.6 | 0.3 | -0.1 | 1.3 |
| 15 | 0.1 | -0.1 | 0.6 | 0.3 | -0.1 | 1.2 |
| 20 | 0.1 | -0.1 | 0.6 | 0.3 | -0.1 | 1.1 |
| 25 | 0.1 | -0.1 | 0.6 | 0.3 | -0.1 | 1.0 |
| 30 | 0.1 | -0.1 | 0.6 | 0.3 | -0.1 | 1.0 |
</details>

![](image/425fa3941c891fc09e223bdd6f71441b9570c566fa268f0553f01121e8becf7c.jpg)

<details>
<summary>line</summary>

| t | A | B | C |
| --- | --- | --- | --- |
| 0 | 0.0001 | 0.0001 | 0.0001 |
| 20 | 0.01 | 0.1 | 10 |
| 40 | 0.01 | 0.1 | 1 |
| 60 | 0.01 | 0.1 | 1 |
| 80 | 0.01 | 0.1 | 1 |
| 100 | 0.01 | 0.1 | 1 |
| 120 | 0.01 | 0.1 | 1 |
| 140 | 0.01 | 0.1 | 1 |
</details>

Figure 4.4: Evolution of the state (solid line) and EKF state estimate (dashed line). Top plot shows negative concentration estimates with the standard EKF. Bottom plot shows large estimate errors and slow convergence with the clipped EKF.

![](image/e29845497cab469c244de4bc74fccbba554b01d111c758ecdfde37a626f5bd38.jpg)

<details>
<summary>line</summary>

| t | A | B | C | A (dashed) | B (dashed) | C (dashed) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.5 | 0.0 | 0.0 | 0.0 |
| 5 | 0.2 | -0.1 | 0.6 | -0.1 | -0.2 | 1.4 |
| 10 | 0.3 | -0.2 | 0.7 | -0.2 | -0.3 | 1.3 |
| 15 | 0.4 | -0.3 | 0.75 | -0.3 | -0.4 | 1.2 |
| 20 | 0.5 | -0.4 | 0.8 | -0.4 | -0.5 | 1.1 |
| 25 | 0.6 | -0.5 | 0.85 | -0.5 | -0.6 | 1.0 |
| 30 | 0.7 | -0.6 | 0.9 | -0.6 | -0.7 | 0.9 |
</details>

![](image/49d705e63d3cf8cb256d49acfc51d9b90ea6c4ce904860211ded7bcac0405e56.jpg)

<details>
<summary>line</summary>
