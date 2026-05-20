The step size increases progressively with each increment of x-value, indicating a step size of approximately half of the step size of f at each point of the step size range shown above the step size axis.
</details>

图4.7.1

步长 h 分别取 0.5, 0.25, 0.1, 0.05, 0.01, 0.005, 0.001 时优化的结果列于表 4.7.2. 相应的优化指标值曲线和加速度跟踪曲线分别如图 4.7.2 \~ 图 4.7.7 所示.

表4.7.2

<table><tr><td>h</td><td>M</td><td> $\beta_{32}$ </td><td> $\beta_{33}$ </td><td>J</td></tr><tr><td>0.5</td><td>0.4</td><td>1.6</td><td>0.5</td><td>16.99</td></tr><tr><td>0.25</td><td>1.4</td><td>5.6</td><td>3.0</td><td>9.47</td></tr><tr><td>0.1</td><td>2.4</td><td>20</td><td>21</td><td>3.53</td></tr><tr><td>0.05</td><td>5.0</td><td>52</td><td>88</td><td>1.67</td></tr><tr><td>0.01</td><td>26.0</td><td>540</td><td>3200</td><td>0.36</td></tr><tr><td>0.005</td><td>40.0</td><td>1300</td><td>12000</td><td>0.18</td></tr><tr><td>0.001</td><td>250.0</td><td>16000</td><td>500000</td><td>0.037</td></tr></table>

![](image/64a17d1b3bd1e4127dfc61207b911cbfa122aa833db3cc4cd872f7fa42699b31.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.1 | 17 |
| 0.2 | 17 |
| 0.3 | 17 |
| 0.4 | 17 |
| 0.5 | 18 |
| 0.6 | 19 |
| 0.7 | 20 |
| 0.8 | 21 |
| 0.9 | 22 |
| 1.0 | 22 |

| n | Value |
| --- | --- |
| 0 | -0.5 |
| 100 | -0.5 |
| 200 | -0.5 |
| 300 | -0.5 |
| 400 | -0.5 |
| 500 | -0.5 |
| 600 | -0.5 |
| 700 | -0.5 |
| 800 | -0.5 |
| 900 | -0.5 |
| 1000 | -0.5 |
</details>

图4.7.2

表4.7.2, 图4.7.2 \~ 图4.7.7 的意思是, 当步长 h 给定, 而扩张状态观测器参数 $\beta_{01} = \frac{1}{h}, \beta_{02}, \beta_{03}$ 取为表4.7.2 中的值时, 用扩张状态观测器(4.7.4) 来估计加速度作用范围不超过 M 的二阶对

![](image/c15ecaed0c78e163e770e3289e3440ff6be550ff722b7d8c3a561e1ca216b5c9.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| 0.5 | 9 |
| 1.0 | 9.2 |
| 1.5 | 9.5 |
| 2.0 | 10.0 |
| 2.5 | 10.8 |
| 3.0 | 12.0 |
</details>

![](image/7deedd7189abdc64b9d4fa7b75253aa5f84d469710f87e96b491ed36959fbfd9.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1.4 |
| 150 | -2.0 |
| 300 | 1.4 |
| 450 | -2.0 |
</details>

图4.7.3  
![](image/8ca8ebe5cfa28f0a41cf6bcb86135e8742e8f943ea03398c42ddde7e26983c58.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 3.5 |
| 0.5 | 3.5 |
| 1.0 | 3.5 |
| 1.5 | 3.5 |
| 2.0 | 3.5 |
| 2.5 | 3.6 |
| 3.0 | 4.0 |
| 3.5 | 4.3 |
| 4.0 | 4.5 |
</details>

![](image/9d3c2419ca89a3d88c43e2caae9195cdf9953bbc8b8f2ca0f485f2b01ca17932.jpg)
