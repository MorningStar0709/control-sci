# Bode Diagram of Second-Order Systems

Next, we present examples of the Bode diagram for underdamped second-order systems and summarize their characteristics. To begin, consider the second-order transfer expressed in our “standard form”

$$G (s) = \frac {K \omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}} \tag {9.50}$$

where $\zeta$ and $\omega _ { n }$ are the damping ratio and undamped natural frequency, respectively. The numerator of $G ( s )$ is a constant that is expressed in a form so that K is the DC gain of the transfer function (i.e., the value of $G ( s )$ with $s = 0 )$ . For now, let’s set the DC gain to unity $( K = 1 )$ and the damping ratio and undamped natural frequency to $\zeta = 0 . 2$ and $\omega _ { n } = 1 0$ rad/s, respectively. With these values Eq. (9.50) becomes

$$G (s) = \frac {1 0 0}{s ^ {2} + 4 s + 1 0 0} \tag {9.51}$$

![](image/c266887c0dbbe6fbc94201618b1c9368aef63c9d8ec399d42f4759ef48497206.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude, dB (Solid Line) | Magnitude, dB (Dashed Line) |
| --- | --- | --- |
| 1 | 0 | 0 |
| 10 | 8 | 0 |
| 100 | -40 | -20 |
</details>

![](image/16fda0238565388ae28db096a7a37cd3183840b1957592e07d6db127472f0de9.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Phase, deg |
| --- | --- |
| 1 | 0 |
| 10 | -90 |
| 100 | -180 |
</details>

Figure 9.24 Bode diagram of second-order system $1 0 0 / ( s ^ { 2 } + 4 s + 1 0 0 )$ .
