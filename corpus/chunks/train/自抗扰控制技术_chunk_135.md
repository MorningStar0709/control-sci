图3.8.16

$$
5. \mathrm{fst} (x, a, b) = \frac {\left(\frac {| x - a | - | x - b |}{b - a} + 1\right)}{2} =
\left\{ \begin{array}{l l} 1, & x > b \\ \frac {x - a}{b - a}, & a \leqslant x \leqslant b \\ 0, x <   a \end{array} \right.
$$

例 10 $f(x)=|x-5|+|x-10|+|x-15|+|x-20|+|x-25|$ （其图形如图 3.8.17 所示）

![](image/20bb6d6e4990063f7d5d725db4cae214bba736ac27b9e2a4394284a43437755e.jpg)  
图 3.8.17

例 11 $f(x)=|x-5|-|x-10|+|x-15|-|x-20|+|x-25|$ （其图形如图 3.8.18 所示）

![](image/72da1591fd7e9dcf3c124e9fe15b775aa1ba61980d63654ea424d3147c2f1f83.jpg)

<details>
<summary>line</summary>

| x | f(x) |
| --- | --- |
| 0 | 15 |
| 5 | 10 |
| 10 | 15 |
| 15 | 10 |
| 20 | 15 |
| 25 | 10 |
| 30 | 15 |
</details>

图3.8.18

例 12 $f(x)=|x-5|-|x-10|+|x-15|-|x-20|+|x-25|-|x-30|$ （其图形如图 3.8.19 所示）

![](image/ae59b619b42b6b07e93344351f97544dc50f993bdaee9c673124096aca863e45.jpg)

<details>
<summary>line</summary>

| x | f(x) |
| --- | --- |
| 5 | -15 |
| 10 | -5 |
| 15 | -5 |
| 20 | 0 |
| 25 | 5 |
| 30 | 15 |
</details>

图3.8.19

灵活应用符号函数与绝对值函数可以构造出许多与条件语句相关的非线性函数,因此一些简单的人工智能是可以用适当的非线性函数来表达出来的.

6. 用 $\operatorname{fst}(x, d_1, d_2)$ 函数的组合来逼近任意函数

设 $f(x)$ 在自变量

$$x _ {0} < x _ {1} < x _ {2} < x _ {3} < x _ {4} < x _ {5}$$

上的值为

$$y _ {0}, y _ {1}, y _ {2}, y _ {3}, y _ {4}, y _ {5}$$

记

$$d _ {1} = y _ {1} - y _ {0}, d _ {2} = y _ {2} - y _ {1}, d _ {3} = y _ {3} - y _ {2}, d _ {4} = y _ {4} - y _ {3}, d _ {5} = y _ {5} - y _ {4}$$

那么函数 $f(x)$ 近似的逼近成

$$
\begin{array}{l} y = y _ {0} + d _ {1} \operatorname{fst} \left(x, x _ {0}, x _ {1}\right) + d _ {2} \operatorname{fst} \left(x, x _ {1}, x _ {2}\right) + d _ {3} \operatorname{fst} \left(x, x _ {2}, x _ {3}\right) + \\ d _ {4} \operatorname{fst} \left(x, x _ {3}, x _ {4}\right) + d _ {5} \operatorname{fst} \left(x, x _ {4}, x _ {5}\right) \\ \end{array}
$$

例 13 用 $\mathrm{fst}(x,a,b)$ 逼近函数 $f(x)=\mathrm{sign}(x)\mid x\mid^{0.5}$

$f(x)$ 在点 $x = 0,0.1,0.3,0.5,0.8,1.0$ 上的函数值分别是：0，0.3162,0.5477,0.7071,0.8944,1.000，那么就用组合函数 $y = 0.3162\mathrm{fst}(x,0,0.1) + 0.2315\mathrm{fst}(x,0.1,0.3) + 0.1593\mathrm{fst}(x,0.3,0.5) + 0.1873\mathrm{fst}(x,0.5,0.8) + 0.1055\mathrm{fst}(x,0.8,1.0)$ 来逼近 $f(x)$ （图3.8.20).

![](image/0468322f84c45e21e38ed51a7d5cc87e83999e113d9f536cf2ff1ecd921a4970.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 0 |
| 0.2 | 0.3 |
| 0.4 | 0.5 |
| 0.6 | 0.7 |
| 0.8 | 0.9 |
| 1.0 | 1.0 |
| 1.2 | 1.1 |
| 1.4 | 1.2 |
</details>

图 3.8.20
