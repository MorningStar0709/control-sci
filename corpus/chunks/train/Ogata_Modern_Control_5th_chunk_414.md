The frequency at which the two asymptotes meet is called the corner frequency or break frequency. For the factor $1 / ( 1 + j \omega T )$ , the frequency $\omega = 1 / T$ is the corner frequency, since at $\omega = 1 / T$ the two asymptotes have the same value. (The low-frequency asymptotic expression at $\omega = 1 / T$ is 20 log 1 dB=0 dB, and the high-frequency asymptotic expression at $\omega = 1 / T$ is also 20 log 1 $\mathrm { d B } = 0 \mathrm { d B } . )$ The corner frequency divides the frequency-response curve into two regions: a curve for the low-frequency region and a curve for the high-frequency region.The corner frequency is very important in sketching logarithmic frequency-response curves.

Figure 7–6 Log-magnitude curve, together with the asymptotes, and phase-angle curve of $1 / ( 1 + j \omega T )$ .   
![](image/f3e26754229d9fd1def36e53b2e4039cf1201c85efa9d9879113b5e5962001b1.jpg)

<details>
<summary>line</summary>

| ω | Asymptote (dB) | Exact curve (dB) | φ (°) |
| --- | --- | --- | --- |
| 1/20T | 0 | 0 | 0 |
| 1/10T | 0 | 0 | -5 |
| 1/5T | 0 | 0 | -15 |
| 1/2T | -5 | -5 | -35 |
| 1/T | -10 | -10 | -45 |
| 2/T | -15 | -15 | -60 |
| 5/T | -20 | -20 | -75 |
| 10/T | -25 | -25 | -85 |
| 20/T | -30 | -30 | -90 |
</details>

The exact phase angle $\phi$ of the factor $1 / ( 1 + j \omega T )$ is

$$\phi = - \tan^ {- 1} \omega T$$

At zero frequency, the phase angle is $0 ^ { \circ } .$ . At the corner frequency, the phase angle is

$$\phi = - \tan^ {- 1} \frac {T}{T} = - \tan^ {- 1} 1 = - 4 5 ^ {\circ}$$

At infinity, the phase angle becomes –90°. Since the phase angle is given by an inversetangent function, the phase angle is skew symmetric about the inflection point at $\phi = - 4 5 ^ { \circ }$ .

The error in the magnitude curve caused by the use of asymptotes can be calculated. The maximum error occurs at the corner frequency and is approximately equal to –3 dB, since

$$- 2 0 \log \sqrt {1 + 1} + 2 0 \log 1 = - 1 0 \log 2 = - 3. 0 3 \mathrm{dB}$$

The error at the frequency one octave below the corner frequency—that is, at $\omega = 1 / ( 2 T ) -$ is

$$- 2 0 \log \sqrt {\frac {1}{4} + 1} + 2 0 \log 1 = - 2 0 \log \frac {\sqrt {5}}{2} = - 0. 9 7 \mathrm{dB}$$

The error at the frequency one octave above the corner frequency—that is, at $\omega = 2 / T -$ is

$$- 2 0 \log \sqrt {2 ^ {2} + 1} + 2 0 \log 2 = - 2 0 \log \frac {\sqrt {5}}{2} = - 0. 9 7 \mathrm{dB}$$
