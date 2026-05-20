# Example 10.14

Consider a unity-feedback control system with the plant transfer function

$$\mathrm{Plant:} G _ {P} (s) = \frac {4}{s (s + 1) (s + 2)}$$

Check the stability margins of the “uncompensated” system (plant only with P-gain). If the damping is poor, improve it by adding a dynamic controller to the forward path.

Figure 10.55a shows the Bode diagram of the plant transfer function $G _ { P } ( s )$ , which we consider the “uncompensated system” with P-gain $K _ { P } = 1$ . We see that both the gain and phase margins are poor: ${ G M } _ { \mathrm { d B } } =$ 3.52 dB and $\phi _ { \mathrm { p m } } = 1 1 . 4 ^ { \circ }$ (damping ratio $\zeta \cong 0 . 1 1 $ ). The two crossover frequencies are close together, which indicates a closed-loop system with small stability margins and hence the P-gain cannot be increased. Decreasing the gain $K _ { P }$ will improve gain and phase margins but it will also slow down the response and degrade steady-state tracking errors. One remedy for the low phase margin (i.e., low damping) is to add a lead controller with a zero near the unity-gain crossover frequency of $\omega _ { \mathrm { p m } } = 1 . 1 4$ rad/s. We choose the following lead controller:

$$\mathrm{Leadcontroller:} G _ {C} (s) = \frac {K (s + 0 . 9)}{s + 5}$$

We select the controller gain $K = 3 . 5$ so that its DC gain is close to unity. This gain selection ensures that the lowfrequency gain of $G _ { C } ( s ) G _ { P } ( s )$ is nearly equal to the low-frequency gain of the plant $G _ { P } ( s )$ and therefore the steadystate tracking accuracy is not compromised. Figure 10.55b shows the Bode diagram of the compensated plant (with lead controller added). The gain margin has increased to 14.6 dB and the phase margin has increased to $5 0 . 6 ^ { \circ }$ (damping ratio $\zeta \cong 0 . 5 )$ . If we compare the phase plots in Fig. 10.55, we see that the lead controller has added phase angle near $\omega = 1$ rad/s as designed, which has subsequently increased the phase margin. Figure 10.56 shows both Bode plots from Fig. 10.55 on the same diagram. The significant increase in phase due to the lead controller is apparent. Consequently, the phase margin (and damping) has been dramatically increased by introducing the lead controller.

![](image/ecf0086650a5f51262f451b0c8a1636517c4e56bdb408d51c2b0464611210b01.jpg)

<details>
<summary>line</summary>
