With K=10, the compensated system will satisfy the steady-state requirement.

We shall next plot the Bode diagram of

$$G _ {1} (j \omega) = \frac {4 0}{j \omega (j \omega + 2)} = \frac {2 0}{j \omega (0 . 5 j \omega + 1)}$$

Figure 7–95 shows the magnitude and phase-angle curves of $G _ { 1 } ( j \omega )$ . From this plot, the phase and gain margins of the system are found to be $1 7 ^ { \circ }$ and ±q dB, respectively. (A phase margin of 17° implies that the system is quite oscillatory. Thus, satisfying the specification on the steady state yields a poor transient-response performance.) The specification calls for a phase margin of at least 50°. We thus find the additional phase lead necessary to satisfy the relative stability requirement is 33°.To achieve a phase margin of 50° without decreasing the value of K, the lead compensator must contribute the required phase angle.

Noting that the addition of a lead compensator modifies the magnitude curve in the Bode diagram, we realize that the gain crossover frequency will be shifted to the right. We must offset the increased phase lag of $G _ { 1 } ( j \omega )$ due to this increase in the gain crossover frequency. Considering the shift of the gain crossover frequency, we may assume that $\phi _ { m }$ , the maximum phase lead required, is approximately 38°. (This means that $5 ^ { \circ }$ has been added to compensate for the shift in the gain crossover frequency.)

Since

$$\sin \phi_ {m} = \frac {1 - \alpha}{1 + \alpha}$$

![](image/9110e5499ad2f9d1b0adb2de800f8602c0089744b34277c6e03068770995e29b.jpg)  
Figure 7–95 Bode diagram for G1(jv)=10G(jv) = 40/Cjv(jv+2)D

$\phi _ { m } = 3 8 ^ { \circ }$ corresponds to $\alpha = 0 . 2 4$ . Once the attenuation factor a has been determined on the basis of the required phase-lead angle, the next step is to determine the corner frequencies $\omega = 1 / T$ and $\omega = 1 / ( \alpha T )$ of the lead compensator. To do so, we first note that the maximum phase-lead angle $\phi _ { m }$ occurs at the geometric mean of the two corner frequencies, or $\omega = 1 / ( \sqrt { \alpha } T )$ [See Equa-. tion $( 7 - 2 6 ) . ]$ The amount of the modification in the magnitude curve at $\omega = 1 / ( \sqrt { \alpha } T )$ due to the inclusion of the term $( T s + 1 ) / ( \alpha T s + 1 )$ is

$$\left| \frac {1 + j \omega T}{1 + j \omega \alpha T} \right| _ {\omega = 1 / (\sqrt {\alpha} T)} = \left| \frac {1 + j \frac {1}{\sqrt {\alpha}}}{1 + j \alpha \frac {1}{\sqrt {\alpha}}} \right| = \frac {1}{\sqrt {\alpha}}$$
