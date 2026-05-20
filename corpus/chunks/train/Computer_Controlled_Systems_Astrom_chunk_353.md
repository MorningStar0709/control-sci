# Comparison

To obtain additional insight into the properties of the controller we compute the loop-transfer functions L for both systems. This is shown in Fig. 5.27. The figure shows that the design based on a notch filter has higher gain at lower frequencies. This can also be seen by comparing the magnitude of the first peak of the load disturbance responses in Figs. 5.25 and 5.26. The loop-transfer function for the controller with the notch filter is, however, misleading because of the canceled factor that does not appear in the loop-transfer function. The system with active damping has a much higher gain around the frequency 1 rad/s, which corresponds to the poorly damped mode.

![](image/a6ea6d60a011d743c3b3149e0ece01ad4200c389ea23b4159564567525e04aad.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 1 |
| 80 | 1 | 0 |
</details>

Figure 5.26 Response of the closed-loop system using the controller designed for active damping.

The sensitivity functions for the systems are shown in Fig. 5.28. The figure shows that the design with active damping is more sensitive to modeling errors than the design based on the notch filter.

![](image/22627f430d72306daab161567d44e6bbc762a1248a555a4c4223b4accc497f36.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Gain (Solid Line) | Gain (Dashed Line) |
| --- | --- | --- |
| 0.01 | ~90 | ~80 |
| 0.1 | ~50 | ~40 |
| 1 | ~10 | ~15 |
| 10 | ~0.01 | ~0.01 |
</details>

Figure 5.27 The magnitude of the loop-transfer function L. Gain is shown with notch design (solid line) and active damping (dashed line).

![](image/e3b0fe78cff31de1c8aee731cd90ce37ead006734f18bd22eec65af39cd5b9fb.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Gain (Solid Line) | Gain (Dashed Line) |
| --- | --- | --- |
| 0.01 | 0.05 | 0.1 |
| 0.1 | 0.5 | 0.8 |
| 1 | 1.0 | 1.2 |
| 10 | 1.0 | 1.0 |
</details>

Figure 5.28 Amplitude curve for the sensitivity function S for a system with notch design (solid line) and a system with active damping of the resonant mode (dashed line).
