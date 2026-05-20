# Changing $\omega$ and $\zeta$

The polynomial $A_{c}$ determines the response to command signals. It also influences the response to load disturbances and measurement errors. Figure 5.11 illustrates the consequences of changing $\omega$ . The results are as we can expect. The response time and the error due to load disturbances decrease inversely proportional to the bandwidth. When the bandwidth is increased, the control signals also increase. The initial control signal is approximately proportional to the square of the bandwidth. Saturation of the control signal thus limits the admissible bandwidth.

Different choices of $\omega$ have only moderate effect on the response to measurement noise. The fluctuations in the control signal are increased a little when the bandwidth is increased. The effects of changing damping $\zeta$ are also as can be expected. A command response without overshoot is obtained for $\zeta = 1$ .

![](image/0c6342cb4c13773e6b0ef46a2d849c7d85419a14d9fbeced21b8aaedaeb384c2.jpg)  
Figure 5.11 Simulation of pole-placement controllers when changing $\omega$ . (a) Output for $\omega = 0.1$ (dashed), 0.2 (solid), and 0.4 (dashed-dotted). (b) Control signal when $\omega = 0.1$ . (c) Control signal when $\omega = 0.4$ .
