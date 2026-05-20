# EXAMPLE 4.5 Direct minimum-variance self-tuning regulator

Consider the same process as in Example 4.4. The process model of Eq. (4.23) is now

$$y (t + 1) = r _ {0} u (t) + s _ {0} y (t) + \varepsilon (t + 1)$$

It is assumed that $r_{0}$ is fixed to the value $\hat{r}_{0}=1$ . Notice that this is different from the true value, which is 3. The parameter $s_{0}$ is estimated by using the least-squares method. The control law becomes

$$u (t) = - \frac {\hat {s} _ {0}}{\hat {r} _ {0}} y (t)$$

Figure 4.6 shows $\hat{s}_0 / \hat{r}_0$ , which is seen to converge rapidly to a value corresponding to the value of the optimal minimum-variance controller, even if $\hat{r}_0$ is not equal to its true value. This is also seen in Fig. 4.7, which shows the loss function when the self-tuner and the optimal minimum-variance controller are used. Compare Figs. 4.3 and 4.5.

![](image/6d95116534e74f789da8e1a200f6b01b27f2793c5daaaabc6336a7a9dd1a604d.jpg)

<details>
<summary>line</summary>

| Time | Self-tuning control | Minimum variance control |
| --- | --- | --- |
| 0 | 0 | 0 |
| 100 | ~100 | ~90 |
| 200 | ~200 | ~180 |
| 300 | ~300 | ~270 |
| 400 | ~450 | ~420 |
| 500 | ~550 | ~520 |
</details>

Figure 4.7 The loss function when the direct self-tuning regulator and the optimal minimum-variance controller are used on the system in Example 4.5.
