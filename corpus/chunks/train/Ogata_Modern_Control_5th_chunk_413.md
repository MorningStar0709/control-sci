![](image/2b15de224a9f124d930af17ff7a7857af30a504f108039efcb313d614a24bdb8.jpg)

<details>
<summary>line</summary>

| ω | dB |
| --- | --- |
| 0.1 | 20 |
| 1 | 0 |
| 10 | -20 |
| 100 | -40 |
</details>

![](image/2786ab3f8f5729345e3cc6842404efa818d5fcf5a1044e06af20ad39d6e21dc6.jpg)

<details>
<summary>line</summary>

| ω | dB |
| --- | --- |
| 0.1 | -20 |
| 1 | 0 |
| 10 | 20 |
| 100 | 40 |
</details>

![](image/69350977a209d24dec98a410a0ad8b81a4fca9b2dafd4274aa564be5b3538a1e.jpg)

<details>
<summary>line</summary>

| ω | φ |
| --- | --- |
| 0.1 | -90° |
| 1 | -90° |
| 10 | -90° |
| 100 | -90° |
</details>

Bode diagram of G(jv) = 1/jv

(a)   
![](image/18b073e1d60b129b8efae34f2bb5d7f66ca082eb6697615306d4e8dda6846967.jpg)

<details>
<summary>line</summary>

| ω | φ |
| --- | --- |
| 0.1 | 90° |
| 1 | 90° |
| 10 | 90° |
| 100 | 90° |
</details>

Bode diagram of G(jv) = jv

First-Order Factors $( 1 ~ + ~ j \omega T ) ^ { \mp 1 }$ . The log magnitude of the first-order factor $1 / ( 1 + j \omega T )$ is

$$2 0 \log \left| \frac {1}{1 + j \omega T} \right| = - 2 0 \log \sqrt {1 + \omega^ {2} T ^ {2}} \mathrm{dB}$$

For low frequencies, such that $\omega \ll 1 / T$ , the log magnitude may be approximated by

$$- 2 0 \log \sqrt {1 + \omega^ {2} T ^ {2}} \div - 2 0 \log 1 = 0 \mathrm{dB}$$

Thus, the log-magnitude curve at low frequencies is the constant 0-dB line. For high frequencies, such that $\omega \gg 1 / T$ ,

$$- 2 0 \log \sqrt {1 + \omega^ {2} T ^ {2}} \doteq - 2 0 \log \omega T \mathrm{dB}$$

This is an approximate expression for the high-frequency range. At $\omega = 1 / T$ , the log magnitude equals 0 dB; at $\omega = 1 0 / T$ , the log magnitude is –20 dB. Thus, the value of –20 log vT dB decreases by 20 dB for every decade of v. For $\omega \gg 1 / T$ , the log-magnitude curve is thus a straight line with a slope of –20 dB/decade (or –6 dB/octave).

Our analysis shows that the logarithmic representation of the frequency-response curve of the factor $1 / ( 1 + j \omega T )$ can be approximated by two straight-line asymptotes, one a straight line at 0 dB for the frequency range $0 < \omega < 1 / T$ and the other a straight line with slope –20 dB/decade (or –6 dBoctave) for the frequency range $1 / T < \omega < \infty .$ . The exact log-magnitude curve, the asymptotes, and the exact phase-angle curve are shown in Figure 7–6.
