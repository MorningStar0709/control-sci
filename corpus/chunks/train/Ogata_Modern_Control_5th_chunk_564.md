Once we choose the gain crossover frequency to be 2 radsec, we can determine the corner frequencies of the phase-lag portion of the lag–lead compensator. Let us choose the corner frequency $\omega = 1 / T _ { 2 }$ (which corresponds to the zero of the phase-lag portion of the compensator) to be 1 decade below the new gain crossover frequency, or at $\omega = 0 . 2 \mathrm { r a d / s e c }$ . For another corner frequency $\omega = 1 / { \left( \beta T _ { 2 } \right) }$ we need the value of, $\beta .$ . The value of $\beta$ can be determined from the consideration of the lead portion of the compensator, as shown next.

For the lead compensator, the maximum phase-lead angle $\phi _ { m }$ is given by

$$\sin \phi_ {m} = \frac {\beta - 1}{\beta + 1}$$

Notice that $\beta = 1 0$ corresponds to $\phi _ { m } = 5 4 . 9 ^ { \circ }$ . Since we need a $5 0 ^ { \circ }$ phase margin, we may choose $\beta = 1 0$ . (Note that we will be using several degrees less than the maximum angle, 54.9°.) Thus,

$$\beta = 1 0$$

Then the corner frequency $\omega = 1 / { \left( \beta T _ { 2 } \right) }$ (which corresponds to the pole of the phase-lag portion of the compensator) becomes

$$\omega = 0. 0 2$$

The transfer function of the phase-lag portion of the lag–lead compensator becomes

$$\frac {s + 0 . 2}{s + 0 . 0 2} = 1 0 \left(\frac {5 s + 1}{5 0 s + 1}\right)$$

The phase-lead portion can be determined as follows: Since the new gain crossover frequency is $\omega = 2$ radsec, from Figure 7–151, $\left| G ( j 2 ) \right|$ @ is found to be 6 dB. Hence, if the lag–lead compensator contributes –6 dB at v=2 radsec, then the new gain crossover frequency is as desired. From this requirement, it is possible to draw a straight line of slope 20 dB/decade passing through the point $( 2 \mathrm { r a d } / \mathrm { s e c } , - 6 \mathrm { d } \mathrm { B } )$ . (Such a line has been manually drawn on Figure 7–151.) The intersections of this line and the 0-dB line and –20-dB line determine the corner frequencies. From this consideration, the corner frequencies for the lead portion can be determined as $\omega = 0 . 4 \mathrm { r a d / s e c }$ and v=4 radsec. Thus, the transfer function of the lead portion of the lag–lead compensator becomes

$$\frac {s + 0 . 4}{s + 4} = \frac {1}{1 0} \left(\frac {2 . 5 s + 1}{0 . 2 5 s + 1}\right)$$

Combining the transfer functions of the lag and lead portions of the compensator, we can obtain the transfer function $G _ { c } ( s )$ of the lag–lead compensator. Since we chose $K _ { c } = 1$ , we have
