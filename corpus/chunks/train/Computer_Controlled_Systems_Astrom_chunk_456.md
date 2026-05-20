# The General Case

It is easy to extend the analysis to the general case of the system shown in Fig. 7.1. The corresponding open-loop system is shown in Fig. 7.23.

It consists of an A-D converter, the computer, a D-A converter, and the process. It is assumed that the D-A converter holds the signal constant over a sampling interval. It is also assumed that the calculations performed by the computer can be expressed by the pulse-transfer function $H(z)$ and that the process is described by the transfer function $G(s)$ .

If a sinusoid

$$v (t) = \sin (\omega t + \varphi) = \operatorname{Im} (\exp i (\omega t + \varphi))$$

is applied to the A-D converter, then the computer will generate a sequence of numbers that in steady state can be described by

$$w (k h) = \operatorname{Im} \left(H (e ^ {i \omega h}) e ^ {i (\omega k h + \varphi)}\right) \quad k = \dots - 1, 0, 1, \dots$$

This sequence is applied to the D-A converter. Because the D-A converter holds the signal constant over a sampling period, the output is the same as if the signal w were applied directly to a hold circuit. The discussion of the previous section can thus be applied: The output contains the fundamental component with frequency $\omega$ and sidebands $k\omega_{s} \pm \omega$ . The signal transmission of the fundamental component may be described by the transfer function

$$
K (i \omega) = \left\{ \begin{array}{l l} \frac {1}{h} H (e ^ {i \omega h}) F (i \omega) & \omega \neq k \omega_ {N} \\ \frac {2}{h} H (e ^ {i \omega h}) F (i \omega) e ^ {i (\pi / 2 - \varphi)} \sin \varphi & \omega = k \omega_ {N} \end{array} \right.
$$

where $\omega_{N}$ is the Nyquist frequency and

$$F (s) = \frac {1}{s} \left(1 - e ^ {- s h}\right) G (s)$$

![](image/45e80fe0c4751664abec21ad1a6ce7fc614d3e0bdec56fd0d323638ad34c4714.jpg)

<details>
<summary>line</summary>

| x | Solid Line | Dashed Line |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 5 | 0.0 | 0.5 |
| 10 | 0.3 | 0.2 |
| 15 | 0.1 | 0.1 |
| 20 | 0.0 | 0.0 |
</details>

![](image/2b0c9b45df5f58755baf9644b534c86e8422271415b08e345b2933cd066de04c.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Phase (Solid Line) | Phase (Dashed Line) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | -150 | -100 |
| 10 | -200 | -150 |
| 15 | -150 | -100 |
| 20 | 0 | 0 |
</details>

Figure 7.24 Magnitude and argument curves of the transfer function for first-order-hold (full) and zero-order-hold (dashed) circuits. The Nyquist frequency is $\omega_{N} = \pi$ .
