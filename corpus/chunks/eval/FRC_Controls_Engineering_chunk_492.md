# B.5 Latency compensation

Linear-Quadratic regulator controller gains tend to be aggressive. If sensor measurements are delayed too long, the LQR may be unstable (see figure B.1). However, we can compensate for the delay if we know the control law applied at future timesteps $( \mathbf { u } = - \mathbf { K } \mathbf { x } )$ and the delay’s duration.

To get the true state at the current time for control purposes, we project our delayed state forward by the delay duration using our model and the control law. Figure B.2 shows improved control with the predicted state.[4]

![](image/c8a63e4beaed436a3f76b9ebcce8165c473ac47bfc90ce1eaa86e7e58d1e5615.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference Position (m) | State (Kp = 234.04) Position (m) | Reference Velocity (m/s) | State (Kp = 5.6) Velocity (m/s) | Input Voltage (V) |
|----------|------------------------|----------------------------------|--------------------------|----------------------------------|-------------------|
| 0        | 0                      | 0                                | 0                        | 0                                | 0                 |
| 1        | 1                      | 1                                | 1                        | 1                                | -10               |
| 2        | 1                      | 1                                | 1                        | 1                                | -10               |
| 3        | 1                      | 1                                | 1                        | 1                                | -10               |
| 4        | 1                      | 1                                | 1                        | 1                                | -10               |
| 5        | 1                      | 1                                | 1                        | 1                                | -10               |
| 6        | 0                      | 0                                | 0                        | 0                                | -10               |
| 7        | 0                      | 0                                | 0                        | 0                                | -10               |
| 8        | 0                      | 0                                | 0                        | 0                                | -10               |
| 9        | 0                      | 0                                | 0                        | 0                                | -10               |
| 10       | 0                      | 0                                | 0                        | 0                                | -10               |
</details>

Figure B.1: Elevator response at 5 ms sample period with 50 ms of output lag

![](image/440f556141b65eb5fcccf7a8605402607e789eebf1a5ed5531144c048a2aa713.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference Position (m) | State (Kp = 49.75) Position (m) | Reference Velocity (m/s) | State (Kd = 0.13) Velocity (m/s) | Input Voltage (V) |
|----------|------------------------|----------------------------------|--------------------------|----------------------------------|-------------------|
| 0        | 1                      | 1                                | 0                        | 0                                | 0                 |
| 1        | 1                      | 1                                | -1                       | -1                               | 10                |
| 2        | 1                      | 1                                | -1                       | -1                               | 0                 |
| 3        | 1                      | 1                                | -1                       | -1                               | 0                 |
| 4        | 1                      | 1                                | -1                       | -1                               | 0                 |
| 5        | 1                      | 1                                | -1                       | -1                               | 0                 |
| 6        | 0                      | 0                                | -1                       | -1                               | -10               |
| 7        | 0                      | 0                                | -1                       | -1                               | 0                 |
| 8        | 0                      | 0                                | -1                       | -1                               | 0                 |
| 9        | 0                      | 0                                | -1                       | -1                               | 0                 |
| 10       | 0                      | 0                                | -1                       | -1                               | 0                 |
</details>

Figure B.2: Elevator response at 5 ms sample period with 50 ms of output lag (latency-compensated)

This method of latency compensation seems to work better for second-order systems than first-order systems, assuming steady-state controller gains from the second case in equation (B.13).
