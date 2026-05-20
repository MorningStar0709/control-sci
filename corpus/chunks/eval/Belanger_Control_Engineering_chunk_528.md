T_s
</details>

Figure 9.5 Symbolic representation of the sampling operation

Fourier series for the pulse train $p(t)$ as follows: $^{1}$

$$p (t) = \sum_ {n = - \infty} ^ {\infty} a _ {n} e ^ {j n \omega_ {0} t} \tag {9.3}a _ {n} = \frac {1}{T _ {s}} \int_ {- T _ {s} / 2} ^ {T _ {s} / 2} u _ {0} (t) e ^ {- j n \omega_ {0} t} d t = \frac {1}{T _ {s}} \tag {9.4}$$

where $\omega_0 = 2\pi / T_s$ .

Recall that the spectrum of $e^{j\Omega t}$ is $u_{0}(\omega - \Omega)$ , an impulse in the frequency domain. It follows that the Fourier transform $p(j\omega)$ is

$$p (j \omega) = \frac {1}{T _ {s}} \sum_ {n = - \infty} ^ {\infty} u _ {0} (j \omega - j n \omega_ {0}). \tag {9.5}$$
