# EXAMPLE 3.8 Direct self-tuner with $d_{0} = 2$

In the derivation of the direct algorithm the parameter $d_{0}$ was the pole excess of the plant. Assume for a moment that we do not know the value of $d_{0}$ and that we treat it as a design parameter instead. Figure 3.12 shows a simulation of the direct algorithm used in Example 3.7 but with $d_{0} = 2$ instead of $d_{0} = 1$ . All the other parameters are the same. Notice that the behavior of the system is quite reasonable without any "ringing" in the control signal. Figure 3.13 shows the parameter estimates. The estimates obtained at time t = 100 correspond to the controller parameters

![](image/a9d1c5ffa5a8307b633d7aca4cf26e54a1adb7f22dab5d35e43223c25e6c4216.jpg)  
Figure 3.12 Command signal $u_{c}$ , process output y, and control signal u when the process described by Eq. (3.16) is controlled with a direct self-tuner with $d_{0} = 2$ .

$$\frac {\hat {r} _ {1} (1 0 0)}{\hat {r} _ {0} (1 0 0)} = - 0. 3 3 7 \quad \frac {\hat {s} _ {0} (1 0 0)}{\hat {r} _ {0} (1 0 0)} = 1. 2 0 \quad \frac {\hat {s} _ {1} (1 0 0)}{\hat {r} _ {0} (1 0 0)} = - 0. 6 7 \quad \frac {\hat {t} _ {0} (1 0 0)}{\hat {r} _ {0} (1 0 0)} = 0. 5 2$$

![](image/ba8f3fd37a42b5937f321351dcbba7381a677639c346ce8d3c5e621e7d104c23.jpg)

<details>
<summary>line</summary>

| Time | t̂₀/r̂₀ | ŝ₀/r̂₀ | r̂₁/r̂₀ | ŝ₁/r̂₀ |
| --- | --- | --- | --- | --- |
| 0 | 1.0 | 0.0 | -2.0 | -2.0 |
| 5 | 0.5 | 1.0 | -1.0 | -1.0 |
| 10 | 0.0 | 1.0 | -0.5 | -0.5 |
| 15 | 0.0 | 1.0 | -0.5 | -0.5 |
| 20 | 0.0 | 1.0 | -0.5 | -0.5 |
</details>

Figure 3.13 Parameter estimates corresponding to Fig. 3.12: $\hat{r}_{1}/\hat{r}_{0}$ (solid line), $\hat{t}_{0}/\hat{r}_{0}$ (dashed line), $\hat{s}_{0}/\hat{r}_{0}$ (dash-dot line), $\hat{s}_{1}/\hat{r}_{0}$ (dotted line).

We thus find the interesting and surprising result that cancellation of the process zero can be avoided by increasing the parameter $d_{0}$ . This observation will be explained later when we will be analyzing the algorithms. ☐
