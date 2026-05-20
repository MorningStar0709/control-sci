# 3.8 几个有用的非线性函数

在许多智能表达中经常应用数量关系条件判断,如某一个变量 x 属于某一范围内变化时相应的另一个变量 y 取另外一个范围值等. 常常用条件语句表述上述事实. 但是我们也可以用适当的非线性函数 $y = f(x)$ 来表示这种数量关系判断条件. 这里有两个基本函数 — 符号函数 $\text{sign}(x - a)$ 和取绝对值函数 $|x - a|$ , 其图形分别如图 3.8.1(a)、(b) 所示.

![](image/2f30c734ea0f7a8f7cf0793235b4168dedcc81ce7737eafc35d2477a6ffb963f.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | -1 |
| 1 | 1 |
| 2 | 1 |
</details>

(a)

![](image/8e4bcc04bb1f3298546801894c6740da8cba472dba408e99016f90f5c75b11cc.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| 0 | 1 |
| 1 | 0 |
| 2 | 1 |
</details>

(b)   
图3.8.1

1. 定义区间函数

$$\operatorname{fsg} _ {0} (x, d) = \frac {\operatorname{sign} (x + d) - \operatorname{sign} (x - d)}{2}$$

是在区间 $[-d,d]$ 上取1,其余取0的函数.

2. 定义更一般的区间函数

$$\operatorname{fsg} (x, a, b) = \frac {\operatorname{sign} (x - a) - \operatorname{sign} (x - b)}{2}$$

其图形如图3.8.2所示 $(a = -1, b = 1)$ . 是在区间 $[a, b]$ 上取1，其余取0的函数.

![](image/1b48b10c4bb5d39741c12ebac98a6699f255cc728dababa962f6b69ec2f0810c.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -3 | 0 |
| -2 | 0 |
| -1 | 1 |
| 0 | 1 |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
</details>

图3.8.2

例1 取 $f(x) = \sin (2\pi x)$ ，那么函数 $y = \operatorname{fsg}(x,0,1.5)f(x)$ 的图形如图3.8.3所示.

![](image/f64855b587658ae34f7ea9f368075ffa0cfe9bd9119b02c92cc78820b507635f.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 0 |
| 0.5 | 1 |
| 1.0 | -1 |
| 1.5 | 0 |
| 2.0 | 1 |
| 2.5 | 0 |
| 3.0 | 0 |
</details>

图3.8.3

在区间 $[0,1.5]$ 上为正弦波,其余为0.

例 2 阶梯函数

$$y = \operatorname{fsg} (x, 0, 1) + 2 \operatorname{fsg} (x, 1, 2) + 3 \operatorname{fsg} (x, 2, 3)$$

其图形如图 3.8.4 所示.

![](image/c72928766236c20c685d0f440ecfff8b06f9b369836bc9aa3dc9ca9119a127ce.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 3 |
</details>

图 3.8.4

例 3 函数

$$
y = \left\{ \begin{array}{l} a, x \in [ d _ {1}, d _ {2} ] \\ b, x \notin [ d _ {1}, d _ {2} ] \end{array} \right.
$$

可表示成

$$y = a \operatorname{fsg} \left(x, d _ {1}, d _ {2}\right) + b \left(1 - \operatorname{fsg} \left(x, d _ {1}, d _ {2}\right)\right)$$

取 $d_{1} = -0.5, d_{2} = 1.0, a = 1.2, b = 0.3$ 时的图形如图 3.8.5 所示.

![](image/45254e84247f8e64589706c14c3c5516f1f02326653b318c2e00906b71264719.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -0.5 | 1.2 |
| 0.5 | 1.2 |
| 1.0 | 0.3 |
</details>

图 3.8.5

例4 函数
