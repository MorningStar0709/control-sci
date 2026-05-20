# When Can Dynamics of Antialiasing Filters Be Neglected?

We have mentioned that the dynamics in the antialiasing filter often must be taken into account. The following analysis gives additional insight. The phase lag at the frequency $\omega_0$ introduced by a second-order Butterworth filter (7.11) is

$$\alpha \approx \frac {2 . 6}{\sqrt {\beta}} \frac {\omega_ {0}}{\omega_ {s}}$$

where $\omega_{s}$ is the sampling frequency, and $\beta$ is the attenuation of the filter at the Nyquist frequency. For a Bessel filter of sixth order the relation is

$$\alpha \approx \frac {8 . 6}{\beta^ {1 / 6}} \frac {\omega_ {0}}{\omega_ {s}}$$

Our rules for selecting the sampling rates in digital systems require that $\omega_{0}h$ is in the range of 0.2 to 0.6. With $\omega_{0}h = 0.2$ the preceding equation implies that the phase lag of the second-order antialiasing filter is

$$\alpha = \frac {0 . 0 8 3}{\sqrt {\beta}}$$

With $\beta = 0.1$ we get $\alpha = 0.26$ rad, or $15^{\circ}$ . With the sixth-order Bessel filter as an antialiasing filter and $\beta = 0.1$ , we get $\alpha = 0.4$ rad, or $23^{\circ}$ . These calculations show that it is necessary to take the dynamics of the antialiasing filter into account for practically all digital designs. Approximating the filter by a delay is a convenient way of doing that.
