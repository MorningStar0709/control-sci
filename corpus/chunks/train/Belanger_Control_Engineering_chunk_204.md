In almost all cases, the loop gain has a magnitude greater than 1 for all $\omega < \omega_{c}$ , and less than 1 for $\omega > \omega_{c}$ . The frequency $\omega_{c}$ at which the loop gain has unit magnitude is called the crossover frequency. In view of Equations 4.29 and 4.30, $\omega_{c}$ is roughly the same as the system bandwidth. Figures 4.17 a) and b) illustrate the crossover frequency and the approximate expressions of Equations 4.30 and 4.31. The crossover frequency is approximately 2 rad/s, where $|FP(j\omega)| = 0$ db. For large loop gain (roughly, more than 20 db, for $\omega < 0.4$ rad/s), Figure 4.17 shows that $FP/(1 + FP)$ is close to 1 (0 db, $0^{\circ}$ of phase); from Figure 4.18, $1/(1 + FP)$ is nearly $1/FP$ (log magnitude and phase are the negatives of those of $FP$ ). For small loop gain (roughly, less than $-20$ db, for $\omega > 6$ rad/s), we see that $FP/(1 + FP)$ approximates $FP$ in magnitude and phase, while $1/(1 + FP)$ is near 1.

![](image/b77f47d1a722b6f1a3518874fede105a3df4135ad53fb73ce91ad390cc1f3117.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | FP Magnitude (db) | FP/(1 + FP) Magnitude (db) |
| --- | --- | --- |
| 0.1 | 32 | 0 |
| 1 | 10 | 5 |
| 10 | -28 | -20 |
</details>

![](image/21945a20de9254690d48fad8d6a25d8c89ea639cc8068e3c02af6c3abf62b55a.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Phase (deg) - FP | Phase (deg) - FP/(1 + FP) |
| --- | --- | --- |
| 0.1 | -100 | 0 |
| 1 | -120 | -20 |
| 10 | -180 | -160 |
</details>

(a)

![](image/db8f4d32faa5233778cd3fe1dbe7a7bb8d58cbdd52d90a85e471d515bf20773d.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (db) |
| --- | --- |
| 0.1 | 30 |
| 1 | 0 |
| 10 | -30 |
</details>

![](image/d486a912f3eb368ef2c8a987527ff0bee1c53a399b5479153b58324eb2051c78.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | 1/FP (Phase deg) | 1/(1 + FP) (Phase deg) |
| --- | --- | --- |
| 0.1 | 95 | -95 |
| 1 | 120 | -120 |
| 10 | 170 | -180 |
</details>

(b)   
Figure 4.17 Illustration of closed-loop frequency response as a function of open-loop response reference output: a) Reference output; b) Disturbance output

The recipe appears simple enough: make the loop gain large in the passband. Unfortunately, as we shall see, stability complicates the picture and restricts our ability to follow the simple recipe. Naive attempts to apply it almost invariably result in unstable designs.
