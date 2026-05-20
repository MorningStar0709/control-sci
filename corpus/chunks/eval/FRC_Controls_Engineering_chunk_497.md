# B.5.3 Estimating measurement delay

There are two common sources of measurement delay: filter delay, and communication delay (e.g., sensor data sent periodically over a network). The delay introduced by a finite-impulse response (FIR) filter is the weighted average of its sample’s delays, where the weights are the magnitudes of the FIR filter’s weights.

Theorem B.5.1 shows the delay introduced by a moving average filter.

Theorem B.5.1 — Moving average filter delay. The delay introduced by a moving average filter with N taps and a sample period of $T$ is $\frac { ( \check { N } - 1 ) T } { 2 }$

Proof:

Let there be a moving average filter with N taps whose sample delays range from 0 to $( N - 1 ) T$ inclusive. The average delay is

$$
\begin{array}{l} L = \frac {\sum_ {k = 0} ^ {N - 1} k T}{N} \\ L = \frac {T \sum_ {k = 0} ^ {N - 1} k}{N} \\ L = \frac {T \frac {(N - 1) ((N - 1) + 1)}{2}}{N} \\ L = \frac {(N - 1) ((N - 1) + 1) T}{2 N} \\ L = \frac {(N - 1) N T}{2 N} \\ L = \frac {(N - 1) T}{2} \\ \end{array}
$$

Theorem B.5.2 shows the delay introduced by a first-order backward finite difference, which is commonly used to estimate velocity from position samples.

Theorem B.5.2 — First-order backward finite difference delay. The delay introduced by a first-order backward finite difference with a sample period of $T$ is $\textstyle { \frac { T } { 2 } }$

Proof:

The first-order backward finite difference with a period of $T$ is xk−xk−1 . Since x $\frac { x _ { k } - x _ { k - 1 } } { T }$ $x _ { k }$ and $x _ { k - 1 }$ have delays of 0 and $T$ respectively, the average delay is $\frac { \dot { T } } { 2 }$

![](image/1eae765c0224657b9c341cb92fc709c51010a9b61f81a430bd59d8c9dc7b291e.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference Velocity (m/s) | State (Kp = 31.24) Velocity (m/s) | Input Voltage (V) |
|----------|---------------------------|------------------------------------|-------------------|
| 0        | 0                         | 0                                  | 0                 |
| 1        | 2                         | 2                                  | 10                |
| 2        | 2                         | 2                                  | 10                |
| 3        | 2                         | 2                                  | 10                |
| 4        | 2                         | 2                                  | 10                |
| 5        | 0                         | 0                                  | -10               |
| 6        | 0                         | 0                                  | 0                 |
| 7        | 0                         | 0                                  | 10                |
| 8        | 0                         | 0                                  | 10                |
| 9        | 0                         | 0                                  | 10                |
| 10       | 0                         | 0                                  | 10                |
</details>

Figure B.3: Drivetrain velocity response at 1 ms sample period with 40 ms of output lag

![](image/c66eefcb035ea9c2fbd9ad13432b664bb5633b39a9264a2c588dcffa15780846.jpg)

<details>
<summary>line</summary>
