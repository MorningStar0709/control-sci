<table><tr><td>h</td><td>1.0</td><td>0.5</td><td>0.25</td><td>0.1</td><td>0.05</td><td>0.02</td><td>0.01</td><td>0.005</td><td>0.0025</td><td>0.001</td><td>0.0005</td></tr><tr><td> $\beta_{\alpha2}$ </td><td>1.2</td><td>3.2</td><td>10</td><td>30</td><td>85</td><td>350</td><td>1300</td><td>2700</td><td>6800</td><td>36000</td><td>80000</td></tr><tr><td> $\beta_{\alpha3}$ </td><td>0.3</td><td>1.3</td><td>7</td><td>38</td><td>180</td><td>1500</td><td>10000</td><td>33000</td><td>120000</td><td>1600000</td><td>5000000</td></tr></table>

如果把扩张状态观测器方程(4.7.4)变成线性扩张状态观测器

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} z _ {1}}{\mathrm{d} t} = z _ {2} - \beta_ {0 1} e \\ \frac {\mathrm{d} z _ {2}}{\mathrm{d} t} = z _ {3} - \beta_ {0 2} e + b u \\ \frac {\mathrm{d} z _ {3}}{\mathrm{d} t} = - \beta_ {0 3} e \end{array} \right. \tag {4.7.5}
$$

那么和上述同样的方法优化出如表4.7.5所示.

表4.7.5

<table><tr><td>h</td><td>M</td><td> $\beta_{02}$ </td><td> $\beta_{03}$ </td><td>J</td></tr><tr><td>0.5</td><td>0.5</td><td>1.6</td><td>0.5</td><td>6.66</td></tr><tr><td>0.25</td><td>1.0</td><td>6.4</td><td>3.9</td><td>3.37</td></tr><tr><td>0.1</td><td>2.3</td><td>39</td><td>59.2</td><td>1.37</td></tr><tr><td>0.05</td><td>4.6</td><td>153</td><td>462</td><td>0.70</td></tr><tr><td>0.001</td><td>21.7</td><td>3692</td><td>54469</td><td>0.14</td></tr><tr><td>0.005</td><td>42.4</td><td>14530</td><td>424890</td><td>0.072</td></tr><tr><td>0.001</td><td>201.0</td><td>35000</td><td>50090000</td><td>0.015</td></tr></table>

对这些数据画出 $\ln (h)$ 和 $\ln (M),\ln (\beta_{02}),\ln (\beta_{03})$ 之间关系曲线及最小二乘拟合直线示于图4.7.11.

![](image/4ea4a8a29047ce3a2ab4a5c7488ada3268242fe5ad98eb2a2d721ed2b8734b37.jpg)

<details>
<summary>line</summary>

| x | ln(M) | ln(β₀) | ln(β₀₀) |
| --- | --- | --- | --- |
| -7 | 18.0 | 15.0 | 12.0 |
| -6 | 16.0 | 13.0 | 10.0 |
| -5 | 14.0 | 11.0 | 8.0 |
| -4 | 12.0 | 9.0 | 6.0 |
| -3 | 10.0 | 7.0 | 4.0 |
| -2 | 8.0 | 5.0 | 2.0 |
| -1 | 6.0 | 3.0 | 0.0 |
| 0 | 4.0 | 1.0 | -2.0 |
</details>

图4.7.11

最小二乘拟合的数值结果为
