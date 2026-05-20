# EXAMPLE 4.9 Predictive control

Consider the process model

$$y (t + 1) + a y (t) = b u (t)$$

The identity of Eq. (4.58) gives

$$q ^ {d} = (q + a) \left(q ^ {d - 1} + f _ {1} q ^ {d - 2} + \dots + f _ {d - 1}\right) + g _ {0}$$

Hence

$$F (q) = q ^ {d - 1} - a q ^ {d - 2} + a ^ {2} q ^ {d - 3} + \dots + (- a) ^ {d - 1}G (q) = (- a) ^ {d}R _ {d} (q) = b F (q)\bar {R} _ {d} (q) = 0$$

and the control law becomes, when $y_{m} = 0$ ,

$$u (t) = - \frac {(- a) ^ {d}}{b (1 - a + \dots + (- a) ^ {d - 1})} y (t) = - \frac {(- a) ^ {d} (1 + a)}{b (1 - (- a) ^ {d})} y (t)$$

The characteristic polynomial of the closed-loop system is

$$P (q) = q + a + \frac {(- a) ^ {d} (1 + a)}{1 - (- a) ^ {d}}$$

which has the pole

$$p _ {d} = - \frac {a + (- a) ^ {d}}{1 - (- a) ^ {d}}$$

If $a \leq 0$ the location of the pole is given by

$$0 \leq p _ {d} < - a \quad | a | \leq 1 \quad (\text { stable open - loop system })0 \leq p _ {d} < 1 \quad | a | > 1 \quad (\text { unstable open - loop system })$$

![](image/99b4b39f6e0a3e5b90878725dfef55f22a5f3cabf042e296cf2c8f13ab62feb1.jpg)

<details>
<summary>line</summary>

| d | a = 0.5 | a = 0.75 | a = 0.9 | a = 1.25 | a = 1.5 |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 5 | ~0.4 | ~0.6 | ~0.8 | ~0.9 | ~1.0 |
| 10 | ~0.4 | ~0.6 | ~0.9 | ~1.0 | ~1.0 |
| 15 | ~0.4 | ~0.6 | ~0.9 | ~1.0 | ~1.0 |
</details>

Figure 4.14 The closed-loop pole $p_{d} = (a^{d} - a)/(a^{d} - 1)$ as function of d for different values of a.

The closed-loop pole for different values of a and d is shown in Fig. 4.14. The example indicates that it can be sufficient to use a prediction horizon of five to ten samples.

It is possible to generalize the result of Example 4.9 to higher-order systems. The conclusion is that the closed-loop response will be slow for slow or unstable systems when the prediction horizon increases. The restriction of Eq. (4.55) is then not very useful.
