# Example 7.9 Frequency response of a sampled-data system

Consider a system composed of a sampler and a zero-order hold, given by (7.27),

followed by a linear system, with the transfer function

$$G (s) = \frac {1}{s + 1}$$

The sampling period is $h = 0.05$ s. The Nyquist frequency is thus $\pi / 0.05 = 62.8$ rad/s. Figure 7.25 shows the Bode diagram of the system. For comparison, the Bode diagram of the transfer function $G$ is also shown in the figure. The curves are very close for frequencies that are much smaller than the Nyquist frequency. The deviations occur first in the phase curve. At $\omega = 0.1\omega_N$ the phase curves differ by about $10^\circ$ . There is no signal transmission at frequencies that are multiples of the sampling frequency $\omega_s$ , because the transfer function of the zero-order hold is zero for these frequencies. The phase curve is also discontinuous at these frequencies. (Compare with Fig. 7.24.) Notice also that there are ambiguities of the transfer function at frequencies that are multiples of the Nyquist frequency that are not shown in Fig. 7.25. The value of $\omega_N$ is indicated by a vertical dashed line in Fig. 7.25.

The interpretation of the Bode diagram requires some care because of the modulation introduced by the sampling. If a sine wave of frequency $\omega$ is introduced, the output signal is the sum of the outputs of the sine wave and all its aliases.

![](image/6dfc67d905d716a61ed4d32c92cc9d058a09ece5334a1b3d70f6f704b3b98530.jpg)  
Figure 7.25 Bode diagrams for a zero-order sample-and-hold circuit followed by a first-order lag (solid). The sampling period is 0.05 s. The dashed line is the frequency curve for the continuous-time first-order lag. The vertical dotted lines indicate the frequencies $\omega = 5, 60$ , and 130 rad/s, respectively. The vertical dashed line indicates the Nyquist frequency.

![](image/1f2c03faa78a2ca57a4e578dca90cae1719190b811e3d11f3a687c269d7268f8.jpg)  
Figure 7.26 Steady-state responses to sinusoids with different frequencies for a zero-order hold followed by a first-order system with a unit time constant. The sampling period is 0.05 s. The frequencies are 5 rad/s in (a), 60 rad/s in (b), and 130 rad/s in (c). They are indicated by dotted lines in Fig. 7.25.
