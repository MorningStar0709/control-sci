# EXAMPLE 7–25

Determine the transfer function of the system whose experimental frequency-response curves are as shown in Figure 7–88.

The first step in determining the transfer function is to approximate the log-magnitude curve by asymptotes with slopes ;20 dBdecade and multiples thereof, as shown in Figure 7–88. We then estimate the corner frequencies. For the system shown in Figure 7–88, the following form of the transfer function is estimated:

$$G (j \omega) = \frac {K (1 + 0 . 5 j \omega)}{j \omega (1 + j \omega) \left[ 1 + 2 \zeta \left(j \frac {\omega}{8}\right) + \left(j \frac {\omega}{8}\right) ^ {2} \right]}$$

The value of the damping ratio z is estimated by examining the peak resonance near v=6 radsec. Referring to Figure 7–9, z is determined to be 0.5.The gain K is numerically equal to the frequency at the intersection of the extension of the low-frequency asymptote that has 20 dB/decade slope and the 0-dB line.The value of K is thus found to be 10.Therefore, G(jv) is tentatively determined as

$$G (j \omega) = \frac {1 0 (1 + 0 . 5 j \omega)}{j \omega (1 + j \omega) \left[ 1 + \left(j \frac {\omega}{8}\right) + \left(j \frac {\omega}{8}\right) ^ {2} \right]}$$

or

$$G (s) = \frac {3 2 0 (s + 2)}{s (s + 1) \left(s ^ {2} + 8 s + 6 4\right)}$$

![](image/8b4e5febde9270ff917092aafc23a8436f3c9062b1f35306a80e9c781eebbef3.jpg)

<details>
<summary>line</summary>

| ω in rad/sec | Magnitude (asymptotic) (dB) | Magnitude (experimental) (dB) | √G (°) | Phase angle (experimental) (°) |
| --- | --- | --- | --- | --- |
| 0.1 | 40 | -20 | -100 | -500 |
| 0.2 | 30 | -20 | -100 | -500 |
| 0.4 | 20 | -20 | -100 | -500 |
| 0.6 | 10 | -20 | -100 | -500 |
| 1 | 0 | -20 | -100 | -500 |
| 2 | -10 | -25 | -150 | -500 |
| 4 | -20 | -35 | -200 | -500 |
| 6 | -30 | -45 | -250 | -500 |
| 10 | -40 | -60 | -300 | -500 |
| 20 | -60 | -80 | -350 | -500 |
| 40 | -80 | -100 | -400 | -500 |
</details>

Figure 7–88 Bode diagram of a system. (Solid curves are experimentally obtained curves.)

This transfer function is tentative because we have not examined the phase-angle curve yet.
