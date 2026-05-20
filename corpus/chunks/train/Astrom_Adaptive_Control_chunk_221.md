# Direct Minimum-Variance and Moving-Average STR

The design calculations for the indirect self-tuning regulators include the solution of a system of equations such as the Diophantine equation (4.18) or (4.20). The time to solve the Diophantine equation may be long in comparison with the sampling period. A self-tuning regulator that directly estimates the controller parameters eliminates the design calculations. It is thus desirable to construct direct self-tuning algorithms. Deterministic direct self-tuners were discussed in Section 3.5. The idea is to use the specification and the process model to make a reparameterization of the system. The same idea will now be used for stochastic systems of the form (4.1). In Section 4.2 it was shown that minimum-variance control is the same as predicting the output $d_{0}$ steps ahead and then determining the control signal $u(t)$ such that the predicted value is equal to the desired output. Consider the reparameterization (4.12), and rewrite the model in the backward shift operator. This gives

![](image/3bc25a4377b8ddcad2462d6cf7d6fc69e2fdd4d88cb1d34b66872e6d473476dd.jpg)

<details>
<summary>line</summary>

| Time | a | ĉ | b̂ |
| --- | --- | --- | --- |
| 0 | -1.0 | 0.0 | 3.0 |
| 100 | -0.8 | 0.0 | 3.0 |
| 200 | -0.7 | 0.0 | 3.0 |
| 300 | -0.6 | 0.0 | 3.0 |
| 400 | -0.5 | 0.0 | 3.0 |
| 500 | -0.4 | 0.0 | 3.0 |
</details>

Figure 4.4 The estimated parameters $\hat{a}(t)$ , $\hat{b}(t)$ , and $\hat{c}(t)$ when the system in Example 4.4 is controlled. The dashed lines correspond to the true parameter values.

![](image/ea3aaf1beec15c2184d394739d6a2de89e857bfb9f0e85b6dcce9b0044f40578.jpg)

<details>
<summary>line</summary>

| Time | ŝ₀ |
| --- | --- |
| 0 | 1.5 |
| 100 | 0.2 |
| 200 | 0.2 |
| 300 | 0.2 |
| 400 | 0.2 |
| 500 | 0.2 |
</details>

Figure 4.5 The controller parameter $\hat{s}_0(t)$ when the system in Example 4.4 is controlled. The dashed line is the optimal parameter for the minimum-variance controller.

$$y (t + d _ {0}) = \frac {1}{C ^ {*}} \left(R ^ {*} u (t) + S ^ {*} y (t)\right) + R _ {1} ^ {*} e (t + d _ {0}) \tag {4.21}$$

where $R_1^* = F^*$ and $\deg R_1 = d_0 - 1$ . Using Eq. (4.18), we get, in the same way,

$$y (t + d) = \frac {B ^ {*}}{C ^ {*}} \left(R ^ {*} u (t) + S ^ {*} y (t)\right) + R _ {1} ^ {*} e (t + d) \tag {4.22}$$

where $\deg R_1 = d - 1$ .

The factors $1/C^{*}$ and $B^{-*}/C^{*}$ in Eqs. (4.21) and (4.22), respectively, can be interpreted as filters for the regressors. (Compare Section 3.5.) Both equations are now written in predictor form, where the controller polynomials $R$ and $S$ appear directly in the model. These equations can be used as a motivation for the following algorithm.
