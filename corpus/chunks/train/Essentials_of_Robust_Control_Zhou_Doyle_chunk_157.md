$$L (s) = \frac {- s + z _ {1}}{s + z _ {1}} \frac {- s + z _ {2}}{s + z _ {2}} \dots \frac {- s + z _ {k}}{s + z _ {k}} L _ {\mathrm{mp}} (s)$$

where $L _ { \mathrm { m p } }$ is stable and minimum phase and $| L ( j \omega ) | = | L _ { \mathrm { m p } } ( j \omega ) |$ . Hence

$$\angle L (j \omega_ {0}) = \angle L _ {\mathrm{mp}} (j \omega_ {0}) + \angle \prod_ {i = 1} ^ {k} \frac {- j \omega_ {0} + z _ {i}}{j \omega_ {0} + z _ {i}}= \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {d \ln | L _ {\mathrm{mp}} |}{d \nu} \ln \coth \frac {| \nu |}{2} d \nu + \sum_ {i = 1} ^ {k} \angle \frac {- j \omega_ {0} + z _ {i}}{j \omega_ {0} + z _ {i}},$$

which gives

$$\angle L (j \omega_ {0}) = \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {d \ln | L |}{d \nu} \ln \coth \frac {| \nu |}{2} d \nu + \sum_ {i = 1} ^ {k} \angle \frac {- j \omega_ {0} + z _ {i}}{j \omega_ {0} + z _ {i}}. \tag {6.12}$$

Since $\angle \frac { - j \omega _ { 0 } + z _ { i } } { j \omega _ { 0 } + z _ { i } } \le 0$ for each $i ,$ a nonminimum phase zero contributes an additional jω0 + zi phase lag and imposes limitations on the rolloff rate of the open-loop gain. For example, suppose L has a zero at $z > 0 ;$ then

$$\phi_ {1} (\omega_ {0} / z) := \left. \angle \frac {- j \omega_ {0} + z}{j \omega_ {0} + z} \right| _ {\omega_ {0} = z, z / 2, z / 4} = - 9 0 ^ {\circ}, - 5 3. 1 3 ^ {\circ}, - 2 8 ^ {\circ},$$

as shown in Figure 6.10. Since the slope of $| L |$ near the crossover frequency is, in general, no greater than −1, which means that the phase due to the minimum phase part, $L _ { \mathrm { m p } } ,$ of L will, in general, be no greater than $- 9 0 ^ { \mathrm { o } }$ , the crossover frequency (or the closed-loop bandwidth) must satisfy

$$\omega_ {c} < z / 2 \tag {6.13}$$

in order to guarantee the closed-loop stability and some reasonable closed-loop performance.

Next suppose L has a pair of complex right-half zeros at $z = x \pm j y$ with $x > 0 \AA$ ; then

$$
\phi_ {2} (\omega_ {0} / | z |) := \angle \frac {- j \omega_ {0} + z}{j \omega_ {0} + z} \left. \frac {- j \omega_ {0} + \bar {z}}{j \omega_ {0} + \bar {z}} \right| _ {\omega_ {0} = | z |, | z | / 2, | z | / 3, | z | / 4}
\approx \left\{ \begin{array}{c c c c c} - 1 8 0 ^ {\circ}, & - 1 0 6. 2 6 ^ {\circ}, & - 7 3. 7 ^ {\circ}, & - 5 6 ^ {\circ}, & \operatorname{Re} (z) \gg \Im (z) \\ - 1 8 0 ^ {\circ}, & - 8 6. 7 ^ {\circ}, & - 5 5. 9 ^ {\circ}, & - 4 1. 3 ^ {\circ}, & \operatorname{Re} (z) \approx \Im (z) \\ - 3 6 0 ^ {\circ}, & 0 ^ {\circ}, & 0 ^ {\circ}, & 0 ^ {\circ}, & \operatorname{Re} (z) \ll \Im (z) \end{array} \right.
$$
