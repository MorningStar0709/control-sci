The disturbance at t = 5 also causes the PF samples with the simple importance function to be in the wrong locations. They do not recover and inaccurate estimates are produced by the PF. Another MHE calculation starts at t = 5 and finishes at t = 6, and the samples are reinitialized with the MHE cost function at t = 5 and run forward. After this resampling, the PF estimates again quickly converge to the true estimates after t = 6.

Next we use the combination of MHE and PF with the optimal importance function. These results are shown in Figure 4.31. We see as in the early part of Figure 4.29 that the samples cannot recover from the poor initial state prior and resampling from the MHE cost function takes place at t = 1 after the first MHE calculation finishes at t = 2. But as in the case of pure PF with the optimal importance function, the disturbance does not move the state so far from the samples that they are unable to recover and continue to provide accurate estimates. The MHE resampling that takes place at t = 5 after MHE finishes at t = 6 does not modify significantly the PF samples that are already well placed. -

![](image/fce8cceaa4b92efe459cf0a7611fa68292d1887de09f627c385c5f5651fb22a4.jpg)

<details>
<summary>line</summary>

| t | c_A | c_B | c_j |
| --- | --- | --- | --- |
| 0 | 0 | 4 | 5 |
| 2 | 1 | 2 | 5 |
| 4 | 1 | 3 | 5 |
| 6 | 1 | 5 | 8 |
| 8 | 1 | 6 | 8 |
| 10 | 1 | 7 | 8 |
| 12 | 1 | 8 | 8 |
</details>

Figure 4.31: Combination MHE/PF with optimal importance function.

Of course, the simulations shown in Figures 4.28–4.31 display the outcome of only single random realizations. A full characterization of the behavior of the four estimators is determined by running many such random simulations and computing the statistics of interest. We have not compiled these statistics because the single simulations are rather time consuming. After running several random simulations for each estimator, these single simulations were selected manually as representative behavior of the different estimators.
