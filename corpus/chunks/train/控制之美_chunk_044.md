![](image/0390b1e859fb137a24432ebed56cd894747286d304c3bc83e2be284abd936129.jpg)

<details>
<summary>line</summary>

| t | x(t) |
| --- | --- |
| 0 | 0 |
| >0 | C/R |
</details>

图2.3.2 系统输出 $x(t) = \frac{C}{R} -\frac{C}{R}\mathrm{e}^{-\frac{R}{L} t}$ 随时间变化

式(2.3.9)中, $x(t)$ 由两项相减组合而成, 分别是 $\frac{C}{R} e^{0t}$ 和 $\frac{C}{R} e^{-\frac{R}{L} t}$ , 第一项中 $e$ 的指数部分系数是 0 , 因此 $\frac{C}{R} e^{0t}$ 等于常数 $\frac{C}{R}$ ; 而第二项中指数部分系数为 $-\frac{R}{L} < 0$ , 表明项 $\frac{C}{R} e^{-\frac{R}{L} t}$ 会随着时间的增加而不断地衰减, 直到为 0 。所以, 系统输出 $x(t)$ 是有界限的, 并且随着时间的增加而趋向于常数 $\frac{C}{R}$ 。在式(2.3.6)中, 当系统输出 $X(s)$ 的分母部分等于 0 时, 可以得到

$$
s \left(s + \frac {R}{L}\right) = 0 \Rightarrow \left\{ \begin{array}{l} s _ {\mathrm{p1}} = 0 \\ s _ {\mathrm{p2}} = - \frac {R}{L} \end{array} \right. \tag {2.3.10}
$$

$s_{p1}$ 和 $s_{p2}$ 被称为系统输出的极点(Poles)，其中， $s_{p1}$ 是输入 $U(s)=C\frac{1}{s}$ 引入的极点。 $s_{p2}=-\frac{R}{L}$ 则是传递函数的极点，这是动态系统自身的极点，体现了动态系统的特性，它可以直接通过传递函数的特征方程(Characteristic Equation)，即令 $G(s)$ 的分母部分为 $0(Ls+R=0)$ 得到。

在此例中， $s_{\mathrm{p1}} = 0$ ，而 $s_{\mathrm{p2}} = -\frac{R}{L} < 0$ ，所以输出 $x(t)$ 将会趋于一个常数。以上的分析说明，在得到系统的传递函数之后，便可以通过简单的代数计算得到系统输出的极点，并以此为依据快速判断系统的表现。也就是说，在得到式(2.3.6)之后就可以判断系统的表现了，这省去了大量的中间过程，并且避免了求解微分方程和卷积的麻烦。
