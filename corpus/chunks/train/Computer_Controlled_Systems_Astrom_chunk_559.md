# Nonlinear Analysis Using Describing Functions

If there is only one nonlinearity in the loop, it is possible to use the method of describing function to determine limit cycles approximately.

Consider the system in Fig. 9.11(a). The method of describing function can be regarded as a generalization of the Nyquist criterion. The critical point -1 is replaced by $-1/Y_{c}(A)$ , where $Y_{c}(A)$ is the describing function of the nonlinearity. The describing function characterizes the transmission of a sinusoidal signal with amplitude A through the nonlinearity. The method predicts a limit cycle if

$$H (e ^ {i \omega h}) = - \frac {1}{Y _ {c} (A)}$$

[compare with Fig. 9.11(b)]. The frequency, $\omega_{1}$ (from the Nyquist curve), and the amplitude, $A_{1}$ (from the describing function), at the intersection are the estimated frequency and the estimated amplitude of the limit cycle. The describing function of a roundoff quantizer is

$$
Y _ {c} (A) = \left\{ \begin{array}{l l} 0 & 0 <   A <   \frac {\delta}{2} \\ \frac {4 \delta}{\pi A} \sum_ {i = 1} ^ {n} \sqrt {1 - \left(\frac {2 i - 1}{2 A} \delta\right) ^ {2}} & \frac {2 n - 1}{2} \delta <   A <   \frac {2 n + 1}{2} \delta \end{array} \right.
$$

The function $Y_{c}$ only takes real values. Its smallest value is zero and its largest value is $4/\pi \approx 1.27$ . The function is graphed in Fig. 9.12. This means that the critical part for quantization consists of the part of the negative real axis from $-\infty$ to -0.78. Describing function analysis thus predicts oscillations due to quantization if the Nyquist curve of the loop gain intersects this line segment. For stable systems this means that quantization will not give rise to oscillations if the amplitude margin is larger than 1.27. Describing function analysis predicts oscillations for all systems that are open-loop unstable.

![](image/28749521f0066fe13fbe9dd872adaab2285b6b6c86ea3c574d9cf4ae257835fc.jpg)

<details>
<summary>line</summary>

| A/δ | Y_c(A) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.2 |
| 1.0 | 0.8 |
| 1.5 | 1.0 |
| 2.0 | 0.9 |
| 2.5 | 1.0 |
| 3.0 | 0.95 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
| 4.5 | 1.0 |
| 5.0 | 1.0 |
</details>

Figure 9.12 The describing function of roundoff.
