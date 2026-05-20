# 9.6.4 Kalman filter as Luenberger observer

A Kalman filter can be represented as a Luenberger observer by letting $\mathbf { L } = \mathbf { A } \mathbf { K } _ { k }$ (see appendix D.2). The Luenberger observer has a constant observer gain matrix L, so the steady-state Kalman gain is used to calculate it (see subsection 9.6.5).

Kalman filter theory provides a way to place the poles of the Luenberger observer optimally in the same way we placed the poles of the controller optimally with LQR. The eigenvalues of the Kalman filter are

$$\operatorname{eig} \left(\mathbf {A} \left(\mathbf {I} - \mathbf {K} _ {k} \mathbf {C}\right)\right) \tag {9.35}$$

![](image/b2cb7e91298a8dee7ba1a2c38a9648b8d458715d6cf628a211a11ce5c6a396ee.jpg)

<details>
<summary>line</summary>

| Time (s) | Robot position estimate (cm) | Robot position variance (cm²) |
| --- | --- | --- |
| 0 | 45 | 10 |
| 10 | 60 | 2 |
| 20 | 65 | 1 |
| 30 | 70 | 1 |
| 40 | 75 | 1 |
| 50 | 85 | 1 |
| 60 | 95 | 1 |
| 70 | 105 | 1 |
| 80 | 115 | 1 |
| 90 | 125 | 1 |
| 100 | 130 | 1 |
</details>

Figure 9.4: Robot position estimate and variance with Kalman filter

![](image/ed225c82360ea4fbedc923c0e99270607ba89962499e084e75ecc6e14f5e07cc.jpg)

<details>
<summary>line</summary>

| Time (s) | Wall position estimate (cm) | Wall position variance (cm²) |
| --- | --- | --- |
| 0 | 200 | 10 |
| 20 | 195 | 2 |
| 40 | 198 | 1 |
| 60 | 200 | 1 |
| 80 | 202 | 1 |
| 100 | 203 | 1 |
</details>

Figure 9.5: Wall position estimate and variance with Kalman filter
