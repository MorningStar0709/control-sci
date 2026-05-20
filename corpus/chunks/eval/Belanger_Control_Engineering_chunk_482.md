| Frequency (rad/s) | Singular Values dB (Solid Line) | Singular Values dB (Dashed Line) |
| --- | --- | --- |
| 0.1 | -20 | -20 |
| 0.5 | -10 | -15 |
| 1.0 | 0 | -5 |
| 5.0 | 4 | -4 |
| 10.0 | 5 | -4 |
</details>

Figure 8.3 Singular values of the sensitivity

Finally,

$$
T (s) = I - S (s) = \frac {1}{s ^ {3} + 2 . 5 s ^ {2} + 2 s + 1} \left[ \begin{array}{c c} 1. 5 s ^ {2} + s + 1 & -. 5 s ^ {2} \\ s ^ {2} (s + 1) & . 5 s ^ {2} + s + 1 \end{array} \right].
$$

(c) The singular value $\overline{\sigma}[S(j\omega)]$ is computed numerically and is displayed in Figure 8.3. Note that $\overline{\sigma}[S(j\omega)]$ is small where $\underline{\sigma}[L(j\omega)] \gg 1$ , and near 1 where $\overline{\sigma}[L(j\omega)] \ll 1$ .
