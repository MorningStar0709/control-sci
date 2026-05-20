# 2. $z$ 变换方法

1) 级数求和法

$$E (z) = \sum_ {n = 0} ^ {\infty} e (n T) z ^ {- n} = e (0) + e (T) z ^ {- 1} + e (2 T) z ^ {- 2} + \dots + e (n T) z ^ {- n} + \dots$$

上式是离散时间函数 $e^{*}(t)$ 的无穷级数表达形式。通常，对于常用函数 z 变换的级数形式，都可以写出其闭合形式。

2）部分分式法

先求出已知连续时间函数 $e(t)$ 的拉普拉斯变换 $E(s)$ ，然后将有理分式函数 $E(s)$ 展成部分分式之和的形式，使每一个部分分式对应简单的时间函数，其相应的 z 变换是已知的，于是可以查 z 变换表，方便地求出 $E(s)$ 对应的 z 变换 $E(z)$ 。

常用时间函数的 z 变换表如表 1-3 所示。由表可见，这些函数的 z 变换都是 z 的真有理分式，且 $E(z)$ 分母 z 多项式的最高次数与 $E(s)$ 分母 s 多项式的最高次数相等。

表 1-3 z 变换表

<table><tr><td>序号</td><td>拉普拉斯变换E(s)</td><td>时间函数e(t)</td><td>z变换E(z)</td></tr><tr><td>1</td><td> $e^{-snT}$ </td><td> $\delta (t-nT)$ </td><td> $z^{-n}$ </td></tr><tr><td>2</td><td>1</td><td> $\delta (t)$ </td><td>1</td></tr><tr><td>3</td><td> $\frac{1}{s}$ </td><td>1(t)</td><td> $\frac{z}{z-1}$ </td></tr><tr><td>4</td><td> $\frac{1}{s^2}$ </td><td>t</td><td> $\frac{Tz}{(z-1)^2}$ </td></tr><tr><td>5</td><td> $\frac{1}{s^3}$ </td><td> $\frac{t^2}{2!}$ </td><td> $\frac{T^2z(z+1)}{2(z-1)^3}$ </td></tr><tr><td>6</td><td> $\frac{1}{s^4}$ </td><td> $\frac{t^3}{3!}$ </td><td> $\frac{T^3z(z^2+4z+1)}{6(z-1)^4}$ </td></tr><tr><td>7</td><td> $\frac{1}{s-(1/T)\ln a}$ </td><td> $a^{t/T}$ </td><td> $\frac{z}{z-a}$ </td></tr><tr><td>8</td><td> $\frac{1}{s+a}$ </td><td> $e^{-at}$ </td><td> $\frac{z}{z-e^{-aT}}$ </td></tr><tr><td>9</td><td> $\frac{1}{(s+a)^2}$ </td><td> $te^{-at}$ </td><td> $\frac{Tze^{-aT}}{(z-e^{-aT})^2}$ </td></tr><tr><td>10</td><td> $\frac{1}{(s+a)^3}$ </td><td> $\frac{1}{2}t^2e^{-at}$ </td><td> $\frac{T^2ze^{-aT}}{2(z-e^{-aT})^2}+\frac{T^2ze^{-2aT}}{(z-e^{-aT})^3}$ </td></tr><tr><td>11</td><td> $\frac{a}{s(s+a)}$ </td><td> $1-e^{-at}$ </td><td> $\frac{(1-e^{-aT})z}{(z-1)(z-e^{-aT})}$ </td></tr><tr><td>12</td><td> $\frac{a}{s^2(s+a)}$ </td><td> $t-\frac{1}{a}(1-e^{-at})$ </td><td> $\frac{Tz}{(z-1)^2}-\frac{(1-e^{-aT})z}{a(z-1)(z-e^{-aT})}$ </td></tr><tr><td>13</td><td> $\frac{1}{(s+a)(s+b)(s+c)}$ </td><td> $\frac{e^{-at}}{(b-a)(c-a)}+\frac{e^{-bt}}{(a-b)(c-b)}+\frac{e^{-ct}}{(a-c)(b-c)}$ </td><td> $\frac{z}{(b-a)(c-a)(z-e^{-aT})}+\frac{z}{(a-b)(c-b)(z-e^{-bT})}+\frac{z}{(a-c)(b-c)(z-e^{-cT})}$ </td></tr></table>
