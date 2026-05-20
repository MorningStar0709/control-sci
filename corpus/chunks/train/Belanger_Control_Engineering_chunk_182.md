# 4.2.3 Frequency-Domain Specifications

Disturbance and observation-noise signals are usually characterized by their spectra; that is often the case for set-point signals as well. This characterization leads naturally to specifications in the frequency domain.

For the SISO case, Equations 4.5 and 4.6 are

$$y (s) = H _ {d} (s) y _ {d} (s) + H _ {w} (s) w (s) + H _ {v} (s) v (s)e (s) = \left(1 - H _ {d} (s)\right) y _ {d} (s) - H _ {w} (s) w (s) - H _ {v} (s) v (s).$$

For purposes of exposition, suppose $y_{d} = v = 0$ , so that

$$e (s) = - H _ {w} (s) w (s).$$

Assume that $w(t)$ is an "energy" signal, i.e., has a Fourier transform. If $H_w(s)$ is the transfer function of a causal, stable system, then the $j$ -axis lies within the region of convergence of $H_w(s)$ , and $H_w(j\omega)$ is its Fourier transform. By Parseval's theorem,

$$
\begin{array}{l} \int_ {0} ^ {\infty} e ^ {2} (t) d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | H _ {w} (j \omega) w (j \omega) | ^ {2} d w \\ = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | H _ {w} (j \omega) | ^ {2} | w (j \omega) | ^ {2} d \omega . \tag {4.8} \\ \end{array}
$$

The left-hand side (LHS) of Equation 4.8 is the integral-squared error (ISE). It is the energy in the error signal and serves as a measure of signal magnitude. The quantity $|w(j\omega)|^{2}$ is the energy density spectrum of w.

In practice, disturbance signals are usually “power” signals, which do not have Fourier transforms. Many such signals exhibit stationarity, which, roughly speaking, means that their average properties do not change with time. For such signals it is possible to define a power density spectrum, which describes the distribution in frequency of the signal power in exactly the same way as the energy density spectrum describes the distribution of energy. For example, a sinusoid of frequency $\omega_{0}$ is a power signal with a power density spectrum consisting of impulses at $\pm\omega_{0}$ . Stationary random processes also have power density spectra. For power signals, the analog of Equation 4.8 is

$$(e _ {r m s}) ^ {2} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | H _ {w} (j \omega) | ^ {2} \Phi_ {w} (j \omega) d \omega \tag {4.9}$$

where $e_{rms} =$ root-mean-squared value of $e$

$$\Phi_ {w} = \text { power density spectrum of } w \text {(a nonnegative quantity). }$$
