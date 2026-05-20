# A Special Case

When performing the frequency-response test, it is natural to cut the loop on the analog side, for example, at A in Fig. 7.1. To simplify the analysis consider the special case in which the output of the D-A converter is equal to the input of the A-D converter. The action of the computer on the signals can then be described as a sample-and-hold circuit. It follows from Fig. 7.19 that a sample-and-hold circuit can be represented as a sampler followed by a hold circuit. The problem is thus reduced to calculation of the response of a sampler followed by a linear time-invariant system.

Equation (7.25) gives the sampled representation $u^{*}$ of the input signal u. A formal Fourier series representation of a sequence of delta functions gives

$$m (t) = \sum_ {k = - \infty} ^ {\infty} \delta (t - k h) = \frac {1}{h} \left(1 + 2 \sum_ {k = 1} ^ {\infty} \cos k \omega_ {s} t\right)$$

where h is the sampling period, and $\omega_{s}$ is the corresponding sampling frequency in radians per second.

Assume that the input to the system is

$$u (t) = \sin (\omega t + \varphi) = \ln \left(\exp i (\omega t + \varphi)\right)$$

The series expansion of the output $u^{*} = um^{*}$ of the sampler then becomes

$$
\begin{array}{l} u ^ {*} (t) = \frac {1}{h} \left[ \sin (\omega t + \varphi) + 2 \sum_ {k = 1} ^ {\infty} \cos (k \omega_ {s} t) \sin (\omega t + \varphi) \right] \\ = \frac {1}{h} \left[ \sin (\omega t + \varphi) + \sum_ {k = 1} ^ {\infty} \left(\sin (k \omega_ {s} t + \omega t + \varphi) - \sin (k \omega_ {s} t - \omega t - \varphi)\right) \right] \\ \end{array}
$$

The signal $u^{*}$ has a component with the frequency $\omega$ of the input signal. This component is multiplied by 1/h because the steady-state gain of a sampler is

![](image/7aa7cb0948554546c7ea3c05c008eaf9a94d3f3f1890dfe2f2d8b84c15a71842.jpg)

<details>
<summary>line</summary>

| Frequency Shift | Label |
| --- | --- |
| -2ωs | -2ωs |
| -ωg | -ωg |
| -ω | -ω |
| ω | ωs |
| ωs | ωs |
| 2ωs | 2ωs |
| 2ωs+ω | 2ωs+ω |
</details>

Figure 7.21 Frequency content of the sampled input signal $u^{*}$ when $u = \sin(\omega t + \varphi)$ .
