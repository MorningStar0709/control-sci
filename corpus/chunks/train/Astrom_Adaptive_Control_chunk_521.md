# Classification of Suboptimal Dual Controllers

The problem of turn-off has led to many suggestions of how to derive controllers that are simple but still have some dual features. Some ways are:

![](image/f809493142ab72b217bcc52b68205a4dde9839f755f099288befae4860a30da8.jpg)

<details>
<summary>line</summary>

| Time | y |
| --- | --- |
| 0 | ~5 |
| 100 | ~-5 |
| 200 | ~-5 |
| 300 | ~-5 |
| 400 | ~-5 |
</details>

![](image/283b10a17bb05076b61a47271541e5cc5e67da2dbd8ec9ec374071a725f2f7cd.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | -1.5 |
| 100 | -1.8 |
| 200 | -1.2 |
| 300 | -1.6 |
| 400 | -1.4 |
</details>

![](image/71b9a44ccb964fe517c592cab906c0c6539f51ec44b9f43f4ae0e3f9efdd8e3b.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 200 | u |
</details>

![](image/b7b738952721cce2473019c399a9fb22f8fa80bf5dcc4c60b1d111d939342e0d.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 100 | -2 |
| 200 | -1 |
| 300 | -1 |
| 400 | -1 |
</details>

![](image/30f90ede4684348a73ac2cf6f9734acde56e32b7100bd233759234949c731cad.jpg)

<details>
<summary>line</summary>

| Time | P_b |
| --- | --- |
| 0 | 0 |
| 100 | 1 |
| 200 | 0 |
| 300 | 1 |
| 400 | 0 |
</details>

![](image/79cde08a2c17d08ffc6893095391f008faac0baf751229c71d10a1d63eac579f.jpg)

<details>
<summary>line</summary>

| Time | Σ y² |
| --- | --- |
| 0 | 0 |
| 100 | ~500 |
| 200 | ~1000 |
| 300 | ~1500 |
| 400 | ~2000 |
</details>

Figure 7.4 Representative simulation when an integrator is controlled by using a cautious controller. Turn-off occurs when the control signal is small.

- Adding perturbation signals to the cautious controller,   
- Constraining the variance of the parameter estimates,   
- Extensions of the loss function, and   
- Serial expansion of the loss function.

Some of these modifications are now discussed.
