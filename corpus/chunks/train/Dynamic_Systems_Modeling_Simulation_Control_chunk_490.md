# Bode Diagram of First-Order Systems

As previously mentioned, we focus on using the Bode diagram rather than the rules associated with sketching the approximate Bode diagram. Furthermore, MATLAB’s bode command allows us to draw the exact Bode diagram. Therefore, we present examples of the Bode diagram for first-order systems and summarize their characteristics.

To begin, consider the first-order transfer expressed in our “standard form”

$$G (s) = \frac {K}{\tau s + 1} \tag {9.49}$$

where K is the DC gain of the transfer function (i.e., the value of G(s) with s = 0) and ?? is the time constant. Clearly, any first-order transfer function (with a constant numerator term) can be written in the standard form of Eq. (9.49). Let’s first observe how the Bode diagram changes with the DC gain K. Figure 9.17 shows the Bode diagrams for transfer function (9.49) with time constant ?? = 0.2 s and three values of the DC gain K. Clearly, changing the DC gain K shifts the magnitude plot up or down but does not change the phase plot (all three gain settings produce the same phase plot). All magnitude plots begin with a “flat” asymptote for low frequencies followed by a linearly decreasing asymptote at high frequencies. The flat (low frequency) and sloped (high frequency) asymptotes are shown as dashed lines on the magnitude plot for K = 1 and these asymptotes intersect at the frequency ?? = 1∕?? = 5 rad/s. The frequency $\omega _ { c }$ where the low- and high-frequency asymptotes intersect is called the corner or break frequency and is always equal to 1∕?? regardless of the DC gain K. Figure 9.17 shows that the three magnitude plots are identical except for a constant offset along the vertical axis. Recall that the DC gain is computed by evaluating the transfer function with $s = 0 .$ . Therefore, because the sinusoidal transfer function is calculated by setting $s = j \omega$ , the DC gain K corresponds to the magnitude at very low frequencies $( \mathrm { i } . \mathrm { e } . , \omega  0 )$ . Consequently, we can compute the magnitude (in dB) of the low-frequency asymptote for the three cases:

![](image/160b9ab459c6cf66995f97b93f6acfe87e988fd7f8845973e106800d1fc92e9b.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | K = 10 | K = 1 | K = 0.25 |
| --- | --- | --- | --- |
| 0.1 | 20 | 0 | -10 |
| 1 | 18 | -2 | -12 |
| 10 | 10 | -10 | -20 |
| 100 | 0 | -25 | -35 |
</details>
