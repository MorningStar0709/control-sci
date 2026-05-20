# EXAMPLE 4.6 MA control of a nonminimum-phase system

Consider an integrator with a time delay $\tau$ . For the sampling period $h > \tau$ the system is described by

$$A (q) = q (q - 1)B (q) = (h - \tau) q + \tau = (h - \tau) (q + b)$$

where

$$b = \frac {\tau}{h - \tau} \quad \text { and } \quad d _ {0} = 1$$

The noise is assumed to be characterized by

$$C (q) = q (q + c) \quad | c | < 1$$

The sampled-data system is nonminimum-phase if $\tau > h/2$ . This implies that the basic minimum-variance self-tuner can be used only if $\tau < h/2$ . Let the

![](image/928bf4a63523703dbfb4a0ec8975327deacf371fc0c669ea9ba7b1da87c0bad4.jpg)

![](image/ccdd1959d8f95c99b3f53f5ef4b4f7e687f7fad36bc4c729424c8f87537c565d.jpg)

<details>
<summary>line</summary>

| Time | y |
| --- | --- |
| 0 | 0.0 |
| 100 | 0.0 |
| 200 | 0.0 |
| 300 | 0.0 |
| 400 | 0.0 |
</details>

![](image/226c8fcf7a126502ee63d91ed5f4f14360e6e015e92e1df47bbe30fd61c176ef.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | 0 |
| 100 | 0 |
| 200 | 0 |
| 300 | 0 |
| 400 | 0 |
</details>

Figure 4.8 Simulation of the self-tuning algorithm on the integrator with time delay in Example 4.6. At t = 100 the delay is changed from 0.4 to 0.6.
(a) d = 1; (b) d = 2.

controller have the structure

$$u (t) = - \hat {s} _ {0} (t) y (t) - \hat {r} _ {1} (t) u (t - 1)$$

Simulations of the system are shown in Fig. 4.8 for $h = 1$ and $c = -0.8$ . The time delay is initially 0.4 and is increased to 0.6 at time $t = 100$ , at which time the sampled-data system gets a zero outside the unit circle. Figure 4.8(a) shows the results obtained with $d = 1$ , the minimum-variance structure. The parameters first converge toward the minimum-variance controller. At $t = 100$ the sampled-data system gets a zero outside the unit circle. The self-tuning regulator then tries to cancel the zero, and the closed-loop system becomes unstable after some time. It does not become unstable exactly at $t = 100$ because it takes a while for the controller parameters to change. The control signal is limited to $\pm 20$ , which explains why the signals do not grow exponentially. The forgetting factor is $\lambda = 0.99$ . Figure 4.8(b) shows the results for the algorithm with $d = 2$ . The moving-average controller is a stable equilibrium for both $\tau = 0.4$ and $\tau = 0.6$ . There will be a shift in the parameter values when the delay is changed, but the closed-loop system is stable.

The controller that gives the smallest attainable variance of the output gives the standard deviations 1.000 and 1.004 when $\tau = 0.4$ and 0.6, respectively, while the moving-average controller gives the standard deviations 1.003 and 1.007 when $\tau = 0.4$ and 0.6, respectively. Degradation in the performance when the moving-average controller is used in this example is thus minor.
