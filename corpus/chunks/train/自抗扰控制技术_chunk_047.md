# 1.5 时间尺度

实际控制对象的具体表现是五花八门的，两个实际物理背景完全不同的对象，把它们作为抽象的被控对象来考察时，如何比较由它们作成的闭环系统的控制品质？尽管各种对象其物理背景很不相同，但是作为被控对象，按控制系统的典型特征，可以归类为几种不同系统。例如，一个工业用电炉子，升温时间花了3h，而另一个实验室用的电炉子，升温时间只花了30min。这两个炉子作为抽象的被控对象，问哪一个对象的过渡过程快，哪一个慢？又如何比较这两个受控系统的动态品质和控制品质呢？

下面看看放大系数为1的一,二,三阶线性系统阶跃响应的快

慢特性.

一阶系统通常表示成

$$\dot {x} = - \frac {1}{T} (x - v _ {0}), W (s) = \frac {1}{T s + 1}$$

式中：T 为系统的时间常数.

时间常数 T 越小, 系统的响应越快. 如果记 r = 1/T, 上述方程变为

$$\dot {x} = - r \left(x - v _ {0}\right) \tag {1.5.1}$$

显然， $r$ 越大， $x(t)$ 跟踪 $v_{0}$ 的速度越快，即系统的阶跃响应越快.图1.5.1显示了 $r = 1$ 和 $r = 5$ 时的阶跃响应．从中看出阶跃响应速度是与 $\pmb{r}$ 成反比.

![](image/51f61b4298677f285ba5f3a7d53321a87af97f584cf94bc1b2e3566784b017ab.jpg)

<details>
<summary>line</summary>

| x | r=1 | r=5 |
| --- | --- | --- |
| 0 | 1.5 | 0 |
| 1 | 2.0 | 0.7 |
| 2 | 2.3 | 0.9 |
| 3 | 2.4 | 0.95 |
| 4 | 2.45 | 0.98 |
| 5 | 2.48 | 0.99 |
| 6 | 2.5 | 0.995 |
</details>

图 1.5.1

二阶系统通常表示成

$$\ddot {x} = - \omega_ {0} ^ {2} \left(x - u + 2 \frac {\xi}{\omega_ {0}} \dot {x}\right)W (s) = \frac {\omega_ {0} ^ {2}}{s ^ {2} + 2 \omega_ {0} \xi s + \omega_ {0} ^ {2}}$$

式中： $\omega_{0}$ 为谐振频率，也是决定系统响应快慢的一个参数； $\xi$ 为阻尼系数．如果 $r = \omega_{0}$ ，那么等价的状态空间描述为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r ^ {2} (x _ {1} - u) - 2 r \xi x _ {2} \\ y = x _ {1} \end{array} \right. \tag {1.5.2}
$$

此系统对不同的 r 和 $\xi$ 的阶跃响应如图 1.5.2 所示.

![](image/53e6b1a12e8b24cb2a976a48fb69cc841ab39a68d242735bdf0519cd67c492e6.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 2 | 1.0 |
| 4 | 1.3 |
| 6 | 1.0 |
| 8 | 1.0 |
| 10 | 1.0 |
</details>

![](image/07ed9d9212f5243865117dd691b7405cbe261878a2b51591b0fd738904f302b1.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 5 | 1 |
| 10 | 1 |
</details>

![](image/4b02841c400d45bfdc16a0e519d98d44977bbf9dbd6e65918bb1669caa7f8f21.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 5 | 0.9 |
| 10 | 1.0 |
</details>

![](image/2bc2c79b68853fbe012143a852f452c5726f0348893a6ea630bc4ba8a42f20de.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 5 | 1.0 |
| 10 | 1.0 |
</details>

![](image/1a197f7b6749640892e630b6668d3eb3fbce094bded2fe718491d9ceb3c4c862.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 3 | 1.2 |
| 5 | 1.0 |
| 10 | 0.8 |
</details>

![](image/c0d13c9b092335477fb6b10277a659c1af593d6d3abb090afa95a33c5251c7d3.jpg)

<details>
<summary>line</summary>
