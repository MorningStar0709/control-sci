The plant is $e^{-sT}P(s)$ , and the model is $\frac{(-T / 2)s + 1}{(T / 2)s + 1} P(s)$ . With $\Delta (s)$ as the multiplicative uncertainty, we have

$$[ 1 + \Delta (s) ] \frac {(- T / 2) s + 1}{(T / 2) s + 1} P (s) = e ^ {- s T} P (s)$$

and therefore

$$\Delta (s) = \frac {(T / 2) s + 1}{(- T / 2) s + 1} e ^ {- s T} - 1.$$

The magnitude bound is

$$\ell (j \omega) = \left| \frac {\frac {1}{2} j \omega T + 1}{- \frac {1}{2} j \omega T + 1} e ^ {- j \omega T} - 1 \right|.$$

This was computed and is plotted in Figure 6.36. We see that $\ell(j\omega)$ is less than 1 for $\omega T < 0.614$ . According to the results of Section 5.6, that is the bandwidth limit of a design that uses this Padé approximation.

![](image/4b806f22d5dfc95e2b2361e3bfffd736c40e91bbca1f480f4f4ac41e3507226b.jpg)

<details>
<summary>line</summary>

| ωT | Value |
| --- | --- |
| 0.2 | 0.05 |
| 0.4 | 0.3 |
| 0.6 | 0.9 |
| 0.8 | 1.8 |
| 1.0 | 1.8 |
| 1.2 | 0.1 |
| 1.4 | 1.9 |
| 1.6 | 0.35 |
</details>

Figure 6.36 The Padé approximation as a multiplicative uncertainty
