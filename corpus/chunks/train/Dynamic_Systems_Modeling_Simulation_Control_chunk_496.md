![](image/3c5b408ce463cb517f220033589d00e64b209c38140779a528bad33e3b0dc502.jpg)

<details>
<summary>line</summary>

| Time, s | e_S(t) (V) | e_C(t) (V) |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.2 | 2.5 | 2.4 |
| 0.4 | -2.5 | -2.6 |
| 0.6 | 0.0 | 0.0 |
| 0.8 | 2.5 | 2.4 |
| 1.0 | -2.5 | -2.6 |
| 1.2 | 0.0 | 0.0 |
| 1.4 | 2.5 | 2.4 |
</details>

Figure 9.23 Desired input signal $e _ { S } ( t )$ and filtered output signal $e _ { C } ( t )$ (Example 9.7).

filter transfer function shown in Fig. 9.21. Figure 9.23 shows the “clean” input signal $e _ { S } ( t )$ and the output voltage $e _ { C } ( t )$ from the low-pass filter. Clearly, the low-pass filter has performed as intended: the RC circuit has filtered or removed the high-frequency noise $e _ { N } ( t )$ from the input voltage $e _ { \mathrm { i n } } ( t )$ such that the filter output $e _ { C } ( t )$ nearly matches the “clean” 2.4-V input signal $e _ { S } ( t )$ .

In summary, the low-pass filter has “passed” the low-frequency signal $e _ { S } ( t )$ with no attenuation and little phase lag. The filter performance can be quantified using its Bode diagram shown in Fig. 9.20: note that the frequency of the desired signal $e _ { S } ( t ) ( \omega = 1 0 \mathrm { r a d / s ) }$ is well below the filter’s corner frequency $\omega _ { c } = 8 3 . 3 3 ~ \mathrm { r a d / s }$ . Therefore, this low-frequency signal is passed with no change in amplitude because the filter’s DC gain is unity (or, 0 dB). Figure 9.20 also shows that the phase angle is about $- 7 ^ { \circ }$ for a frequency of 10 rad/s and consequently there is very little phase lag between $e _ { C } ( t )$ and $e _ { S } ( t )$ in Fig. 9.23. Finally, the Bode diagram in Fig. 9.20 shows that the magnitude is nearly −20 dB for the high-frequency noise signal (?? = 800 rad/s). As an absolute-value magnitude −20 dB is 0.1, and, therefore, the low-pass filter has reduced the amplitude of the noise component $e _ { N } ( t )$ from 0.2 V to $0 . 2 \times 0 . 1 = 0 . 0 2 \mathrm { V } .$ .
