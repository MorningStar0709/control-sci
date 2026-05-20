<table><tr><td rowspan="2">Order</td><td colspan="2">Butterworth</td><td colspan="2">ITAE</td><td colspan="2">Bessel</td></tr><tr><td> $\omega/\omega_B$ </td><td> $\zeta$ </td><td> $\omega/\omega_B$ </td><td> $\zeta$ </td><td> $\omega/\omega_B$ </td><td> $\zeta$ </td></tr><tr><td>2</td><td>1</td><td>0.71</td><td>1</td><td>0.71</td><td>1.27</td><td>0.87</td></tr><tr><td rowspan="2">4</td><td>1</td><td>0.38</td><td>1.48</td><td>0.32</td><td>1.59</td><td>0.62</td></tr><tr><td>1</td><td>0.92</td><td>0.83</td><td>0.83</td><td>1.42</td><td>0.96</td></tr><tr><td rowspan="3">6</td><td>1</td><td>0.26</td><td>1.30</td><td>0.32</td><td>5.14</td><td>0.49</td></tr><tr><td>1</td><td>0.71</td><td>0.98</td><td>0.60</td><td>4.57</td><td>0.82</td></tr><tr><td>1</td><td>0.97</td><td>0.79</td><td>0.93</td><td>4.34</td><td>0.98</td></tr></table>

$$G _ {f} (s) = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}}$$

Let $\omega_{B}$ be the desired bandwidth of the filter. The damping $\zeta$ and the frequency $\omega$ for filters of different orders are given in Table 11.1. The Bessel filter has the interesting property that its phase curve is approximately linear, which implies that the waveform is also approximately invariant.

The prefilter introduces additional dynamics into the system that have to be taken into account in the control design. The Bessel filter can be approximated with a time delay. Assume that the bandwidth of the filter is chosen to be

$$\left| G _ {a a} (i \omega_ {N}) \right| = \beta$$

where $G_{aa}(s)$ is the transfer function of the filter and $\omega_{N} = \pi/h$ is the Nyquist frequency. Parameter $\beta$ is the attenuation of the filter at the Nyquist frequency. Table 11.2 gives the approximate time delay $T_{d}$ as a function of $\beta$ . The table also gives $\omega_{N}$ as a function of filter bandwidth $\omega_{B}$ . The relative delay increases with attenuation. For reasonable values of the attenuation the delay is more than one sampling period. This means that the dynamics of the filter must be taken into account in the control design. We illustrate this by an example.

Table 11.2 The approximate time delay $T_{d}$ due to the anti-aliasing filter as a function of the desired attenuation $\beta$ at the Nyquist frequency for a fourth-order Bessel filter. h is the sampling period.

<table><tr><td> $\beta$ </td><td> $\omega_{N}/\omega_{B}$ </td><td> $T_{d}/h$ </td></tr><tr><td>0.05</td><td>3.1</td><td>2.1</td></tr><tr><td>0.1</td><td>2.5</td><td>1.7</td></tr><tr><td>0.2</td><td>2.0</td><td>1.3</td></tr><tr><td>0.5</td><td>1.4</td><td>0.9</td></tr><tr><td>0.7</td><td>1.0</td><td>0.7</td></tr></table>
