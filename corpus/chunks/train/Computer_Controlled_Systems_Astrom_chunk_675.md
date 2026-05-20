Sometimes the specifications are given in terms of the maximum allowed deviations in the states and the control signals for a given disturbance. One rule of thumb to decide the weights in (11.4) is to choose the diagonal elements as the inverse value of the square of the allowed deviations. Another way is to consider only penalties on the state variables and constraints on the control deviations. If the constraints are quadratic, a method using a Lagrange multiplier gives a criterion such as (11.9).

![](image/a5367b4c2c939f2fe1aa45e1c9cb7352c3c2158418ed97af55c34db740348f74.jpg)

<details>
<summary>line</summary>

| k - 1 | Signal | Estimate |
| --- | --- | --- |
| 0 | Peak | Low |
| 1 | Peak | Mid |
| 2 | Peak | High |
| 3 | Peak | High |
| 4 | Peak | High |
| 5 | Peak | High |
| 6 | Peak | High |
| 7 | Peak | High |
| 8 | Peak | High |
| 9 | Peak | High |
| 10 | Peak | High |
| 11 | Peak | High |
| 12 | Peak | High |
| 13 | Peak | High |
| 14 | Peak | High |
| 15 | Peak | High |
| 16 | Peak | High |
| 17 | Peak | High |
| 18 | Peak | High |
| 19 | Peak | High |
| 20 | Peak | High |
| 21 | Peak | High |
| 22 | Peak | High |
| 23 | Peak | High |
| 24 | Peak | High |
| 25 | Peak | High |
| 26 | Peak | High |
| 27 | Peak | High |
| 28 | Peak | High |
| 29 | Peak | High |
| 30 | Peak | High |
| 31 | Peak | High |
| 32 | Peak | High |
| 33 | Peak | High |
| 34 | Peak | High |
| 35 | Peak | High |
| 36 | Peak | High |
| 37 | Peak | High |
| 38 | Peak | High |
| 39 | Peak | High |
| 40 | Peak | High |
| 41 | Peak | High |
| 42 | Peak | High |
| 43 | Peak | High |
| 44 | Peak | High |
| 45 | Peak | High |
| 46 | Peak | High |
| 47 | Peak | High |
| 48 | Peak | High |
| 49 | Peak | High |
| 50 | Peak | High |
| 51 | Peak | High |
| 52 | Peak | High |
| 53 | Peak | High |
| 54 | Peak | High |
| 55 | Peak | High |
| 56 | Peak | High |
| 57 | Peak | High |
| 58 | Peak | High |
| 59 | Peak | High |
| 60 | Peak | High |
| 61 | Peak | High |
| 62 | Peak | High |
| 63 | Peak | High |
| 64 | Peak | High |
| 65 | Peak | High |
| 66 | Peak | High |
| 67 | Peak | High |
| 68 | Peak | High |
| 69 | Peak | High |
| 70 | Peak | High |
| 71 | Peak | High |
| 72 | Peak | High |
| 73 | Peak | High |
| 74 | Peak | High |
| 75 | Peak | High |
| 76 | Peak | High |
| 77 | Peak | High |
| 78 | Peak | High |
| 79 | Peak | High |
| 80 | Peak | High |
| 81 | Peak | High |
| 82 | Peak | High |
| 83 | Peak | High |
| 84 | Peak | High |
| 85 | Peak | High |
| 86 | Peak | High |
| 87 | Peak | High |
| 88 | Peak | High |
| 89 | Peak | High |
| 90 | Peak | High |
| 91 | Peak | High |
| 92 | Peak | High |
| 93 | Peak | High |
| 94 | Peak | High |
| 95 | Peak | High |
| 96 | Peak | High |
| 97 | Peak | High |
| 98 | Peak | High |
| 99 | Peak | High |
| 100 | Peak | High |
| k-1   (Estimate) - Estimate<chart label: k
</details>

![](image/3399ad77707ea63b7f527ca3b79837c63a54154647d568b6533dae4c60286348.jpg)

![](image/f3cc32f1f7ba82cc8c9f64358a8fe03d70919e3a71a100456ecba0d82f26f1f8.jpg)

<details>
<summary>line</summary>

| k + 1 | Prediction |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 1 |
| 4 | 0 |
| 5 | -1 |
| 6 | -2 |
| 7 | -1 |
| 8 | 0 |
| 9 | 1 |
| 10 | 2 |
| 11 | 1 |
| 12 | 0 |
| 13 | -1 |
| 14 | -2 |
| 15 | -1 |
| 16 | 0 |
| 17 | 1 |
| 18 | 2 |
| 19 | 1 |
| 20 | 0 |
</details>

Figure 11.6 Smoothing, filtering, and prediction.
