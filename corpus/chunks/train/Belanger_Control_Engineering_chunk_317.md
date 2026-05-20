# Solution

Figure 6.10 (MATLAB bode, nichols), shows the gain-phase locus and the Nichols chart. By inspection, the peak of $|T(j\omega)|$ is approximately 4.5 db and occurs at about $\omega = 1.2$ rad/s. From the gain-phase locus of $L^{-1}(j\omega)$ , we infer that $|S(j\omega)|$ has a peak of approximately 6.3 db at a frequency of 1.3 rad/s. Note that setting an upper limit on $|S|$ or $|T|$ is tantamount to surrounding the critical point $(-1, 0)(-180^{\circ}, 0 \text{ db in the gain-phase plane})$ by “forbidden regions” inside which L (or $L^{-1}$ ) may not be.

![](image/b6f91148157df5299d8233452b453bda31b0f0928e21dfe9b024d9f997e84cf5.jpg)

<details>
<summary>line</summary>

| Phase (deg) | Magnitude (dB) for L(jω) | Magnitude (dB) for E^(-1)(jω) |
| --- | --- | --- |
| -350 | -40 | -10 |
| -300 | -20 | -8 |
| -250 | 0 | -6 |
| -200 | 20 | -4 |
| -150 | 40 | -2 |
| -100 | 60 | 0 |
| -50 | 80 | 2 |
| 0 | 100 | 4 |
</details>

Figure 6.10 Gain-phase plot and Nichols chart

It is possible to design a pure-gain control system for a given maximum value of $|T(j\omega)|$ or $|S(j\omega)|$ by using the gain-phase plane. Adding k db of gain slides the whole locus of $L(j\omega)$ up by k db and the locus of $L^{-1}(j\omega)$ down by the same amount. It is usually not difficult to see how many decibels should be added or taken away in order for the locus of L or $L^{-1}$ to just graze the M-contour corresponding to the desired peak value.
