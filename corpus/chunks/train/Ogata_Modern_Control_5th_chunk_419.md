At $\omega = \infty ,$ , the phase angle becomes $- 1 8 0 ^ { \circ }$ . The phase-angle curve is skew symmetric about the inflection point—the point where $\phi = - 9 0 ^ { \circ }$ .There are no simple ways to sketch such phase curves. We need to refer to the phase-angle curves shown in Figure 7–9.

The frequency-response curves for the factor

$$1 + 2 \zeta \left(j \frac {\omega}{\omega_ {n}}\right) + \left(j \frac {\omega}{\omega_ {n}}\right) ^ {2}$$

can be obtained by merely reversing the sign of the log magnitude and that of the phase angle of the factor

$$\frac {1}{1 + 2 \zeta \left(j \frac {\omega}{\omega_ {n}}\right) + \left(j \frac {\omega}{\omega_ {n}}\right) ^ {2}}$$

To obtain the frequency-response curves of a given quadratic transfer function, we must first determine the value of the corner frequency $\omega _ { n }$ and that of the damping ratio $\zeta .$ . Then, by using the family of curves given in Figure 7–9, the frequency-response curves can be plotted.

The Resonant Frequency ${ \pmb { \omega } } _ { r }$ and the Resonant Peak Value $M _ { r }$ . The magnitude of

$$G (j \omega) = \frac {1}{1 + 2 \zeta \left(j \frac {\omega}{\omega_ {n}}\right) + \left(j \frac {\omega}{\omega_ {n}}\right) ^ {2}}$$

is

$$\left| G (j \omega) \right| = \frac {1}{\sqrt {\left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) ^ {2} + \left(2 \zeta \frac {\omega}{\omega_ {n}}\right) ^ {2}}} \tag {7-9}$$

If $\left| G ( j \omega ) \right|$ has a peak value at some frequency, this frequency is called the resonant frequency. Since the numerator of $\left| G ( j \omega ) \right|$ is constant, a peak value of@ $\left| G ( j \omega ) \right|$ will occur@ when

$$g (\omega) = \left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) ^ {2} + \left(2 \zeta \frac {\omega}{\omega_ {n}}\right) ^ {2} \tag {7-10}$$

is a minimum. Since Equation (7–10) can be written

$$g (\omega) = \left[ \frac {\omega^ {2} - \omega_ {n} ^ {2} (1 - 2 \zeta^ {2})}{\omega_ {n} ^ {2}} \right] ^ {2} + 4 \zeta^ {2} (1 - \zeta^ {2}) \tag {7-11}$$

the minimum value of $g ( \omega )$ occurs at $\omega = \omega _ { n } \sqrt { 1 - 2 \zeta ^ { 2 } }$ Thus the resonant frequency. $\omega _ { r }$ is

$$\omega_ {r} = \omega_ {n} \sqrt {1 - 2 \zeta^ {2}}, \quad \text { for } 0 \leq \zeta \leq 0. 7 0 7 \tag {7-12}$$
