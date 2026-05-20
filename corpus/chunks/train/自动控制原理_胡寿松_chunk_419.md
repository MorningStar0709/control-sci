# (5) 卷积定理

设 $x(nT)$ 和 $y(nT)$ 为两个采样函数, 其离散卷积定义为

$$x (n T) * y (n T) = \sum_ {k = 0} ^ {\infty} x (k T) y [ (n - k) T ] \tag {7-33}$$

则由卷积定理：若

$$g (n T) = x (n T) * y (n T)$$

必有 $G(z) = X(z)\cdot Y(z)$ (7-34)

证明 由 $z$ 变换

$$X (z) = \sum_ {k = 0} ^ {\infty} x (k T) z ^ {- k}, \quad Y (z) = \sum_ {n = 0} ^ {\infty} y (n T) z ^ {- n}$$

再由定理已知条件

$$G (z) = \mathscr {L} [ g (n T) ] = \mathscr {L} [ x (n T) * y (n T) ] \tag {7-35}$$

所以 $X(z)\cdot Y(z) = \sum_{k = 0}^{\infty}x(kT)z^{-k}Y(z)$

根据平移定理及 $z$ 变换定义，有

$$z ^ {- k} Y (z) = \mathscr {L} \{y [ (n - k) T ] \} = \sum_ {n = 0} ^ {\infty} y [ (n - k) T ] z ^ {- n}$$

故 $X(z)\cdot Y(z) = \sum_{k = 0}^{\infty}x(kT)\sum_{n = 0}^{\infty}y[(n - k)T]z^{-n}$

交换求和次序并代入式(7-33)，上式可写为

$$
\begin{array}{l} X (z) \cdot Y (z) = \sum_ {n = 0} ^ {\infty} \left\{\sum_ {k = 0} ^ {\infty} x (k T) g [ (n - k) T ] \right\} z ^ {- n} \\ = \sum_ {n = 0} ^ {\infty} [ x (n T) * y (n T) ] z ^ {- n} \\ \end{array}
$$

最后，由定理已知条件及式(7-35)证得

$$G (z) = X (z) \cdot Y (z)$$

卷积定理指出,两个采样函数卷积的 z 变换,就等于该两个采样函数相应 z 变换的乘积。在离散系统分析中,卷积定理是沟通时域与 z 域的桥梁。
