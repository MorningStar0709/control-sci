$$T (s) = \frac {\left(\frac {K _ {P} s + K _ {I}}{s}\right) \left(\frac {4 0 0}{s + 2 0 . 4}\right)}{1 + \left(\frac {K _ {P} s + K _ {I}}{s}\right) \left(\frac {4 0 0}{s + 2 0 . 4}\right)} = \frac {4 0 0 (K _ {P} s + K _ {I})}{s ^ {2} + (2 0 . 4 + 4 0 0 K _ {P}) s + 4 0 0 K _ {I}} \tag {10.18}$$

Equation (10.18) immediately tells us that the closed-loop DC gain is unity for any nonzero value of the integral gain $K _ { I } .$ . In addition, the closed-loop transfer function now has a first-order numerator and second-order denominator due to the PI controller. A PI controller has two free gains for selection $( K _ { P }$ and $K _ { I } )$ and we will demonstrate the PI controller using the previous P-gains $( K _ { P } = 1 , 0 . 5$ , and 0.2 V-s/rad). For example, when $K _ { P } = 1 \mathrm { V - s / r a d }$ , Eq. (10.18) shows that the closed-loop characteristic equation is

$$\mathrm{P-gain} K _ {P} = 1 \mathrm{V-s/rad:} s ^ {2} + 4 2 0. 4 s + 4 0 0 K _ {I} = 0$$

If the I-gain $( K _ { I } )$ is too large, the second-order characteristic equation will become underdamped and oscillations will occur. If $K _ { I }$ is too small, the characteristic roots will be real and negative, but they will be near the origin and hence the response will be slow. Figure 10.17 shows the closed-loop motor speed with three PI controller gain settings. All three motor responses reach the desired 50-rad/s reference speed at steady state because of the addition of the integral control loop. If we compare the responses in Figs. 10.16 and 10.17 for a particular $K _ { P }$ gain, we see that adding integral control has slightly slowed down the response. Again, if our DC motor has an armature voltage limit (say, a maximum of 12 V), then the PI controller with gains $K _ { P } = 0 . 2 \ : \mathrm { V }$ -s/rad and $K _ { I } = 4$ V/rad is the only feasible choice for the three PI control options shown in Fig. 10.17.

![](image/84f7cc578ddc9166835e0a9ca60bb1b61dbbaa189479e96fa5cc69e716471caa.jpg)

<details>
<summary>line</summary>

| Time, s | DC motor speed, ω(t), rad/s (K_P = 0.2 V-s/rad, K_I = 4 V/rad) | DC motor speed, ω(t), rad/s (K_P = 0.5 V-s/rad, K_I = 10 V/rad) | DC motor speed, ω(t), rad/s (K_P = 1 V-s/rad, K_I = 20 V/rad) |
| --- | --- | --- | --- |
| 0.00 | 0 | 0 | 0 |
| 0.01 | ~48 | ~35 | ~25 |
| 0.02 | ~50 | ~45 | ~35 |
| 0.03 | ~50 | ~48 | ~42 |
| 0.04 | ~50 | ~49 | ~46 |
| 0.05 | ~50 | ~49.5 | ~48 |
| 0.06 | ~50 | ~49.8 | ~49 |
| 0.07 | ~50 | ~49.9 | ~49.5 |
| 0.08 | ~50 | ~50 | ~49.8 |
</details>

Figure 10.17 Closed-loop response of DC motor with PI controller (Example 10.5).

In summary, the simple proportional (P) controller cannot provide good steady-state tracking for a step reference speed command to the DC motor. Adding an integral control loop (PI controller) eliminates the steady-state error and the motor speed eventually tracks the reference input. Increasing the P-gain speeds up the closed-loop response, but large values of $K _ { P }$ will lead to excessive control inputs (armature voltage $e _ { \mathrm { i n } } ( t )$ , in this case).
