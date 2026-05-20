<details>
<summary>scatter</summary>

f=2.4sign(sin(0.05))
| x | y |
| --- | --- |
| 60 | -2 |
| 100 | -2 |
| 140 | -2 |
| 180 | -2 |
| 200 | -2 |
</details>

图4.7.4

![](image/be9cb1745746ab20f5e2506e444a77bdfec2809b28c2e896bcc041c254bb222c.jpg)

图4.7.5  
![](image/8b2f674f559a22c78378725c05f193e4315e98d2f53052851ca4a465f94afe49.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| 10 | 0.36 |
| 15 | 0.37 |
| 20 | 0.36 |
| 25 | 0.38 |
| 30 | 0.39 |
| 35 | 0.40 |
| 40 | 0.42 |
| 45 | 0.44 |
| 50 | 0.46 |
</details>

![](image/f15647ba5eed08190b11ed18c71ede29915d1601816d7fc59f60693780f234db.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 5 | 25 |
| 10 | -40 |
| 15 | 25 |
| 20 | -40 |
The chart displays a step function with parameters h=0.01, β₁₁, 100, β₃₂, 540, β₃₃, M=3200. The function is annotated as f=26sign(ln(0.5c)).
</details>

图4.7.6

![](image/1c2937b6efdd21180e158a63c3ebcbe3ae2a1a76439f98d0c11a066b788d358e.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.18 |
| 20 | 0.18 |
| 40 | 0.18 |
| 60 | 0.22 |
| 80 | 0.24 |
| 100 | 0.26 |
</details>

![](image/975356b7c45553290254b6d049d51f63e29596a7631d5ae86270e199f75d0718.jpg)

<details>
<summary>line</summary>

f=40sign(sin(1.0t))
| x | y |
| --- | --- |
| 0 | 50 |
| 2 | 50 |
| 4 | -50 |
| 6 | 50 |
| 8 | 50 |
| 10 | -50 |
h=0.005,β₀₁=200,β₀₂=1300,β₀₃=12000,M=40.0
</details>

图4.7.7

象的状态和扰动作用是最好的.

我们画出表4.7.2中的 $\ln(h)$ 和 $\ln(M)$ ， $\ln(\beta_{02})$ ， $\ln(\beta_{03})$ 之间的关系曲线几乎都是直线，如图4.7.8所示.

![](image/cc7499157970646d87446944f38f79296ffec34a7f17c1d64a19337d7e3367ee.jpg)

<details>
<summary>line</summary>

| ln(h) | ln(M) | ln(β₀₂) | ln(β₀₃) |
| --- | --- | --- | --- |
| -7 | 15 | 12 | 8 |
| -6 | 12 | 10 | 6 |
| -5 | 10 | 8 | 4 |
| -4 | 8 | 6 | 2 |
| -3 | 6 | 4 | 0 |
| -2 | 4 | 2 | -2 |
| -1 | 2 | 0 | -4 |
| 0 | 0 | -2 | -6 |
</details>

图 4.7.8

对这些曲线作最小二乘拟合得

$\ln(M)$ 的拟合为 $\ln(M) \approx -1.4451 - 1.0056\ln(h)$

$\ln (\beta_{02})$ 的拟合为 $\ln (\beta_{02})\approx -0.4762 - 1.4673\ln (h)$

$\ln (\beta_{03})$ 的拟合为 $\ln (\beta_{03})\approx -2.1537 - 2.2093\ln (h)$

因此有如下近似公式

![](image/19bb25c933eb966eca952a6600e25e02fb22945f4d6c0322520b2cc9cd555643.jpg)

<details>
<summary>line</summary>

| x | ln(M) | ln(β₁₀) | ln(β₁₀) |
| --- | --- | --- | --- |
| -7 | 12.0 | 8.0 | 6.0 |
| -6 | 10.0 | 6.0 | 4.0 |
| -5 | 8.0 | 4.0 | 2.0 |
| -4 | 6.0 | 2.0 | 0.0 |
| -3 | 4.0 | 0.0 | -2.0 |
| -2 | 2.0 | -2.0 | -4.0 |
| -1 | 0.0 | -4.0 | -6.0 |
| 0 | -2.0 | -6.0 | -8.0 |
</details>

图 4.7.9
