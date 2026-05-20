where $K _ { \mathrm { L F } }$ is the “lead filter” gain. Figure 11.47 shows the closed-loop responses of the nonlinear and linear hydraulic actuator models using the lead controller with gain $K _ { \mathrm { L F } } = 2 0 0 0$ (the lead controller gain was selected so that its DC gain matches the P-gain $K _ { P } = 5 0 0 \mathrm { V / m } )$ . Note that the output/input amplitude ratio is roughly the same as the closed-loop response using P-control because the DC gain of the lead controller matches the P-gain $K _ { P } .$ . However, adding the lead controller has improved the closed-loop response because the time lag between input and output peaks has been reduced. We can use the MATLAB commands to compute the magnitude and phase angle:

![](image/5f15af3ec940bce4936456adea0d3e25985d4db9a39aa9674d8ecb21db411405.jpg)

<details>
<summary>line</summary>

| Time, s | Reference and actual piston position, x(t), cm | Nonlinear and linear EHA responses |
| --- | --- | --- |
| 0.0 | 30 | 30 |
| 0.5 | 20 | 20 |
| 1.0 | 20 | 20 |
| 1.5 | 20 | 20 |
| 2.0 | 25 | 25 |
</details>

Figure 11.47 Closed-loop responses of the nonlinear and linear EHA models with sinusoidal ${ \boldsymbol { x } } _ { \mathrm { r e f } } ( t )$ and lead controller with gain $K _ { \mathsf { L F } } = 2 0 0 0$ .

>> K_LF = 2000; % lead filter gain
>> sysGc = tf([1 10], [1 40]); % lead filter $G_{\mathrm{C}}(s)$ >> sysG = tf(2648.15, [1 630 122500 0]);
>> sysT = feedback(K_LF*sysGc*sysG,1) % plant transfer function $G(s)$ >> w = 2*2*pi; % closed-loop transfer function $T(s)$ >> [mag,phase] = bode(sysT,w) % 2 Hz frequency, rad/s
% closed-loop frequency response

The magnitude is 0.6532 (roughly 10/15, as expected) and the phase angle is $- 2 5 . 3 4 ^ { \circ } \left( - 0 . 4 4 2 3 \mathrm { r a d } \right)$ , which is less than half of the phase lag for the closed-loop system using proportional control. Hence, the time lag using the lead controller is $0 . 4 4 2 3 \mathrm { r a d } / ( 4 \pi \mathrm { r a d } / \mathrm { s } ) = 0 . 0 3 5 \mathrm { s } .$ , which is half the time lag for the P-control system.
