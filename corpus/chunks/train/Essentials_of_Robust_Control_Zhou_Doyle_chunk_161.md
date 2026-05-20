This integral implies that the sensitivity reduction ability of the system may be severely limited by the open-loop unstable poles and nonminimum phase zeros, especially when these poles and zeros are close to each other.

Define

$$\theta (z) := \int_ {- \omega_ {l}} ^ {\omega_ {l}} \frac {x _ {0}}{x _ {0} ^ {2} + (\omega - y _ {0}) ^ {2}} d \omega$$

Then

$$
\begin{array}{l} \pi \ln \prod_ {i = 1} ^ {m} \left| \frac {z + p _ {i}}{z - p _ {i}} \right| = \int_ {- \infty} ^ {\infty} \ln | S (j \omega) | \frac {x _ {0}}{x _ {0} ^ {2} + (\omega - y _ {0}) ^ {2}} d \omega \\ \leq (\pi - \theta (z)) \ln \| S (j \omega) \| _ {\infty} + \theta (z) \ln (\epsilon), \\ \end{array}
$$

which gives

$$\| S (s) \| _ {\infty} \geq \left(\frac {1}{\epsilon}\right) ^ {\frac {\theta (z)}{\pi - \theta (z)}} \left(\prod_ {i = 1} ^ {m} \left| \frac {z + p _ {i}}{z - p _ {i}} \right|\right) ^ {\frac {\pi}{\pi - \theta (z)}}$$

This lower bound on the maximum sensitivity shows that for a nonminimum phase system, its sensitivity must increase significantly beyond one at certain frequencies if the sensitivity reduction is to be achieved at other frequencies.
