<details>
<summary>line</summary>

| time (s) | y (solid line) | y (dotted line) |
| --- | --- | --- |
| 0 | 0.25 | 0.25 |
| 50 | 0.25 | 0.25 |
| 100 | -0.25 | -0.25 |
| 150 | -0.15 | -0.15 |
| 200 | 0.15 | 0.15 |
| 250 | -0.25 | -0.25 |
| 300 | -0.15 | -0.15 |
| 350 | 0.15 | 0.15 |
| 400 | -0.25 | -0.25 |
| 450 | -0.15 | -0.15 |
</details>

setpoint y(sp-MPC) target (ys) y(targ-MPC)

![](image/d2c0d31d02878882601b6dd6693f8e4344ce74b10ff702252d2484259b97be9b.jpg)

<details>
<summary>line</summary>

| time (s) | u |
| --- | --- |
| 0 | -1.0 |
| 50 | 1.0 |
| 100 | -0.5 |
| 150 | -1.0 |
| 200 | 1.0 |
| 250 | -0.5 |
| 300 | -1.0 |
| 350 | 1.0 |
| 400 | -0.5 |
</details>

target (us)  u(targ-MPC) u(sp-MPC)

Figure 2.6: Closed-loop performance of sp-MPC and targ-MPC.

and state space realization

$$
G (s) = \frac {- 0 . 2 6 2 3}{6 0 s ^ {2} + 5 9 . 2 s + 1} \quad A = \left[ \begin{array}{c c} 0. 8 5 7 2 5 2 & 0. 8 8 4 1 7 9 \\ - 0. 0 1 4 7 3 6 & - 0. 0 1 5 1 3 9 \end{array} \right]

B = \left[ \begin{array}{c} 8. 5 6 4 9 0 \\ 0. 8 8 4 1 8 \end{array} \right] \qquad C = \left[ \begin{array}{c c} - 0. 0 0 4 3 7 1 7 & 0 \end{array} \right]
$$

sampled with $\Delta = 1 0 \mathrm { ~ s ~ }$ . The input u is constrained $| u | \le 1$ . The desired output setpoint is $y _ { \mathrm { s p } } = 0 . 2 5$ , which corresponds to a steady-state input value of −0.953. The regulator parameters are $Q _ { \gamma } \ = \ 1 0 , R \ =$ $0 , S = 1 , Q = C ^ { \prime } Q _ { y } C + 0 . 0 1 I _ { 2 }$ . A horizon length of $N = 8 0$ is used. In time intervals 50–130, 200–270, and 360–430, a state disturbance $d _ { x } = [ 1 7 . 1 , 1 . 7 7 ] ^ { \prime }$ causes the input to saturate at its lower limit. The output setpoint is unreachable under the influence of this state disturbance. The closed-loop performance of sp-MPC and targ-MPC under the described disturbance scenario are shown in Figure 2.6. The closedloop performance of the two control formulations are compared in Table 2.3.

In the targ-MPC framework, the controller tries to reject the state disturbance and minimize the deviation from the new steady-state target. This requires a large, undesirable control action that forces the input to move between the upper and lower constraints. The sp-MPC framework, on the other hand, attempts to minimize the deviation from setpoint and subsequently the input just rides the lower input constraint.

The greater cost of control action in targ-MPC is shown by the cost index $V _ { u }$ in Table 2.3. The cost of control action in targ-MPC exceeds that of sp-MPC by nearly 100%. The control in targ-MPC causes the output of the system to move away from the (unreachable) setpoint faster than the corresponding output of sp-MPC. Since the control objective is to be close to the setpoint, this undesirable behavior is eliminated by sp-MPC. -
