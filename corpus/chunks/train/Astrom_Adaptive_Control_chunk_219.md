# EXAMPLE 4.4 Stochastic indirect self-tuning regulator

Consider the process (4.4) in Example 4.2 with a = -0.9, b = 3, and c = -0.3. The minimum-variance controller is given by the proportional controller

$$u (t) = \frac {a - c}{b} y (t) = - s _ {0} y (t) = - 0. 2 y (t)$$

This gives the closed-loop system

$$y (t) = e (t)$$

The ELS method is used to estimate the unknown parameters a, b, and c. The estimates are obtained from Eq. (2.21) with

$$
\begin{array}{l} \theta^ {T} = \left( \begin{array}{c c c} a & b & c \end{array} \right) \\ \varphi^ {T} (t - 1) = \left( \begin{array}{c c c} - y (t - 1) & u (t - 1) & \varepsilon (t - 1) \end{array} \right) \\ \varepsilon (t) = y (t) - \varphi^ {T} (t - 1) \hat {\theta} (t - 1) \\ \end{array}
$$

The controller is

$$u (t) = \frac {\hat {a} (t) - \hat {c} (t)}{\hat {b} (t)} y (t)$$

![](image/34983c4ac2ff3563ce010a9d6dec33b332a1b86968b76a605b2984893cec79cc.jpg)

<details>
<summary>line</summary>

| Time | y | u |
| --- | --- | --- |
| 0 | -3.0 | -1.5 |
| 50 | 0.5 | 0.2 |
| 100 | -0.8 | -0.3 |
| 150 | 1.2 | 0.4 |
| 200 | -0.6 | -0.1 |
| 250 | 0.9 | 0.3 |
| 300 | -1.1 | -0.2 |
| 350 | 1.5 | 0.5 |
| 400 | -0.7 | -0.4 |
| 450 | 0.8 | 0.1 |
| 500 | -1.3 | -0.6 |
</details>

Figure 4.2 Output and input when an indirect self-tuning regulator based on minimum-variance control is used to control the system in Example 4.4.

Figure 4.2 shows the result of a simulation of the algorithm. The initial values in the simulation are

$$\hat {a} (0) - 0\hat {b} (0) = 1\hat {c} (0) = 0P (0) = 1 0 0 I$$

Figure 4.3 shows the accumulated loss

$$V (t) = \sum_ {i = 1} ^ {t} y ^ {2} (i)$$

when the optimal minimum-variance controller and the indirect self-tuning regulator are used. The curve of the accumulated loss of the STR is almost parallel to the optimal curve. This means that the performance of the self-tuning regulator is almost optimal except for a short startup transient. Figure 4.4 shows the estimated process parameters. The parameter estimates have not converged to the true values during the simulated period. However, the controller parameter $\hat{s}_0(t) = (\hat{a}(t) - \hat{c}(t)) / \hat{b}(t)$ converges faster, as can be seen in Fig. 4.5. For a fixed controller the closed-loop system is stable when $-0.03 < s_0 < 0.63$ . Notice that during some of the first steps the controller parameter $\hat{s}_{0}(t)$ is such that the closed-loop system would be unstable if the controller were frozen to those values.
