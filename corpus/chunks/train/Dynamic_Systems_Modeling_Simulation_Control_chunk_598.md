Figure 10.42 shows that as the single control gain K increases, the two closed-loop roots move toward each other along the negative real axis starting from the open-loop roots at $s = 0$ and $s = - 0 . 3$ until they meet and break away from the real axis at approximately −0.154. As the gain K is increased, the closed-loop roots become complex and move along symmetric semicircles until they reenter the negative real axis at approximately −5.85. As the gain K is further increased to infinity, one closed-loop root follows an asymptote along the negative real axis $\mathrm { t o } - \infty$ , while the other closed-loop root terminates at the open-loop zero at $s = - 3$ . Figure 10.42 shows a region near the real-axis break-in point where the closed-loop roots have large negative real parts (hence, the transient response decays quickly) and are close to the real axis (good damping). We may use the rlocfind MATLAB command to place the cross-hair target on the root-locus branch in this desired region in order to obtain the corresponding gain K. One such candidate design point is $K = 5 . 5 1 4$ , which results in closed-loop poles at $s = - 5 . 6 6 4 0 \pm j 1$ .0016 (marked with cross “+” on Fig. 10.42). With these closed-loop poles, the undamped natural frequency is $\omega _ { n } = \sqrt { 5 . 6 6 4 ^ { 2 } + 1 . 0 0 1 6 ^ { 2 } } = 5 . 7 5$ rad/s and the damping ratio is $\zeta = 5 . 6 6 4 / 5 . 7 5 = 0 . 9 8 5$ , which will result in a fast, well-damped transient response. Figure 10.43 shows the closed-loop response to a step

![](image/f718dbe2eb32922ab922c8b940e78afcd5123f556b4af1a358eaf8b33b8ef5a1.jpg)

<details>
<summary>scatter</summary>

| Point Type | Real Axis | Imaginary Axis |
| --- | --- | --- |
| Design point | -6.0 | 1.0 |
| Open-loop plant poles | 0.0 | 0.0 |
| PD controller zero at s = -3 | -3.0 | 0.0 |
| Fast, well-damped closed-loop poles | -6.0 | -1.0 |
</details>

Figure 10.42 Root-locus plot for system with PD controller (Example 10.12).

![](image/2c81d619fdb80027141512e2f09f4f3df8cb9539be248b1515ebe5e36c1937e5.jpg)

<details>
<summary>line</summary>

| Time, s | Position, x(t), m |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.11 |
| 1.0 | 0.1 |
| 1.5 | 0.1 |
</details>

Figure 10.43 Closed-loop step response using PD controller with gain K = 5.514 (Example 10.12).

position input $x _ { \mathrm { r e f } } ( t ) = 0 . 1$ m (using design gain $K = 5 . 5 1 4 )$ and verifies that the transient response is indeed well damped and dies out quickly.
