# Example 6.7 (dc Servo)

For the dc servo of Example 2.1 (Chapter 2), calculate the values of the gain k of a gain feedback controller such that the phase margin is at least $50^{\circ}$ and the gain margin at least 6 db.

![](image/dc76a367322d3d755bbd2b42fcfbac6611c9e67101d277f7f53e2886b364471a.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (dB) |
| --- | --- |
| 10⁻¹ | 25 |
| 10⁰ | 0 |
| 10¹ | -25 |
| 10² | -80 |
</details>

![](image/ce66bb56109755f7f293702af0e94bc5ee2b1232d2b2e35ad388a5ae0d4c2524.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Phase (deg) |
| --- | --- |
| 1.5 | -140 |
| 7.4 | -180 |
</details>

Figure 6.16 Bode plots

Solution The transfer function is given in Equation 3.21 (Chapter 3), and in Example 6.4. Figure 6.16 shows the Bode plots.

Gain margin: The phase is $180^{\circ}$ at $\omega = 7.4$ rad/s. The magnitude at that frequency is -23.21 db. For a 6-db gain margin, the gain can be at most 17.21 db.

Phase margin: The phase is $-180^{\circ} + 50^{\circ} = -130^{\circ}$ at $\omega = 1.5$ rad/s, and the
