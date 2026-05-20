$$
\begin{array}{l} \sigma_ {X} ^ {2} = E \{X ^ {2} \} = E \{(X _ {t} \sin \theta_ {i} + Z _ {t} \cos \theta_ {i}) ^ {2} \} \\ = [ \sin^ {2} \theta_ {i} ] \sigma_ {X t} ^ {2} + [ \sin 2 \theta_ {i} ] \langle X _ {t}, Y _ {t} \rangle + [ \cos^ {2} \theta_ {i} ] \sigma_ {Z t} ^ {2}. \tag {5.40} \\ \end{array}
$$

Next, we note that $\sigma _ { X } ^ { 2 }$ is dependent on the variance of the altitude error $z _ { t } ^ { 2 }$ , which can be large. The value of the cross-correlation $\langle X _ { t } , Z _ { t } \rangle$ is relatively small. The normalized CEP radius, $R _ { C E P }$ , can be obtained in terms of $\sigma _ { Y }$ from the following relation:

$$(R _ {C E P} / \sigma_ {Y}) = (0. 5 6 2 / K) + 0. 6 1 5 \quad \text { for } \quad K \geq 0. 3, \tag {5.41}$$

![](image/0d932acae1386e64623a9aaa27350dfdbcf0afebc20a7ab98f2ff18dbc6761dc.jpg)

<details>
<summary>line</summary>

| Flight time, min | Initial platform tilt (CEP) | Accelerometer error (CEP) | Gyro drift (CEP) |
| --- | --- | --- | --- |
| 0 | 7 | 18 | 16 |
| 10 | 0 | 20 | 14 |
| 20 | 0 | 12 | 10 |
| 30 | 0 | 2 | 8 |
| 40 | 0 | 2 | 6 |
| 50 | 0 | 2 | 4 |
| 60 | 0 | 2 | 2 |
| 70 | 0 | 2 | 2 |
| 80 | 0 | 2 | 2 |
| 90 | 0 | 2 | 2 |
| 100 | 0 | 2 | 2 |
| 110 | 0 | 2 | 2 |
| 120 | 0 | 2 | 2 |
</details>

Fig. 5.25. INS performance with GPS update and after loss of GPS signal.

where

$$K \equiv (\sigma_ {Y} ^ {2} / \sigma_ {X} ^ {2}) ^ {1 / 2}.$$

Covariance simulation is used to derive weapon delivery aircraft navigation accuracies as a function of their trajectories to the target. Figure 5.25 shows the horizontal position and velocity errors of a typical INS using GPS updates, obtained from a covariance analysis simulation.
