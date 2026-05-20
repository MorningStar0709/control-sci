# EXAMPLE 3.5 Indirect self-tuner without cancellation of process zero

Consider the same process as in Example 3.4, but use a control design in which there is no cancellation of the process zero. The parameters are estimated in the same way as in Example 3.4, but the control law is now computed as in Example 3.2. Polynomial $A_{\omega}$ is of first order. As in the previous examples the initial transient depends critically on the initial state of the

![](image/1c63a76ab9da0a7adb4ace3b924e4cd2e9f08b231d3eff1bf8e0ff7d689d3498.jpg)

<details>
<summary>line</summary>

| Time | u_c | y |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | 1 | 1 |
| 10 | 0 | 0 |
| 15 | 1 | 1 |
| 20 | 1 | 1 |
| 25 | 1 | 1 |
| 30 | -1 | -1 |
| 35 | -1 | -1 |
| 40 | -1 | -1 |
| 45 | -1 | -1 |
| 50 | -1 | -1 |
| 55 | 1 | 1 |
| 60 | 1 | 1 |
| 65 | 1 | 1 |
| 70 | 1 | 1 |
| 75 | -1 | -1 |
| 80 | -1 | -1 |
| 85 | -1 | -1 |
| 90 | -1 | -1 |
| 95 | -1 | -1 |
| 100 | -1 | -1 |
</details>

![](image/e3bc2f938317d3a6f8a94c7b4082aebae5c7d702acb8c5fd2280febbdc475470.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | -3.0 |
| 50 | 1.5 |
| 75 | -2.0 |
| 80 | 0.0 |
| 90 | 0.0 |
| 100 | 0.0 |
</details>

Figure 3.6 Same as in Fig. 3.4 but without cancellation of the process zero.

![](image/96f7284274d98a069636a6acd84e322567a53c1d4f4265bd33550a944c83e0d2.jpg)

<details>
<summary>line</summary>

| Time | â₂ | â₁ | b̂₁ | b̂₀ |
| --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.2 | 0.0 |
| 500 | 0.0 | -1.5 | 0.1 | 0.08 |
</details>

Figure 3.7 Parameter estimates corresponding to the simulation in Fig. 3.6. The true parameter values are indicated by dashed lines.

recursive estimator. For the design calculation it must be required that initial values are chosen so that polynomials A and B do not have a common factor. In this case the initial estimates were chosen to be $\hat{a}_{1}(0) = \hat{a}_{2}(0) = 0$ , $\hat{b}_{0}(0) = 0.01$ , and $\hat{b}_{1}(0) = 0.2$ . The P-matrix was initialized as a diagonal matrix with $P(1,1) = P(2,2) = 100$ and $P(3,3) = P(4,4) = 1$ as in Example 3.4. Figure 3.6 shows results of a simulation of the direct algorithm with $a_{o} = 0$ . Notice that the behavior of the process output is quite similar to that in Fig. 3.4 but that there is no “ringing” in the control signal. The parameter estimates are shown in Fig. 3.7. The values obtained at time t = 100 are

$$\hat {a} _ {1} (1 0 0) = - 1. 5 7 \quad (- 1. 6 0 6 5) \quad \hat {b} _ {0} (1 0 0) = 0. 0 9 2 \quad (0. 1 0 6 5)\hat {a} _ {2} (1 0 0) = 0. 5 7 \quad (0. 6 0 6 5) \quad \hat {b} _ {1} (1 0 0) = 0. 1 1 2 \quad (0. 0 9 0 2)$$
