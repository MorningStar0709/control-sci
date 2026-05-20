# Robustness

The consequences of modeling errors will now be investigated. To do this it is assumed that the real process has the transfer function

$$G ^ {\prime} (s) = \frac {\omega_ {0} ^ {2}}{s ^ {2} + \omega_ {0} ^ {2}} \cdot \frac {k (a _ {d} - s)}{a _ {d} + s}$$

instead of $G(s) = \omega_{0}^{2}/(s^{2} + \omega_{0}^{2})$ . This means that the real system has additional phase lag that has been neglected in the design. Figure 5.22 shows the influence of unmodeled dynamics when $a_{d} = 15$ and 10 and when the nominal controller is used. The figure also shows the sensitivity to gain variations.

The Bode diagram for the loop-transfer function L in the nominal case is shown in Fig. 5.23. The figure shows that the phase margin is reduced when the gain is decreased. This explains the simulations in Fig. 5.22 where the system becomes more oscillatory when the gain is decreased.

![](image/51fb990f2987d5a54f653fac9da42a1b4cf0c7ed5bf8253ecc06c87e289894cb.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 5 | 1 |
| 10 | 1 |
| 15 | 0.8 |
| 20 | 1 |
| 25 | 1 |
| 30 | 1 |
| 35 | 1 |
| 40 | 1 |
</details>

![](image/6adde07010619e0be10530a98d8c7da2302b5bd61140c394dd4e53796f55ca44.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 5 | 1 |
| 10 | ~0.8 |
| 15 | ~0.9 |
| 20 | ~0.7 |
| 25 | ~0.9 |
| 30 | ~0.8 |
| 35 | ~0.9 |
| 40 | ~0.9 |
</details>

![](image/44c91685d238eadd5ac076c2134eb9ec6bfe119ebed80e4fd0561022207b38ab.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0 |
| 5 | 1 |
| 10 | 1 |
| 15 | 0.8 |
| 20 | 1 |
| 25 | 1 |
| 30 | 1 |
| 35 | 1 |
| 40 | 1 |
</details>

![](image/f7fe10d6c0e510c01e28c0d590c324abe0db881598c8976bdbb89f84ed37f985.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0 |
| 5 | 1 |
| 10 | 1 |
| 15 | 0.8 |
| 20 | 1 |
| 25 | 1 |
| 30 | 1 |
| 35 | 1 |
| 40 | 1 |
</details>

Figure 5.22 Responses when using the nominal controller when (a) $a_{d} = 15$ and $k = 1$ , (b) $a_{d} = 25$ and $k = 0.5$ , (c) $a_{d} = 10$ and $k = 1$ , and (d) $a_{d} = 25$ and $k = 1.5$ .

![](image/ea0480869fb96ab44f786c69b56779d5b5dc6d34bd78f08938f9ad1fc0c0b6ee.jpg)

<details>
<summary>line</summary>

| x | Gain |
| --- | --- |
| 0.01 | 100 |
| 0.1 | 50 |
| 1 | 1000 |
| 10 | 1 |
</details>

![](image/2655077e1db04f7c5bac05ed18128255657d3e32bd98f1c97106e05326e3cdf6.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Phase |
| --- | --- |
| 0.01 | -100 |
| 0.1 | -100 |
| 1 | 0 |
| 10 | -200 |
</details>

Figure 5.23 Bode diagram for the loop-transfer function L for the nominal process for the harmonic oscillator.
