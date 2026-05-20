This is not of the form $kL'(s)$ ; it is not possible, as in the SISO case, to plot the locus for $L'(s)$ and count encirclements of the point $(-1 / k, 0)$ . It is necessary to plot different loci for different values of $k$ , each time ascertaining the number of encirclements of the point $(-1, 0)$ .

In this case, it is impossible to put the three Nyquist plots on the same graph because of the widely different scales. Figure 8.4 shows Bode plots for $k = 0.1$ , 1.0, and 10. Here, $P = 0$ . There are no real axis crossings for $k = 0.1$ and $k = 1$ .

![](image/c4370c80cede6f65657541c1118f8c41fecb1746a7dfb8b01e8216e0d11d8f26.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | k = 10 | k = 1 | k = .1 |
| --- | --- | --- | --- |
| 0.1 | 80 | 40 | 10 |
| 1 | 20 | 0 | -20 |
| 10 | 20 | -20 | -40 |
| 100 | 0 | -40 | -60 |
</details>

![](image/a513ca8b9ed7dc795af10a3acfb3cae19e25a132fd606d1c24452e2f63069319.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | k = .1 | k = 1 | k = 10 |
| --- | --- | --- | --- |
| 0.1 | -120 | -180 | -190 |
| 1 | -100 | -140 | -200 |
| 10 | -90 | -95 | -95 |
| 100 | -85 | -90 | -90 |
</details>

Figure 8.4 Determinant bode plots for three values of the gain

but one occurs for k = 10 at a frequency slightly greater than 1 rad/s and at a magnitude clearly greater than 1. Therefore, the system is stable for k = 0.1 and 1, and unstable for k = 10.
