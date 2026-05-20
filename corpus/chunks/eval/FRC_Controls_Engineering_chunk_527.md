# DC motor transfer function

If poles are much farther left in the LHP than the typical system dynamics exhibit, they can be considered negligible. Every system has some form of unmodeled high frequency, nonlinear dynamics, but they can be safely ignored depending on the operating regime.

To demonstrate this, consider the transfer function for a second-order DC motor (a CIM motor) from voltage to velocity.

$$G (s) = \frac {K}{(J s + b) (L s + R) + K ^ {2}}$$

where $J ~ = ~ 3 . 2 2 8 4 \times 1 0 ^ { - 6 } ~ k g { - } m ^ { 2 } , b ~ = ~ 3 . 5 0 7 7 \times 1 0 ^ { - 6 } ~ N { - } m { - } s , ~ K _ { e } ~ = ~ K _ { t } ~ = ~$ 0.0181 V /rad/s, R = 0.0902 Ω, and L = 230 × 10−6 H.

This system is second-order because it has two poles; one corresponds to velocity and the other corresponds to current. To make position the output instead, we’ll multiply by $\frac { 1 } { s }$ because position is the integral of velocity.[3]

$$G (s) = \frac {K}{s ((J s + b) (L s + R) + K ^ {2})}$$

Compare the step response of this system (figure E.5) with the step response of this system with L set to zero (figure E.6). For small values of K, both systems are stable and have nearly indistinguishable step responses due to the exceedingly small contribu tion from the fast pole. The high frequency dynamics only cause instability for large values of K that induce fast system responses. In other words, the system responses of the second-order model and its first-order approximation are similar for low frequency operating regimes.

![](image/ce5c8cc1e95103e6e52b9b9c46c1f767f6446c1767c177f2644124e6b6a6a6fc.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference | Step response |
| -------- | --------- | ------------- |
| 0.00     | 1.0       | 0.0           |
| 0.05     | 1.0       | 0.9           |
| 0.10     | 1.0       | 1.0           |
| 0.15     | 1.0       | 1.0           |
| 0.20     | 1.0       | 1.0           |
| 0.25     | 1.0       | 1.0           |
</details>

![](image/08b0224b6f13ed0d75f9d70a8f39c85b88667a4f7c5cac282cd6214db546caa9.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference | Step response |
| -------- | --------- | ------------- |
| 0.00     | 1.0       | 0.0           |
| 0.05     | 1.0       | 0.9           |
| 0.10     | 1.0       | 1.0           |
| 0.15     | 1.0       | 1.0           |
| 0.20     | 1.0       | 1.0           |
| 0.25     | 1.0       | 1.0           |
</details>

Figure E.5: Step response of second-order DC motor plant augmented with position $( L = 2 3 0 \mu \mathrm { H } )$   
Figure E.6: Step response of first-order DC motor plant augmented with position $( L = 0 \mu \mathrm { H } )$ L

Why can’t unstable poles close to the origin be ignored in the same way? The response of high frequency stable poles decays rapidly. Unstable poles, on the other hand, represent unstable dynamics which cause the system output to grow to infinity. Regardless of how slow these unstable dynamics are, they will eventually dominate the response.
