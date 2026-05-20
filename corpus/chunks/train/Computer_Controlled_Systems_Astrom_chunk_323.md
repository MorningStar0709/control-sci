# Example 5.9 Influence of the observer polynomial 1

Consider a system with the pulse-transfer function

$$H (z) = \frac {0 . 1}{z - 1}$$

Assume that the desired pulse-transfer function from command to output is given by

$$H _ {m} (z) = \frac {0 . 2}{z - 0 . 8}$$

We have thus $A_{c}(z)=z-0.8$ . The observer polynomial can be chosen as $A_{o}=1$ , which gives the controller

$$u (k) = 2 \left(u _ {c} (k) - y (k)\right)$$

and the desired closed-loop transfer function. The process output is then given by (compare with Fig. 5.3)

$$X (z) = \frac {0 . 2}{z - 0 . 8} U _ {c} (z) + \frac {0 . 1}{z - 0 . 8} V (z) - \frac {0 . 2}{z - 0 . 8} E (z)$$

The Bode diagrams for the transmission of load disturbances and measurement errors are shown in Fig. 5.8. The gain from low-frequency load disturbances is 0.5 and from low-frequency measurement disturbances is 1. High-frequency load and measurement disturbances are well attenuated.

Figure 5.8 shows that the proportional feedback gives a closed-loop system that is sensitive to load disturbances. A less-sensitive system can be obtained by introducing an observer polynomial of higher degree and constraints on the polynomial R, as shown in the next example.

![](image/574362fe729829c76d5f80c5898caa82215abc659d17cbb846664c6b1a70a13e.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Gain (Solid) | Gain (Dashed) | Gain (Dotted) |
| --- | --- | --- | --- |
| 0.01 | ~0.5 | ~0.2 | ~0.05 |
| 0.1 | ~0.7 | ~0.4 | ~0.1 |
| 1 | ~0.3 | ~0.2 | ~0.1 |
| 10 | ~0.1 | ~0.1 | ~0.1 |
</details>

![](image/598cdef402d0241d4abad6f6952b36ddd10dcf77085d341fd663654b5b95030b.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Gain (Solid Line) | Gain (Dashed Line) | Gain (Dotted Line) |
| --- | --- | --- | --- |
| 0.01 | 1.0 | 1.0 | 1.0 |
| 0.1 | ~0.9 | ~0.95 | ~0.98 |
| 1.0 | ~0.3 | ~0.6 | ~0.8 |
| 10.0 | ~0.1 | ~0.2 | ~0.4 |
</details>

Figure 5.9 Bode diagram for the signal transmission from (a) load disturbances and (b) measurement error to process output for the controller in Example 5.10. The observer polynomial has a = 0.99 (solid), a = 0.9 (dashed), a = 0.5 (dashed-dotted), and a = 0 (dotted).
