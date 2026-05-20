![](image/c7623d1d42eae055726e2396ba4dd190ba824e71256a23d7315f76145da96312.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Phase, deg |
| --- | --- |
| 0.1 | 0 |
| 1 | -25 |
| 10 | -60 |
| 100 | -90 |
</details>

Figure 9.17 Bode diagrams of first-order system $K / ( 0 . 2 s + 1 )$ .

$$K = 1 0: \quad | G (j 0) | _ {\mathrm{dB}} = 2 0 \log_ {1 0} (1 0) = 2 0 \mathrm{dB}K = 1: \qquad | G (j 0) | _ {\mathrm{dB}} = 2 0 \log_ {1 0} (1) = 0 \mathrm{dB}K = 0. 2 5: | G (j 0) | _ {\mathrm{dB}} = 2 0 \log_ {1 0} (0. 2 5) = - 1 2. 0 4 \mathrm{dB}$$

These values match the low-frequency asymptotes shown in Fig. 9.17. It is important for the reader to keep in mind that for a first-order system, a 0-dB low-frequency asymptote corresponds to a transfer function with a unity DC gain. If the low-frequency asymptote exhibits a negative decibel value, then the DC gain is less than one. In summary, varying the DC gain K will shift the magnitude plot up or down from the 0-dB line by $2 0 \mathrm { l o g } _ { 1 0 } ( K )$ decibels but will have no effect on the phase plot. For a first-order system the phase angle $\phi$ always begins at $0 ^ { \circ }$ at low frequencies and asymptotically approaches $- 9 0 ^ { \circ }$ at very high frequencies.

Next, consider the “standard form” first-order transfer function (9.49) with a unity DC gain $( K = 1 )$ and different time constants. Figure 9.18 shows the Bode diagrams for transfer function (9.49) with $K = 1$ and three time constants ??. Clearly, all three magnitude plots have the same 0-dB low-frequency asymptote because the DC gain is fixed at $K = 1$ . Changing the time constant ?? changes the corner frequency $( \omega _ { c } = 1 / \tau$ rad/s) where the low- and high-frequency asymptotes intersect. The three corner frequencies on Fig. 9.18 are

![](image/79237ab3efda8b91e11392416d878691d2ad09131339c08820a1f581fb8c90ac.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | τ = 1 s (ωc = 1 rad/s) | τ = 0.2 s (ωc = 5 rad/s) | τ = 0.05 s (ωc = 20 rad/s) |
| --- | --- | --- | --- |
| 0.01 | 0 | 0 | 0 |
| 0.1 | -5 | -10 | -15 |
| 1 | -15 | -25 | -30 |
| 10 | -30 | -40 | -45 |
| 100 | -45 | -55 | -60 |
| 1000 | -60 | -70 | -75 |
</details>

![](image/fb2c5f01e44e56f73675337b8b6fa6a0890c11c1305f2061dd0585e544eb03f5.jpg)

<details>
<summary>line</summary>
