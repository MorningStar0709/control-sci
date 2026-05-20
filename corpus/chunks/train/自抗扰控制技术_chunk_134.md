# 3. 最优开关函数

积分器串联型的位置分量, 当控制量受限 $\left|u\right|\leqslant1$ 时, 从静止状态转移到某一给定距离的过程, 其最速控制是遵守一定规则的开关函数. 对各阶次积分器串联型对象在这个过程的最速开关规律可按如下方式产生. 定义函数

$$\operatorname{fss} (x, a, b) = \operatorname{sign} (x - a) (1 - \operatorname{sign} (x - b)) / 2, a < b$$

如果取 b = 1.5, a = 1, 那么曲线 $\mathrm{fss}(x, a, b)$ 的形状如图 3.8.10 所示.

![](image/68fab850e07bc7d057513456400951428bc266d50fe17d40e93001ada8cb4ec0.jpg)  
图 3.8.10

当0<x<1时,y=1,其他都等于0.是一阶纯积分器对象的最速控制规律.

二阶积分器串联型对象的最速开关规律如图 3.8.11 所示.

![](image/4c88255007b1c762cea1e82b6ca833c5b020c803b13efacdd154db12a38fefba.jpg)

<details>
<summary>line</summary>

| x | y = fss(t, 1, 2) |
| --- | --- |
| 0.0 | 1 |
| 1.0 | -1 |
| 2.0 | 0 |
| 3.0 | 0 |
</details>

图3.8.11

三,四阶积分器串联型对象的开关规律分别如图 3.8.12 和图 3.8.13 所示.

![](image/e2d06278f869ced18b4d62b6f1239dad642fc5e8b95c4b254d44236dfedbb4d0.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.5 | 1 |
| 1 | -1 |
| 2.5 | -1 |
| 3 | 1 |
| 4 | -1 |
| 5 | 0 |
</details>

图 3.8.12  
![](image/3ecd842007f3832613bedcaa44bd1d92ea857a45181ba5459edc8be94282bdcc.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1 |
| 1 | -1 |
| 2 | -1 |
| 3 | 1 |
| 4 | -1 |
| 5 | -1 |
| 6 | 0 |
| 7 | 0 |
</details>

图 3.8.13

4. 绝对值函数之差

$$
\operatorname{fst} _ {0} (x, d) = \frac {| x + d | - | x - d |}{2 d} = \left\{ \begin{array}{l l} x, & | x | <   d \\ \operatorname{sign} (x), & | x | \geqslant d \end{array} \right.
$$

d = 1 时的图形为图 3.8.14.

![](image/b34eba4c7583fbde47c771db7945187525d9a2b3d33cb8c1dc617b8caee0912b.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -1 | -1 |
| -1 | -1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
</details>

图 3.8.14

在区间 $[-d,d]$ 上是斜率为 $\frac{1}{d}$ 的直线,而这个区间之外取 $\mathrm{sign}(x)$ 的线性饱和函数.

例8 $f(x) = \mathrm{sign}(x)\sqrt{|x|}$ ，那么 $y = \mathrm{dfst}_0(f(x), d) = \frac{|f(x) + d| - |f(x) - d|}{2}$ 在区间 $[-d, d]$ 上取 $f(x)$ ，而其外取 $\mathrm{sign}(f(x))$ （图3.8.15）.

![](image/62a05c4f11280f9a21c745d346a6f20af6d8441fb5de58a20feae566c84ab96e.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -3.0 | -1.5 |
| -2.0 | -1.0 |
| -1.0 | -0.5 |
| 0.0 | 0.0 |
| 1.0 | 0.5 |
| 2.0 | 1.0 |
| 3.0 | 1.5 |
</details>

图 3.8.15

例9 $f = \sin (x),y = d\mathrm{fst}_0(f,d) = \frac{|f + d| - |f - d|}{2}$ 是从曲线 $f = \sin (x)$ 中只取 $-d\sim d$ 之间的值(图3.8.16).

![](image/d03c564459b2e52ecf7d2227d747b8769c61347fe4263847fd5110d436251ab0.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -3 | 0 |
| -2 | -1 |
| -1 | -1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 0.875 |
| 3 | 0 |
</details>
