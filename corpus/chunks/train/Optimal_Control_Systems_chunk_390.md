\- Step 5: Time-Optimal Control Sequences: From the solutions of the costates (7.2.12), we see that $\lambda_2^*(t)$ is a straight line, and that there are four possible (assuming initial conditions $\lambda_1(0)$ and $\lambda_2(0)$ to be nonzero) solutions as shown in Figure 7.7. Also shown are the four possible optimal control sequences

$$\{+ 1 \}, \{- 1 \}, \{+ 1, - 1 \}, \{- 1, + 1 \} \tag {7.2.13}$$

that satisfy the optimal control relation (7.2.10). Let us reiterate that the admissible optimal control sequences are the ones given by (7.2.13). That is, a control sequence like $\{+1,-1,+1\}$ is not an optimal control sequence. Also, the control sequence $\{+1,-1,+1\}$ requires two switchings which is in violation of the earlier result (Theorem 7.3) that a second (nth) order system will have at most 1 $(n-1)$ switchings. From Figure 7.7, we see that the time-optimal control for the second order (double integral) system is a piecewise constant and can switch at most once. In order to arrive at closed-loop realization of the optimal control, we need to find the phase $(x_{1}(t),x_{2}(t))$ plane (state) trajectories.

![](image/46c4e86a87ae4791910a3e876c930d2eac3b371530ca7eb64050e884bbf32f80.jpg)

<details>
<summary>line</summary>

| t | u*(t) | λ₂(t) |
| --- | --- | --- |
| 0 | +1 | -1 |
| >0 | +1 | 0 |
</details>

(a) $\lambda_1(0) > 0$ ; $\lambda_2(0) < 0$

![](image/f3d3c32be925b174ab5771c8b3b2c64c285d008e25d1aa7373cd93d9604ac968.jpg)

<details>
<summary>line</summary>

| t | λ₂(t) | u*(t) |
| --- | --- | --- |
| 0 | 0 | -1 |
| +1 | 1 | -1 |
</details>

(b) $\lambda_1(0) < 0$ ; $\lambda_2(0) > 0$

![](image/9acad0704bd1d375e05dd9fb6c9d7cd51d29527a4e3d4023d4b0de22c7cb4951.jpg)

<details>
<summary>line</summary>

| t | u*(t) | λ₂(t) |
| --- | --- | --- |
| 0 | +1 | -1 |
| >0 | -1 | 0 |
</details>

(c) $\lambda_1(0) < 0$ ; $\lambda_2(0) < 0$

![](image/9f888df79cf2f7eae52952f75b5538e79ad7978c34d2aa2fba15845278d454a0.jpg)

<details>
<summary>line</summary>

| t | u*(t) |
| --- | --- |
| 0 | 0 |
| 1 | -1 |
| 2 | +1 |
| 3 | +1 |
| 4 | +1 |
</details>

(d) $\lambda_1(0) > 0$ ; $\lambda_2(0) > 0$   
Figure 7.7 Possible Costates and the Corresponding Controls

\- Step 6: State Trajectories: Solving the state equations (7.2.3), we have

$$x _ {1} ^ {*} (t) = x _ {1} ^ {*} (0) + x _ {2} ^ {*} (0) t + \frac {1}{2} U t ^ {2},x _ {2} ^ {*} (t) = x _ {2} ^ {*} (0) + U t, \tag {7.2.14}$$
