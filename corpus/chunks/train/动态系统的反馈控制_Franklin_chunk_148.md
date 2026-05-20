# 例 3.20 用 Matlab 进行变换

求以下微分方程所示系统的传递函数：

$$\ddot {y} + 6 \dot {y} + 2 5 y = 9 u + 3 \dot {u}$$

解答。利用式(3.41)和式(3.42)给出的微分关系式，我们可以得到

![](image/3c8252ff5b95d407c1526975e60aa6b572ae54a7f73758fb892b19f6bf8067af.jpg)

<details>
<summary>line</summary>

| 时间/s | ω/crad/s |
| --- | --- |
| 0 | 0 |
| 0.5 | 1.2 |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
</details>

图3.6 交流电机的暂态响应

$$\frac {Y (s)}{U (s)} = \frac {3 s + 9}{s ^ {2} + 6 s + 2 5}$$

Matlab 语句如下。

numG = [3 9]; % form numerator
denG = [1 6 25]; % form denominator

如果想得到因式分解形式的传递函数，只要变换到 tf 描述即可。因此，Matlab 命令为

% convert from numerator-denominator polynomials to pole-zero form $[z,p,k]=tf2zp(numG,denG)$

结果为 $z = [-3]$ ， $p = [-3 + 4j - 3 - 4j]^{\mathrm{T}}$ ， $k = [3]$ 。这意味着传递函数也可以写为

$$\frac {Y (s)}{U (s)} = \frac {3 (s + 3)}{(s + 3 - 4 \mathrm{j}) (s + 3 + 4 \mathrm{j})}$$

我们也可以将零极点描述转化为传递函数描述，需要用到Matlab中zp2tf命令，即

% convert from pole-zero form to numerator-denominator polynomials [numG, denG] = zp2tf(z, p, k)

对于此例， $z=[-3]$ ， $p=[-3+j4;\quad-3-j4]$ ， $k=[3]$ 可得传递函数的分子分母多项式。
