<details>
<summary>line</summary>

| t | cj (system) | cj (estimate) | cb (system) | cb (estimate) | cA (system) | cA (estimate) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.0 | 4.0 | 3.0 | 2.0 | -1.0 | -2.0 |
| 2 | 2.0 | 3.5 | 2.5 | 1.5 | -0.5 | -1.5 |
| 4 | 3.0 | 3.0 | 2.0 | 1.0 | 0.0 | -1.0 |
| 6 | 4.0 | 2.5 | 1.5 | 0.5 | 0.5 | -0.5 |
| 8 | 5.0 | 2.0 | 1.0 | 0.0 | 1.0 | 0.0 |
| 10 | 6.0 | 1.5 | 0.5 | -0.5 | 1.5 | 0.5 |
| 12 | 7.0 | 1.0 | 0.0 | -1.0 | 2.0 | 1.0 |
</details>

Figure 4.29: Pure PF with optimal importance function.

Next we assume that the MHE optimization cannot finish in one sample, but requires M samples. If we attempt a pure MHE solution in this situation, the estimator falls hopelessly behind; an estimate using data $\mathbf { y } ( k - M , k ) , k \geq M$ is not available until time Mk. Instead we use MHE/PF as follows.

1. At time k run MHE on data ${ \bf y } ( k - M , k )$ . This computation is assumed to finish at time $k + M$ . For simplicity, assume N large and a noninformative prior.   
2. Draw samples from $N ( \hat { x } ( k ) , P ( k ) )$ . Run the particle filtering update from time k to time $k + M$ . For illustrative purposes, we assume this PF step finishes in one sample.   
3. Update k to $k + M$ and repeat.

For illustrative purposes, we choose $M = 1 0$ and apply the combination of MHE and PF with the simple importance function, also using 50 particles as before. The results are shown in Figure 4.30. Notice that again the poor initial samples lead to significant estimate error.

![](image/a7012daa59ffed0ca9c1b0b3bbb983b27046344aec2a7c38f213c15ffa3c51d1.jpg)

<details>
<summary>line</summary>

| t | c_A | c_B | y |
| --- | --- | --- | --- |
| 0 | -1.5 | 5.0 | 4.0 |
| 1 | 1.0 | 4.5 | 5.5 |
| 2 | 1.5 | 4.0 | 4.5 |
| 3 | 1.5 | 3.5 | 4.0 |
| 4 | 1.5 | 3.0 | 4.5 |
| 5 | 1.5 | 2.5 | 5.0 |
| 6 | 1.5 | 2.0 | 7.0 |
| 7 | 1.5 | 1.5 | 7.5 |
| 8 | 1.5 | 1.0 | 7.8 |
| 9 | 1.5 | 1.0 | 8.0 |
| 10 | 1.5 | 1.0 | 8.2 |
| 11 | 1.5 | 1.0 | 8.5 |
| 12 | 1.5 | 1.0 | 8.8 |
</details>

Figure 4.30: Combination MHE/PF with simple importance function.

But the inaccurate sample is repaired after M = 10 samples. The MHE calculation completes by about t = 2, and the samples are reinitialized from the MHE cost function at t = 1, and run forward from t = 1. These reinitialized samples converge to the true state shortly after t = 1.7
