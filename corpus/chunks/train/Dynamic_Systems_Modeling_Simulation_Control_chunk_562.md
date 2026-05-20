# Reaction-curve method

Although the exact system dynamics of the reaction tank are not provided in Fig. 10.22, we assume that the physical system is available in order to derive the reaction curve by experimentation. Figure 10.23 shows the S-shaped reaction curve that results from a positive (alkaline) flow rate step input u(t) applied to the open-loop plant. We can estimate the delay time as $T _ { d } = \boldsymbol { 3 0 } ~ \mathrm { s }$ and the maximum slope as $\bar { R } = 2 . 5 / \bar { T } = 2 . 5 / 1 5 0 \bar { = } 0 . 0 1 6 \bar { 7 }$ . Using Table 10.1, the PID gains are

Proportional gain: $K _ { P } = \frac { 1 . 2 } { R T _ { d } } = 2 . 4$ RT

Integral gain: $K _ { I } = \frac { 0 . 6 } { R T _ { d } ^ { 2 } } = 0 . 0 4$

Derivative gain: $K _ { D } = \frac { 0 . 6 } { R } = 3 6$

![](image/4352958c70d49cdc60c47065920829cdd59b369e419188fc8608d88a02e3c28a.jpg)

<details>
<summary>line</summary>

| Time, s | Tank solution pH |
| --- | --- |
| 0 | 7.0 |
| 100 | 8.3 |
| 200 | 9.0 |
| 300 | 9.4 |
| 400 | 9.5 |
| 500 | 9.5 |
</details>

Figure 10.23 Reaction-curve response for a step input (Example 10.7).

![](image/d1d0d48d6eb0864dc6cdc71b502e3e7a54f19fab5118addc70be64de90375717.jpg)

<details>
<summary>line</summary>

| Time, s | Tank solution pH (K_P = 2.4, K_I = 0.04, K_D = 36) | Tank solution pH (K_P = 2.4, K_I = 0.04, K_D = 54) |
| --- | --- | --- |
| 0 | 7.0 | 7.0 |
| 100 | 10.0 | 9.7 |
| 200 | 8.5 | 8.9 |
| 300 | 9.2 | 9.0 |
| 400 | 9.0 | 9.0 |
| 500 | 9.0 | 9.0 |
</details>

Figure 10.24 Closed-loop step response using a PID controller (Example 10.7).

Figure 10.24 shows the closed-loop step response with r(t) = 9 (reference pH) with these PID controller gains. The solid-line response shows that the PID controller has reduced the transient response to roughly one-quarter of its peak value (pH = 10) after one cycle, which is the design goal of the Ziegler–Nichols tuning rules summarized in Table 10.1. Recall that the Ziegler–Nichols rules provide the control engineer with a feasible starting point for selecting the PID gains. The peak overshoot can be reduced by increasing the D-gain as demonstrated by the dashed-line curve in Fig. 10.24, where $K _ { D }$ is increased by 50%. The closed-loop response with $K _ { D } = 5 4$ exhibits a reduced peak response (pH = 9.7) and a quicker response with a settling time less than 200 s.
