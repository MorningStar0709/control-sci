# Example 6.16

For $P(s) = ke^{-sT} / (\tau s + 1)$ , compute the range of $k$ for stability, given unity feedback.

Solution With $P'(s) = e^{-sT} / (\tau s + 1)$ , it is easy to see that

$$| P ^ {\prime} (j \omega) | = \frac {| e ^ {- j \omega T} |}{| j \omega \tau + 1 |} = \frac {1}{(\tau^ {2} \omega^ {2} + 1) ^ {1 / 2}}\neq P ^ {\prime} (j \omega) = - \omega T - \tan^ {- 1} \omega \tau .$$

As $\omega$ increases, the magnitude decreases monotonically while the phase becomes indefinitely more negative. The result, shown in Figure 6.33, is a spiral Nyquist plot.

![](image/819b71813bdccaa2cab0bf1bfe7cee3908e2396db20556fa58ea4ca729e36847.jpg)

<details>
<summary>contour</summary>

| x | y |
| --- | --- |
| -0.2 | 0.1 |
| 0.0 | 0.0 |
| 0.2 | -0.1 |
| 0.4 | -0.3 |
| 0.6 | -0.2 |
| 0.8 | -0.1 |
| 1.0 | 0.0 |
</details>

Figure 6.33 Nyquist plot, system with delay plus single time constant

Because there are no RHP poles, we require zero encirclements, so the point $(-1 / k, 0)$ must be to the left of point $A$ . The system is simple enough to allow some analytical headway. Since the phase is $180^{\circ}$ at $A$ ,

$$- \omega T - \tan^ {- 1} \omega \tau = - \pi - 2 \pi n$$

where $n =$ a nonnegative integer. Each value of $n$ corresponds to a negative-real-axis crossing. Point $A$ corresponds to the lowest-frequency crossing, i.e., to $n = 0$ . Therefore, the frequency satisfies

$$\tan^ {- 1} \omega \tau = \pi - \omega T$$

or

$$\omega \tau = \tan (\pi - \omega T)\frac {\tau}{T} (\omega T) = - \tan \omega T.$$

This transcendental equation has no analytic solution. Figure 6.34 shows the functions $-\tan \omega T$ and $\frac{\tau}{T} (\omega T)$ versus $\omega T$ . The intersection point $\omega_0$ (the lowest-frequency crossing of the negative real axis) is near $\omega T = \pi /2$ for large $\tau /T$ , and nearer $\omega T = \pi$ for small $\tau /T$ .

![](image/f8cfc2596b4151688a2bbe31253a5776a18da5f57a2bed5d62abcca3edea8236.jpg)

<details>
<summary>scatter</summary>

| ωT | Value |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | -1.0 |
| 1.0 | -2.0 |
| 1.5 | -3.0 |
| 2.0 | -4.0 |
| 2.5 | -5.0 |
| 3.0 | -6.0 |
| 3.5 | -7.0 |
</details>

Figure 6.34 Illustration of the transcendental equation

For stability, the point $(-1 / k, 0)$ must be to the left of $A$ , so

$$- \frac {1}{k} < - | P ^ {\prime} (j \omega_ {0}) |k < \frac {1}{| P ^ {\prime} (j \omega_ {0}) |} = (\tau^ {2} \omega_ {0} ^ {2} + 1) ^ {1 / 2} = \left(\frac {\tau^ {2}}{T ^ {2}} \omega_ {0} ^ {2} T ^ {2} + 1\right) ^ {1 / 2}.$$
