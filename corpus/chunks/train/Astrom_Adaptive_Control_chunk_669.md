# EXAMPLE 11.7 A constant regression vector causes windup

Consider a process with the transfer function

$$G (s) = \frac {\beta}{s + \alpha}$$

with an indirect adaptive controller based on estimation of parameters a and b in the discrete-time model

$$y (k h + h) + a y (k h) = b u (k h)$$

The control design is the same as in Example 11.5. The controller has integral action. The parameters have the values $\alpha = 1$ and $\beta = 1$ , the sampling period is $h = 0.5$ s, there is measurement noise with a standard deviation of 0.05, the setpoint is piecewise constant, and the forgetting factor is $\lambda = 0.95$ . To illustrate the effect of poor excitation, the setpoint will be kept constant for long periods of time.

The parameters are in $R^{2}$ . To have excitation, the regression vectors should also span $R^{2}$ persistently. When the setpoint is constant, the input and the

![](image/a78803992bedcfcdac6f526e9acec848ef707f7ce2a47ca9bf811bed3f63ea15.jpg)

<details>
<summary>line</summary>

| Time | u_c | y |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 30 | -1.0 | -1.0 |
| 50 | 1.0 | 1.0 |
| 120 | -1.0 | -1.0 |
| 150 | -1.0 | -1.0 |
</details>

![](image/8b1dde120e9737dbd209a17cc28b028695aefc1de02e64c97968b656c75dba70.jpg)

<details>
<summary>line</summary>

| Time | p11 |
| --- | --- |
| 0 | 30 |
| 50 | 0 |
| 100 | 20 |
| 150 | 0 |
</details>

![](image/6c64f0378388d424350828995a4fee9127078d54960199ce4954f17346a7a5e8.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 1 |
| 50 | -1 |
| 100 | 1 |
| 150 | -1 |
</details>

![](image/35732c8ae5fccc1e82fe2362a4f97672d66cf6bd3e05feb599cd92ec4f1e5a23.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | -2.0 |
| 50 | 0.0 |
| 100 | 0.5 |
| 150 | 0.0 |
</details>

Figure 11.12 Illustration of estimator windup due to poor excitation. (a) Output y and setpoint $u_{c}$ ; (b) covariance $p_{11}$ ; (c) control signal u; and (d) estimator gain $k_{1}$ .

![](image/c4ae7aafb37d4f7ddddb27b5adb2f15e2740109daa255fbf4ad72dde244b5ca1.jpg)

<details>
<summary>line</summary>

| Time | â | b̂ | k̂ |
| --- | --- | --- | --- |
| 0 | -0.5 | 0.5 | 1.0 |
| 50 | -0.5 | 0.5 | 1.0 |
| 100 | 0.5 | 1.0 | 1.0 |
| 150 | -0.5 | 0.5 | 1.0 |
</details>

Figure 11.13 Parameter estimates in the case of estimator windup due to poor excitation. The dashed lines show the correct values of the parameters and of the gain of the process.
