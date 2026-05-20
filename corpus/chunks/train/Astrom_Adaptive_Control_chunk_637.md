# Sampling and Pre- and Postfiltering

The choice of sampling rate is an important issue in digital control. The sampling rate influences many properties of a system such as following of command signals, rejection of load disturbances and measurement noise, and sensitivity to unmodeled dynamics. Selection of sampling rates is thus an essential design issue.

One rule of thumb that is useful for deterministic design methods is to let the sampling interval h be chosen such that

$$\omega_ {o} h \approx 0. 2 - 0. 6$$

where $\omega_{o}$ is the natural frequency of the dominating poles of the closed-loop system. This corresponds to 12–60 samples per undamped natural period. The sampling frequency is $\omega_{s}=2\pi/h$ .

In all digital systems it is important that signals are filtered before they are sampled. All components of the signal with frequencies above the Nyquist frequency, $\omega_{N} = \omega_{s}/2 = \pi/h$ should be eliminated. If this is not done, a signal component with frequencies $\omega > \omega_{N}$ will appear as low-frequency components with the frequency

$$\omega_ {a} = \left| \left(\left(\omega + \omega_ {N}\right) \bmod \omega_ {\mathrm{s}}\right) - \omega_ {N} \right|$$

This phenomenon is called aliasing, and the prefilters introduced before a sampler are called anti-aliasing filters. Suitable choices of anti-aliasing filters are second- or fourth-order Butterworth, ITAE (integral time absolute error), or Bessel filters. They consist of one or several cascaded filters of the form

Table 11.1 Damping and natural frequency of second-, fourth-, and sixth-order Butterworth, ITAE, and Bessel filters. The filters have the bandwidth $\omega_{B}$ .
