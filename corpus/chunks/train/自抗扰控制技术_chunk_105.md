这说明,在线性状态反馈(3.2.20)的作用下,闭环系统抑制未知扰动 $w(x_{1},x_{2},t)$ 的能力是与量 $\left(\frac{w_{0}}{k}\right)$ 成正比.

下面对系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = w (x _ {1}, x _ {2}, t) + u \end{array} , | w (x _ {1}, x _ {2}, t) | <   w _ {0} \right.
$$

实施不同增益 k 的状态反馈 $u = -k(x_{1} + 2\zeta x_{2})$ 时的仿真结果.

实施这个状态反馈之后的闭环系统为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - k (x _ {1} + 2 \zeta x _ {2}) + w (x _ {1}, x _ {2}, t) \end{array} \right.
$$

取 $k = 5,10,20$ 时，抑制扰动 $w(x_{1},x_{2},t) = 1$ 的情况.如1.4节所指出的那样， $k,2k\zeta$ 之比为 $r^2,2r$ （见式(1.4.2))，因此 $k$ 分别取5，10,20时， $2k\zeta$ 分别为4.4732,6.324,8.944.

从这个仿真图3.2.3可以看出， $k$ 越大，反馈抑制扰动的能力越大，其数量关系是与反馈增益 $k$ 成反比.

下面看看非线性状态反馈

$$u = - k \left(\left| x _ {1} \right| ^ {- \frac {1}{2}} x _ {1} + 2 \zeta x _ {2}\right) = - k \left(\left| x _ {1} \right| ^ {\frac {1}{2}} \operatorname{sign} \left(x _ {1}\right) + 2 \zeta x _ {2}\right) \tag {3.2.25}$$

的一些特性.

![](image/769cc55d48e1b6c71f8d8c57e3e5618864d2df0c0d9ba1450d5ce49fffb79af2.jpg)

<details>
<summary>line</summary>

| k | x₁ |
| --- | --- |
| 0 | 0.8 |
| 5 | 0.2 |
| 10 | 0.2 |
| 15 | 0.2 |
| 20 | 0.2 |
</details>

![](image/cc61966eb8423d09a430f1aa7576702e7586e0371b1b67dd27a15ff7f50de0dd.jpg)

<details>
<summary>line</summary>

| k | x₁ |
| --- | --- |
| 0 | 1.0 |
| 5 | 0.1 |
| 10 | 0.1 |
| 15 | 0.1 |
| 20 | 0.1 |
</details>

![](image/6156c0d786cb1e8ab44dc68a71e7d05bfc4e75da2ba163077500be3a1db349d5.jpg)

<details>
<summary>line</summary>

| k | x₁ |
| --- | --- |
| 0 | 1 |
| 5 | 0.1 |
| 10 | 0.05 |
| 15 | 0.03 |
| 20 | 0.02 |
</details>

图3.2.3

实施这个非线性状态反馈所得的闭环系统为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - k \left(\left| x _ {1} \right| ^ {- \frac {1}{2}} x _ {1} + 2 \zeta x _ {2}\right) + w \left(z _ {1}, x _ {2}, t\right) \end{array} \right. \tag {3.2.26}
$$

对这个闭环系统,仿造前述线性反馈情形,取如下李亚普诺夫函数

$$V \left(x _ {1}, x _ {2}\right) = \frac {1}{3 k ^ {2} \zeta} \left[ \left(k + k ^ {2} + 4 k ^ {2} \zeta^ {2}\right) \mid x _ {1} \mid^ {\frac {3}{2}} + 3 k \zeta x _ {1} x _ {2} + \frac {3}{4} (1 + k) x _ {2} ^ {2} \right] \tag {3.2.27}$$

那么记 $A = 3k^{2}\zeta$ ，有

$$A \frac {\partial V}{\partial x _ {1}} = \frac {3}{2} (k + k ^ {2} + 4 k ^ {2} \zeta^ {2}) | x _ {1} | ^ {- \frac {1}{2}} x _ {1} + 3 k \zeta x _ {2},A \frac {\partial V}{\partial x _ {2}} = 3 k \zeta x _ {1} + \frac {3}{2} x _ {2} + \frac {3}{2} k x _ {2}$$

这时，沿闭环系统轨线求函数 $V(x_{1},x_{2})$ 的导数，得
