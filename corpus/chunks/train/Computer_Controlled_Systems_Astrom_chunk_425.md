# 7.4 Aliasing or Frequency Folding

If a continuous-time signal that has the Fourier transform $F$ is sampled periodically, it follows from (7.4) and (7.5) that the sampled signal $f(kh), k = \ldots, -1, 0, 1, \ldots$ can be interpreted as the Fourier coefficients of the function $F_s$ , defined by (7.3).

The function $F_{s}$ can thus be interpreted as the Fourier transform of the sampled signal. The function of (7.3) is periodic with a period equal to the sampling frequency $\omega_{s}$ . If the continuous-time signal has no frequency components higher than the Nyquist frequency, the Fourier transform is simply a periodic repetition of the Fourier transform of the continuous-time signal (see Fig. 7.7).

It follows from (7.3) that the value of the Fourier transform of the sampled signal at $\omega$ is the sum of the values of the Fourier transform of the continuous-time signal at the frequencies $\omega + n\omega_s$ . After sampling, it is thus no longer possible to separate the contributions from these frequencies. The frequency $\omega$ can thus be considered to be the alias of $\omega + n\omega_s$ . It is customary to consider only positive frequencies. The frequency $\omega$ is then the alias of $\omega_s - \omega$ , $\omega_s + \omega$ , $2\omega_s - \omega$ , $2\omega_s + \omega, \ldots$ , where $0 \leq \omega < \omega_N$ . After sampling, a frequency thus cannot be distinguished from its aliases. The fundamental alias for a frequency

![](image/c80db777f2aacd18f265458a3540cdb8342b1f82edff958b78ac09227782859d.jpg)  
Figure 7.7 The relationship between the Fourier transform for continuous and sampled signals for different sampling frequencies. For simplicity it has been assumed that the Fourier transform is real.

$\omega_{1} > \omega_{N}$ is given by

$$\omega = \left| \left(\omega_ {1} + \omega_ {N}\right) \bmod \left(\omega_ {s}\right) - \omega_ {N} \right| \tag {7.10}$$

Notice that although sampling is a linear operation, it is not time-invariant. This explains why new frequencies will be created by the sampling. This is discussed further in Sec. 7.7.
