<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 2 | 0.3 |
| 4 | 0.5 |
| 6 | 0.5 |
| 8 | 0.5 |
| 10 | 0.5 |
</details>

图2.6.3  
![](image/e717fd061569c458e98afe14d7ae6faa4ec813d41b0a60b74ef07d2bf3d3a89b.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 2 | 30 |
| 4 | 50 |
| 6 | 50 |
| 8 | 50 |
| 10 | 50 |
</details>

图2.6.4

例 2 对非线性系统

$$\ddot {x} + x + 2 \dot {x} (1 - x ^ {2}) = u$$

建立的逆系统为

$$u = \operatorname{fhan} \left(x _ {1} - v, x _ {2}, r, h\right) + 2 x _ {2} \left(1 - x _ {1} ^ {2}\right) + x _ {1}$$

阶跃信号分别取 u = 0.1, u = 0.9 时原系统的阶跃响应和 v = 0.1, v = 0.9 时的串联系统的阶跃响应的比较结果分别示于图 2.6.5 和图 2.6.6.

![](image/4523b7ef4dd480538364cca1e440488c0b3f86b37983ceddb6316711f1eeb413.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 2 | 0.06 |
| 4 | 0.08 |
| 6 | 0.10 |
| 8 | 0.10 |
| 10 | 0.10 |
</details>

图2.6.5  
![](image/9e033bc5f21c2bce38e177f7d385fe311efe61c84b2cbe18152b659221f293b0.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 2 | 0.6 |
| 4 | 1.0 |
| 6 | 0.8 |
| 8 | 0.7 |
| 10 | 0.9 |
</details>

图2.6.6

从这些仿真结果看,无论是线性对象,还是非线性对象,只要其数学模型已知,就能用跟踪微分器构造出很好的逆系统,或对原系统配置零点系统,使复合系统的传递特性几乎接近于1:1.
