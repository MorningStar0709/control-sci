The variation of the closed-loop response with gain $K _ { P }$ can be determined by using the root-locus method. We can easily produce the root locus by using the following MATLAB commands:

```matlab
>> sysG = tf(2648.15, [ 1 630 122500 0 ]);    % forward transfer function
>> rlocus(sysG)    % plot root locus 
```

The first command builds the forward transfer function G(s), and the second command creates the root locus, which is shown in Fig. 11.43. The closed-loop poles begin at the open-loop roots (poles) when the proportional gain $K _ { P }$ is zero. In this case, the open-loop poles are s = 0 (the integrator) and $s = - 3 1 5 \pm j 1 5 2 . 5 6$ (the solenoid–valve dynamics). Figure 11.43 shows that two closed-loop poles move from the two complex open-loop poles to the negative real axis, and a single closed-loop pole moves to the left from the origin to a break-away point near −153 on the negative real axis. If the proportional gain $K _ { P }$ is too high, two closedloop poles follow $\pm 6 0 ^ { \circ }$ asymptotes and eventually cross the imaginary axis, rendering the closed-loop system unstable.

The root-locus diagram shown in Fig. 11.43 indicates that with the proper gain selection the three closed-loop poles can be large negative values, and consequently the closed-loop response will be extremely fast and overdamped (no oscillations in the transient response). As an example, let the proportional gain be $K _ { P } = 2 8 5 0 \mathrm { V / m }$ and compute the closed-loop poles using MATLAB’s rlocus command

![](image/270b670412326f61a95b626bb9415a24a7f68f2610dc9c0eac9f1ed59839a05d.jpg)

<details>
<summary>line</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -300 | 150 |
| 0 | 0 |
| 100 | -500 |
</details>

Figure 11.43 Root locus for the linear EHA model with proportional control.
