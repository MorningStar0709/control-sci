# (2) 绘制根轨迹图

利用 MATLAB 绘制根轨迹的一般步骤如下：

1) 先将特征方程写成下列形式 $1 + K \frac{p(s)}{q(s)} = 0$ ，其中 $K$ 为所研究的变化参数，得到等效开环传递函数 $G = \frac{p(s)}{q(s)}$ 。

2）调用 rlocus 命令绘制根轨迹。

命令格式：rlocus(G)

(3) 综合应用(系统性能复域分析)

例B-3 已知单位负反馈系统的开环传递函数为

![](image/1f964e2fae5a2a98629e1a2f129de3652ac2ea15c51a0c5be1a3fc8ee5d943cc.jpg)

<details>
<summary>line</summary>

| t/s | σ(t) - Solid Line | σ(t) - Dotted Line |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.2 | 0.5 |
| 1.0 | 0.6 | 1.0 |
| 1.5 | 1.0 | 1.5 |
| 2.0 | 1.4 | 2.0 |
| 2.5 | 1.8 | 2.5 |
| 3.0 | 2.2 | 3.0 |
</details>

图 B-5 单位斜坡响应

$$G (s) = \frac {2 0}{(s + 4) (s + K)}$$

试画出 K 从零变化到无穷时的根轨迹图，并求出系统临界阻尼时对应的 K 值及其闭环极点。

解 由题意,系统闭环特征多项式为

$$D (s) = s ^ {2} + 4 s + K s + 4 K + 2 0 = s ^ {2} + 4 s + 2 0 + K (s + 4) = 0$$

等效开环传递函数

$$G ^ {*} (s) = \frac {K (s + 4)}{s ^ {2} + 4 s + 2 0}$$

下面调用 rlocus 命令绘制根轨迹, M 文件 example3 如下:

<table><tr><td>G=tf([1 4],[1 4 20]);</td><td>%建立等效开环传递函数模型</td></tr><tr><td>figure(1)</td><td></td></tr><tr><td>pzmap(G);</td><td>%绘制零、极点分布图</td></tr><tr><td>figure(2)</td><td></td></tr><tr><td>rlocus(G);</td><td>%绘制根轨迹</td></tr></table>

图 B-6, 图 B-7 分别为 example3. m 执行后得到的零、极点分布图和根轨迹图。

![](image/32b1dccf18ae7af13302d8de59afc6915da14103f9b307429bde21517cf75105.jpg)

<details>
<summary>line</summary>

| Point | Real Axis | Imaginary Axis |
| --- | --- | --- |
| 1 | -4.0 | 0 |
| 2 | -2.0 | 4 |
| 3 | -2.0 | -4 |
</details>

图 B-6 零、极点分布图

![](image/6049e34eb9c2badfc5e008926f5aa02966908ae604f28b8d3ba7e9c9e9743462.jpg)

<details>
<summary>line</summary>
