# Example 1.5 Creation of higher frequencies by sampling

Figure 1.12 shows what can happen when a sinusoidal signal of frequency 4.9 Hz is applied to the system in Example 1.1, which has a sampling period of 10 Hz. It follows from Eq. (1.6) that a signal component with frequency 5.1 Hz is created by sampling. This signal interacts with the original signal with frequency 4.9 Hz to give the beating of 0.1 Hz shown in the figure.

![](image/a64d84da135c8cde9b6d013deda5c9e72e1a24587c845cdfc405940cc2ce0fbb.jpg)  
Figure 1.12 Sinusoidal excitation of the sampled system in Example 1.5. (a) Input sinusoidal with frequency 4.9 Hz. (b) Sampled-system output. The sampling period is 0.1 s. (c) Output of the corresponding continuous-time system.

There are many aspects of sampled systems that indeed can be understood by linear time-invariant theory. The examples given indicate, however, that the sampled systems cannot be fully understood within that framework. It is thus useful to have other tools for analysis.

The phenomenon that the sampling process creates new frequency components is called aliasing. A consequence of Eq. (1.6) is that there will be low-frequency components created whenever the sampled signal contains frequencies that are larger than half the sampling frequency. The frequency $\omega_{N} = \omega_{s}/2$ is called the Nyquist frequency and is an important parameter of a sampled system.
