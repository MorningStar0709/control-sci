$$
\begin{array}{l} \omega_ {g} = \text { glint   half - power   frequency }, \\ \Omega = \text { rotation   rate   of   target }, \\ S = \text {   target   characteristic   length   (or   span) }, \\ \lambda = \text { radar   wavelength }. \\ \end{array}
$$

The variance of the glint error is given by the integral of the spectral density (3.87d). Thus,

$$\sigma_ {g} ^ {2} = \int \Phi_ {g} (\omega) d \omega ,$$

which yields, after defining $z = \omega / \omega _ { g }$ and $d z = d \omega / \omega _ { g }$

$$\sigma_ {g} ^ {2} = \int d z / (1 + z ^ {2}) = \pi \Phi_ {0} \omega_ {g}. \tag {3.87e}$$

A frequency analysis of the time record of glint from an aircraft target often suggests that its spectrum approximates white noise passed through a first-order lag of the form [3]

$$\Phi_ {g} = (K _ {g} ^ {2}) / (1 + \omega_ {g} ^ {2} T _ {g} ^ {2}) \quad \text { in units of m } ^ {2} / \text { rad / sec }, \tag {3.87f}$$

where $T _ { g }$ is the guidance time constant (typically in the range 0.1 to 0.25 sec), and $L _ { g } ^ { 2 }$ is the mean-square value of the glint and is given by $L _ { g } ^ { 2 } = \pi K _ { g } ^ { 2 } / 2 T _ { g }$ (if $T _ { g }$ and $L _ { g }$ are known approximately, then $K _ { g } ^ { 2 }$ can be evaluated).

Range-Independent Noise (RIN): This noise, also known as fading noise, has a constant angular amplitude, and is caused by amplitude fluctuations of the target occurring at the information frequency in the missile receiver, for example, at the conical scan frequency of a conical scanning missile seeker. Range-independent noise $\sigma _ { f }$ is inherent in the missile receiver. The noise can be modeled as $\sigma _ { f } \approx N ( 0 , r _ { f } )$ , that is, zero mean and variance, with equivalent white noise power spectral density  given by

$$\Phi = 2 \tau_ {f} r _ {f}$$

where $\tau _ { f }$ is the correlation time constant and $r _ { f }$ is the variance. Also, RIN may be caused by the seeker servo system. (Another type of noise commonly encountered in connection with a missile radar seeker noise is range-dependent noise. However, this is strictly a ground-tracking radar noise, used in command guidance systems.)
