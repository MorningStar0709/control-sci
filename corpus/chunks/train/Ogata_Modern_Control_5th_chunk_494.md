To find the closed-loop frequency response by use of the Nichols chart, the $G ( j \omega )$ locus is constructed in the log-magnitude-versus-phase plane by use of MATLAB or from the Bode diagram. Figure $7 - 8 5 ( \mathrm { a } )$ shows the $G ( j \omega )$ locus together with the M and N loci. The closed-loop frequency-response curves may be constructed by reading the magnitudes and phase angles at various frequency points on the $G ( j \omega )$ locus from the M and N loci, as shown in Figure $7 - 8 5 ( \mathrm { b } )$ . Since the largest magnitude contour touched by the $G ( j \omega )$ locus is 5 dB, the resonant peak magnitude $M _ { r }$ is 5 dB. The corresponding resonant peak frequency is 0.8 radsec.

![](image/69e10585999564d060c7f0d5cb0abd8270edea42c95df6d3afbf7d38287aae19.jpg)  
Figure 7–84 Nichols chart.

Notice that the phase crossover point is the point where the $G ( j \omega )$ locus intersects the $- 1 8 0 ^ { \circ }$ axis (for the present system, $\omega = 1 . 4 \ : \mathrm { r a d / s e c } )$ , and the gain crossover point is the point where the locus intersects the 0-dB axis (for the present system, $\omega = 0 . 7 6 \ \mathrm { r a d / s e c } )$ . The phase margin is the horizontal distance (measured in degrees) between the gain crossover point and the critical point $( 0 \mathrm { d B } , - 1 8 0 ^ { \circ } )$ . The gain margin is the distance (in decibels) between the phase crossover point and the critical point.

The bandwidth of the closed-loop system can easily be found from the $G ( j \omega )$ locus in the Nichols diagram. The frequency at the intersection of the $G ( j \omega )$ locus and the $M = - 3$ dB locus gives the bandwidth.

If the open-loop gain K is varied, the shape of the $G ( j \omega )$ locus in the log-magnitudeversus-phase diagram remains the same, but it is shifted up (for increasing $K )$ or down (for decreasing $K )$ along the vertical axis. Therefore, the $G ( j \omega )$ locus intersects the M and N loci differently, resulting in a different closed-loop frequency-response curve. For a small value of the gain K, the $G ( j \omega )$ locus will not be tangent to any of the M loci, which means that there is no resonance in the closed-loop frequency response.

![](image/0d302492e871fdab63a077f93a92a2c5c28712a5ba95cf94227d5e2d2437015e.jpg)  
Figure 7–85 (a) Plot of $G ( j \omega )$ superimposed on Nichols chart; (b) closed-loop frequency-response curves.
