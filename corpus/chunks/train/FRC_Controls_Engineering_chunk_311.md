# Simulation

Figure 9.3 shows the state estimates and measurements of the Kalman filter over time. Figure 9.4 shows the position estimate and variance over time. Figure 9.5 shows the wall position estimate and variance over time. Notice how the variances decrease over time as the filter gathers more measurements. This means that the filter becomes more confident in its state estimates.

![](image/a4576c4118a1254b0b69ac62d626be99b9499aa3d850898b6a2cd8d57b28592e.jpg)

<details>
<summary>line</summary>

| Time (s) | Robot position estimate (cm) | Robot velocity estimate (cm/s) | Wall position estimate (cm) | Robot to corner measurement (cm) | Robot to wall measurement (cm) |
| --- | --- | --- | --- | --- | --- |
| 0 | 55 | 0 | 200 | 45 | 150 |
| 20 | 65 | 0 | 200 | 70 | 130 |
| 40 | 75 | 0 | 200 | 85 | 120 |
| 60 | 90 | 0 | 200 | 100 | 110 |
| 80 | 105 | 0 | 200 | 125 | 95 |
| 100 | 125 | 0 | 200 | 135 | 75 |
</details>

Figure 9.3: State estimates and measurements with Kalman filter

The final precisions in estimating the position of the robot and the wall are the square roots of the corresponding elements in the covariance matrix. That is, 0.5188 m and 0.4491 m respectively. They are smaller than the precision of the raw measurements, ${ \sqrt { 1 0 } } = 3 . 1 6 2 3$ m. As expected, combining the information from several measurements produces a better estimate than any one measurement alone.
