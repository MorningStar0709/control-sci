# Example 8.1 Frequency prewarping

Assume that the integrator

$$G (s) = \frac {1}{s}$$

should be implemented as a digital filter. Using the transformation of (8.6) without prewarping gives

$$H _ {T} (z) = \frac {1}{\frac {2}{h} \cdot \frac {z - 1}{z + 1}} = \frac {h}{2} \cdot \frac {z + 1}{z - 1}$$

Prewarping gives

$$H _ {P} (z) = \frac {\tan (\omega_ {1} h / 2)}{\omega_ {1}} \cdot \frac {z + 1}{z - 1}$$

The frequency function of $H_{P}$ is

$$H _ {P} \left(e ^ {i \omega h}\right) = \frac {\tan \left(\omega_ {1} h / 2\right)}{\omega_ {1}} \cdot \frac {e ^ {i \omega h} + 1}{e ^ {i \omega h} - 1} = \frac {\tan \left(\omega_ {1} h / 2\right)}{\omega_ {1}} \quad \frac {1}{i \tan (\omega h / 2)}$$

thus $G(i\omega)$ and $H_{P}\left(e^{i\omega h}\right)$ are equal for $\omega = \omega_{1}$ .
