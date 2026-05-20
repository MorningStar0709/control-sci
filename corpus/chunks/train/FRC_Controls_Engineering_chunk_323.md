# 9.7.2 Example

We will modify the robot model so that instead of a velocity of 0.8 cm/s with random noise, the velocity is modeled as a random walk from the current velocity.

$$
\mathbf {x} _ {k} = \left[ \begin{array}{l} x _ {k} \\ v _ {k} \\ x _ {k} ^ {w} \end{array} \right] \tag {9.46}

\mathbf {x} _ {k + 1} = \left[ \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \mathbf {x} _ {k} + \left[ \begin{array}{l} 0 \\ 0. 1 \\ 0 \end{array} \right] w _ {k} \tag {9.47}
$$

We will use the same observation model as before.

Using the same data from subsubsection 9.6.3, figures 9.6, 9.7, and 9.8 show the improved state estimates and figure 9.9 shows the improved robot position covariance with a Kalman smoother.

Notice how the wall position produced by the smoother is a constant. This is because that state has no dynamics, so the final estimate from the Kalman filter is already the best estimate.

![](image/335a5ecb30c60ebc4c9c915f8544feac6de7fc2d9d08011d935e57d8099be842.jpg)

<details>
<summary>line</summary>

| Time (s) | Kalman filter | Kalman smoother |
| --- | --- | --- |
| 0 | 0.2 | 0.8 |
| 10 | 1.7 | 0.6 |
| 20 | -0.2 | 0.4 |
| 30 | 1.0 | 0.9 |
| 40 | 1.2 | 0.8 |
| 50 | 0.9 | 1.3 |
| 60 | 1.5 | 1.2 |
| 70 | 0.8 | 0.5 |
| 80 | 0.9 | 0.6 |
| 90 | 1.4 | 0.8 |
| 100 | 0.5 | 0.8 |
</details>

Figure 9.7: Robot velocity with Kalman smoother

![](image/dbe305e81a2713f638206fd077e8e48625879874dc869c04a0de276155ad3ea5.jpg)

<details>
<summary>line</summary>

| Time (s) | Kalman filter | Kalman smoother |
| --- | --- | --- |
| 0 | 197 | 200 |
| 10 | 193 | 200 |
| 20 | 194 | 200 |
| 30 | 195 | 200 |
| 40 | 196 | 200 |
| 50 | 197 | 200 |
| 60 | 198 | 200 |
| 70 | 199 | 200 |
| 80 | 200 | 200 |
| 90 | 201 | 200 |
| 100 | 200 | 200 |
</details>

Figure 9.8: Wall position with Kalman smoother

![](image/2414099c0ca81a3932410eb3f1ab93756a3a0ae467474dfb3d62334591cbf221.jpg)

<details>
<summary>line</summary>

| Time (s) | Kalman filter | Kalman smoother |
| --- | --- | --- |
| 0 | 1.0 | 0.05 |
| 10 | 0.1 | 0.02 |
| 20 | 0.07 | 0.01 |
| 40 | 0.06 | 0.01 |
| 60 | 0.06 | 0.01 |
| 80 | 0.06 | 0.01 |
| 100 | 0.06 | 0.01 |
</details>

Figure 9.9: Robot position variance with Kalman smoother

See Roger Labbe’s book Kalman and Bayesian Filters in Python for more on smoothing.[6]
