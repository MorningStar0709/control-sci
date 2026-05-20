# 5.5.6 Counting Encirclements

It is sometimes tricky to count encirclements, especially if only the positive-frequency half of the Nyquist plot is given, as is the case with most software packages. The following procedure is proposed. We count the net number of real-axis crossings to the left of the point $(- \frac{1}{k}, 0)$ , with clockwise (decreasing phase) crossings being positive. The number of encirclements must equal the net number of crossings, because the Nyquist locus is a closed contour. (The procedure presented here is given more ample justification in Vidyasagar et al. [7].)

Figure 5.23 shows a positive-frequency Nyquist plot, with parts of the negative-frequency portion indicated with dashed lines. We see that (i) a real-axis crossing of the positive-frequency portion for $\omega_0$ , $0 < \omega_0 < \infty$ , actually corresponds to two crossings of the complete locus, and (ii) the real-axis points at $\omega = 0$ and $\omega = \infty$ contribute one crossing of the complete locus. This leads to a simple rule: to obtain $N$ , count algebraically (positive for clockwise) the real-axis crossings left of $(- \frac{1}{k}, 0)$ —once if $\omega = 0$ or $\infty$ or twice if $0 < \omega < \infty$ . In Figure 5.23, $N = 0$ for $(- \frac{1}{k}, 0)$ in region A, $-1$ for $(- \frac{1}{k}, 0)$ in region B, and $1 (= 2 - 1)$ for $(- \frac{1}{k}, 0)$ in region C.

![](image/5f224da850f1f2eef941afd87f9865bb9b035e824bbfd2434868ee273befb6e4.jpg)

<details>
<summary>text_image</summary>

A
ω = 0
B
ω = ω₀
C
ω = ∞
</details>

Figure 5.23 Counting encirclements from the positive frequency portion of the Nyquist plot

Quite often, the frequency response is presented as Bode plots rather than Nyquist plots. Since only the real-axis crossings are considered, it is relatively simple to obtain the necessary information from Bode plots. Bode plots offer the advantage of logarithmic scales, avoiding the scaling problems that are frequently present in Nyquist plots.
