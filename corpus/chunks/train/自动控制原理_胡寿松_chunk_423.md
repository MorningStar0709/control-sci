# (3) 反演积分法

反演积分法又称留数法。采用反演积分法求取 $z$ 反变换的原因是：在实际问题中遇到的 $z$ 变换函数 $E(z)$ ，除了有理分式外，也可能是超越函数，此时无法应用部分分式法及幂级数法来求 $z$ 反变换，而只能采用反演积分法。当然，反演积分法对 $E(z)$ 为有理分式的情况也是适用的。由于 $E(z)$ 的幂级数展开形式为

$$
\begin{array}{l} E (z) = \sum_ {n = 0} ^ {\infty} e (n T) z ^ {- n} \\ = e (0) + e (T) z ^ {- 1} + e (2 T) z ^ {- 2} + \dots + e (n T) z ^ {- n} + \dots \tag {7-40} \\ \end{array}
$$

所以函数 $E(z)$ 可以看成是 z 平面上的劳伦级数。级数的各系数 $e(nT)(n=0,1,\cdots)$ 可以由积分的方法求出，因为在求积分值时要用到柯西留数定理，故也称之为留数法。

为了推导反演积分公式，用 $z^{n - 1}$ 乘以式(7-40)两端，得到

$$E (z) z ^ {n - 1} = e (0) z ^ {n - 1} + e (T) z ^ {n - 2} + \dots + e (n T) z ^ {- 1} + \dots \tag {7-41}$$

设 $\Gamma$ 为 $z$ 平面上包围 $E(z)z^{n - 1}$ 全部极点的封闭曲线，且设沿 $\Gamma$ 反时针方向对式(7-46)的两端同时积分，可得

$$
\begin{array}{l} \oint_ {\Gamma} E (z) z ^ {n - 1} \mathrm{d} z = \oint_ {\Gamma} e (0) z ^ {n - 1} \mathrm{d} z + \oint_ {\Gamma} e (T) z ^ {n - 2} \mathrm{d} z + \dots \\ + \oint_ {\Gamma} e (\dot {n} T) z ^ {- 1} d z + \dots \tag {7-42} \\ \end{array}
$$

由复变函数论可知,对于围绕原点的积分闭路 $\Gamma$ ,有如下关系式:

$$
\oint_ {\Gamma} z ^ {k - n - 1} \mathrm{d} z = \left\{ \begin{array}{l l} 0, & \text {当} k \neq n \\ 2 \pi \mathrm{j}, & \text {当} k = n \end{array} \right.
$$

故在式(7-42)右端中，除

$$\oint_ {\Gamma} e (n T) z ^ {- 1} \mathrm{d} z = e (n T) \cdot 2 \pi \mathrm{j}$$

外，其余各项均为零。由此得到反演积分公式

$$e (n T) = \frac {1}{2 \pi \mathrm{j}} \oint_ {\Gamma} E (z) z ^ {n - 1} \mathrm{d} z \tag {7-43}$$

根据柯西留数定理, 设函数 $E(z)z^{n-1}$ 除有限个极点 $z_{1}, z_{2}, \cdots, z_{k}$ 外, 在域 G 上是解析的。如果有闭合路径 $\Gamma$ 包含了这些极点, 则有

$$e (n T) = \frac {1}{2 \pi \mathrm{j}} \oint_ {\Gamma} E (z) z ^ {n - 1} \mathrm{d} z = \sum_ {i = 1} ^ {k} \operatorname{Res} [ E (z) z ^ {n - 1} ] _ {z \rightarrow z _ {i}} \tag {7-44}$$

式中， $\operatorname{Res}[E(z)z^{n-1}]_{z \to z_i}$ 表示函数 $E(z)z^{n-1}$ 在极点 $z_i$ 处的留数。

例7-13 设 $z$ 变换函数

$$E (z) = \frac {z ^ {2}}{(z - 1) (z - 0 . 5)}$$

试用留数法求其 z 反变换。

解 因为函数

$$E (z) z ^ {n - 1} = \frac {z ^ {n + 1}}{(z - 1) (z - 0 . 5)}$$

有 $z_{1} = 1$ 和 $z_{2} = 0.5$ 两个极点，极点处留数

$$\operatorname{Res} \left[ \frac {z ^ {n + 1}}{(z - 1) (z - 0 . 5)} \right] _ {z \rightarrow 1} = \lim _ {z \rightarrow 1} \left[ \frac {(z - 1) z ^ {n + 1}}{(z - 1) (z - 0 . 5)} \right] = 2\operatorname{Res} \left[ \frac {z ^ {n + 1}}{(z - 1) (z - 0 . 5)} \right] _ {z \rightarrow 0. 5} = \lim _ {z \rightarrow 0. 5} \left[ \frac {(z - 0 . 5) z ^ {n + 1}}{(z - 1) (z - 0 . 5)} \right] = - (0. 5) ^ {n}$$

所以由式(7-44)得

$$e (n T) = 2 - (0. 5) ^ {n}$$

相应的采样函数
