# Alternative Conditions

To further investigate the sensitivity of the closed-loop system to changes in the process model, it is assumed that the design is based on the model H = B/A, and the true model is $H^{0} = B^{0}/A^{0}$ . From Theorem 3.5 it follows that the closed-loop system is stable if

$$\left| H (z) - H ^ {0} (z) \right| \leq \left| \frac {H (z)}{H _ {m} (z)} \right| \cdot \left| \frac {H _ {f f} (z)}{\bar {H} _ {f b} (z)} \right| = \left| \frac {H (z) T (z)}{H _ {m} (z) S (z)} \right| \tag {5.40}$$

for $|z| = 1$ , where it follows from (5.30) and (5.31) that $H_{m} = t_{0}B / A_{c}$ , $H_{ff} = T / R$ , and $H_{fb} = S / R$ . The relative accuracy that is needed for stability is

$$\frac {| H (z) - H ^ {0} (z) |}{| H (z) |} \leq \frac {1}{| H _ {m} (z) |} \left. \frac {H _ {f f} (z)}{H _ {f h} (z)} \right|$$

It is easy to use this result. When a design is performed, the right-hand side of (5.40) can easily be calculated for $z = e^{i\omega h}$ . Notice that it does not depend on the true pulse-transfer function.

The condition given in (5.40) has good physical interpretation. Consider first the ratio $H/H_{m}$ . The pulse-transfer function H of the process is typically large for low frequencies and decreases for high frequencies (see Fig. 5.6). The desired pulse-transfer function $H_{m}$ of the closed-loop system is typically unity for low frequencies. There is a small increase around the crossover frequency and $H_{m}$ decreases for high frequencies. The frequency response of $H_{m}$ is also shown in Fig. 5.6. The ratio $H/H_{m}$ is easy to obtain from the figure. It is clear from the figure that it is sufficient to have good model precision only in certain frequency ranges. The consequences of changing the desired bandwidth of the closed-loop system can also be determined. The requirements on the model accuracy are relaxed if the closed-loop bandwidth is decreased. A more-precise model will be needed if the desired bandwidth is increased. The requirements on model precision are smaller for frequencies where the feedforward gain is larger than the feedback gain. The ratio of the feedforward- and the feedback-pulse-transfer functions $H_{ff}/H_{fb} = T/S$ is equal to one for a controller with error feedback.

![](image/f1bab4182187f5933576a55e3ddaa9b1ad72728594dd8a2854e87e2763eeee6e.jpg)  
Figure 5.6 Bode diagrams for H and $H_{m}$ . The ratio $H/H_{m}$ , which appears in (5.40), is easily found in the figure.
