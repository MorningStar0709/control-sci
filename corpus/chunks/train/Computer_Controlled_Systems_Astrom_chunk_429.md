# Prefiltering

A practical difficulty is that real signals do not have Fourier transforms that vanish outside a given frequency band. The high-frequency components may appear to be low-frequency components due to aliasing. The problem is particularly serious if there are periodic high-frequency components. To avoid the alias problem, it is necessary to filter the analog signals before sampling. This may be done in many different ways.

Table 7.1 Damping $\zeta$ and natural frequency $\omega$ for Butterworth, ITAE (Integral Time Absolute Error), and Bessel filters. The higher-order filters with arbitrary bandwidth $\omega_{E}$ are obtained by cascading filters of the form (7.12).

<table><tr><td rowspan="2">Order</td><td colspan="2">Butterworth</td><td colspan="2">ITAE</td><td colspan="2">Bessel</td></tr><tr><td> $\omega$ </td><td> $\zeta$ </td><td> $\omega$ </td><td> $\zeta$ </td><td> $\omega$ </td><td> $\zeta$ </td></tr><tr><td>2</td><td>1</td><td>0.71</td><td>0.99</td><td>0.71</td><td>1.27</td><td>0.87</td></tr><tr><td>4</td><td>1</td><td>0.38</td><td>1.49</td><td>0.32</td><td>1.60</td><td>0.62</td></tr><tr><td></td><td></td><td>0.92</td><td>0.84</td><td>0.83</td><td>1.43</td><td>0.96</td></tr><tr><td>6</td><td>1</td><td>0.26</td><td>1.51</td><td>0.24</td><td>1.90</td><td>0.49</td></tr><tr><td></td><td></td><td>0.71</td><td>1.13</td><td>0.60</td><td>1.69</td><td>0.82</td></tr><tr><td></td><td></td><td>0.97</td><td>0.92</td><td>0.93</td><td>1.61</td><td>0.98</td></tr></table>

Table 7.2 Approximate time delay $T_{d}$ of Bessel filters of different orders.

<table><tr><td>Order</td><td> $T_{d}$ </td></tr><tr><td>2</td><td> $1.3/\omega_{B}$ </td></tr><tr><td>4</td><td> $2.1/\omega_{B}$ </td></tr><tr><td>6</td><td> $2.7/\omega_{B}$ </td></tr></table>

Practically all analog sensors have some kind of filter, but the filter is seldom chosen for a particular control problem. It is therefore often necessary to modify the filter so that the signals obtained do not have frequencies above the Nyquist frequency.

Sometimes the simplest solution is to introduce an analog filter in front of the sampler. A standard analog circuit for a second-order filter is

$$G _ {f} (s) = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}} \tag {7.11}$$
