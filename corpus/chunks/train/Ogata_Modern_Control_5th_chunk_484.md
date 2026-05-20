3. The resonant peak frequency $\omega _ { r }$ and the damped natural frequency $\omega _ { d }$ for the step transient response are very close to each other for lightly damped systems.

The three relationships just listed are useful for correlating the step transient response with the frequency response of higher-order systems, provided that they can be approximated by the standard second-order system or a pair of complex-conjugate closed-loop poles. If a higher-order system satisfies this condition, a set of time-domain specifications may be translated into frequency-domain specifications. This simplifies greatly the design work or compensation work of higher-order systems.

In addition to the phase margin, gain margin, resonant peak $M _ { r }$ , and resonant frequency $\omega _ { r }$ , there are other frequency-domain quantities commonly used in performance specifications. They are the cutoff frequency, bandwidth, and the cutoff rate. These will be defined in what follows.

Cutoff Frequency and Bandwidth. Referring to Figure 7–76, the frequency $\omega _ { b }$ at which the magnitude of the closed-loop frequency response is 3 dB below its zero-frequency value is called the cutoff frequency. Thus

$$\left| \frac {C (j \omega)}{R (j \omega)} \right| < \left| \frac {C (j 0)}{R (j 0)} \right| - 3 \mathrm{dB}, \quad \text { for } \omega > \omega_ {b}$$

For systems in which $\left| C ( j 0 ) / R ( j 0 ) \right| = 0$ dB,

$$\left| \frac {C (j \omega)}{R (j \omega)} \right| < - 3 \mathrm{dB}, \quad \text { for } \omega > \omega_ {b}$$

The closed-loop system filters out the signal components whose frequencies are greater than the cutoff frequency and transmits those signal components with frequencies lower than the cutoff frequency.

The frequency range $0 \leq \omega \leq \omega _ { b }$ in which the magnitude of $C ( j \omega ) / R ( j \omega )$ is greater than –3 dB is called the bandwidth of the system. The bandwidth indicates the frequency where the gain starts to fall off from its low-frequency value. Thus, the bandwidth indicates how well the system will track an input sinusoid. Note that for a given $\omega _ { n } .$ , the rise time increases with increasing damping ratio z. On the other hand, the bandwidth decreases with the increase in $\zeta .$ Therefore, the rise time and the bandwidth are inversely proportional to each other.

![](image/289b09f29aaf2b724359f9dc568eadc27766374e86423f7106b247db9a93eae2.jpg)
