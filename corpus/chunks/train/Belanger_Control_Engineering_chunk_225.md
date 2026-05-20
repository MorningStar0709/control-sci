# Example 4.9

For $P(s) = (-s + 1) / [(-s + 2)(s + 3)]$ (see Example 4.7), calculate the optimal $S(s)$ , given the weight function $W(s) = (0.1\tau s + 1) / (\tau s + 1)$ . The magnitude $|W(j\omega)|$ is shown in Figure 4.24, where it is seen that low frequencies, up to the bandwidth $1 / \tau$ , are given more weight than high frequencies.

Solution The RHP pole gives

$$B _ {p} (s) = \frac {- s + 2}{s + 2}.$$

Since there is one RHP zero, $M = 1$ and $B'(s) = 1$ . From Equation 4.59,

$$
\begin{array}{l} k = \frac {W (1)}{B _ {p} (1)} \\ = \frac {. 1 \tau + 1}{\tau + 1} \frac {3}{1} \\ = 3 \frac {. 1 \tau + 1}{\tau + 1}. \\ \end{array}
$$

![](image/eceea7f49023a4eb1333fdcc22ea57fc7c70739f8b023d392096c229acfc08e6.jpg)

<details>
<summary>line</summary>

| ωT | Magnitude (db) |
| --- | --- |
| 0.01 | 0 |
| 0.1 | -1 |
| 1 | -4 |
| 10 | -16 |
| 100 | -20 |
</details>

Figure 4.24 Frequency weighting function

Using Equation 4.61,

$$S = 3 \frac {. 1 \tau + 1}{\tau + 1} \frac {- s + 2}{s + 2} \frac {\tau s + 1}{. 1 \tau s + 1}.$$

Note that, using Equation 4.62,

$$| S (j \omega) | = 3 \frac {. 1 \tau + 1}{\tau + 1} \sqrt {\frac {\omega^ {2} \tau^ {2} + 1}{. 0 1 \omega^ {2} \tau^ {2} + 1}}.$$

For $\tau \gg 1$ (high bandwidth = 1/ $\tau$ ), $k \approx 3$ . For $\tau \gg 1$ (low bandwidth), $k \approx .3$ . Clearly, the results are better at low frequencies if we do not demand high bandwidth. Figure 4.25 shows magnitude curves for a few values of $\tau$ .

The sensitivity function of Example 4.9 does not satisfy the condition that F be proper. This is not surprising, since that requirement was not imposed on the solution. One way to modify the solution is to define

$$T ^ {\prime} (s) = \frac {T (s)}{(\tau s + 1) ^ {n}} \tag {4.63}$$

where $n$ is such as to ensure that the pole excess of $T'$ is at least as great as that of $P$ , and $\tau$ is a small time constant. In effect, $T'(j\omega) \approx T(j\omega)$ for $\omega \ll 1\tau$ , so

![](image/8994b2dd5968d5818ff4315b366c3a3e05cf044eaade75d8a9967703fa3e66f1.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | τ = .1 | τ = 1 | τ = 10 |
| --- | --- | --- | --- |
| 0.01 | -5 | -5 | -5 |
| 0.1 | 0 | 0 | -2 |
| 1 | 5 | 5 | 5 |
| 10 | 15 | 15 | 15 |
| 100 | 25 | 25 | 25 |
</details>

Figure 4.25 Optimal sensitivity magnitudes for different bandwidths

that $T' \approx T$ at low frequencies. Then

$$S ^ {\prime} (s) = 1 - \frac {T (s)}{(\tau s + 1) ^ {n}}. \tag {4.64}$$

The rest of the design is as before.
