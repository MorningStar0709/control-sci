# Example 9.5 Effects of A-D quantization for the double integrator

Figure 9.15 shows a simulation of digital control of a double integrator where the A-D converter is quantized with the level 0.02. The controller is the same as the one used in Sec. 5.7. It is given by

$$R (q) u (k) = T (q) u _ {c} (k) - S (q) y (k)$$

where

$$R (q) = (q - 1) (q + 0. 1 8 8)S (q) = 0. 7 1 5 q ^ {2} - 1. 2 8 1 q + 0. 5 8 0 \tag {9.14}T (q) = (3. 4 7 3 q ^ {2} - 2. 5 5 5 q + 4. 7 0 0) \cdot 1 0 ^ {- 2}$$

![](image/8b59084204f2352c30d63cbc06bda8755c942b24f89e0799d51d490015049991.jpg)

<details>
<summary>line</summary>

| Real axis | Imaginary axis |
| --- | --- |
| -7.0 | 2.5 |
| -6.0 | 1.5 |
| -4.0 | 0.0 |
| -2.0 | -1.0 |
| 0.0 | 0.0 |
</details>

Figure 9.16 Nyquist curve for the sampled loop gain for the double integrator, when using the controller defined by (9.14).

and the sampling period 1 s. The simulation clearly shows that there is a limit-cycle oscillation where the output changes one quantization level. The period is 28 s. The describing functions analysis predicts a limit cycle with period 39 s. See Fig. 9.16, which shows the Nyquist curve of the sampled loop gain. The describing function method predicts that the amplitude of the oscillation is $\delta/2$ , which agrees well with the behavior of the output of the process. Describing function analysis gives correct qualitative results in this case, but the prediction of the period is poor because the signals deviate significantly from sinusoids.

We will also use another method to estimate the amplitudes of the fluctuations caused by the quantization. To do this, first observe that the output signal oscillates with one quantization level up or down at widely spaced intervals. This means that the controller output is given by the pulse response of the controller, that is,

$$- \frac {S (z)}{R (z)} = - 0. 7 1 0 + 0. 7 0 0 z ^ {- 1} - 0. 1 4 5 z ^ {- 2} + 0. 0 1 3 4 z ^ {- 3} \dots \tag {9.15}$$

multiplied by the quantization level. This gives an excellent prediction of the fluctuations in the control signal. Compare with Fig. 9.15. Notice that the first coefficient in the expansion of -S/R is equal to -s₀.

This example shows that the periodic ripple in the control signal due to quantization in the A-D converter can be estimated from a simple pulse-response calculation. In the next example we will analyze the effect of quantization in the D-A converter.

![](image/bc640d6736e83ae2e04c2965b8c1e1c7ab1c9b8dadca83db397beb8b10f52422.jpg)

<details>
<summary>line</summary>

| Time | Output | Unquantized | Input |
| --- | --- | --- | --- |
| 0 | 0 | 0.04 | 0.03 |
| 50 | 1 | -0.01 | -0.01 |
| 100 | 1 | 0.00 | -0.01 |
| 150 | 1 | 0.00 | -0.01 |
</details>

Figure 9.17 Digital control of the double integrator with a quantized D-A converter.
