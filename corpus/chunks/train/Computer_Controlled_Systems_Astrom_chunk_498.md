# Selection of Sampling Interval

The choice of sampling period depends on many factors. One way to determine the sampling period is to use continuous-time arguments. The sampled system can be approximated by the hold circuit, followed by the continuous-time system. For small sampling periods, the transfer function of the hold circuit can be

approximated as

$$\frac {1 - e ^ {- s h}}{s h} \approx \frac {1 - 1 + s h - (s h) ^ {2} / 2 + \cdots}{s h} = 1 - \frac {s h}{2} + \dots$$

The first two terms correspond to the series expansion of $\exp(-sh/2)$ . That is, for small h, the hold can be approximated by a time delay of half a sampling interval. Assume that the phase margin can be decreased by $5^{\circ}$ to $15^{\circ}$ . This gives the following rule of thumb:

$$h \omega_ {c} \approx 0. 1 5 \text { to } 0. 5$$

where $\omega_{c}$ is the crossover frequency (in radians per second) of the continuous-time system. This rule gives quite short sampling periods. The Nyquist frequency will be about 5 to 20 times larger than the crossover frequency.
