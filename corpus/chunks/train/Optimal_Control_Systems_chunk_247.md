# Gain Margin

We recall that the gain margin of a feedback control system is the amount of loop gain (usually in decibels) that can be changed before the closed-loop system becomes unstable. Let us now apply the well-known Nyquist criterion to the unity feedback, optimal control system depicted in Figure 4.11. Here, we assume that the Nyquist path is clockwise (CW) and the corresponding Nyquist plot makes counter-clockwise (CCW) encirclements around the critical point $-1+j0$ . According to Nyquist stability criterion, for closed-loop stability, the Nyquist plot (or diagram) makes CCW encirclements as many times as there are poles of the transfer function $G_{o}(s)$ lying in the right half of the s-plane.

From Figure 4.11 and the return difference relation (4.5.21), we note that

$$\left| (1 + \bar {\mathbf {k}} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {b}) \right| \geq 1 \tag {4.5.34}$$

implies that the distance between the critical point $-1 + j0$ and any point on the Nyquist plot is at least 1 and the resulting Nyquist plot is shown in Figure 4.12 for all positive values of $\omega$ (i.e., 0 to $\infty$ ). This

![](image/187df072acd395369d52a4299a923b3341887aca6a90598e81606eb900bb4165.jpg)

<details>
<summary>text_image</summary>

Im
1
-2
-1
Re
P
G₀(jω)
ω
1 + G₀(jω)
</details>

Figure 4.12 Nyquist Plot of $G_{o}(j\omega)$

means that the Nyquist plot of $G_{o}(j\omega)$ is constrained to avoid all the points inside the unit circle (centered at $-1 + j0$ ). Thus, it is clear that the closed-loop optimal system has infinite gain margin. Let us proceed further to see if there is a lower limit on the gain factor.
