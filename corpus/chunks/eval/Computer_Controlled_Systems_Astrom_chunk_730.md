# Systems with Unstable Inverses

Remark 4 to Theorem 12.2 mentions that the control law given by (12.27) cancels all process zeros. If there are process zeros outside the unit disc, the closed-loop system will then have unstable modes that are unobservable from the output. The implications of this are discussed first. Other control laws that do not require all zeros of $B(z)$ to be inside the unit disc are then presented.

Solving Eq. (12.28) for y and u gives

$$y (k) = \frac {F (q)}{q ^ {d - 1}} e (k)$$

and

$$u (k) = - \frac {G (q)}{q ^ {d - 1} B (q)} e (k)$$

![](image/8185c978d199e2ac8d5423860403c10b1fb550bb73a07da62332d7357c801028.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | ~0 | 0 |
| 50 | ~-2 | ~0 |
| 100 | ~2 | ~10^4 |
</details>

Figure 12.5 Simulation of the system in Example 12.8 with the control law given by Theorem 12.2 that cancels an unstable process zero.

The necessity of the assumption that B is stable is clearly seen from these equations. If the polynomial B is unstable, the system has unstable modes, which are excited by the disturbance. These unstable modes are coupled to the control signal and the control signal grows exponentially. However, the output signal remains bounded because the unstable modes are not coupled to the output. An example illustrates what happens.
