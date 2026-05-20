# Sensitivity to Modeling Errors

The process model has one parameter, the process gain k. Figure 5.14 illustrates the consequences of changing the process gain for the nominal design with k = 1. A gain change of 20% has little effect on the system, but an increase or decrease of a factor of 2.5 is not acceptable. An interesting observation is that the sensitivity to process changes is reduced by using a shorter sampling period. This is illustrated in Fig. 5.15.

Additional insight into the sensitivity to modeling errors is obtained by investigating the loop-transfer function

$$\mathcal {L} = \frac {B S}{A R}$$

![](image/9138d18e7af41efec7bd83f4cac0cdeb540253e4fb2573885c0ceeecd28f65e5.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 10 | 1 |
| 20 | 1.2 |
| 30 | 0.9 |
| 40 | 1.0 |
| 50 | 0.8 |
| 60 | 1.1 |
| 70 | 0.9 |
| 80 | 1.0 |
| 90 | 1.0 |
| 100 | 1.0 |
</details>

![](image/dcee896a60721bb0df0d981a2d03cffe624d4314b81afc8642d563f63e47164b.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 25 | 1 |
| 50 | 1 |
| 75 | 1 |
| 100 | 1 |
</details>

![](image/5f460c25fbdc29d47ca691d547dc87c9d41e1b7a0be9728beab4bd176168c204.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0 |
| 50 | 1 |
| 100 | 1 |
</details>

![](image/6781506ed0f46422001458edd26b32c10c8f69e0d7583b989c28209361bbff32.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0 |
| 50 | 1 |
| 100 | 1 |
</details>

Figure 5.14 Outputs of the system with the nominal controller when the process gain is changed. (a) k = 0.4, (b) k = 0.8, (c) k = 1.2, and (d) k = 2.5.

![](image/f7882b00e3d4284785876c6cb1e04548da1d5b96a427f5e5b436ba2b2f8d2bb2.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 50 | 1 |
| 100 | 1 |
</details>

![](image/a83ca81336a782ffd1df2c922c67f2af44e16c3a8801381f7aa38da2f06e6e05.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 50 | 1 |
| 100 | 1 |
</details>

![](image/621149f116b61c5929272a695251f300828697c28382016b8e597cb7f42373cc.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0 |
| 50 | 1 |
| 100 | 1 |
</details>

![](image/2019063e78b2e599ac390ee333e5b43b38954fca7f3cfa243a64bb70610258ff.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0 |
| 50 | 1 |
| 100 | 1 |
</details>
