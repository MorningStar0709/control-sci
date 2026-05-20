$$M = \frac {1}{\mathrm{e} ^ {1 . 4 4 5 1} h ^ {1 . 0 0 5 6}} \approx \frac {1}{4 . 2 4 h} \approx \frac {1}{4 h}\beta_ {0 1} \approx \frac {1}{h}\beta_ {0 2} = \frac {1}{\mathrm{e} ^ {0 . 4 7 6 2} h ^ {1 . 4 6 7 3}} \approx \frac {1}{1 . 6 h ^ {1 . 5}}\beta_ {0 3} = \frac {1}{\mathrm{e} ^ {2 . 1 5 3 7} h ^ {2 . 2 0 9 3}} \approx \frac {1}{8 . 6 h ^ {2 . 2}}$$

这个近似公式是说当系统的采样步长 h 给定时, 扩张状态观测器(4.7.4)的参数 $\beta_{01}, \beta_{02}, \beta_{03}$ 按上述公式确定, 那么扩张状态观测器(4.7.4)就能较好地估计出加速度不超出 M 范围的系统的状态和加速度.

在上述计算中线性区间 $\delta$ 的取法对扩张状态观测器的参数影响很大, 如 $\delta$ 取大时, 参数 $\beta_{02}, \beta_{13}$ 增大很多, 相反 $\delta$ 取小, $\beta_{02}, \beta_{13}$ 降低很多.

例如，取 $\delta = 5h, \beta_{01} = \frac{1}{h}$ ，扰动幅值 $M = \frac{1}{h}$ 的对象，用扩张状态观测器(4.7.4）进行估计的仿真计算结果列于表4.7.3.

表4.7.3

<table><tr><td>h</td><td>M</td><td> $\beta_{03}$ </td><td> $\beta_{05}$ </td><td>J</td></tr><tr><td>1</td><td>0.2</td><td>0.55</td><td>0.1</td><td>33.31</td></tr><tr><td>0.5</td><td>0.5</td><td>1.6</td><td>0.51</td><td>19.83</td></tr><tr><td>0.25</td><td>1.2</td><td>5.5</td><td>3.2</td><td>11.44</td></tr><tr><td>0.1</td><td>2.5</td><td>31</td><td>41</td><td>5.10</td></tr><tr><td>0.05</td><td>5</td><td>150</td><td>410</td><td>2.22</td></tr><tr><td>0.01</td><td>20</td><td>3600</td><td>55000</td><td>0.44</td></tr><tr><td>0.005</td><td>40</td><td>15000</td><td>460000</td><td>0.21</td></tr><tr><td>0.001</td><td>200</td><td>390000</td><td>58000000</td><td>0.042</td></tr></table>

以 $\lg (h)$ 为自变量，以 $\lg (\beta_{02}),\lg (\beta_{03})$ 为函数值的曲线和用最小二乘法逼近的直线图如图4.7.10所示.

![](image/a0f7bdc2b7dcb5edb0631351f2549c34da8d908e00b1c711bd349a488cda2757.jpg)

<details>
<summary>line</summary>

| X | Y (Solid Line) | Y (Dashed Line) |
| --- | --- | --- |
| -3.5 | 7 | 6 |
| -3 | 6 | 5 |
| -2.5 | 5 | 4 |
| -2 | 4 | 3 |
| -1.5 | 3 | 2 |
| -1 | 2 | 1 |
| -0.5 | 1 | 0 |
| 0 | 0 | -1 |
</details>

图4.7.10

逼近直线给出的公式为

$$
\begin{array}{l} \lg (\beta_ {0 2}) = \lg \left(\frac {1 0 ^ {0 . 0 7 4 1}}{h ^ {1 . 4 6 8 6}}\right), \beta_ {0 2} = \frac {1 . 1 8 6}{h ^ {1 . 4 7}}; \\ \lg (\beta_ {0 3}) = \lg \left(\frac {1}{1 0 ^ {0 . 5 4 8 3} h ^ {2 . 2 0 7 9}}\right), \beta_ {0 3} = \frac {0 . 2 8 3}{h ^ {2 . 2 1}} \\ \end{array}
$$

由上式可得表4.7.4.

表4.7.4
