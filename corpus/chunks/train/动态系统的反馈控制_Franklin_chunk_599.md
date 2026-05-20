# 例 9.13 条件稳定系统

考虑图 9.14 所示的反馈系统。利用奈奎斯特图确定极限环的幅值和频率。

解答。如图9.32所示，把系统的奈奎斯特曲线与 $-\frac{1}{K_{\mathrm{eq}}(a)}$ 曲线画在一起。注意，由式(9.29)可知描述函数的负倒数为

$$
\begin{array}{l} - \frac {1}{K _ {\mathrm{eq}} (a)} = - \frac {1}{\frac {2}{\pi} \left(k \arcsin \left(\frac {N}{a k}\right) + \frac {N}{a} \sqrt {1 - \left(\frac {N}{k a}\right) ^ {2}}\right)} \\ = - \frac {1}{\frac {2}{\pi} \left(\arcsin \left(\frac {0 . 1}{a}\right) + \frac {0 . 1}{a} \sqrt {1 - \left(\frac {0 . 1}{a}\right) ^ {2}}\right)} \\ \end{array}
$$

它是一条与负半轴重合的直线，也是以输入信号幅值 a 为参数的函数。两条曲线在负实轴 -0.5 处的交点对应频率为 $\omega_{1}=1$ 的极限环。在 k=1 和 N=0.1 时描述函数如图 9.33 所示， $K_{eq}=0.2$ 的幅值相当于 $a_{1}=0.63$ 的输入幅值。

![](image/e3357e0d7072d742e64b8bef248a0e1b4a370f50e0b999e4632880f10a7a91d5.jpg)

<details>
<summary>other</summary>

| Parameter | Value |
| --- | --- |
| α | 0.63 |
| ω | 1 |
| K | -1 |
</details>

图 9.32 用奈奎斯特图和描述函数确定极限环

![](image/a719373b89a6b31eea36037d0af048899eb365539f227186b4dc1da1ea62595b.jpg)

<details>
<summary>line</summary>

| a | K_eq |
| --- | --- |
| 0 | 1.0 |
| 2 | 0.1 |
| 4 | 0.05 |
| 6 | 0.02 |
| 8 | 0.01 |
| 10 | 0.0 |
</details>

图 9.33 N=0.1, k=1 时饱和非线性的描述函数

或者，从图 9.15 所示的本例的根轨迹可见，穿越虚轴处的增益值为 0.2；再根据式(9.29)，我们可得

$$K _ {\mathrm{eq}} = \frac {2}{\pi} \left(\arcsin \left(\frac {0 . 1}{a}\right) + \frac {0 . 1}{a} \sqrt {1 - \left(\frac {0 . 1}{a}\right) ^ {2}}\right) = 0. 2$$

如果我们用反正弦函数的自变量来近似替代反正弦函数，即

$$\arcsin \left(\frac {0 . 1}{a}\right) \approx \frac {0 . 1}{a}$$

那么

$$\frac {2}{\pi} \left(\left(\frac {0 . 1}{a}\right) + \frac {0 . 1}{a} \sqrt {1 - \left(\frac {0 . 1}{a}\right) ^ {2}}\right) = 0. 2$$

由上式可得多项式方程

$$\pi^ {2} a ^ {4} - 2 \pi a ^ {3} + (0. 1) ^ {2} = 0$$

相应的解为 a=0.63。通过测量图 9.16 上的时间记录，振荡的幅值为 0.62，与我们的预测很相符。

对于含有记忆非线性的系统，也可以使用奈奎斯特技术，正如下面的例子所说。
