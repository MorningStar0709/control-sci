# EXAMPLE 3.7 Direct self-tuner with $d_{0} = 1$

Consider the system in Example 3.1. Since $\deg A = 2$ and $\deg B = 1$ , we have $\deg A_m = 2$ and $\deg A_0 = 0$ . Hence $A_0 = 1$ , and we will choose $B_m = qA_m(1)$ . Equation (3.29) in Algorithm 3.3 then gives $T = qA_m(1)$ . The controller structure is given by $\deg R = \deg S = \deg T = \deg A - 1 = 1$ . The model given by Eq. (3.27) therefore becomes

$$y (t) = r _ {0} u _ {f} (t - 1) + r _ {1} u _ {f} (t - 2) + s _ {0} y _ {f} (t - 1) + s _ {1} y _ {f} (t - 2) \tag {3.30}$$

where

$$u _ {f} (t) + a _ {m 1} u _ {f} (t - 1) + a _ {m 1} u _ {f} (t - 2) = u (t)y _ {f} (t) + a _ {m 1} y _ {f} (t - 1) + a _ {m 1} y _ {f} (t - 2) = y (t)$$

It is now straightforward to obtain a direct self-tuner by applying Algorithm 3.3. The parameters of the model given by Eq. (3.30) are thus estimated, and the control signal is then computed from

$$\hat {r} _ {0} u (t) + \hat {r} _ {1} u (t - 1) = \hat {t} _ {0} u _ {\mathrm{c}} (t) - \hat {s} _ {0} y (t) - \hat {s} _ {1} y (t - 1)$$

where $\hat{r}_{0}, \hat{r}_{1}, \hat{s}_{0}$ , and $\hat{s}_{1}$ are the estimates obtained and $\hat{t}_{0}$ is given by Eq. (3.29), that is,

$$\hat {t} _ {0} = 1 + a _ {m 1} + a _ {m 2}$$

![](image/2ef3e1ef3f6c95d43ff7c61f45e869a069cca98b037f70a309ef3fe709c3ad60.jpg)

<details>
<summary>line</summary>

| Time | u_c | y |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | 1.5 | 0 |
| 10 | 1 | 0 |
| 15 | 1 | 0 |
| 20 | 1 | 0 |
| 25 | -1 | -1 |
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

![](image/be3699d1d4206819d9acc88d1122a5816caf30eceb8bc33b188c7f514bea1c10.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 2.0 |
| 5 | -4.0 |
| 10 | 1.5 |
| 15 | -0.5 |
| 20 | 0.0 |
| 25 | -3.5 |
| 30 | 0.5 |
| 35 | -0.5 |
| 40 | 0.0 |
| 45 | 2.5 |
| 50 | -1.0 |
| 55 | 0.0 |
| 60 | 0.0 |
| 65 | 0.0 |
| 70 | -3.5 |
| 75 | -1.0 |
| 80 | 0.5 |
| 85 | -0.5 |
| 90 | 0.0 |
| 95 | 0.0 |
| 100 | 0.0 |
</details>

Figure 3.10 Command signal $u_{c}$ , process output y, and control signal u when the process given by Eq. (3.16) is controlled by using a direct self-tuner with $d_{0}=1$ . Compare with Fig. 3.4.

![](image/2bec558e5d868733ad38b6751f9716b24e60b524ffc9a2042c9bda350c3d1263.jpg)

<details>
<summary>line</summary>

| Time | t̂₀/r̂₀ | ŝ₀/r̂₀ | r̂₁/r̂₀ | ŝ₁/r̂₀ |
| --- | --- | --- | --- | --- |
| 0 | 2 | 0 | 0 | -4 |
| 5 | 2 | 0 | 0 | -2 |
| 10 | 2 | 0 | 0 | -1 |
| 15 | 2 | 0 | 0 | -1 |
| 20 | 2 | 0 | 0 | -1 |
</details>
