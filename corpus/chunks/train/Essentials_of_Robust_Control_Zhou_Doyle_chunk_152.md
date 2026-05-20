| normalized frequency | sensitivity function (line 1) | sensitivity function (line 2) | sensitivity function (line 3) | sensitivity function (line 4) | sensitivity function (line 5) | sensitivity function (line 6) | sensitivity function (line 7) | sensitivity function (line 8) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 0.01 | 0.02 | 0.03 | 0.04 | 0.05 | 0.06 | 0.07 | 0.08 |
| 1.0 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 |
| 10.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
</details>

Figure 6.4: Sensitivity function S for $\xi = 0 . 0 5 , 0 . 1 , 0 . 2 , 0 . 5 , 0 . 8$ , and 1 with normalized frequency $\left( \omega / \omega _ { n } \right)$

The frequency response of the sensitivity function S is shown in Figure $6 . 4$ . Note that $| S ( j \omega _ { n } / \sqrt { 2 } ) | = 1$ . We can regard the closed-loop bandwidth $\omega _ { b } \approx \omega _ { n } / \sqrt { 2 }$ , since beyond this frequency the closed-loop system will not be able to track the reference and the disturbance will actually be amplified.

Next, note that

$$M _ {s} := \| S \| _ {\infty} = | S (j \omega_ {\mathrm{max}}) | = \frac {\alpha \sqrt {\alpha^ {2} + 4 \xi^ {2}}}{\sqrt {(1 - \alpha^ {2}) ^ {2} + 4 \xi^ {2} \alpha^ {2}}}$$

where $\alpha = \sqrt { 0 . 5 + 0 . 5 \sqrt { 1 + 8 \xi ^ { 2 } } }$ and $\omega _ { \mathrm { m a x } } = \alpha \omega _ { n }$ . For example, $M _ { s } = 5 . 1 2 3$ when $\xi = 0 . 1$ . The relationship between $\xi$ and $M _ { s }$ is shown in Figure 6.5. It is clear that the overshoot can be excessive if $M _ { s }$ is large. Hence a good control design should not have a very large $M _ { s }$ .

Now suppose we are given the time domain performance specifications then we can determine the corresponding requirements in frequency domain in terms of the bandwidth $\omega _ { b }$ and the peak sensitivity $M _ { s }$ . Hence a good control design should result in a sensitivity function $S$ satisfying both the bandwidth $\omega _ { b }$ and the peak sensitivity $M _ { s }$ requirements, as shown in Figure 6.6. These requirements can be approximately represented as

$$| S (s) | \leq \left| \frac {s}{s / M _ {s} + \omega_ {b}} \right|, s = j \omega , \forall \omega$$

![](image/5524f1eebb36c1d9f6ba96f0df4de09eacd63d85bf864cb6d5b2476ccb9b2e9a.jpg)

<details>
<summary>line</summary>

| damping ratio | peak sensitivity |
| --- | --- |
| 0.1 | 5.0 |
| 0.2 | 3.0 |
| 0.3 | 2.0 |
| 0.4 | 1.7 |
| 0.5 | 1.5 |
| 0.6 | 1.4 |
| 0.7 | 1.3 |
| 0.8 | 1.25 |
| 0.9 | 1.2 |
| 1.0 | 1.15 |
</details>

Figure 6.5: Peak sensitivity $M _ { s }$ versus damping ratio $\xi$
