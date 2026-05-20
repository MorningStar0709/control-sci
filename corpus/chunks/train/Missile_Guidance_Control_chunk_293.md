$$\lambda_ {E} = R _ {m} (\theta_ {m} - \theta_ {t}) - K _ {G} R _ {m} \left(\frac {d \theta_ {t}}{d t}\right) \{(R _ {t} - R _ {m}) / (\dot {R} _ {m} - \dot {R} _ {t}) \}, \tag {4.57}$$

where $K _ { G }$ is a proportionality constant used to tune the guidance system. Similarly, it can be shown that the lateral error for the azimuth plane is given by

$$\lambda_ {A} = R _ {m} (\psi_ {m} - \psi_ {t}) \cos \theta_ {t} - K _ {G} R _ {m} \left(\frac {d \theta_ {t}}{d t}\right) \{(R _ {t} - R _ {m}) / (\dot {R} _ {m} - \dot {R} _ {t}) \} \cos \theta_ {t}. \tag {4.58}$$

Note that in both these equations, the second term goes to zero as the missile approaches the target. Furthermore, the proportionality constant $K _ { G }$ can assume the following values:

If

$K _ { G } = 1$ , the intercept is a constant-bearing collision course.

$\begin{array} { r } { K _ { G } = \frac { 1 } { 2 } } \end{array}$ represents the half-rectified lead angle guidance mode.

$K _ { G } = 0$ represents the 3-point guidance mode (see Section 4.2.2 for definition).

In order to follow a proportional navigation course, the missile must be able to measure changes in the line of sight. Usually, this is accomplished, among other methods, by a conical scanning method. Here the received signal is amplitude modulated as a function of the angular position of the target from the antenna boresight reference. Scan information is retained throughout the mixing process in the missile circuits. It is extracted in the missile speedgate and coupled back to the front antenna drive as a tracking command. In the head control, the error command (ε), derived from the percentage of modulation, is summed with the output of the head gyro feedback circuit to establish proportionality between the error and the head rate. Under steady-state conditions,

$$\varepsilon = \tau_ {1} \left(\frac {d \lambda}{d t}\right),$$
