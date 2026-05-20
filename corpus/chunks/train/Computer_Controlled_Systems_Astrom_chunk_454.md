1/h. The signal also has components corresponding to the sidebands $k\omega_{s} \pm \omega$ . The frequency content of the output $u^{*}$ of the sampler is shown in Fig. 7.21. The output signal y is obtained by linear filtering of the signal $u^{*}$ with a system having the transfer function $F(s)$ . The output thus has components with the fundamental frequency $\omega$ and the sidebands $k\omega_{s} \pm \omega$ .

For $\omega \neq k\omega_{N}$ , where $\omega_{N}$ is the Nyquist frequency, the fundamental component of the output is

$$y (t) = \frac {1}{h} \operatorname{Im} \left(F (i \omega) e ^ {t (\omega t + \varphi)}\right)$$

For $\omega = k\omega_{N}$ , the frequency of one of the sidebands coincides with the fundamental frequency. Two terms thus contribute to the component with frequency $\omega$ . This component is

$$
\begin{array}{l} y (t) = \frac {1}{\hbar} \operatorname{Im} \left(F (i \omega) e ^ {i (\omega t + \varphi)} - F (i \omega) e ^ {i (\omega t - \varphi)}\right) \\ = \frac {1}{h} \operatorname{Im} \left(\left(1 - e ^ {2 i \varphi}\right) F (i \omega) e ^ {i (\omega t - \varphi)}\right) \\ = \frac {1}{h} \operatorname{Im} \left(2 e ^ {i (\pi / 2 - \varphi)} \sin \varphi F (i \omega) e ^ {i (\omega t + \varphi)}\right) \\ \end{array}
$$

If the input signal is a sine wave with frequency $\omega$ , it is found that the output contains the fundamental frequency $\omega$ and the sidebands $k\omega_{s} \pm \omega, k = 1, 2, \ldots$ (compare with the discussion of aliasing in Sec. 7.4). The transmission of the fundamental frequency is characterized by

$$
\hat {F} (i \omega) = \left\{ \begin{array}{l l} \frac {1}{h} F (i \omega) & \quad \omega \neq k \omega_ {N} \\ \frac {2}{h} F (i \omega) e ^ {i (\pi / 2 - \varphi)} \sin \varphi & \quad \omega = k \omega_ {N} \end{array} \right.
$$

For $\omega \neq k\omega_{N}$ , the transmission is simply characterized by a combination of the transfer functions of the sample-and-hold circuit and the system G. The factor 1/h is due to the steady-state gain of the sampler.

![](image/c0e340f7482681f5cdc24000df3ed1877b2af43537cb1db6df5cd296468ac51a.jpg)  
Figure 7.22 Sampling of a sinusoidal signal at a rate that corresponds to the Nyquist frequency. Notice that the amplitude and the phase of the sampled signal depend strongly on how the sine wave is synchronized to the sampling instants.
