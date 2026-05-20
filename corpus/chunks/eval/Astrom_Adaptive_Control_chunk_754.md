The industrial digester in the study produced 350 tons per day of kraft pulp. Two grades, R and K, are manufactured. From identification experiments it was found that the digester can be described by the model

![](image/60c0b7b19ba394387b81c68a6454f45774fd6ec20cab6b9ad62292d984fb5b30.jpg)

<details>
<summary>line</summary>

| Time (min) | Conventional | Adaptive |
| --- | --- | --- |
| 0 | 150 | 80 |
| 50 | 20 | 0 |
| 100 | 10 | 0 |
| 150 | 30 | 0 |
</details>

Figure 12.13 Autocovariance of the chip level under conventional and adaptive control. (With courtesy of Paprican.)

$$(1 + a _ {1} q ^ {- 1}) \Delta y (t) = (b _ {0} + b _ {1} q ^ {- 1} + b _ {2} q ^ {- 2}) \Delta u (t - 2) + (1 + c _ {1} q ^ {- 1} + c _ {2} q ^ {- 2}) e (t)$$

where $\Delta y(t)$ is the difference in level, $\Delta u(t)$ is the change in blow flow, and $e(t)$ is white noise. The sampling period is 5 minutes. The identification experiments also indicated that it would be feasible to use fixed values of all the parameters except the $b_{i}$ 's. The adaptive controller will thus be able to compensate for gain changes and changes in the time delay of the process. A GPC algorithm with $N_{u}=1$ , $N_{1}=1$ , and $N_{2}=15-20$ is used (see Eq. 4.61). Figure 12.13 shows the autocovariance of the level when conventional PID control and adaptive control were used. The chip level signal is essentially uncorrelated after three lags (15 minutes). The standard deviation of the level decreased from 11.3% to 8.6%. This improvement of the chip level leads to direct improvements in pulp quality. Table 12.1 shows permanganate number (P-number), which is a standard laboratory test of the residual lignin in the pulp. The P-number is closely related to the kappa number. The P-numbers were measured on samples from the blow flow collected once every two hours. For both grades (R and K) the average P-numbers are closer to the target values, and the standard deviations are reduced.

In summary, the advantages of the adaptive controller are

- Reduction of chip level and P-number variability,   
- Reduced need for operator intervention,   
- Elimination of manual retuning, and   
• Prediction of potential problems with hang-ups in the chip column.

The pulp digester study is an example of a special-purpose adaptive controller. The process model is tailored to fit the specific application, and the parameters can be related to physical parts of the system.
